from .cls import Isotope, Element
import json
import pathlib

from .cls import ElementDB

with open(pathlib.Path(__file__).parent / "element_data.json") as f:
    db = json.load(f)
EDB = ElementDB(db)

__all__ = ['Isotope', 'Element', 'EDB']
