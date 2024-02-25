import dataclasses
import functools
import itertools
import operator
from collections import namedtuple
from typing import Sequence, Optional, Literal
import tqdm
import numpy as np
import pandas as pd
from typing import Optional
from .expr import ChemFormula

from .elements import EDB
from .expr import ChemFormula

MS1Ion = namedtuple("MS1Ion", ["MS1_IDX", "RT", "MZ", "INT"])

    
def isotope_distribution(
    elements: dict[str, int],
    normalize_mass: Optional[Literal["highest", "first", "last"]] = None,
    normalize_distribution: bool = False,
):
    # {'Br': 4, 'Cl': 2}

    mass = []
    distribution = []
    names = []
    for ele, num in elements.items():
        iso_weights, iso_dists, iso_names = EDB[ele].isotopes_distribution(num)
        mass.append(iso_weights)
        distribution.append(iso_dists)
        names.append(iso_names)

    mass = np.asarray([np.sum(item) for item in itertools.product(*mass)])
    distribution = np.asarray(
        [np.prod(item) for item in itertools.product(*distribution)]
    )
    names = np.asarray(
        [functools.reduce(operator.add, item) for item in itertools.product(*names)],
        dtype=object,
    )  # type: ignore
    if normalize_distribution:
        distribution /= distribution.max()

    if normalize_mass == "highest":
        mass -= mass[distribution.argmax()]
    elif normalize_mass == "first":
        mass -= mass.min()
    elif normalize_mass == "last":
        mass -= mass.max()

    order = np.argsort(mass)
    mass = mass[order]
    distribution = distribution[order]
    names = names[order]
    return mass, distribution, names


def monoisotopic_mass(formula: str | ChemFormula):
    if isinstance(formula, str):
        formula = ChemFormula(formula)

    return formula.mass


def find_ms(
    ms: float | np.ndarray,
    target_mz: float | Sequence[float],
    mass_acc: float,
    labels: Sequence[str] = None,
):
    ms = np.atleast_1d(ms)
    target_mz = np.atleast_1d(target_mz)
    ms = ms.reshape(1, -1)
    target_mz = target_mz.reshape(-1, 1)
    r = np.logical_and(
        (1 - mass_acc) * target_mz <= ms, ms <= (1 + mass_acc) * target_mz
    ).any(axis=1)
    if labels is None:
        labels = [f"{x:.4f}" for x in target_mz.ravel()]
    a = pd.Series(r, labels)
    return a


def find_by_mz(
    ms: pd.DataFrame,
    target_mz: float | Sequence[float],
    mass_acc: float,
    labels: Sequence[str] = None,
):
    hit = ms["MZ"].apply(
        find_ms, target_mz=target_mz, mass_acc=mass_acc, labels=labels
    )
    return hit


def get_closest_ion(mz, ms1mz, ms1int):
    mz_idx = np.abs(mz - ms1mz).argmin()
    return ms1mz[mz_idx], ms1int[mz_idx]


def ms2_ms1_roi(ms2, ms1, mass_deviation, prog_wrapper=tqdm.tqdm):
    roi_id = pd.Series(-1, index=ms2.index, dtype=int, name="group_id")
    ms2_roi_idx = 0
    ms2_idx_to_ms1_roi = {}
    for idx in prog_wrapper(roi_id.index):
        if roi_id.at[idx] == -1:
            ms2_roi_idx += 1
            roi_id.at[idx] = ms2_roi_idx
            mz_list = [ms2.at[idx, "Precursor"]]
            ms1_idx_start = ms2.at[idx, "MS1_IDX"]

            p = ms1_idx_start
            spec = ms1.loc[p]
            m, i = get_closest_ion(ms2.at[idx, "Precursor"], spec.MZ, spec.INT)
            roi_ms1 = [MS1Ion(p, ms1.at[p, "RT"], m, i)]
            # forward:
            while p < ms1.index.max():
                mz_mean = np.mean(mz_list)
                p += 1
                spec = ms1.loc[p]
                ms2_hit = (ms2["MS1_IDX"] == p) & (
                    np.abs(ms2["Precursor"] - mz_mean) < mz_mean * mass_deviation
                )
                if ms2_hit.any():
                    roi_id[ms2_hit] = ms2_roi_idx
                    mz_list.extend(ms2.loc[ms2_hit, "Precursor"].to_list())
                else:
                    e = np.abs(spec.MZ - mz_mean)
                    if np.any(e <= mz_mean * mass_deviation):
                        mz_list.append(spec.MZ[np.argmin(e)])
                    else:
                        break
                m, i = get_closest_ion(mz_mean, spec.MZ, spec.INT)
                roi_ms1.append(MS1Ion(p, ms1.at[p, "RT"], m, i))

            p = ms1_idx_start
            # backward:
            while p > ms1.index.min():
                mz_mean = np.mean(mz_list)
                p -= 1
                spec = ms1.loc[p]
                ms2_hit = (ms2["MS1_IDX"] == p) & (
                    np.abs(ms2["Precursor"] - mz_mean) < mz_mean * mass_deviation
                )
                if ms2_hit.any():
                    roi_id[ms2_hit] = ms2_roi_idx
                    mz_list.extend(ms2.loc[ms2_hit, "Precursor"].to_list())
                else:
                    e = np.abs(spec.MZ - mz_mean)
                    if np.any(e <= mz_mean * mass_deviation):
                        mz_list.append(spec.MZ[np.argmin(e)])
                    else:
                        break
                m, i = get_closest_ion(mz_mean, spec.MZ, spec.INT)
                roi_ms1.append(MS1Ion(p, ms1.at[p, "RT"], m, i))
            ms2_idx_to_ms1_roi[ms2_roi_idx] = pd.DataFrame(roi_ms1)
    df = pd.concat((ms2["MS1Int"], roi_id), axis=1)
    return df, ms2_idx_to_ms1_roi

def eic(target_mz, ms1, rtol=5e-6):
    max_mz = target_mz * (1+rtol)
    min_mz = target_mz * (1-rtol)

    def f(s, max_mz, min_mz):
        mz = s.MZ
        sel_int = s.INT[(min_mz <= mz) & (mz <= max_mz)]
        return sel_int.sum()
    tic_int = ms1[['MZ', 'INT']].apply(f, axis=1, args=(max_mz, min_mz))
    return pd.DataFrame(data={'RT': ms1['RT'], 'EIC_INT': tic_int})


def search_from_another_ms1(target_mz, rt, ms1, mass_acc, rt_atol=1):
    eic_df = eic(target_mz, ms1, mass_acc)
    sel = np.logical_and(eic_df['RT'] > (
        rt - rt_atol), eic_df['RT'] < (rt + rt_atol))
    return eic_df.loc[sel, 'EIC_INT'].max()


