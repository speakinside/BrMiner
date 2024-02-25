import itertools
import typing

import numpy as np

from .elements import EDB
from .tools import isotope_distribution
from .utils import rbf


class Pattern(typing.NamedTuple):
    mz: float
    intensity: float
    certainty: float
    mz_sel: np.ndarray
    intensity_sel: np.ndarray


def validate_ms(ms, ms_diff, ms_acc):
    min_mz = np.max(ms / (1 + ms_acc) - ms_diff)
    max_mz = np.min(ms / (1 - ms_acc) - ms_diff)
    return min_mz <= max_mz


class MSPatternFinder:
    def __init__(
        self,
        elements,
        mass_acc=5e-6,
        intensity_sigma=0.1,
        top_n=None,
        ratio_lb=0,
        intensity_lb=0,
    ) -> None:
        self.elements: dict = elements
        self.mass_acc = mass_acc
        self.intensity_sigma = intensity_sigma
        self.top_n = top_n
        self.ratio_lb = ratio_lb
        self.intensity_lb = intensity_lb
        self.mz_lb = sum(
            [
                (EDB[ele].standard_atomic_weight * num)
                for (ele, num) in self.elements.items()
            ]
        )

    def match(self, mz, intensity) -> list[Pattern]:

        mass_diffs, intensity_ratio, _ = isotope_distribution(
            self.elements, normalize_mass="highest", normalize_distribution=True
        )

        significant = intensity_ratio >= self.ratio_lb
        mass_diffs = mass_diffs[significant]
        intensity_ratio = intensity_ratio[significant]

        if self.top_n is not None:
            top_idx = np.argsort(intensity_ratio)[-self.top_n:]
            mass_diffs = mass_diffs[top_idx]
            intensity_ratio = intensity_ratio[top_idx]

        results = []
        for idx, (center_mz, center_mz_int) in enumerate(zip(mz, intensity)):
            if center_mz_int < self.intensity_lb or center_mz < self.mz_lb:
                continue

            combines = []
            for mz_diff in mass_diffs:
                if mz_diff == 0:
                    combines.append([idx])
                    continue
                mz_min = (1 - self.mass_acc) * (
                    center_mz / (1 + self.mass_acc) + mz_diff
                )
                mz_max = (1 + self.mass_acc) * (
                    center_mz / (1 - self.mass_acc) + mz_diff
                )
                combines.append(np.argwhere(
                    (mz_min <= mz) & (mz <= mz_max)).ravel())

            candidates = tuple(itertools.product(*combines))

            best_idxes = None
            best_p = 0
            for indices in candidates:
                indices = np.asarray(indices).ravel()
                if not validate_ms(mz[indices], mass_diffs, self.mass_acc):
                    continue
                int_candi = intensity[indices]
                k = np.inner(int_candi, intensity_ratio) / np.inner(
                    int_candi, int_candi
                )
                delta = intensity_ratio - int_candi * k
                p = rbf(delta, 0, self.intensity_sigma).min()
                if p > best_p:
                    best_p = p
                    best_idxes = indices

            if best_idxes is not None:
                pattern = Pattern(
                    mz=center_mz,
                    intensity=center_mz_int,
                    certainty=best_p,
                    mz_sel=mz[best_idxes],
                    intensity_sel=intensity[best_idxes],
                )
                results.append(pattern)
        return results


