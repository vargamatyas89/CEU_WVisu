"""
Registration and aggregation of the country/region modules (each country/region lives in its own source file:
hungary.py, romania.py, slovakia.py, austria.py, croatia.py, serbia.py, slovenia.py, zakarpattia.py, germany_danube.py, bulgaria.py)
"""

from . import austria
from . import bulgaria
from . import croatia
from . import germany_danube
from . import hungary
from . import romania
from . import serbia
from . import slovakia
from . import slovenia
from . import zakarpattia

REGISTERED_COUNTRY_MODULES = [
    hungary,
    romania,
    slovakia,
    austria,
    croatia,
    serbia,
    slovenia,
    zakarpattia,
    germany_danube,
    bulgaria,
]

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
