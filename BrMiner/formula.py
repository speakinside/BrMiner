import numpy as np
from constraint import MaxSumConstraint, MinSumConstraint, Problem
from collections.abc import Sequence
from .defines import ELECTRON_MASS
from .elements import EDB, Element, Isotope
from .elements.table import *
from .expr import ChemFormula


def predict_formula(
    mz: float,
    mass_acc: float = 5e-6,
    charge: int = 0,
    lim_C: Sequence[int] = range(100),
    lim_H: Sequence[int] = range(200),
    lim_O: Sequence[int] = range(51),
    lim_DoU: Sequence[int] = range(51),
    lim_N: Sequence[int] = (0,),
    lim_P: Sequence[int] = (0,),
    lim_Cl35: Sequence[int] = (0,),
    lim_Cl37: Sequence[int] = (0,),
    lim_Br79: Sequence[int] = (0,),
    lim_Br81: Sequence[int] = (0,),
):
    prob = Problem()
    prob.addVariable(C12, lim_C)
    prob.addVariable(H1, lim_H)
    prob.addVariable(O16, lim_O)
    prob.addVariable(P31, lim_P)
    prob.addVariable(N14, lim_N)
    prob.addVariable(Cl35, lim_Cl35)
    prob.addVariable(Cl37, lim_Cl37)
    prob.addVariable(Br79, lim_Br79)
    prob.addVariable(Br81, lim_Br81)
    prob.addVariable("DoU", lim_DoU)

    def f(c, dou, p, h, n, cl35, cl37, br79, br81):
        return 2 * (c - dou) + 2 + 3 * p + n + charge == h + cl35 + cl37 + br79 + br81

    prob.addConstraint(f, [C12, "DoU", P31, H1, N14, Cl35, Cl37, Br79, Br81])
    prob.addConstraint(
        MaxSumConstraint(
            mz / (1 - mass_acc) + ELECTRON_MASS * charge,
            [
                C12.mass,
                H1.mass,
                O16.mass,
                P31.mass,
                N14.mass,
                Cl35.mass,
                Cl37.mass,
                Br79.mass,
                Br81.mass,
            ],
        ),
        [C12, H1, O16, P31, N14, Cl35, Cl37, Br79, Br81],
    )
    prob.addConstraint(
        MinSumConstraint(
            mz / (1 + mass_acc) + ELECTRON_MASS * charge,
            [
                C12.mass,
                H1.mass,
                O16.mass,
                P31.mass,
                N14.mass,
                Cl35.mass,
                Cl37.mass,
                Br79.mass,
                Br81.mass,
            ],
        ),
        [C12, H1, O16, P31, N14, Cl35, Cl37, Br79, Br81],
    )

    results = prob.getSolutions()
    all_dou = [r.pop("DoU") for r in results]
    return [
        ChemFormula(r, charge=charge, attrs={"DoU": dou}).simplify()
        for (r, dou) in zip(results, all_dou)
    ]
