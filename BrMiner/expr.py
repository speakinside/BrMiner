import re
from collections import defaultdict
from collections.abc import Mapping
from copy import deepcopy
from typing import Union, Any, Optional, Literal, Iterable

from .defines import ELECTRON_MASS
from .elements import EDB, Element, Isotope

ELE_PATTERN = re.compile(r"\[[A-Z][a-z]*\d*\]\d*|[A-Z][a-z]*\d*(?![^\[]*\])")
PATTERN2 = re.compile(
    r"((?<=\[)[A-Z][a-z]*\d*(?=\])" "|" r"[A-Z][a-z]*(?![^\[]*\]))\]?(\d*)"
)


def str_parser(sformula: str):
    sformula = sformula.replace(" ", "")
    normal_formula = sformula.rstrip("+")
    charge = len(sformula) - len(normal_formula)
    if charge == 0:
        normal_formula = sformula.rstrip("-")
        charge = -(len(sformula) - len(normal_formula))

    comps = re.findall(ELE_PATTERN, normal_formula)
    if sum(map(len, comps)) != len(normal_formula):
        raise ValueError()
    dic: defaultdict[Isotope, int] = defaultdict(lambda: 0)

    for comp in comps:
        obj = PATTERN2.search(comp)
        if obj:
            ele, count = obj.group(1, 2)
            ele = EDB[ele]
            if isinstance(ele, Element):
                ele = ele.dominant_isotope
            dic[ele] += int(count) if count else 1
    return dict(dic), charge


def _CH_first_ord_key_map(ele: Isotope):
    symbol = ele.symbol
    if symbol == "C":
        return chr(0)
    elif symbol == "H":
        return chr(1)
    return symbol


def element_sort(
    eles: Iterable[Isotope], format: Literal["CH first", "hill"] = "CH first"
):
    if format == "CH first" or any(iso.symbol == "C" for iso in eles):
        return sorted(eles, key=_CH_first_ord_key_map)
    else:
        return sorted(eles, key=lambda iso: iso.symbol)


class ChemFormula:
    def __init__(
        self,
        expr: "Optional[str | Mapping[Isotope, int] | ChemFormula]" = None,
        charge: Optional[int] = None,
        attrs: Optional[dict[str, Any]] = None,
    ) -> None:
        if attrs:
            self.attrs = deepcopy(attrs)
        else:
            self.attrs = {}
        if isinstance(expr, ChemFormula):
            self.ele_d = expr.ele_d.copy()
            self.attrs = expr.attrs.copy()
            self.charge = expr.charge

        elif isinstance(expr, str):
            ele_d, c = str_parser(expr)
            if charge is None:
                self.charge = c
            elif charge != c:
                raise ValueError()
            else:
                self.charge = charge
            self.ele_d = ele_d  # {EDB[k].dominant_isotope: v for k, v in ele.items()}
        else:
            self.ele_d = {}
            self.charge = 0 if charge is None else charge
            if expr is not None:
                for k, v in expr.items():
                    if isinstance(k, Isotope):
                        self.ele_d[k] = v
                    else:
                        k = EDB[k]
                        if isinstance(k, Element):
                            k = k.dominant_isotope
                        self.ele_d[k] = v

    def simplify(self):
        for k in list(self.ele_d.keys()):
            if self.ele_d[k] == 0:
                del self.ele_d[k]
        return self

    def empirical_formula(
        self,
        show_isotope=True,
        show_charge=True,
        format: Literal["CH first", "hill"] = "CH first",
    ):
        """Return empirical formula

        Parameters
        ----------
        show_isotope : bool, optional
            Whether to show mass in the formula, by default True
        show_charge : bool, optional
            Whether to show charge in the formula, by default True
        format : Literal["CH first", "hill"], optional
            The rule to organize the elements in the formula. 
            "CH first" will write C and H elements first and the rest in alphabetical order.
            "hill" write the same as "CH first" when the formula contains C. Else, all the elements, including hydrogen, are listed alphabetically.
            by default "CH first"

        Returns
        -------
        str
            Empirical formula
        """
        if show_isotope:
            formula = "".join(
                f"[{iso.fsymbol()}]{k if (k:=self.ele_d[iso])!=1 else ''}"
                for iso in element_sort(self.ele_d.keys(), format)
            )
        else:
            dic = {}
            for iso in element_sort(self.ele_d.keys(), format):
                dic[iso.symbol] = dic.get(iso.symbol, 0) + self.ele_d[iso]
            formula = "".join(
                f"{sym}{num if num != 1 else ''}" for (sym, num) in dic.items()
            )
        if show_charge and self.charge != 0:
            sign = "+" if self.charge > 0 else "-"
            if (charge := abs(self.charge)) == 1:
                charge = ""
            formula += f"{sign}{charge}"
        return formula

    def monoisotopic_formula(
        self,
        show_charge=False,
        format: Literal["CH first", "hill"] = "CH first",
    ):
        return self.empirical_formula(
            show_isotope=False, show_charge=show_charge, format=format
        )

    def is_empty(self):
        return len(self.ele_d) == 0

    def copy(self):
        return ChemFormula(self.ele_d, self.charge, self.attrs)

    def html(self):
        def make_html(ele: Isotope, count: int):
            return (
                f"<sup>{'' if ele.is_dominant else round(ele.mass)}</sup>"
                f"{ele.symbol}"
                f"<sub>{int(count) if count != 1 else ''}</sub>"
            )

        s = "".join(
            make_html(k, v) for (k, v) in sorted(self.ele_d.items(), key=lambda x: x[0])
        )
        sign = "+" if self.charge > 0 else "-"
        if self.charge == 0:
            return s
        else:
            abs_charge = abs(self.charge)
            return f"[{s}]<sup>{abs_charge if abs_charge!=1 else ''}{sign}</sup>"

    def __eq__(self, other: "ChemFormula|str") -> bool:
        from itertools import chain

        if isinstance(other, str):
            other = ChemFormula(other)
        if isinstance(other, ChemFormula):
            if self.charge == other.charge:
                for k in set(chain(self.ele_d.keys(), other.ele_d.keys())):
                    if self.ele_d.get(k, 0) != self.ele_d.get(k, 0):
                        break
                else:
                    return True
        return False

    def __add__(self, other: "ChemFormula"):
        ele = {}
        for k in set(self.ele_d.keys()) | set(other.ele_d.keys()):
            ele[k] = self.ele_d.get(k, 0) + other.ele_d.get(k, 0)
        return ChemFormula(ele, self.charge + other.charge)

    def __iadd__(self, other: "ChemFormula"):
        for k in other.ele_d.keys():
            self.ele_d[k] = self.ele_d.get(k, 0) + other[k]
        self.charge += other.charge

    def __sub__(self, other: "ChemFormula"):
        ele = {}
        for k in set(self.ele_d.keys()) | set(other.ele_d.keys()):
            ele[k] = self.ele_d.get(k, 0) - other.ele_d.get(k, 0)
        return ChemFormula(ele, self.charge - other.charge)

    def __isub__(self, other: "ChemFormula"):
        for k in other.ele_d.keys():
            self.ele_d[k] = self.ele_d.get(k, 0) - other[k]
        self.charge -= other.charge

    def __str__(self) -> str:
        return self.empirical_formula()

    def __hash__(self) -> int:
        return hash(str(self))

    def __repr__(self) -> str:
        return f"<{ChemFormula.__name__}: {str(self)}>"

    def _repr_latex_(self) -> str:
        s = " ".join(
            f"{k.fsymbol(latex=True)}_{{{int(v)}}}"
            for (k, v) in sorted(self.ele_d.items(), key=lambda x: x[0])
        )
        if self.charge != 0:
            sign = "+" if self.charge > 0 else "-"
            if abs(self.charge) == 1:
                sup = sign
            else:
                sup = f"{abs(self.charge)}{sign}"
            s = f"[{s}]^{{{sup}}}"
        return f"${s}$"

    def __getitem__(self, key: str | Isotope | Element):
        if isinstance(key, str):
            if isinstance(key := EDB[key], Element):
                key = key.dominant_isotope
        elif isinstance(key, Element):
            key = key.dominant_isotope
        return self.ele_d.get(key, 0)

    def __setitem__(self, key: str | Isotope | Element, value):
        if isinstance(key, str):
            if isinstance(key := EDB[key], Element):
                key = key.dominant_isotope
        elif isinstance(key, Element):
            key = key.dominant_isotope
        self.ele_d[key] = value

    def __delitem__(self, key):
        del self.ele_d[key]

    @property
    def mass(self) -> float:
        return (
            sum((k.mass * v for (k, v) in self.ele_d.items()))
            - ELECTRON_MASS * self.charge
        )
