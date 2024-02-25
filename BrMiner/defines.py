import enum
from enum import StrEnum  # only python 3.11 above

# https://physics.nist.gov/cgi-bin/cuu/Value?meu
ELECTRON_MASS = 5.48579909065e-4


@enum.unique
class ColumnNames(StrEnum):
    SpecMZ = "SpecMZ"
    SpecINT = "SpecINT"
    RT = "RT"

    PrecursorMZ = "Precursor"
    PrecursorInt = "PrecursorInt"
    PrecursorMS1Int = "MS1INT"
    Charge = "Charge"

    MS1IDX = "MS1IDX"
    MS2IDX = "MS2IDX"
    ProductsIDX = "ProductsIDX"

    OPEClass = "Class"
    ROIGroupID = "ROIGroupID"  
    Isotopes = "Isotopes"
    IsTriester = "Tri-ester"
  
    FormulaList = "Formulas"
    Formula = "Formula"
    Deviation = "Deviation"

    __repr__ = str.__repr__
