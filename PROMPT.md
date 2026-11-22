# Fluvio — Master Prompt: Interactive Central Europe, Danube Basin & Zakarpattia (HU, RO, SK, AT, HR, RS, SI, UA-ZK) Hydrological Map & 7-Day Weather-Coupled Water Level Forecast Application

You can copy and use the prompt below with any coding LLM or AI agent to generate or extend this full-stack application.

---

```markdown
Role & Objective:
You are a Senior Full-Stack Geospatial & Hydrological Web Engineer. Build a complete, production-ready web application (lightweight Python or Node.js backend + modern HTML5/CSS3/JavaScript interactive frontend) that displays the national borders and interactive hydrographic map (major rivers, minor creeks/streams/canals, and lakes) of Hungary (Magyarország), Romania (Románia), Slovakia (Szlovákia), Austria (Ausztria), Croatia (Horvátország), Serbia (Szerbia), Slovenia (Szlovénia), and Zakarpattia Oblast / Kárpátalja (Ukraine — scoped strictly to the Carpathian Basin Upper Tisza headwaters), shows official water level measurements on hover, and provides a real-time 1–7 day forecast slider driven by official hydrological forecasts and live meteorological data.

Support an interactive UI language switcher covering all represented countries'/regions' languages plus English (`hu`, `en`, `ro`, `sk`, `de`, `hr`, `sr`, `sl`, `uk`), defaulting to Hungarian.

---

### 1. System Architecture & Live Data Sources

Because official Danube Basin hydrological endpoints (`hydroinfo.hu` / `vizugy.hu` / INHGA / SHMÚ / eHYD / DHMZ `hidro.dhz.hr` / RHMZ `hidmet.gov.rs` / ARSO `arso.gov.si`) do not send permissive CORS headers for direct browser `fetch()` requests and serve ISO-8859-2 / UTF-8 HTML tables, implement a two-tier architecture:

1. **Lightweight Backend Server (`server.py`) & Modular Country Definitions (`countries/`)**:
   - Store each country's hydrological stations, catchments, and metadata in its own dedicated source file:
     - Backend modules:
       - `countries/hungary.py` (108 stations: 64 major river/lake gauges + 44 smaller creeks, streams, canals, backwaters, and reservoirs)
       - `countries/romania.py` (78 stations: 56 major river/lake gauges + 22 smaller mountain rivers and tributaries)
       - `countries/slovakia.py` (45 stations: 27 major river/reservoir gauges + 18 smaller Carpathian streams and tributaries, linked to SHMÚ `14xxxx` codes)
       - `countries/austria.py` (41 stations: 26 major Alpine river/lake gauges + 15 smaller Alpine streams and tributaries, linked to eHYD `24xxxx` codes)
       - `countries/croatia.py` (45 stations: 27 major river/lake gauges + 18 smaller Slavonian/karst streams and tributaries, linked to live DHMZ `hidro.dhz.hr` `dhmz_id` and `54xxxx` codes)
       - `countries/serbia.py` (46 stations: 31 major river/lake gauges + 15 smaller Vojvodina/Central Serbian rivers and DTD canals, linked to live RHMZ `hidmet.gov.rs` `rhmz_id` and `54xxxx` codes)
       - `countries/slovenia.py` (37 stations: 22 major river/lake gauges + 15 smaller Alpine/Karst streams, linked to live ARSO `arso.gov.si/xml/vode/hidro_podatki_zadnji.xml` `arso_id` and `546102`)
       - `countries/zakarpattia.py` (24 stations: 15 major Upper Tisza/Latorca/Ung/Borzsa/Nagyág/Synevyr stations + 9 smaller Carpathian streams and Bereg canals, driven by GloFAS v4 + Open-Meteo and calibrated against live cross-border OVF/SHMÚ/INHGA gauges)
       - Aggregated by `countries/__init__.py` (424 stations total across 40 catchments).
     - Frontend vector geometry modules:
       - `static/countries/hungary_geo.js` (`window.COUNTRY_GEO_MODULES["HU"]`)
       - `static/countries/romania_geo.js` (`window.COUNTRY_GEO_MODULES["RO"]`)
       - `static/countries/slovakia_geo.js` (`window.COUNTRY_GEO_MODULES["SK"]`)
       - `static/countries/austria_geo.js` (`window.COUNTRY_GEO_MODULES["AT"]`)
       - `static/countries/croatia_geo.js` (`window.COUNTRY_GEO_MODULES["HR"]`)
       - `static/countries/serbia_geo.js` (`window.COUNTRY_GEO_MODULES["RS"]`)
       - `static/countries/slovenia_geo.js` (`window.COUNTRY_GEO_MODULES["SI"]`)
       - `static/countries/zakarpattia_geo.js` (`window.COUNTRY_GEO_MODULES["UA"]`)
   - Serves the frontend static assets (`index.html`, `styles.css`, `app.js`, `countries/*_geo.js`) and exposes a JSON REST API (`/api/hydro-data` and `/api/refresh`).
   - Scrapes and parses live official hydrological observations from TWO official Hungarian portals plus Copernicus GloFAS v4:
     - **OVF `hydroinfo.hu`** (`dunhif_a.html`, `tishif_a.html`, `tohid.html`, `dunelotH.html`, `tiselotH.html`) for primary Hungarian (`44xxxx`) and Romanian (`74xxxx`) river gauges and 6-day official forecasts.
     - **OVF Operative Water Level Portal `https://www.vizugy.hu/` (`OperativVizallas` JS telemetry arrays)**: parses live hourly measurements (`Vizallas`, `Vizhozam`, `Vizho`, `LKV`, `LNV`, `UtolsoMeresIdopontja`) across 272 operative gauges covering smaller Hungarian streams, creeks, main canals, and reservoirs (`Által-ér`, `Gaja-patak`, `Cuhai-Bakony-ér`, `Császár-víz`, `Torna-patak`, `Gyöngyös-patak`, `Arany-patak`, `Ikva-patak`, `Sorok-Perint`, `Pinka`, `Répce`, `Rábca`, `Marcal`, `Kerka`, `Kebele-patak`, `Principális-csatorna`, `Hanság-főcsatorna`, `Nádor-csatorna`, `Nyugati-övcsatorna`, `Tetves-patak`, `Keleti-Bozót-csatorna`, `Koppány-patak`, `Völgységi-patak`, `Rinya-patak`, `Bükkösdi-víz`, `Fekete-víz`, `Karasica`, `Baranya-csatorna`, `Szentendrei-Duna`, `Kemence-patak`, `Zagyva-patak / Maconkai-tározó`, `Galga-patak`, `Eger-patak`, `Bán-patak`, `Takta`, `Lónyay-főcsatorna`, `Keleti-főcsatorna`, `Nagykunsági-főcsatorna`, `Jászsági-főcsatorna`, `Duna-völgyi-főcsatorna`, `Kösely-főcsatorna`, `Királyhegyesi-Száraz-ér`, `Gyálai Holt-Tisza`, `Tatai Öreg-tó`).
     - **Copernicus EFAS / Open-Meteo GloFAS v4 (0.05° / 5 km grid) & INHGA (`74xxxx`)** for smaller Romanian rivers and mountain streams (`Csigér / Cigher`, `Kis-Szamos / Someșul Mic` at Kolozsvár, `Nagy-Szamos / Someșul Mare` at Beszterce, `Aranyos / Arieș` at Torda, `Kis-Küküllő / Târnava Mică` at Dicsőszentmárton, `Feketeügy / Râul Negru` at Kézdivásárhely, `Cibin` at Nagyszeben, `Sebes / Sebeș`, `Berzava / Bârzava` at Resicabánya, `Karas / Caraș`, `Cserna / Cerna` at Herkulesfürdő, `Dâmbovița` at Bukarest, `Prahova` at Ploiești, `Vedea` at Alexandria, `Tatros / Trotuș` at Ónfalva, `Bârlad` at Vaslui, `Suceava`).
     - Danube basin & Romanian Lower Danube (`Báziás / Baziaș` → `Orsova / Orșova` → `Szörényvár / Turnu Severin` → `Calafat` → `Corabia` → `Turnu Măgurele` → `Gyurgyevó / Giurgiu` → `Călărași` → `Cernavodă` → `Brăila` → `Galac / Galați` → `Tulcea` → `Sulina`): `https://www.hydroinfo.hu/tables/dunhif_a.html`
     - Tisza basin & Transylvanian/Partium rivers (`Máramarossziget / Sighetu Marmației`, `Visó / Vișeu`, `Iza`, `Túr / Tur`, `Szamos / Someș`: Dés, Sülelmed, Szatmárnémeti; `Lápos / Lăpuș`, `Kraszna / Crasna`, `Berettyó / Barcău`: Szilágynagyfalu, Szalárd; `Sebes-Körös / Crișul Repede`: Csucsa, Nagyvárad; `Fekete-Körös / Crișul Negru`: Belényes, Tenke, Nagyzerénd; `Fehér-Körös / Crișul Alb`: Honctő, Kisjenő; `Maros / Mureș`: Gyulafehérvár, Branyicska/Déva, Soborsin, Arad, Nagylak; `Sztrigy / Strei`): `https://www.hydroinfo.hu/tables/tishif_a.html`
     - Major Hungarian lakes (`Balaton`, `Velencei-tó`, `Fertő-tó`): `https://www.hydroinfo.hu/tables/tohid.html`
     - Official OVF 6-day water level predictions (`cm` and `± cm` confidence intervals): `https://www.hydroinfo.hu/tables/dunelotH.html` and `https://www.hydroinfo.hu/tables/tiselotH.html`
   - Includes additional INHGA reference stations for Romania's extra-Carpathian and interior basins (`Olt`: Sepsiszentgyörgy, Râmnicu Vâlcea, Slatina; `Zsil / Jiu`: Craiova; `Argeș`: Pitești; `Ialomița`: Slobozia; `Bodza / Buzău`; `Szeret / Siret`: Roman, Focșani/Lungoci; `Aranyos-Beszterce / Bistrița`: Karácsonkő / Piatra Neamț; `Prut`: Ungheni/Jászvásár; `Temes / Timiș`: Lugos; `Béga / Bega`: Temesvár; `Nagy-Küküllő / Târnava Mare`: Medgyes; `Felső-Maros`: Marosvásárhely; plus major Romanian lakes: `Razim–Sinoe-tó`, `Békási-tó / Lacul Bicaz`, `Vidraru-tó`).
   - Queries the **Open-Meteo Weather Forecast API** (`https://api.open-meteo.com/v1/forecast`) and **Open-Meteo GloFAS Flood API** (`https://flood-api.open-meteo.com/v1/flood`) in a single batched coordinate request for 7-day daily precipitation (`precipitation_sum`), max/min temperature (`temperature_2m_max`), evapotranspiration (`et0_fao_evapotranspiration`), and river discharge (`river_discharge`) across 17 catchment basins covering Hungary and Romania.
   - Implements a **Coupled Hydro-Meteorological Forecast Engine**:
     - For stations with official OVF 1–6 day predictions, anchors Days +1 to +6 to the official OVF forecast and extrapolates Day +7 using Open-Meteo GloFAS discharge trends and catchment precipitation.
     - For stations and lakes without direct 6-day OVF table entries, computes Days +1 to +7 water level projections (`cm`) and uncertainty bands (`± cm`) from current 24h momentum, upstream wave propagation lag, catchment precipitation (`mm`), and GloFAS river discharge ratios.
     - Supports interactive weather scenario modifiers on the client (Baseline live Open-Meteo forecast, Intense catchment rainfall +50 mm, Extreme cyclone +120 mm, Prolonged drought) that recalculate the 1–7 day river response in real time.

---

### 2. Interactive Map & Cartographic Requirements

0. **100% Free & Open-Source Topographic Basemaps (No API Key Required)**:
   - Use strictly free, open-source community tile providers (ODbL / CC-BY-SA) with an interactive switcher in the map legend:
     - **OpenTopoMap** (`https://{s}.tile.opentopomap.org/{z}/{x}/{y}.png`): Real SRTM elevation contour lines, hillshading, and OpenStreetMap topography (default).
     - **CyclOSM / OpenStreetMap France** (`https://{s}.tile-cyclosm.openstreetmap.fr/cyclosm/{z}/{x}/{y}.png`): Hillshaded terrain and hydrography.
     - **OpenStreetMap HOT** (`https://{s}.tile.openstreetmap.fr/hot/{z}/{x}/{y}.png`): High-contrast humanitarian style.
     - **OpenStreetMap Standard** (`https://tile.openstreetmap.org/{z}/{x}/{y}.png`): Official OSM Foundation tiles.
     - **100% Offline Vector Mode**: Option to turn off external raster tiles completely and display only the embedded GeoJSON borders, lakes, and river reaches.

1. **Hungary & Romania National Borders (`Magyarország és Románia államhatára`)**:
   - Render high-resolution GeoJSON polygons of both Hungary's national borders (`#fbbf24` gold) and Romania's national borders (`#c084fc` violet) with glowing boundary strokes and a dual-cutout exterior dim mask outside Hungary and Romania.
   - Provide a Country / Region selector (`🇭🇺 + 🇷🇴 Magyarország és Románia`, `🇭🇺 Magyarország`, `🇷🇴 Románia`) that filters stations and smoothly flies/zooms the map to the selected country or the combined region.
2. **Hydrographic Network (112 River Reaches & 8 Lake Basins across HU & RO)**:
   - Include high-precision vector geometries clipped to Hungary and Romania for:
     - **Hungary & Transboundary Rivers**: Duna, Tisza, Dráva, Mura, Rába, Mosoni-Duna, Lajta, Ráckevei-Soroksári Duna, Zala, Sió, Kapos, Ipoly, Zagyva, Tarna, Sajó, Bódva, Hernád, Bodrog, Szamos, Kraszna, Túr, Berettyó, Sebes-Körös, Fekete-Körös, Fehér-Körös, Kettős-Körös, Hármas-Körös, Hortobágy-Berettyó, Maros.
     - **Romania Rivers & Delta**: Al-Duna & Duna-delta (Chilia, Sulina, Sf. Gheorghe, Borcea branches), Visó (Vișeu), Iza, Lápos (Lăpuș), Nagy-Küküllő (Târnava Mare), Sztrigy (Strei), Béga (Bega), Temes (Timiș), Olt, Zsil (Jiu), Argeș, Ialomița, Bodza (Buzău), Szeret (Siret) & tributaries (Moldova, Tatros/Trotuș, Bârlad), Aranyos-Beszterce (Bistrița), Prut.
     - **Major Lakes**: Balaton (East & West basins), Velencei-tó, Tisza-tó, Fertő-tó, Razim–Sinoe-tó, Békási-tó (Lacul Bicaz), Vidraru-tó.
3. **Dynamic Visual Encoding (Color & Stroke Thickness)**:
   - Dynamically color and scale the thickness of each river reach, lake polygon, and station marker based on its water level status at the selected forecast day:
     - **Kisvíz / Aszályos szint** (`#06b6d4`)
     - **Normál vízjárás** (`#38bdf8`)
     - **Emelkedett vízszint** (`#10b981`)
     - **I. fokú árvízi készültség** (`#f59e0b`)
     - **II. fokú árvízi készültség** (`#f97316`)
     - **III. fokú árvízi készültség** (`#ef4444`)

---

### 3. Interactive Hover Tooltip Card & 0–7 Day Real-Time Slider

1. Hovering over any river reach, lake, or station marker displays a floating Hungarian hydrological card showing:
   - Country tag (`HU` / `RO`), water body name, reach name, official station name, station code (`Állomáskód`), and river kilometer (`fkm`).
   - Water level (`cm`) for the active slider day (`Ma` or `+1..+7 nap`), confidence interval (`± cm`), change relative to today (`Δ cm`), 24-hour trend badge (`Áradó ▲`, `Apadó ▼`, `Stagnáló ▬`), discharge (`m³/s`), and morning water temperature (`°C`).
   - Official flood threshold progress bar (`LKV`, `I. fok`, `II. fok`, `III. fok`, `LNV`).
   - Catchment weather forecast (`mm` precipitation, `°C` temperature) and an embedded 7-day SVG sparkline hydrograph with shaded `± cm` confidence cone.
2. Provide a native `<input type="range" min="0" max="7" step="1">` timeline slider with calendar date ticks and an Auto-Play (`Lejátszás / Szünet`) animation button that updates all 120 reaches across Hungary and Romania in real time.
```
