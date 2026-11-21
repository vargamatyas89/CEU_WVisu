"""
Ország-modulok regisztrációja és összesítése (Minden ország külön forrásfájlban: hungary.py, romania.py)
"""

from . import hungary
from . import romania

REGISTERED_COUNTRY_MODULES = [hungary, romania]

COUNTRIES_META = {
    mod.COUNTRY_META["code"]: mod.COUNTRY_META
    for mod in REGISTERED_COUNTRY_MODULES
}

CATCHMENTS = {}
for mod in REGISTERED_COUNTRY_MODULES:
    CATCHMENTS.update(mod.CATCHMENTS)

STATIONS_CATALOG = []
for mod in REGISTERED_COUNTRY_MODULES:
    STATIONS_CATALOG.extend(mod.STATIONS)
