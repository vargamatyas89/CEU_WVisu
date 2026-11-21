# Master Prompt: Interactive Hungarian Hydrological Map & 7-Day Weather-Coupled Water Level Forecast Application

You can copy and use the prompt below with any coding LLM or AI agent to generate or extend this full-stack application.

---

```markdown
Role & Objective:
You are a Senior Full-Stack Geospatial & Hydrological Web Engineer. Build a complete, production-ready web application (lightweight Python or Node.js backend + modern HTML5/CSS3/JavaScript interactive frontend) that displays Hungary's national borders and interactive hydrographic map (rivers and lakes), shows official water level measurements on hover, and provides a real-time 1–7 day forecast slider driven by official hydrological forecasts and live meteorological data.

All user-facing UI text, labels, tooltips, alerts, and legends MUST be in Hungarian.

---

### 1. System Architecture & Live Data Sources

Because official Hungarian hydrological endpoints (`hydroinfo.hu` / `vizugy.hu`) do not send permissive CORS headers for direct browser `fetch()` requests and serve ISO-8859-2 encoded HTML tables, implement a two-tier architecture:

1. **Lightweight Backend Server (`server.py` or `server.js`)**:
   - Serves the frontend static assets (`index.html`, `styles.css`, `app.js`, `hungary_geo.js`) and exposes a JSON REST API (`/api/hydro-data` and `/api/refresh`).
   - Scrapes and parses live official hydrological observations from the Hungarian National Hydrological Forecasting Service (Országos Vízjelző Szolgálat - OVF / `hydroinfo.hu`):
     - Danube basin current observations: `https://www.hydroinfo.hu/tables/dunhif_a.html`
     - Tisza basin current observations: `https://www.hydroinfo.hu/tables/tishif_a.html`
     - Major Hungarian lakes (Balaton, Velencei-tó, Fertő-tó): `https://www.hydroinfo.hu/tables/tohid.html`
     - Official OVF 6-day water level predictions (`cm` and `± cm` confidence intervals): `https://www.hydroinfo.hu/tables/dunelotH.html` and `https://www.hydroinfo.hu/tables/tiselotH.html`
   - Queries the **Open-Meteo Weather Forecast API** (`https://api.open-meteo.com/v1/forecast`) and **Open-Meteo GloFAS Flood API** (`https://flood-api.open-meteo.com/v1/flood`) for 7-day daily precipitation (`precipitation_sum`), max/min temperature (`temperature_2m_max`), evapotranspiration (`et0_fao_evapotranspiration`), and river discharge (`river_discharge`) across Hungary's primary catchment basins.
   - Implements a **Coupled Hydro-Meteorological Forecast Engine**:
     - For stations with official OVF 1–6 day predictions, anchors Days +1 to +6 to the official OVF forecast and extrapolates Day +7 using Open-Meteo GloFAS discharge trends and catchment precipitation.
     - For tributary stations and lakes without direct 6-day OVF table entries, computes Days +1 to +7 water level projections (`cm`) and uncertainty bands (`± cm`) from current 24h momentum, upstream wave propagation lag, catchment precipitation (`mm`), and evapotranspiration.
     - Supports interactive weather scenario modifiers on the client (e.g., Baseline live Open-Meteo forecast, Intense catchment rainfall +50 mm, Extreme cyclone +120 mm, Prolonged drought) that recalculate the 1–7 day river response in real time.
   - Includes a built-in fallback dataset so the application remains 100% functional even if upstream servers are temporarily unreachable.

---

### 2. Interactive Map & Cartographic Requirements

1. **Hungary National Border (`Magyarország államhatára`)**:
   - Render a high-resolution GeoJSON polygon of Hungary's national borders with a glowing boundary stroke and a subtle exterior mask outside Hungary to focus visual attention on the country's hydrography.
2. **Hydrographic Network (Rivers & Lakes)**:
   - Include high-precision vector geometries clipped to Hungary for:
     - **Major Rivers**: Duna, Tisza, Dráva, Mura, Rába, Mosoni-Duna, Lajta, Ráckevei-Soroksári Duna, Zala, Sió, Kapos, Ipoly, Zagyva, Tarna, Sajó, Bódva, Hernád, Bodrog, Szamos, Kraszna, Berettyó, Sebes-Körös, Fekete-Körös, Fehér-Körös, Kettős-Körös, Hármas-Körös, Hortobágy-Berettyó, Maros.
     - **Major Lakes**: Balaton, Velencei-tó, Tisza-tó, Fertő-tó.
   - Divide rivers into logical **hydrological reaches (folyószakaszok)**, each associated with its governing official OVF gauging station (vízmérce).
3. **Dynamic Visual Encoding (Color & Stroke Thickness)**:
   - Dynamically color and scale the thickness of each river reach, lake polygon, and station marker based on its water level status at the selected forecast day:
     - **Kisvíz / Aszályos szint** (Low water / Drought): Cyan/Amber-tinted thin line
     - **Normál vízjárás** (Normal water level): Vibrant Hydro Blue (`#38bdf8` / `#0284c7`), normal stroke width
     - **Emelkedett vízszint** (Elevated water level, approaching Alert I): Teal/Emerald (`#10b981`), medium-thick stroke
     - **I. fokú árvízi készültség** (Flood Alert Level I): Yellow/Amber (`#f59e0b`), thick stroke with subtle pulse
     - **II. fokú árvízi készültség** (Flood Alert Level II): Orange (`#f97316`), very thick stroke
     - **III. fokú árvízi készültség / Rekordközeli** (Flood Alert Level III): Crimson Red (`#ef4444`), maximum stroke width + glowing halo

---

### 3. Interactive Hover Tooltip Card & Station Inspector

When the user moves the cursor over any river reach, lake, or station marker:
1. Highlight the hovered river segment and station marker immediately.
2. Display a floating **Hydrological Hover Card (Hidrológiai Adatlap)** that tracks the cursor smoothly without clipping outside the viewport, showing:
   - **Header**: Water body name, reach name, official station name, OVF station code (`Állomáskód`), and river kilometer (`fkm`).
   - **Primary Metrics**:
     - Water level (`cm`) for the active slider day (`Ma` or `+1..+7 nap`), with confidence interval (`± cm`) for forecast days.
     - Change relative to today (`Δ cm`) and 24-hour trend badge (`Áradó ▲`, `Apadó ▼`, `Stagnáló ▬`).
     - Water discharge (`m³/s`) and morning water temperature (`°C`).
   - **Official Flood Threshold Progress Bar**:
     - Visual gauge comparing the current/forecast water level (`cm`) against `LKV` (lowest recorded), `I. fok`, `II. fok`, `III. fok` flood alert thresholds, and `LNV` (highest recorded).
   - **Catchment Weather Forecast Summary**:
     - Expected daily precipitation (`mm`), cumulative precipitation up to the selected day (`mm`), and temperature (`°C`) from Open-Meteo.
   - **Embedded 7-Day Mini Hydrograph (SVG Sparkline)**:
     - Plots the water level trajectory from Day 0 (Today) through Day +7, shades the `± cm` confidence interval cone, marks the I/II/III flood alert threshold lines, and highlights the currently selected day with a vertical marker dot.
3. Clicking a station or river reach pins its full hydrological report into the sidebar inspector panel.

---

### 4. Real-Time 0–7 Day Forecast Slider & Controls

1. **Interactive Timeline Slider (`0–7 nap`)**:
   - Provide a native `<input type="range" min="0" max="7" step="1">` control with day ticks (`Ma (Aktuális)`, `+1 nap`, `+2 nap`, `+3 nap`, `+4 nap`, `+5 nap`, `+6 nap`, `+7 nap`) and exact calendar dates.
   - Moving the slider (`input` event) must update the entire map (river reach colors, line thicknesses, station badges, open hover card, and sidebar summary statistics) at 60 FPS with zero network lag.
   - Include an **Auto-Play / Animation button (`Lejátszás / Szünet`)** that cycles through Days 0 → 7 automatically to visualize flood wave propagation down the Danube and Tisza.
2. **Weather Forecast Scenario Selector**:
   - Allow switching between:
     - `Valós Open-Meteo előrejelzés` (Live 7-day meteorological forecast)
     - `+50 mm Csapadékhullám` (Simulated intense rainfall across catchments)
     - `+120 mm Extrém ciklon / Árhullám` (Simulated extreme flood wave stress test)
     - `Tartós szárazság / Aszály` (Simulated dry/drought recession)
3. **Filter & Search Toolbar**:
   - Filter by water basin (`Összes vízgyűjtő`, `Duna-vízgyűjtő`, `Tisza-vízgyűjtő`, `Dráva és Mura`, `Nagy tavak`), search stations by name/river, and toggle map layers (station markers, river labels, catchment weather overlay, light/dark cartographic theme).

---

### 5. Modern Web Standards & UI Polish

- Include `<meta name="color-scheme" content="light dark">` in `<head>` and `color-scheme: light dark` on `:root`, using glassmorphic HUD panels that adapt cleanly between dark and light themes.
- Style the native `<input type="range">` using custom CSS properties (`--control-value`, `--attr-min`, `--attr-max`, `--slider-progress`) with separate `::-webkit-slider-*` and `::-moz-range-*` rule blocks and visible `:focus-visible` outlines.
- Ensure keyboard accessibility, responsive layout, and Hungarian number/date formatting (`Intl.DateTimeFormat('hu-HU')`).
```
