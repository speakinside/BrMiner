import dataclasses
import itertools
import re
from collections.abc import Mapping
from functools import cached_property, lru_cache
from typing import NamedTuple, Union

import numpy as np
import numpy.typing as npt
import typing
from scipy.special import binom


class IsotopeDistribution(NamedTuple):
    atomic_weight: npt.NDArray[np.float64]
    distribution: npt.NDArray[np.float64]
    names: npt.NDArray[np.str_]


@dataclasses.dataclass(eq=True, order=True, frozen=True)
class Isotope:
    symbol: str
    mass_number: int
    mass: float
    mass_uncertainty: float
    abundance: float
    abundance_uncertainty: float

    def fsymbol(self, show_mass=True, latex=False):
        # formatted symbol
        if show_mass:
            mass = round(self.mass)
        else:
            mass = ""

        if latex:
            return fr"{{}}^{{{mass}}}\mathrm{{{self.symbol}}}"

        return f"{self.symbol}{mass}"

    def __repr__(self) -> str:
        return f"<Isotope: {self.symbol}{round(self.mass)} {self.abundance:.4f}>"

    def __hash__(self) -> int:
        return hash((self.symbol, self.mass))

    def _repr_latex_(self):
        return (
            fr"$^{{{round(self.mass)}}}\mathrm{{{self.symbol}}}: {self.abundance:.4f}$"
        )

    @cached_property
    def is_dominant(self):
        return self.element.dominant_isotope == self

    @cached_property
    def element(self):
        from . import EDB

        return typing.cast(Element, EDB[self.symbol])


@dataclasses.dataclass(eq=True, frozen=True)
class Element:
    name: str
    symbol: str
    atomic_number: int
    isotopes: tuple[Isotope]

    def __init__(
        self,
        name: str,
        symbol: str,
        atomic_number: int,
        isotopes: list[dict[str, Union[int, str, float]]],
    ) -> None:
        super().__setattr__("name", name)
        super().__setattr__("symbol", symbol)
        super().__setattr__("atomic_number", atomic_number)
        super().__setattr__(
            "isotopes", tuple(Isotope(symbol=symbol, **isotope) for isotope in isotopes) # type:ignore
        )

    @cached_property
    def standard_atomic_weight(self):
        return sum([isotope.mass * isotope.abundance for isotope in self.isotopes])

    @cached_property
    def dominant_isotope(self):
        return max(self.isotopes, key=lambda x: x.abundance)

    @lru_cache(maxsize=128)
    def isotopes_distribution(self, n: int):
        from ..expr import ChemFormula

        isotope_mass = np.asarray([iso.mass for iso in self.isotopes], float)
        abundance = np.asarray([iso.abundance for iso in self.isotopes], float)

        combinations = np.array(
            [
                c
                for c in itertools.product(range(n + 1), repeat=len(self.isotopes))
                if sum(c) == n
            ]
        )
        cumsum_comb = combinations.cumsum(1)
        N = np.full_like(cumsum_comb, n)
        N[:, 1:] -= cumsum_comb[:, :-1]

        freq = binom(N, combinations)
        distribution = np.prod(np.power(abundance, combinations) * freq, 1)
        atomic_weight = np.sum(isotope_mass * combinations, 1)
        names = np.asarray(
            [ChemFormula(dict(zip(self.isotopes, c))).simplify() for c in combinations]
        )

        return IsotopeDistribution(atomic_weight, distribution, names)

    def fuzzy_find(self, mass):
        deficit = [abs(isotope.mass - mass) for isotope in self.isotopes]
        idx = np.argmin(deficit)
        if deficit[idx] > 1:
            raise ValueError()
        return self.isotopes[idx]

    def __hash__(self) -> int:
        return hash(self.name)

    def __repr__(self) -> str:
        return f"<Element {self.name}>"

    def _repr_latex_(self):
        return fr"$\mathrm{{{self.symbol}}}: {self.standard_atomic_weight:.4f}$"


class ElementDB(Mapping):
    def __init__(self, db: list[dict]) -> None:
        self.symbol_map = {}
        self.atomic_number_map = {}

        for data in db:
            ele = Element(**data)
            self.symbol_map[ele.symbol] = ele
            self.atomic_number_map[ele.symbol] = ele

    def __getitem__(self, key: Union[str, int]) -> Union[Element, Isotope]:
        # return `Element` or `Isotope` depending on the form of key
        if isinstance(key, int):
            return self.atomic_number_map[key]

        if key.isalpha():
            return self.symbol_map[key.capitalize()]

        ele, mass, _ = re.split(r"(\d+\.?\d*)", key)
        return self.symbol_map[ele.capitalize()].fuzzy_find(float(mass))

    def get_isotope(self, name) -> Isotope:
        # always return `Isotope`
        if isinstance(ele := self[name], Element):
            ele = ele.dominant_isotope
        return ele

    def __getattr__(self, name: str) -> Union[Element, Isotope]:
        try:
            return self[name]
        except KeyError as e:
            raise AttributeError from e

    def __iter__(self):
        return iter(self.symbol_map)

    def __len__(self):
        return len(self.symbol_map)
