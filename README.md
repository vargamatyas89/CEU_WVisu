# WVis — Central European & Danube Basin Interactive Hydrological Map

Interactive web application for visualizing real-time water levels and 1–7 day weather-coupled water level forecasts across **6 Central European & Danube Basin countries** (**Hungary, Romania, Slovakia, Austria, Croatia, and Serbia**), covering **363 gauging stations** across **33 catchments** (231 major river/lake gauges and 132 smaller creeks, streams, canals, and reservoirs).

Built with a **zero-dependency Python 3 standard-library backend** (`server.py`) and a **vanilla HTML5 / CSS3 / JavaScript + Leaflet frontend** with 100% free, open-source topographic basemaps and a modular per-country file architecture.

---

## Features

- **Interactive 6-Country Hydrographic Map (`HU • RO • SK • AT • HR • RS`)**:
  - Distinct color-coded national borders and an exterior dim mask framing all six countries.
  - High-resolution vector river reaches and lake polygons dynamically styled in color and stroke weight according to current or forecasted flood alert stages (*Kisvíz*, *Normál*, *Emelkedett*, *I. fok*, *II. fok*, *III. fok*).
  - Dedicated toggle and filter for **smaller waters** (*kisvízfolyások, patakok, főcsatornák, tározók*) alongside major rivers and lakes.
- **Instant Hover Tooltip Cards & Pinned Inspector**:
  - Hovering over any river reach, lake, or station marker displays a floating Hungarian-language hydrological card with official water level (`cm`), 24-hour change (`cm`), trend indicator (*Áradó / Apadó / Stagnáló*), discharge (`m³/s`), water temperature (`°C`), flood threshold progress bar (`LKV`, `I.–III. fok`, `LNV`), catchment rainfall/temperature, and an embedded **7-day SVG sparkline hydrograph** with a shaded `± cm` uncertainty cone.
  - Clicking any reach, lake, or station pins its detailed card to the right-hand inspector sidebar.
- **Real-Time 0–7 Day Forecast Timeline Slider & Weather Scenario Simulator**:
  - Scrub seamlessly across **Ma (0.) to +7 nap** or press **▶ Lejátszás** to animate wave propagation across all 363 reaches in real time.
  - Coupled hydrological forecasting combines official 6-day OVF predictions with **Open-Meteo** daily precipitation/evapotranspiration and **Copernicus GloFAS v4** (5 km grid) river discharge forecasts.
  - Interactive client-side weather scenarios: live baseline forecast, `+50 mm` intense catchment rainfall, `+120 mm` extreme cyclone/flood wave, and prolonged drought.
- **100% Free & Open-Source Topographic Basemaps (No API Key Required)**:
  - **OpenTopoMap** (SRTM elevation contours & hillshading — default)
  - **CyclOSM / OSM France** (hillshaded relief & hydrography)
  - **OpenStreetMap HOT** (high-contrast humanitarian style)
  - **OpenStreetMap Standard** (ODbL)
  - **100% Offline Vector Mode** (disables raster tiles completely)
- **Adaptive Light & Dark Theme**:
  - Honors OS `prefers-color-scheme` automatically with a manual **◐ Téma** toggle and adaptive tile shading.

---

## Country Coverage & Modular Architecture

Each country is isolated in its own backend telemetry/station module (`countries/<country>.py`) and frontend vector geometry module (`static/countries/<country>_geo.js`):

| Country | Code | Border Color | Catchments | Total Stations | Major Rivers / Lakes | Smaller Waters (Creeks / Canals) | Primary Live Telemetry Sources |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| 🇭🇺 **Hungary** (*Magyarország*) | `HU` | `#fbbf24` | 11 | **108** | 64 | 44 | OVF `hydroinfo.hu` (`44xxxx` + 6-day forecasts), OVF `vizugy.hu` (`OperativVizallas`), GloFAS v4 |
| 🇷🇴 **Romania** (*Románia*) | `RO` | `#c084fc` | 6 | **78** | 56 | 22 | INHGA via `hydroinfo.hu` (`74xxxx`), Open-Meteo & GloFAS v4 |
| 🇸🇰 **Slovakia** (*Szlovákia*) | `SK` | `#22d3ee` | 4 | **45** | 27 | 18 | SHMÚ via `hydroinfo.hu` (`14xxxx`), Open-Meteo & GloFAS v4 |
| 🇦🇹 **Austria** (*Ausztria*) | `AT` | `#fb7185` | 4 | **41** | 26 | 15 | eHYD via `hydroinfo.hu` (`24xxxx`), Open-Meteo & GloFAS v4 |
| 🇭🇷 **Croatia** (*Horvátország*) | `HR` | `#a3e635` | 4 | **45** | 27 | 18 | DHMZ `hidro.dhz.hr` (live automatic gauges), `hydroinfo.hu` (`54xxxx`), GloFAS v4 |
| 🇷🇸 **Serbia** (*Szerbia*) | `RS` | `#818cf8` | 4 | **46** | 31 | 15 | RHMZ `hidmet.gov.rs` (`stanje_voda.php`), `hydroinfo.hu` (`54xxxx`), GloFAS v4 |
| **Total** | **6** | — | **33** | **363** | **231** | **132** | **~294 live real-time gauges + 47 official 6-day OVF forecasts** |

---

## Live Data Sources

Because official national hydrological portals serve ISO-8859-2 / UTF-8 HTML tables without permissive CORS headers, `server.py` aggregates, caches (15-minute TTL), and normalizes them into JSON:

1. **OVF Hydroinfo (`https://www.hydroinfo.hu/`)**:
   - `dunhif_a.html`, `tishif_a.html`, `tohid.html` — live Danube, Tisza, and lake measurements across `HU` (`44xxxx`), `RO` (`74xxxx`), `SK` (`14xxxx`), `AT` (`24xxxx`), `HR`/`RS` (`54xxxx`).
   - `dunelotH.html`, `tiselotH.html` — official 6-day hydrological forecasts with `± cm` confidence intervals.
2. **OVF Operative Water Levels (`https://www.vizugy.hu/`)**:
   - Live hourly telemetry arrays covering smaller Hungarian streams, creeks, main canals, backwaters, and reservoirs.
3. **DHMZ Croatia (`https://hidro.dhz.hr/hidroweb/skripte/hidrobazahtml.py?funkc=podaciautomatskih`)**:
   - Live automatic station water levels across the Danube, Drava, Mura, Sava, Kupa, Una, and Adriatic karst basins.
4. **RHMZ Serbia (`https://www.hidmet.gov.rs/latin/osmotreni/stanje_voda.php`)**:
   - Live water levels, 24-hour trends, discharges, and water temperatures across the Danube, Tisza, Sava, Drina, Lim, Morava, Ibar, Timok, and Banat/Vojvodina rivers.
5. **Open-Meteo Weather & Copernicus GloFAS v4 Flood APIs**:
   - Batched 8-day meteorological (`precipitation_sum`, `temperature_2m_max/min`, `et0_fao_evapotranspiration`, `wind_speed_10m_max`) and GloFAS v4 (`river_discharge`) forecasts across all 33 catchments.

---

## Project Structure

```text
.
├── server.py                      # Python 3 HTTP server, live scrapers, forecast engine & REST API
├── countries/
│   ├── __init__.py                # Registers and aggregates all country modules
│   ├── hungary.py                 # Hungary (HU) catchments & 108 stations
│   ├── romania.py                 # Romania (RO) catchments & 78 stations
│   ├── slovakia.py                # Slovakia (SK) catchments & 45 stations
│   ├── austria.py                 # Austria (AT) catchments & 41 stations
│   ├── croatia.py                 # Croatia (HR) catchments & 45 stations
│   └── serbia.py                  # Serbia (RS) catchments & 46 stations
├── static/
│   ├── index.html                 # Application shell, controls, legend & timeline dock
│   ├── styles.css                 # Responsive layout, light/dark theme tokens & slider styling
│   ├── app.js                     # Leaflet map engine, hover cards, SVG hydrograph & scenario logic
│   └── countries/
│       ├── hungary_geo.js         # Hungary border, river reaches & lake polygons
│       ├── romania_geo.js         # Romania border, river reaches & lake polygons
│       ├── slovakia_geo.js        # Slovakia border, river reaches & reservoir polygons
│       ├── austria_geo.js         # Austria border, river reaches & lake polygons
│       ├── croatia_geo.js         # Croatia border, river reaches & lake polygons
│       └── serbia_geo.js          # Serbia border, river reaches & lake polygons
├── PROMPT.md                      # Master engineering prompt describing the full specification
├── LICENSE                        # Apache License 2.0
└── README.md
```

---

## Quick Start

### Prerequisites
- **Python 3.9+** (no third-party `pip` packages required; uses only the Python standard library)
- Internet access for live telemetry scraping, Open-Meteo/GloFAS forecasts, and Leaflet/OSM tiles

### Run Locally

```bash
git clone https://github.com/vargamatyas89/CEU_WVisu.git
cd CEU_WVisu
python3 server.py
```

By default, the server pre-warms the live hydrological & meteorological cache and listens on **`http://localhost:8080`**. You can override the port with the `PORT` environment variable:

```bash
PORT=8090 python3 server.py
```

---

## Backend REST API

| Endpoint | Method | Description |
| :--- | :---: | :--- |
| `/` | `GET` | Serves the interactive frontend (`static/index.html`) |
| `/api/hydro-data` | `GET` | Returns cached (15-min TTL) JSON payload with metadata, 33 catchments, and 363 station 8-day timelines |
| `/api/refresh` | `GET` | Forces an immediate live refresh from all upstream hydrological and meteorological providers |

---

## Adding Another Country

Thanks to the modular design, adding a new country requires only:
1. Create `countries/<country>.py` exporting `COUNTRY_META`, `CATCHMENTS`, and `STATIONS`, and register it in `countries/__init__.py`.
2. Create `static/countries/<country>_geo.js` populating `window.COUNTRY_GEO_MODULES["<ISO2>"]` with `border`, `bounds`, `border_color`, `reaches`, and `lakes`.
3. Include the new `<script src="/countries/<country>_geo.js"></script>` tag and country filter/legend entry in `static/index.html` and border color variables in `static/styles.css`.

---

## License

Licensed under the [Apache License 2.0](LICENSE). Open-source map tiles are attributed to OpenStreetMap contributors (ODbL), OpenTopoMap (CC-BY-SA), and CyclOSM / OSM France.
