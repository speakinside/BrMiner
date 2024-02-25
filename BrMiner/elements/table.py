from . import EDB
from .cls import Element, Isotope

__all__ = [
    # Elements
    "H",
    "He",
    "Li",
    "Be",
    "B",
    "C",
    "N",
    "O",
    "F",
    "Ne",
    "Na",
    "Mg",
    "Al",
    "Si",
    "P",
    "S",
    "Cl",
    "Ar",
    "K",
    "Ca",
    "Sc",
    "Ti",
    "V",
    "Cr",
    "Mn",
    "Fe",
    "Co",
    "Ni",
    "Cu",
    "Zn",
    "Ga",
    "Ge",
    "As",
    "Se",
    "Br",
    "Kr",
    "Rb",
    "Sr",
    "Y",
    "Zr",
    "Nb",
    "Mo",
    "Ru",
    "Rh",
    "Pd",
    "Ag",
    "Cd",
    "In",
    "Sn",
    "Sb",
    "Te",
    "I",
    "Xe",
    "Cs",
    "Ba",
    "La",
    "Ce",
    "Pr",
    "Nd",
    "Sm",
    "Eu",
    "Gd",
    "Tb",
    "Dy",
    "Ho",
    "Er",
    "Tm",
    "Yb",
    "Lu",
    "Hf",
    "Ta",
    "W",
    "Re",
    "Os",
    "Ir",
    "Pt",
    "Au",
    "Hg",
    "Tl",
    "Pb",
    "Bi",
    "Th",
    "Pa",
    "U",
    # Isotopes
    "H1",
    "H2",
    "He3",
    "He4",
    "Li6",
    "Li7",
    "Be9",
    "B10",
    "B11",
    "C12",
    "C13",
    "N14",
    "N15",
    "O16",
    "O17",
    "O18",
    "F19",
    "Ne20",
    "Ne21",
    "Ne22",
    "Na23",
    "Mg24",
    "Mg25",
    "Mg26",
    "Al27",
    "Si28",
    "Si29",
    "Si30",
    "P31",
    "S32",
    "S33",
    "S34",
    "S36",
    "Cl35",
    "Cl37",
    "Ar36",
    "Ar38",
    "Ar40",
    "K39",
    "K40",
    "K41",
    "Ca40",
    "Ca42",
    "Ca43",
    "Ca44",
    "Ca46",
    "Ca48",
    "Sc45",
    "Ti46",
    "Ti47",
    "Ti48",
    "Ti49",
    "Ti50",
    "V50",
    "V51",
    "Cr50",
    "Cr52",
    "Cr53",
    "Cr54",
    "Mn55",
    "Fe54",
    "Fe56",
    "Fe57",
    "Fe58",
    "Co59",
    "Ni58",
    "Ni60",
    "Ni61",
    "Ni62",
    "Ni64",
    "Cu63",
    "Cu65",
    "Zn64",
    "Zn66",
    "Zn67",
    "Zn68",
    "Zn70",
    "Ga69",
    "Ga71",
    "Ge70",
    "Ge72",
    "Ge73",
    "Ge74",
    "Ge76",
    "As75",
    "Se74",
    "Se76",
    "Se77",
    "Se78",
    "Se80",
    "Se82",
    "Br79",
    "Br81",
    "Kr78",
    "Kr80",
    "Kr82",
    "Kr83",
    "Kr84",
    "Kr86",
    "Rb85",
    "Rb87",
    "Sr84",
    "Sr86",
    "Sr87",
    "Sr88",
    "Y89",
    "Zr90",
    "Zr91",
    "Zr92",
    "Zr94",
    "Zr96",
    "Nb93",
    "Mo92",
    "Mo94",
    "Mo95",
    "Mo96",
    "Mo97",
    "Mo98",
    "Mo100",
    "Ru96",
    "Ru98",
    "Ru99",
    "Ru100",
    "Ru101",
    "Ru102",
    "Ru104",
    "Rh103",
    "Pd102",
    "Pd104",
    "Pd105",
    "Pd106",
    "Pd108",
    "Pd110",
    "Ag107",
    "Ag109",
    "Cd106",
    "Cd108",
    "Cd110",
    "Cd111",
    "Cd112",
    "Cd113",
    "Cd114",
    "Cd116",
    "In113",
    "In115",
    "Sn112",
    "Sn114",
    "Sn115",
    "Sn116",
    "Sn117",
    "Sn118",
    "Sn119",
    "Sn120",
    "Sn122",
    "Sn124",
    "Sb121",
    "Sb123",
    "Te120",
    "Te122",
    "Te123",
    "Te124",
    "Te125",
    "Te126",
    "Te128",
    "Te130",
    "I127",
    "Xe124",
    "Xe126",
    "Xe128",
    "Xe129",
    "Xe130",
    "Xe131",
    "Xe132",
    "Xe134",
    "Xe136",
    "Cs133",
    "Ba130",
    "Ba132",
    "Ba134",
    "Ba135",
    "Ba136",
    "Ba137",
    "Ba138",
    "La138",
    "La139",
    "Ce136",
    "Ce138",
    "Ce140",
    "Ce142",
    "Pr141",
    "Nd142",
    "Nd143",
    "Nd144",
    "Nd145",
    "Nd146",
    "Nd148",
    "Nd150",
    "Sm144",
    "Sm147",
    "Sm148",
    "Sm149",
    "Sm150",
    "Sm152",
    "Sm154",
    "Eu151",
    "Eu153",
    "Gd152",
    "Gd154",
    "Gd155",
    "Gd156",
    "Gd157",
    "Gd158",
    "Gd160",
    "Tb159",
    "Dy156",
    "Dy158",
    "Dy160",
    "Dy161",
    "Dy162",
    "Dy163",
    "Dy164",
    "Ho165",
    "Er162",
    "Er164",
    "Er166",
    "Er167",
    "Er168",
    "Er170",
    "Tm169",
    "Yb168",
    "Yb170",
    "Yb171",
    "Yb172",
    "Yb173",
    "Yb174",
    "Yb176",
    "Lu175",
    "Lu176",
    "Hf174",
    "Hf176",
    "Hf177",
    "Hf178",
    "Hf179",
    "Hf180",
    "Ta181",
    "W180",
    "W182",
    "W183",
    "W184",
    "W186",
    "Re185",
    "Re187",
    "Os184",
    "Os186",
    "Os187",
    "Os188",
    "Os189",
    "Os190",
    "Os192",
    "Ir191",
    "Ir193",
    "Pt190",
    "Pt192",
    "Pt194",
    "Pt195",
    "Pt196",
    "Pt198",
    "Au197",
    "Hg196",
    "Hg198",
    "Hg199",
    "Hg200",
    "Hg201",
    "Hg202",
    "Hg204",
    "Tl203",
    "Tl205",
    "Pb204",
    "Pb206",
    "Pb207",
    "Pb208",
    "Bi209",
    "Th230",
    "Th232",
    "Pa231",
    "U234",
    "U235",
    "U238",
]

# Element
H: Element = EDB["H"]
He: Element = EDB["He"]
Li: Element = EDB["Li"]
Be: Element = EDB["Be"]
B: Element = EDB["B"]
C: Element = EDB["C"]
N: Element = EDB["N"]
O: Element = EDB["O"]
F: Element = EDB["F"]
Ne: Element = EDB["Ne"]
Na: Element = EDB["Na"]
Mg: Element = EDB["Mg"]
Al: Element = EDB["Al"]
Si: Element = EDB["Si"]
P: Element = EDB["P"]
S: Element = EDB["S"]
Cl: Element = EDB["Cl"]
Ar: Element = EDB["Ar"]
K: Element = EDB["K"]
Ca: Element = EDB["Ca"]
Sc: Element = EDB["Sc"]
Ti: Element = EDB["Ti"]
V: Element = EDB["V"]
Cr: Element = EDB["Cr"]
Mn: Element = EDB["Mn"]
Fe: Element = EDB["Fe"]
Co: Element = EDB["Co"]
Ni: Element = EDB["Ni"]
Cu: Element = EDB["Cu"]
Zn: Element = EDB["Zn"]
Ga: Element = EDB["Ga"]
Ge: Element = EDB["Ge"]
As: Element = EDB["As"]
Se: Element = EDB["Se"]
Br: Element = EDB["Br"]
Kr: Element = EDB["Kr"]
Rb: Element = EDB["Rb"]
Sr: Element = EDB["Sr"]
Y: Element = EDB["Y"]
Zr: Element = EDB["Zr"]
Nb: Element = EDB["Nb"]
Mo: Element = EDB["Mo"]
Ru: Element = EDB["Ru"]
Rh: Element = EDB["Rh"]
Pd: Element = EDB["Pd"]
Ag: Element = EDB["Ag"]
Cd: Element = EDB["Cd"]
In: Element = EDB["In"]
Sn: Element = EDB["Sn"]
Sb: Element = EDB["Sb"]
Te: Element = EDB["Te"]
I: Element = EDB["I"]
Xe: Element = EDB["Xe"]
Cs: Element = EDB["Cs"]
Ba: Element = EDB["Ba"]
La: Element = EDB["La"]
Ce: Element = EDB["Ce"]
Pr: Element = EDB["Pr"]
Nd: Element = EDB["Nd"]
Sm: Element = EDB["Sm"]
Eu: Element = EDB["Eu"]
Gd: Element = EDB["Gd"]
Tb: Element = EDB["Tb"]
Dy: Element = EDB["Dy"]
Ho: Element = EDB["Ho"]
Er: Element = EDB["Er"]
Tm: Element = EDB["Tm"]
Yb: Element = EDB["Yb"]
Lu: Element = EDB["Lu"]
Hf: Element = EDB["Hf"]
Ta: Element = EDB["Ta"]
W: Element = EDB["W"]
Re: Element = EDB["Re"]
Os: Element = EDB["Os"]
Ir: Element = EDB["Ir"]
Pt: Element = EDB["Pt"]
Au: Element = EDB["Au"]
Hg: Element = EDB["Hg"]
Tl: Element = EDB["Tl"]
Pb: Element = EDB["Pb"]
Bi: Element = EDB["Bi"]
Th: Element = EDB["Th"]
Pa: Element = EDB["Pa"]
U: Element = EDB["U"]

# Isotopes
H1: Isotope = EDB["H1"]
H2: Isotope = EDB["H2"]
He3: Isotope = EDB["He3"]
He4: Isotope = EDB["He4"]
Li6: Isotope = EDB["Li6"]
Li7: Isotope = EDB["Li7"]
Be9: Isotope = EDB["Be9"]
B10: Isotope = EDB["B10"]
B11: Isotope = EDB["B11"]
C12: Isotope = EDB["C12"]
C13: Isotope = EDB["C13"]
N14: Isotope = EDB["N14"]
N15: Isotope = EDB["N15"]
O16: Isotope = EDB["O16"]
O17: Isotope = EDB["O17"]
O18: Isotope = EDB["O18"]
F19: Isotope = EDB["F19"]
Ne20: Isotope = EDB["Ne20"]
Ne21: Isotope = EDB["Ne21"]
Ne22: Isotope = EDB["Ne22"]
Na23: Isotope = EDB["Na23"]
Mg24: Isotope = EDB["Mg24"]
Mg25: Isotope = EDB["Mg25"]
Mg26: Isotope = EDB["Mg26"]
Al27: Isotope = EDB["Al27"]
Si28: Isotope = EDB["Si28"]
Si29: Isotope = EDB["Si29"]
Si30: Isotope = EDB["Si30"]
P31: Isotope = EDB["P31"]
S32: Isotope = EDB["S32"]
S33: Isotope = EDB["S33"]
S34: Isotope = EDB["S34"]
S36: Isotope = EDB["S36"]
Cl35: Isotope = EDB["Cl35"]
Cl37: Isotope = EDB["Cl37"]
Ar36: Isotope = EDB["Ar36"]
Ar38: Isotope = EDB["Ar38"]
Ar40: Isotope = EDB["Ar40"]
K39: Isotope = EDB["K39"]
K40: Isotope = EDB["K40"]
K41: Isotope = EDB["K41"]
Ca40: Isotope = EDB["Ca40"]
Ca42: Isotope = EDB["Ca42"]
Ca43: Isotope = EDB["Ca43"]
Ca44: Isotope = EDB["Ca44"]
Ca46: Isotope = EDB["Ca46"]
Ca48: Isotope = EDB["Ca48"]
Sc45: Isotope = EDB["Sc45"]
Ti46: Isotope = EDB["Ti46"]
Ti47: Isotope = EDB["Ti47"]
Ti48: Isotope = EDB["Ti48"]
Ti49: Isotope = EDB["Ti49"]
Ti50: Isotope = EDB["Ti50"]
V50: Isotope = EDB["V50"]
V51: Isotope = EDB["V51"]
Cr50: Isotope = EDB["Cr50"]
Cr52: Isotope = EDB["Cr52"]
Cr53: Isotope = EDB["Cr53"]
Cr54: Isotope = EDB["Cr54"]
Mn55: Isotope = EDB["Mn55"]
Fe54: Isotope = EDB["Fe54"]
Fe56: Isotope = EDB["Fe56"]
Fe57: Isotope = EDB["Fe57"]
Fe58: Isotope = EDB["Fe58"]
Co59: Isotope = EDB["Co59"]
Ni58: Isotope = EDB["Ni58"]
Ni60: Isotope = EDB["Ni60"]
Ni61: Isotope = EDB["Ni61"]
Ni62: Isotope = EDB["Ni62"]
Ni64: Isotope = EDB["Ni64"]
Cu63: Isotope = EDB["Cu63"]
Cu65: Isotope = EDB["Cu65"]
Zn64: Isotope = EDB["Zn64"]
Zn66: Isotope = EDB["Zn66"]
Zn67: Isotope = EDB["Zn67"]
Zn68: Isotope = EDB["Zn68"]
Zn70: Isotope = EDB["Zn70"]
Ga69: Isotope = EDB["Ga69"]
Ga71: Isotope = EDB["Ga71"]
Ge70: Isotope = EDB["Ge70"]
Ge72: Isotope = EDB["Ge72"]
Ge73: Isotope = EDB["Ge73"]
Ge74: Isotope = EDB["Ge74"]
Ge76: Isotope = EDB["Ge76"]
As75: Isotope = EDB["As75"]
Se74: Isotope = EDB["Se74"]
Se76: Isotope = EDB["Se76"]
Se77: Isotope = EDB["Se77"]
Se78: Isotope = EDB["Se78"]
Se80: Isotope = EDB["Se80"]
Se82: Isotope = EDB["Se82"]
Br79: Isotope = EDB["Br79"]
Br81: Isotope = EDB["Br81"]
Kr78: Isotope = EDB["Kr78"]
Kr80: Isotope = EDB["Kr80"]
Kr82: Isotope = EDB["Kr82"]
Kr83: Isotope = EDB["Kr83"]
Kr84: Isotope = EDB["Kr84"]
Kr86: Isotope = EDB["Kr86"]
Rb85: Isotope = EDB["Rb85"]
Rb87: Isotope = EDB["Rb87"]
Sr84: Isotope = EDB["Sr84"]
Sr86: Isotope = EDB["Sr86"]
Sr87: Isotope = EDB["Sr87"]
Sr88: Isotope = EDB["Sr88"]
Y89: Isotope = EDB["Y89"]
Zr90: Isotope = EDB["Zr90"]
Zr91: Isotope = EDB["Zr91"]
Zr92: Isotope = EDB["Zr92"]
Zr94: Isotope = EDB["Zr94"]
Zr96: Isotope = EDB["Zr96"]
Nb93: Isotope = EDB["Nb93"]
Mo92: Isotope = EDB["Mo92"]
Mo94: Isotope = EDB["Mo94"]
Mo95: Isotope = EDB["Mo95"]
Mo96: Isotope = EDB["Mo96"]
Mo97: Isotope = EDB["Mo97"]
Mo98: Isotope = EDB["Mo98"]
Mo100: Isotope = EDB["Mo100"]
Ru96: Isotope = EDB["Ru96"]
Ru98: Isotope = EDB["Ru98"]
Ru99: Isotope = EDB["Ru99"]
Ru100: Isotope = EDB["Ru100"]
Ru101: Isotope = EDB["Ru101"]
Ru102: Isotope = EDB["Ru102"]
Ru104: Isotope = EDB["Ru104"]
Rh103: Isotope = EDB["Rh103"]
Pd102: Isotope = EDB["Pd102"]
Pd104: Isotope = EDB["Pd104"]
Pd105: Isotope = EDB["Pd105"]
Pd106: Isotope = EDB["Pd106"]
Pd108: Isotope = EDB["Pd108"]
Pd110: Isotope = EDB["Pd110"]
Ag107: Isotope = EDB["Ag107"]
Ag109: Isotope = EDB["Ag109"]
Cd106: Isotope = EDB["Cd106"]
Cd108: Isotope = EDB["Cd108"]
Cd110: Isotope = EDB["Cd110"]
Cd111: Isotope = EDB["Cd111"]
Cd112: Isotope = EDB["Cd112"]
Cd113: Isotope = EDB["Cd113"]
Cd114: Isotope = EDB["Cd114"]
Cd116: Isotope = EDB["Cd116"]
In113: Isotope = EDB["In113"]
In115: Isotope = EDB["In115"]
Sn112: Isotope = EDB["Sn112"]
Sn114: Isotope = EDB["Sn114"]
Sn115: Isotope = EDB["Sn115"]
Sn116: Isotope = EDB["Sn116"]
Sn117: Isotope = EDB["Sn117"]
Sn118: Isotope = EDB["Sn118"]
Sn119: Isotope = EDB["Sn119"]
Sn120: Isotope = EDB["Sn120"]
Sn122: Isotope = EDB["Sn122"]
Sn124: Isotope = EDB["Sn124"]
Sb121: Isotope = EDB["Sb121"]
Sb123: Isotope = EDB["Sb123"]
Te120: Isotope = EDB["Te120"]
Te122: Isotope = EDB["Te122"]
Te123: Isotope = EDB["Te123"]
Te124: Isotope = EDB["Te124"]
Te125: Isotope = EDB["Te125"]
Te126: Isotope = EDB["Te126"]
Te128: Isotope = EDB["Te128"]
Te130: Isotope = EDB["Te130"]
I127: Isotope = EDB["I127"]
Xe124: Isotope = EDB["Xe124"]
Xe126: Isotope = EDB["Xe126"]
Xe128: Isotope = EDB["Xe128"]
Xe129: Isotope = EDB["Xe129"]
Xe130: Isotope = EDB["Xe130"]
Xe131: Isotope = EDB["Xe131"]
Xe132: Isotope = EDB["Xe132"]
Xe134: Isotope = EDB["Xe134"]
Xe136: Isotope = EDB["Xe136"]
Cs133: Isotope = EDB["Cs133"]
Ba130: Isotope = EDB["Ba130"]
Ba132: Isotope = EDB["Ba132"]
Ba134: Isotope = EDB["Ba134"]
Ba135: Isotope = EDB["Ba135"]
Ba136: Isotope = EDB["Ba136"]
Ba137: Isotope = EDB["Ba137"]
Ba138: Isotope = EDB["Ba138"]
La138: Isotope = EDB["La138"]
La139: Isotope = EDB["La139"]
Ce136: Isotope = EDB["Ce136"]
Ce138: Isotope = EDB["Ce138"]
Ce140: Isotope = EDB["Ce140"]
Ce142: Isotope = EDB["Ce142"]
Pr141: Isotope = EDB["Pr141"]
Nd142: Isotope = EDB["Nd142"]
Nd143: Isotope = EDB["Nd143"]
Nd144: Isotope = EDB["Nd144"]
Nd145: Isotope = EDB["Nd145"]
Nd146: Isotope = EDB["Nd146"]
Nd148: Isotope = EDB["Nd148"]
Nd150: Isotope = EDB["Nd150"]
Sm144: Isotope = EDB["Sm144"]
Sm147: Isotope = EDB["Sm147"]
Sm148: Isotope = EDB["Sm148"]
Sm149: Isotope = EDB["Sm149"]
Sm150: Isotope = EDB["Sm150"]
Sm152: Isotope = EDB["Sm152"]
Sm154: Isotope = EDB["Sm154"]
Eu151: Isotope = EDB["Eu151"]
Eu153: Isotope = EDB["Eu153"]
Gd152: Isotope = EDB["Gd152"]
Gd154: Isotope = EDB["Gd154"]
Gd155: Isotope = EDB["Gd155"]
Gd156: Isotope = EDB["Gd156"]
Gd157: Isotope = EDB["Gd157"]
Gd158: Isotope = EDB["Gd158"]
Gd160: Isotope = EDB["Gd160"]
Tb159: Isotope = EDB["Tb159"]
Dy156: Isotope = EDB["Dy156"]
Dy158: Isotope = EDB["Dy158"]
Dy160: Isotope = EDB["Dy160"]
Dy161: Isotope = EDB["Dy161"]
Dy162: Isotope = EDB["Dy162"]
Dy163: Isotope = EDB["Dy163"]
Dy164: Isotope = EDB["Dy164"]
Ho165: Isotope = EDB["Ho165"]
Er162: Isotope = EDB["Er162"]
Er164: Isotope = EDB["Er164"]
Er166: Isotope = EDB["Er166"]
Er167: Isotope = EDB["Er167"]
Er168: Isotope = EDB["Er168"]
Er170: Isotope = EDB["Er170"]
Tm169: Isotope = EDB["Tm169"]
Yb168: Isotope = EDB["Yb168"]
Yb170: Isotope = EDB["Yb170"]
Yb171: Isotope = EDB["Yb171"]
Yb172: Isotope = EDB["Yb172"]
Yb173: Isotope = EDB["Yb173"]
Yb174: Isotope = EDB["Yb174"]
Yb176: Isotope = EDB["Yb176"]
Lu175: Isotope = EDB["Lu175"]
Lu176: Isotope = EDB["Lu176"]
Hf174: Isotope = EDB["Hf174"]
Hf176: Isotope = EDB["Hf176"]
Hf177: Isotope = EDB["Hf177"]
Hf178: Isotope = EDB["Hf178"]
Hf179: Isotope = EDB["Hf179"]
Hf180: Isotope = EDB["Hf180"]
Ta181: Isotope = EDB["Ta181"]
W180: Isotope = EDB["W180"]
W182: Isotope = EDB["W182"]
W183: Isotope = EDB["W183"]
W184: Isotope = EDB["W184"]
W186: Isotope = EDB["W186"]
Re185: Isotope = EDB["Re185"]
Re187: Isotope = EDB["Re187"]
Os184: Isotope = EDB["Os184"]
Os186: Isotope = EDB["Os186"]
Os187: Isotope = EDB["Os187"]
Os188: Isotope = EDB["Os188"]
Os189: Isotope = EDB["Os189"]
Os190: Isotope = EDB["Os190"]
Os192: Isotope = EDB["Os192"]
Ir191: Isotope = EDB["Ir191"]
Ir193: Isotope = EDB["Ir193"]
Pt190: Isotope = EDB["Pt190"]
Pt192: Isotope = EDB["Pt192"]
Pt194: Isotope = EDB["Pt194"]
Pt195: Isotope = EDB["Pt195"]
Pt196: Isotope = EDB["Pt196"]
Pt198: Isotope = EDB["Pt198"]
Au197: Isotope = EDB["Au197"]
Hg196: Isotope = EDB["Hg196"]
Hg198: Isotope = EDB["Hg198"]
Hg199: Isotope = EDB["Hg199"]
Hg200: Isotope = EDB["Hg200"]
Hg201: Isotope = EDB["Hg201"]
Hg202: Isotope = EDB["Hg202"]
Hg204: Isotope = EDB["Hg204"]
Tl203: Isotope = EDB["Tl203"]
Tl205: Isotope = EDB["Tl205"]
Pb204: Isotope = EDB["Pb204"]
Pb206: Isotope = EDB["Pb206"]
Pb207: Isotope = EDB["Pb207"]
Pb208: Isotope = EDB["Pb208"]
Bi209: Isotope = EDB["Bi209"]
Th230: Isotope = EDB["Th230"]
Th232: Isotope = EDB["Th232"]
Pa231: Isotope = EDB["Pa231"]
U234: Isotope = EDB["U234"]
U235: Isotope = EDB["U235"]
U238: Isotope = EDB["U238"]

