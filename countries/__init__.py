"""
Ország-modulok regisztrációja és összesítése (Minden ország külön forrásfájlban:
hungary.py, romania.py, slovakia.py, austria.py, croatia.py, serbia.py)
"""

from . import austria
from . import croatia
from . import hungary
from . import romania
from . import serbia
from . import slovakia

REGISTERED_COUNTRY_MODULES = [hungary, romania, slovakia, austria, croatia, serbia]

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
