/**
 * WVis — Magyarország és Románia Interaktív Víztérképe és 1–7 Napos Vízállás-Előrejelzése
 * Client-side Interactive Cartography, Real-Time Forecast Slider & Hydrograph Engine
 */

(() => {
  "use strict";

  // Application State
  const state = {
    payload: null,
    stationsByCode: new Map(),
    activeDay: 0,
    scenario: "live", // 'live' | 'rain50' | 'rain120' | 'drought'
    countryFilter: "all", // 'all' | 'HU' | 'RO'
    basinFilter: "all",
    searchQuery: "",
    hoveredCode: null,
    pinnedCode: "442027", // Default pinned: Budapest (Duna)
    playTimer: null,
    showMinorWaters: true,
    showStations: true,
    showLabels: true,
    showBasemap: true,
    basemapSource: "opentopomap", // 'opentopomap' | 'cyclosm' | 'osm_hot' | 'osm_standard' | 'none'
    darkMode: window.matchMedia("(prefers-color-scheme: dark)").matches,
  };

  // Geographic Bounds for Quick Zoom
  const REGION_BOUNDS = {
    all: [
      [43.58, 16.05],
      [48.62, 29.75],
    ],
    HU: [
      [45.72, 16.08],
      [48.60, 22.92],
    ],
    RO: [
      [43.60, 20.22],
      [48.28, 29.72],
    ],
  };

  // Alert Level Colors
  const ALERT_COLORS = {
    low: "#06b6d4",
    normal: "#38bdf8",
    elevated: "#10b981",
    deg1: "#f59e0b",
    deg2: "#f97316",
    deg3: "#ef4444",
  };

  // DOM References
  const sliderEl = document.getElementById("forecast-day-slider");
  const ticksContainer = document.getElementById("slider-ticks-container");
  const dayBadgeEl = document.getElementById("slider-day-badge");
  const weatherPillEl = document.getElementById("slider-weather-summary");
  const hoverCardEl = document.getElementById("hydro-hover-card");
  const pinnedPanelEl = document.getElementById("pinned-station-panel");
  const stationListEl = document.getElementById("station-list");
  const stationCountBadge = document.getElementById("station-count-badge");
  const playBtn = document.getElementById("btn-play-timeline");
  const countrySelect = document.getElementById("country-filter");
  const basinSelect = document.getElementById("basin-filter");
  const scenarioSelect = document.getElementById("weather-scenario");
  const searchInput = document.getElementById("station-search");
  const refreshBtn = document.getElementById("btn-refresh");
  const themeBtn = document.getElementById("btn-theme-toggle");

  // KPI Elements
  const kpiActiveDay = document.getElementById("kpi-active-day");
  const kpiActiveDate = document.getElementById("kpi-active-date");
  const kpiRisingCount = document.getElementById("kpi-rising-count");
  const kpiMaxRise = document.getElementById("kpi-max-rise");
  const kpiAlertCount = document.getElementById("kpi-alert-count");
  const kpiAlertDetail = document.getElementById("kpi-alert-detail");
  const kpiPrecipAvg = document.getElementById("kpi-precip-avg");
  const kpiTempAvg = document.getElementById("kpi-temp-avg");
  const metaSourceLabel = document.getElementById("meta-source-label");

  // Leaflet Map & Layer References
  let map = null;
  const openSourceTileLayers = {};
  const reachLayersByCode = new Map();
  const lakeLayersByCode = new Map();
  const stationMarkersByCode = new Map();

  // Sync Native Range Slider Custom Properties (modern-web-guidance: slider)
  function syncSliderCSSVariables() {
    sliderEl.style.setProperty("--attr-min", sliderEl.min || "0");
    sliderEl.style.setProperty("--attr-max", sliderEl.max || "7");
    sliderEl.style.setProperty("--control-value", sliderEl.value);
  }

  // Format Hungarian Date String
  function formatHuDate(isoDateStr) {
    if (!isoDateStr) return "";
    try {
      const [y, m, d] = isoDateStr.split("-").map(Number);
      const dt = new Date(y, m - 1, d);
      return new Intl.DateTimeFormat("hu-HU", {
        month: "short",
        day: "numeric",
        weekday: "short",
      }).format(dt);
    } catch {
      return isoDateStr;
    }
  }

  // Classify Alert Status dynamically when scenario modifiers apply
  function classifyAlert(levelCm, thresholds) {
    if (levelCm >= thresholds.deg3) {
      return { code: "deg3", label: "III. fokú árvízi készültség" };
    }
    if (levelCm >= thresholds.deg2) {
      return { code: "deg2", label: "II. fokú árvízi készültség" };
    }
    if (levelCm >= thresholds.deg1) {
      return { code: "deg1", label: "I. fokú árvízi készültség" };
    }
    const elevatedCutoff =
      thresholds.deg1 - Math.max(60, Math.round((thresholds.deg1 - thresholds.low) * 0.25));
    if (levelCm >= elevatedCutoff) {
      return { code: "elevated", label: "Emelkedett vízszint" };
    }
    if (levelCm <= thresholds.low) {
      return { code: "low", label: "Kisvíz / Alacsony vízállás" };
    }
    return { code: "normal", label: "Normál vízjárás" };
  }

  // Get Scenario-Adjusted Timeline Entry for a Station and Day Index (0..7)
  function getStationDayData(station, dayIdx) {
    const base = station.timeline[dayIdx] || station.timeline[0];
    if (dayIdx === 0 || state.scenario === "live") {
      return base;
    }

    let extraRainPerDay = 0;
    if (state.scenario === "rain50") extraRainPerDay = 50 / 7;
    if (state.scenario === "rain120") extraRainPerDay = 120 / 7;
    if (state.scenario === "drought") extraRainPerDay = -4.5;

    const lag = station.lag_days || 1;
    const respFactor = station.response_factor || 2.8;
    const effectiveDays = Math.max(0.4, dayIdx - lag * 0.45);

    let levelOffset = 0;
    if (state.scenario === "drought") {
      const span = Math.max(80, station.thresholds.deg1 - station.thresholds.low);
      levelOffset = -Math.round(effectiveDays * (station.basin === "tavak" ? 1.5 : span * 0.045));
    } else {
      const waveMultiplier = Math.pow(effectiveDays, 1.18) * respFactor * 0.92;
      levelOffset = Math.round(extraRainPerDay * waveMultiplier);
    }

    const adjLevel = base.level_cm + levelOffset;
    const prevAdj =
      dayIdx === 1
        ? station.timeline[0].level_cm
        : getStationDayData(station, dayIdx - 1).level_cm;
    const dailyChange = adjLevel - prevAdj;
    const deltaToday = adjLevel - station.timeline[0].level_cm;

    const addPrecip = state.scenario === "drought" ? -base.precip_mm : extraRainPerDay;
    const adjPrecip = Math.max(0, Number((base.precip_mm + addPrecip).toFixed(1)));
    const adjCumPrecip = Math.max(
      0,
      Number((base.cum_precip_mm + addPrecip * dayIdx).toFixed(1))
    );

    const span = Math.max(120, station.thresholds.deg1 - station.thresholds.low);
    const adjDischarge = Math.max(
      1,
      Number((base.discharge_m3s * Math.exp((levelOffset / span) * 0.75)).toFixed(1))
    );

    const alertInfo = classifyAlert(adjLevel, station.thresholds);

    return {
      ...base,
      level_cm: adjLevel,
      daily_change_cm: dailyChange,
      delta_from_today_cm: deltaToday,
      discharge_m3s: adjDischarge,
      precip_mm: adjPrecip,
      cum_precip_mm: adjCumPrecip,
      alert_level: alertInfo.code,
      alert_label: alertInfo.label,
    };
  }

  // Initialize Leaflet Map and 100% Free Open-Source Cartographic Layers
  function initMap() {
    map = L.map("map", {
      center: [46.25, 22.85],
      zoom: 6.4,
      zoomSnap: 0.25,
      minZoom: 5.5,
      maxZoom: 13,
      zoomControl: true,
    });

    map.fitBounds(REGION_BOUNDS.all, { padding: [24, 24] });

    // 1. OpenTopoMap (Open-Source Topographic & SRTM Relief Map — CC-BY-SA / ODbL)
    openSourceTileLayers.opentopomap = L.tileLayer(
      "https://{s}.tile.opentopomap.org/{z}/{x}/{y}.png",
      {
        attribution:
          'Alaptérkép: &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> (ODbL), SRTM | Stílus: &copy; <a href="https://opentopomap.org">OpenTopoMap</a> (CC-BY-SA)',
        subdomains: "abc",
        maxZoom: 17,
      }
    );

    // 2. CyclOSM / OpenStreetMap France (Open-Source Hillshaded Relief & Hydrography — ODbL / CC-BY-SA)
    openSourceTileLayers.cyclosm = L.tileLayer(
      "https://{s}.tile-cyclosm.openstreetmap.fr/cyclosm/{z}/{x}/{y}.png",
      {
        attribution:
          'Alaptérkép: &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>, <a href="https://github.com/cyclosm/cyclosm-cartocss-style">CyclOSM</a> (OSM France)',
        subdomains: "abc",
        maxZoom: 19,
      }
    );

    // 3. OpenStreetMap HOT (Humanitarian OpenStreetMap Team / OSM France — ODbL)
    openSourceTileLayers.osm_hot = L.tileLayer(
      "https://{s}.tile.openstreetmap.fr/hot/{z}/{x}/{y}.png",
      {
        attribution:
          'Alaptérkép: &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> közreműködők, HOT (OSM France)',
        subdomains: "abc",
        maxZoom: 19,
      }
    );

    // 4. OpenStreetMap Standard (Official OSM Foundation Tile Server — ODbL)
    openSourceTileLayers.osm_standard = L.tileLayer(
      "https://tile.openstreetmap.org/{z}/{x}/{y}.png",
      {
        attribution:
          'Alaptérkép: &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> közreműködők (ODbL)',
        maxZoom: 19,
      }
    );

    updateBasemapTheme();

    // Custom panes for strict z-index ordering
    map.createPane("maskPane").style.zIndex = 250;
    map.createPane("borderPane").style.zIndex = 350;
    map.createPane("lakePane").style.zIndex = 410;
    map.createPane("riverGlowPane").style.zIndex = 420;
    map.createPane("riverPane").style.zIndex = 440;
    map.createPane("stationPane").style.zIndex = 480;

    renderBordersAndGeography();
    map.on("zoomend", () => {
      renderStationMarkers();
    });
  }

  function updateBasemapTheme() {
    if (!map) return;
    const mapContainer = document.getElementById("map");
    if (mapContainer) {
      mapContainer.classList.toggle("dark-relief-tiles", state.darkMode);
      mapContainer.classList.toggle("light-relief-tiles", !state.darkMode);
    }

    for (const layer of Object.values(openSourceTileLayers)) {
      if (map.hasLayer(layer)) {
        map.removeLayer(layer);
      }
    }

    if (state.showBasemap && state.basemapSource !== "none") {
      const activeTileLayer =
        openSourceTileLayers[state.basemapSource] || openSourceTileLayers.opentopomap;
      activeTileLayer.addTo(map);
    }
  }

  // Render All Registered Country Modules (Borders, Lakes, and River Reaches from static/countries/*_geo.js)
  function renderBordersAndGeography() {
    const countryModules = Object.values(window.COUNTRY_GEO_MODULES || {});
    if (!countryModules.length) return;

    const worldRing = [
      [-85, -180],
      [85, -180],
      [85, 180],
      [-85, 180],
    ];
    const maskRings = [worldRing];

    for (const cMod of countryModules) {
      if (cMod.bounds && cMod.code) {
        REGION_BOUNDS[cMod.code] = cMod.bounds;
      }
      const borderLatLngs = (cMod.border || []).map((pt) => [pt[1], pt[0]]);
      if (borderLatLngs.length) {
        maskRings.push(borderLatLngs);
        const borderColor = cMod.border_color || "#fbbf24";

        // Country National Border outer glow + crisp boundary line
        L.polyline(borderLatLngs, {
          pane: "borderPane",
          color: borderColor,
          weight: 6,
          opacity: 0.22,
          interactive: false,
        }).addTo(map);

        L.polyline(borderLatLngs, {
          pane: "borderPane",
          color: borderColor,
          weight: 2.2,
          opacity: 0.88,
          dashArray: "7 4",
          interactive: false,
        }).addTo(map);
      }

      // Render Country's Major Lakes
      for (const lake of cMod.lakes || []) {
        const latlngs = lake.polygon.map((p) => [p[1], p[0]]);
        const poly = L.polygon(latlngs, {
          pane: "lakePane",
          color: "#38bdf8",
          weight: 2.2,
          fillColor: "#0284c7",
          fillOpacity: 0.55,
        }).addTo(map);

        bindHydroHoverAndClick(poly, lake.station_code);
        lakeLayersByCode.set(lake.station_code, poly);
      }

      // Render Country's Hydrological River Reaches
      for (const reach of cMod.reaches || []) {
        const code = reach.station_code;
        const multiLatLngs = reach.lines.map((line) => line.map((pt) => [pt[1], pt[0]]));
        if (!multiLatLngs.length) continue;

        const isMinor = reach.water_category === "minor";
        const baseWeight = reach.is_main_river ? 4.2 : isMinor ? 1.9 : 2.7;

        const glowLine = L.polyline(multiLatLngs, {
          pane: "riverGlowPane",
          color: "#38bdf8",
          weight: baseWeight + 5,
          opacity: 0.18,
          lineCap: "round",
          lineJoin: "round",
          interactive: false,
        }).addTo(map);

        const visibleLine = L.polyline(multiLatLngs, {
          pane: "riverPane",
          color: "#38bdf8",
          weight: baseWeight,
          opacity: 0.92,
          lineCap: "round",
          lineJoin: "round",
          interactive: false,
        }).addTo(map);

        const hitLine = L.polyline(multiLatLngs, {
          pane: "riverPane",
          color: "#ffffff",
          weight: 16,
          opacity: 0.0,
          lineCap: "round",
          lineJoin: "round",
          interactive: true,
        }).addTo(map);

        bindHydroHoverAndClick(hitLine, code);

        reachLayersByCode.set(code, {
          glowLine,
          visibleLine,
          hitLine,
          isMain: reach.is_main_river,
          isMinor,
          basin: reach.basin,
        });
      }
    }

    // Exterior dim mask cutting out all registered countries
    L.polygon(maskRings, {
      pane: "maskPane",
      color: "transparent",
      fillColor: "#020611",
      fillOpacity: 0.52,
      interactive: false,
    }).addTo(map);
  }

  // Bind Hover & Click Events to a River Reach, Lake, or Station Marker
  function bindHydroHoverAndClick(layer, stationCode) {
    layer.on("mouseover", (e) => {
      state.hoveredCode = stationCode;
      highlightStationOnMap(stationCode, true);
      showHoverCard(stationCode, e.originalEvent);
    });

    layer.on("mousemove", (e) => {
      positionHoverCard(e.originalEvent);
    });

    layer.on("mouseout", () => {
      if (state.hoveredCode === stationCode) {
        state.hoveredCode = null;
      }
      highlightStationOnMap(stationCode, false);
      hideHoverCard();
    });

    layer.on("click", () => {
      pinStation(stationCode, true);
    });
  }

  // Build or Update Gauging Station Markers on the Map
  function renderStationMarkers() {
    for (const [code, st] of state.stationsByCode.entries()) {
      let entry = stationMarkersByCode.get(code);
      const dayData = getStationDayData(st, state.activeDay);
      const color = ALERT_COLORS[dayData.alert_level] || ALERT_COLORS.normal;

      if (!entry) {
        const marker = L.circleMarker([st.lat, st.lon], {
          pane: "stationPane",
          radius: 5.8,
          color: "#ffffff",
          weight: 2,
          fillColor: color,
          fillOpacity: 1,
        }).addTo(map);

        const tooltip = L.tooltip({
          permanent: true,
          direction: "top",
          offset: [0, -7],
          className: "station-map-label",
        });

        marker.bindTooltip(tooltip);
        bindHydroHoverAndClick(marker, code);

        entry = { marker, tooltip };
        stationMarkersByCode.set(code, entry);
      }

      const isVisible = matchesFilters(st);
      const isMinor = st.water_category === "minor";
      const alertWeightBoost =
        dayData.alert_level === "deg3"
          ? 4.5
          : dayData.alert_level === "deg2"
          ? 3.2
          : dayData.alert_level === "deg1"
          ? 2.2
          : dayData.alert_level === "elevated"
          ? 1.2
          : 0;

      if (isVisible && state.showStations) {
        if (!map.hasLayer(entry.marker)) entry.marker.addTo(map);
        const baseRadius = code === state.pinnedCode ? 8 : isMinor ? 4.4 : 5.6;
        entry.marker.setStyle({
          fillColor: color,
          radius: baseRadius + alertWeightBoost * 0.65,
          weight: code === state.pinnedCode ? 2.8 : isMinor ? 1.5 : 1.8,
        });

        const sign = dayData.delta_from_today_cm > 0 ? "+" : "";
        const deltaTxt =
          state.activeDay === 0
            ? ""
            : ` (${sign}${dayData.delta_from_today_cm})`;
        entry.tooltip.setContent(`${st.name}: ${dayData.level_cm} cm${deltaTxt}`);

        const currentZoom = map ? map.getZoom() : 7;
        const shouldShowLabel =
          state.showLabels &&
          (!isMinor ||
            currentZoom >= 7.75 ||
            state.basinFilter === "minor_only" ||
            Boolean(state.searchQuery) ||
            code === state.pinnedCode);

        if (shouldShowLabel) {
          if (!entry.marker.isTooltipOpen()) entry.marker.openTooltip();
        } else {
          if (entry.marker.isTooltipOpen()) entry.marker.closeTooltip();
        }
      } else {
        if (map.hasLayer(entry.marker)) map.removeLayer(entry.marker);
      }
    }
  }

  // Update River Reaches & Lakes Styling Based on Active Day & Weather Scenario
  function updateMapHydrographyStyles() {
    for (const [code, rLayer] of reachLayersByCode.entries()) {
      const st = state.stationsByCode.get(code);
      if (!st) continue;

      const isVisible = matchesFilters(st);
      const dayData = getStationDayData(st, state.activeDay);
      const color = ALERT_COLORS[dayData.alert_level] || ALERT_COLORS.normal;

      const span = Math.max(120, st.thresholds.deg1 - st.thresholds.low);
      const normalizedStage = Math.max(
        0,
        Math.min(1.6, (dayData.level_cm - st.thresholds.low) / span)
      );
      const baseW = rLayer.isMain ? 3.8 : rLayer.isMinor ? 1.85 : 2.4;
      const stageBoost = normalizedStage * (rLayer.isMain ? 3.5 : rLayer.isMinor ? 1.6 : 2.2);
      const isHoveredOrPinned = code === state.hoveredCode || code === state.pinnedCode;

      const weight = baseW + stageBoost + (isHoveredOrPinned ? 2.2 : 0);

      rLayer.visibleLine.setStyle({
        color,
        weight: isVisible ? weight : 1.0,
        opacity: isVisible ? 0.94 : 0.08,
      });

      rLayer.glowLine.setStyle({
        color,
        weight: isVisible ? weight + (rLayer.isMinor ? 5 : 7) : 0,
        opacity: isVisible
          ? isHoveredOrPinned
            ? 0.5
            : dayData.alert_level === "normal"
            ? 0.16
            : 0.36
          : 0,
      });
    }

    for (const [code, poly] of lakeLayersByCode.entries()) {
      const st = state.stationsByCode.get(code);
      if (!st) continue;
      const isVisible = matchesFilters(st);
      const dayData = getStationDayData(st, state.activeDay);
      const color = ALERT_COLORS[dayData.alert_level] || ALERT_COLORS.normal;
      const isHoveredOrPinned = code === state.hoveredCode || code === state.pinnedCode;

      poly.setStyle({
        color: isHoveredOrPinned ? "#ffffff" : color,
        weight: isHoveredOrPinned ? 3.2 : 2.0,
        fillColor: color,
        fillOpacity: isVisible ? (isHoveredOrPinned ? 0.78 : 0.55) : 0.12,
        opacity: isVisible ? 0.95 : 0.2,
      });
    }
  }

  function highlightStationOnMap(code, isHovering) {
    updateMapHydrographyStyles();
    const mEntry = stationMarkersByCode.get(code);
    if (mEntry) {
      mEntry.marker.setStyle({
        weight: isHovering || code === state.pinnedCode ? 3.2 : 1.8,
      });
    }
  }

  // Generate SVG 7-Day Hydrograph Sparkline for Hover Card & Sidebar Inspector
  function buildSparklineSVG(station, activeDayIdx, width = 310, height = 84) {
    const days = [0, 1, 2, 3, 4, 5, 6, 7].map((d) => getStationDayData(station, d));
    const levels = days.map((d) => d.level_cm);
    const uncs = days.map((d) => d.uncertainty_cm);

    const minVal = Math.min(
      ...levels.map((l, i) => l - uncs[i]),
      station.thresholds.low
    ) - 15;
    const maxVal = Math.max(
      ...levels.map((l, i) => l + uncs[i]),
      station.thresholds.deg1 * 0.75
    ) + 20;
    const range = Math.max(40, maxVal - minVal);

    const padL = 28;
    const padR = 10;
    const padT = 10;
    const padB = 18;
    const plotW = width - padL - padR;
    const plotH = height - padT - padB;

    const xFor = (d) => padL + (d / 7) * plotW;
    const yFor = (val) => padT + plotH - ((val - minVal) / range) * plotH;

    const upperPts = days.map((d, i) => `${xFor(i).toFixed(1)},${yFor(d.level_cm + d.uncertainty_cm).toFixed(1)}`);
    const lowerPts = [...days]
      .reverse()
      .map((d, revI) => {
        const i = 7 - revI;
        return `${xFor(i).toFixed(1)},${yFor(d.level_cm - d.uncertainty_cm).toFixed(1)}`;
      });
    const conePolygon = [...upperPts, ...lowerPts].join(" ");
    const linePts = days.map((d, i) => `${xFor(i).toFixed(1)},${yFor(d.level_cm).toFixed(1)}`).join(" ");

    let threshLines = "";
    const checkThresholds = [
      { val: station.thresholds.deg1, color: "#f59e0b", label: "I. fok" },
      { val: station.thresholds.deg2, color: "#f97316", label: "II. fok" },
      { val: station.thresholds.low, color: "#06b6d4", label: "Kisvíz" },
    ];
    for (const th of checkThresholds) {
      if (th.val >= minVal && th.val <= maxVal) {
        const ty = yFor(th.val).toFixed(1);
        threshLines += `
          <line x1="${padL}" y1="${ty}" x2="${width - padR}" y2="${ty}" stroke="${th.color}" stroke-width="1" stroke-dasharray="3 3" opacity="0.7"/>
          <text x="${width - padR - 2}" y="${Number(ty) - 2}" fill="${th.color}" font-size="8.5" text-anchor="end">${th.label} (${th.val})</text>
        `;
      }
    }

    const activeD = days[activeDayIdx];
    const ax = xFor(activeDayIdx).toFixed(1);
    const ay = yFor(activeD.level_cm).toFixed(1);
    const activeColor = ALERT_COLORS[activeD.alert_level] || "#38bdf8";

    const dayTicks = days
      .map((d, i) => {
        const tx = xFor(i).toFixed(1);
        const lbl = i === 0 ? "Ma" : `+${i}n`;
        const weight = i === activeDayIdx ? "700" : "400";
        const fill = i === activeDayIdx ? activeColor : "#94a3b8";
        return `<text x="${tx}" y="${height - 3}" fill="${fill}" font-size="9" font-weight="${weight}" text-anchor="middle">${lbl}</text>`;
      })
      .join("");

    return `
      <svg viewBox="0 0 ${width} ${height}" width="100%" height="${height}" aria-label="7 napos vízállás előrejelzési görbe">
        <rect x="${padL}" y="${padT}" width="${plotW}" height="${plotH}" fill="rgba(15,23,42,0.22)" rx="4"/>
        ${threshLines}
        <polygon points="${conePolygon}" fill="${activeColor}" opacity="0.18"/>
        <polyline points="${linePts}" fill="none" stroke="${activeColor}" stroke-width="2.3" stroke-linecap="round" stroke-linejoin="round"/>
        <line x1="${ax}" y1="${padT}" x2="${ax}" y2="${padT + plotH}" stroke="#ffffff" stroke-width="1.2" stroke-dasharray="2 2" opacity="0.75"/>
        <circle cx="${ax}" cy="${ay}" r="4.5" fill="${activeColor}" stroke="#ffffff" stroke-width="2"/>
        <text x="2" y="${padT + 8}" fill="#94a3b8" font-size="8.5">${Math.round(maxVal)}</text>
        <text x="2" y="${padT + plotH}" fill="#94a3b8" font-size="8.5">${Math.round(minVal)}</text>
        ${dayTicks}
      </svg>
    `;
  }

  // Build Station Hydrological Card HTML (shared between Hover Tooltip & Pinned Inspector)
  function buildStationCardHTML(station, isPinnedView = false) {
    const dayData = getStationDayData(station, state.activeDay);
    const todayData = station.timeline[0];

    const deltaSign = dayData.delta_from_today_cm > 0 ? "+" : "";
    const dailySign = dayData.daily_change_cm > 0 ? "+" : "";

    let trendClass = "trend-flat";
    let trendIcon = "▬ Stagnáló";
    if (dayData.daily_change_cm >= 3) {
      trendClass = "trend-up";
      trendIcon = "▲ Áradó";
    } else if (dayData.daily_change_cm <= -3) {
      trendClass = "trend-down";
      trendIcon = "▼ Apadó";
    }

    const th = station.thresholds;
    const span = Math.max(50, th.lnv - th.lkv);
    const pct = Math.max(2, Math.min(98, ((dayData.level_cm - th.lkv) / span) * 100));

    const uncText =
      state.activeDay === 0 ? "Hivatalos mérés" : `±${dayData.uncertainty_cm} cm sáv`;

    const fkmText = station.fkm > 0 ? ` • ${station.fkm} fkm` : "";
    const countryCode = station.country || "HU";

    return `
      <div class="hover-header">
        <div>
          <span class="hover-river-badge">
            <span class="country-tag country-${countryCode}">${countryCode}</span>${station.river}${fkmText} • Kód: ${station.code}
          </span>
          <h3 class="hover-station-title">${station.name}</h3>
          <div class="hover-reach-sub">${station.reach_name}</div>
        </div>
        <span class="alert-pill alert-${dayData.alert_level}">${dayData.alert_label}</span>
      </div>

      <div class="hover-metrics-grid">
        <div class="metric-box">
          <span class="metric-box-label">${dayData.label} vízállás</span>
          <strong class="metric-box-val">${dayData.level_cm} cm</strong>
          <span class="metric-box-label">${uncText}</span>
        </div>
        <div class="metric-box">
          <span class="metric-box-label">24 órás változás</span>
          <strong class="metric-box-val ${trendClass}">${dailySign}${dayData.daily_change_cm} cm</strong>
          <span class="metric-box-label ${trendClass}">${trendIcon}</span>
        </div>
        <div class="metric-box">
          <span class="metric-box-label">${state.activeDay === 0 ? "Vízhozam & Hőfok" : "Eltérés a maitól"}</span>
          <strong class="metric-box-val">${
            state.activeDay === 0
              ? `${dayData.discharge_m3s} m³/s`
              : `${deltaSign}${dayData.delta_from_today_cm} cm`
          }</strong>
          <span class="metric-box-label">Vízhőfok: ${station.water_temp_c} °C</span>
        </div>
      </div>

      <div class="threshold-gauge">
        <div class="threshold-labels">
          <span>LKV: ${th.lkv} cm</span>
          <span>I. fok: ${th.deg1} cm</span>
          <span>III. fok: ${th.deg3} cm</span>
          <span>LNV: ${th.lnv} cm</span>
        </div>
        <div class="threshold-bar-track">
          <div class="threshold-marker" style="left: ${pct.toFixed(1)}%;"></div>
        </div>
      </div>

      <div class="sparkline-container">
        <div class="sparkline-title">
          <span><strong>7 napos vízállás-görbe</strong> (${formatHuDate(dayData.date)})</span>
          <span>Csapadék: <strong>${dayData.precip_mm} mm</strong> (Σ ${dayData.cum_precip_mm} mm) • ${dayData.temp_max_c}°C</span>
        </div>
        ${buildSparklineSVG(station, state.activeDay, isPinnedView ? 345 : 310, 82)}
        <div class="threshold-labels" style="margin-top: 2px; margin-bottom: 0;">
          <span>Forrás: ${dayData.source}</span>
          <span>Ma: ${todayData.level_cm} cm → +7n: ${getStationDayData(station, 7).level_cm} cm</span>
        </div>
      </div>
    `;
  }

  // Show and Position Floating Hover Card
  function showHoverCard(stationCode, mouseEvent) {
    const st = state.stationsByCode.get(stationCode);
    if (!st) return;
    hoverCardEl.innerHTML = buildStationCardHTML(st, false);
    hoverCardEl.classList.remove("hidden");
    positionHoverCard(mouseEvent);
  }

  function positionHoverCard(mouseEvent) {
    if (!mouseEvent || hoverCardEl.classList.contains("hidden")) return;
    const cardW = 355;
    const cardH = 310;
    const offset = 18;

    let left = mouseEvent.clientX + offset;
    let top = mouseEvent.clientY + offset;

    if (left + cardW > window.innerWidth - 16) {
      left = mouseEvent.clientX - cardW - offset;
    }
    if (top + cardH > window.innerHeight - 16) {
      top = mouseEvent.clientY - cardH - offset;
    }

    hoverCardEl.style.left = `${Math.max(12, left)}px`;
    hoverCardEl.style.top = `${Math.max(12, top)}px`;
  }

  function hideHoverCard() {
    hoverCardEl.classList.add("hidden");
  }

  // Pin Station to Right Inspector Panel
  function pinStation(stationCode, panMap = false) {
    const st = state.stationsByCode.get(stationCode);
    if (!st) return;
    state.pinnedCode = stationCode;
    pinnedPanelEl.innerHTML = buildStationCardHTML(st, true);

    if (panMap && map) {
      map.panTo([st.lat, st.lon], { animate: true, duration: 0.45 });
    }
    updateMapHydrographyStyles();
    renderStationMarkers();
    highlightSelectedStationRow();
  }

  // Filter Check (Country, Basin / Water Category, Search Query)
  function matchesFilters(station) {
    if (!state.showMinorWaters && station.water_category === "minor" && state.basinFilter !== "minor_only") {
      return false;
    }
    if (state.countryFilter !== "all" && (station.country || "HU") !== state.countryFilter) {
      return false;
    }
    if (state.basinFilter === "minor_only") {
      if (station.water_category !== "minor") return false;
    } else if (state.basinFilter !== "all" && station.basin !== state.basinFilter) {
      return false;
    }
    if (state.searchQuery) {
      const q = state.searchQuery.toLowerCase();
      const hay = `${station.name} ${station.river} ${station.reach_name} ${station.code} ${station.country}`.toLowerCase();
      if (!hay.includes(q)) return false;
    }
    return true;
  }

  // Render Right-Hand Scrollable Station List
  function renderStationList() {
    if (!state.payload) return;
    const filtered = state.payload.stations.filter(matchesFilters);
    stationCountBadge.textContent = String(filtered.length);

    stationListEl.innerHTML = filtered
      .map((st) => {
        const d = getStationDayData(st, state.activeDay);
        const sign = d.delta_from_today_cm > 0 ? "+" : "";
        const deltaStr =
          state.activeDay === 0
            ? `${d.daily_change_cm >= 0 ? "+" : ""}${d.daily_change_cm} cm / 24ó`
            : `${sign}${d.delta_from_today_cm} cm a maihoz`;
        const isSel = st.code === state.pinnedCode ? "selected" : "";
        const cCode = st.country || "HU";

        return `
          <div class="station-row ${isSel}" data-code="${st.code}">
            <div class="station-row-left">
              <span class="station-row-name">
                <span class="country-tag country-${cCode}">${cCode}</span>${st.name}
                <small style="font-weight:500;opacity:0.75;">(${st.river})</small>
              </span>
              <span class="station-row-meta">${st.reach_name}</span>
            </div>
            <div class="station-row-right">
              <span class="station-row-level">${d.level_cm} cm</span>
              <span class="alert-pill alert-${d.alert_level}" style="font-size:0.65rem;padding:0.1rem 0.42rem;">${deltaStr}</span>
            </div>
          </div>
        `;
      })
      .join("");

    stationListEl.querySelectorAll(".station-row").forEach((row) => {
      const code = row.getAttribute("data-code");
      row.addEventListener("click", () => pinStation(code, true));
      row.addEventListener("mouseenter", () => {
        state.hoveredCode = code;
        highlightStationOnMap(code, true);
      });
      row.addEventListener("mouseleave", () => {
        state.hoveredCode = null;
        highlightStationOnMap(code, false);
      });
    });
  }

  function highlightSelectedStationRow() {
    stationListEl.querySelectorAll(".station-row").forEach((row) => {
      row.classList.toggle("selected", row.getAttribute("data-code") === state.pinnedCode);
    });
  }

  // Update KPI Cards & Timeline Slider Header
  function updateDashboardKPIs() {
    if (!state.payload) return;
    const stations = state.payload.stations.filter(matchesFilters);
    if (!stations.length) return;

    const sampleDay = getStationDayData(stations[0], state.activeDay);
    const fmtDate = formatHuDate(sampleDay.date);

    let risingCount = 0;
    let maxRise = -9999;
    let maxRiseStation = "";
    let alertOrElevatedCount = 0;
    let degAlertCount = 0;
    let precipSum = 0;
    let tempSum = 0;

    for (const st of stations) {
      const d = getStationDayData(st, state.activeDay);
      if (d.daily_change_cm > 2) risingCount++;
      const refChange = state.activeDay === 0 ? d.daily_change_cm : d.delta_from_today_cm;
      if (refChange > maxRise) {
        maxRise = refChange;
        maxRiseStation = st.name;
      }
      if (["elevated", "deg1", "deg2", "deg3"].includes(d.alert_level)) {
        alertOrElevatedCount++;
      }
      if (["deg1", "deg2", "deg3"].includes(d.alert_level)) {
        degAlertCount++;
      }
      precipSum += d.precip_mm;
      tempSum += d.temp_max_c;
    }

    const avgPrecip = (precipSum / stations.length).toFixed(1);
    const avgTemp = (tempSum / stations.length).toFixed(1);

    kpiActiveDay.textContent =
      state.activeDay === 0 ? "Ma (Aktuális)" : `+${state.activeDay} napos előrejelzés`;
    kpiActiveDate.textContent = fmtDate;

    kpiRisingCount.textContent = `${risingCount} / ${stations.length}`;
    kpiMaxRise.textContent =
      maxRise > -999
        ? `Max: ${maxRise >= 0 ? "+" : ""}${maxRise} cm (${maxRiseStation})`
        : "Stagnáló";

    kpiAlertCount.textContent = String(alertOrElevatedCount);
    kpiAlertDetail.textContent =
      degAlertCount > 0
        ? `${degAlertCount} szakasz árvízi fokozatban`
        : alertOrElevatedCount > 0
        ? `${alertOrElevatedCount} emelkedett vízszintű szakasz`
        : "Minden szakasz normál mederben";

    kpiPrecipAvg.textContent = `${avgPrecip} mm`;
    kpiTempAvg.textContent = `Átlag max: ${avgTemp} °C`;

    const dayTitle =
      state.activeDay === 0
        ? `Ma (${fmtDate}) — Hivatalos OVF & INHGA mért vízállások`
        : `+${state.activeDay} nap (${fmtDate}) — Becsült várható vízállás`;
    dayBadgeEl.textContent = dayTitle;
    weatherPillEl.textContent = `Vízgyűjtő csapadék: ${avgPrecip} mm • Hőmérséklet: ${avgTemp} °C`;
    sliderEl.setAttribute("aria-valuetext", dayTitle);

    document.querySelectorAll(".step-chip").forEach((btn) => {
      btn.classList.toggle("active", Number(btn.dataset.day) === state.activeDay);
    });
    document.querySelectorAll(".slider-tick").forEach((t) => {
      t.classList.toggle("active", Number(t.dataset.day) === state.activeDay);
    });
  }

  // Build Timeline Slider Date Ticks (Days 0..7)
  function renderSliderTicks() {
    if (!state.payload || !state.payload.stations.length) return;
    const refTimeline = state.payload.stations[0].timeline;

    ticksContainer.innerHTML = refTimeline
      .map((item, idx) => {
        const lbl = idx === 0 ? "Ma (0.)" : `+${idx} nap`;
        return `
          <div class="slider-tick ${idx === state.activeDay ? "active" : ""}" data-day="${idx}">
            <span>${lbl}</span>
            <span class="tick-date">${formatHuDate(item.date)}</span>
          </div>
        `;
      })
      .join("");

    ticksContainer.querySelectorAll(".slider-tick").forEach((tickEl) => {
      tickEl.addEventListener("click", () => {
        setActiveDay(Number(tickEl.dataset.day));
      });
    });
  }

  // Set Active Forecast Day (0..7) and Refresh Map & Panels in Real Time
  function setActiveDay(dayIdx) {
    state.activeDay = Math.max(0, Math.min(7, dayIdx));
    sliderEl.value = String(state.activeDay);
    syncSliderCSSVariables();

    updateMapHydrographyStyles();
    renderStationMarkers();
    updateDashboardKPIs();
    renderStationList();

    if (state.pinnedCode) {
      const pinnedSt = state.stationsByCode.get(state.pinnedCode);
      if (pinnedSt) {
        pinnedPanelEl.innerHTML = buildStationCardHTML(pinnedSt, true);
      }
    }
    if (state.hoveredCode && !hoverCardEl.classList.contains("hidden")) {
      const hovSt = state.stationsByCode.get(state.hoveredCode);
      if (hovSt) {
        hoverCardEl.innerHTML = buildStationCardHTML(hovSt, false);
      }
    }
  }

  // Fetch Hydrological & Meteorological Data from Backend API
  async function loadHydroData(forceRefresh = false) {
    try {
      refreshBtn.disabled = true;
      refreshBtn.textContent = "⟳ Betöltés...";
      const endpoint = forceRefresh ? "/api/refresh" : "/api/hydro-data";
      const resp = await fetch(endpoint);
      const data = await resp.json();

      state.payload = data;
      state.stationsByCode.clear();
      for (const st of data.stations) {
        state.stationsByCode.set(st.code, st);
      }

      metaSourceLabel.textContent = `OVF hydroinfo.hu, vizugy.hu & INHGA (HU: ${data.meta.hu_stations}, RO: ${data.meta.ro_stations} • ${data.meta.minor_stations} kisvízfolyás/csatorna, észlelés: ${data.meta.observation_date}) & GloFAS v4`;

      renderSliderTicks();
      setActiveDay(state.activeDay);
      if (state.pinnedCode) {
        pinStation(state.pinnedCode, false);
      }
    } catch (err) {
      console.error("Failed to load hydro data:", err);
      metaSourceLabel.textContent = "Hiba az adatok betöltésekor — ellenőrizze a szervert.";
    } finally {
      refreshBtn.disabled = false;
      refreshBtn.textContent = "⟳ Élő frissítés";
    }
  }

  // Event Listeners Setup
  function initControls() {
    syncSliderCSSVariables();

    sliderEl.addEventListener("input", () => {
      setActiveDay(Number(sliderEl.value));
    });

    document.querySelectorAll(".step-chip").forEach((chip) => {
      chip.addEventListener("click", () => {
        setActiveDay(Number(chip.dataset.day));
      });
    });

    playBtn.addEventListener("click", () => {
      if (state.playTimer) {
        clearInterval(state.playTimer);
        state.playTimer = null;
        playBtn.textContent = "▶ Lejátszás";
      } else {
        playBtn.textContent = "⏸ Szünet";
        state.playTimer = setInterval(() => {
          const nextDay = (state.activeDay + 1) % 8;
          setActiveDay(nextDay);
        }, 1350);
      }
    });

    countrySelect.addEventListener("change", () => {
      state.countryFilter = countrySelect.value;
      const bounds = REGION_BOUNDS[state.countryFilter] || REGION_BOUNDS.all;
      if (map) {
        map.flyToBounds(bounds, { padding: [24, 24], duration: 0.65 });
      }
      setActiveDay(state.activeDay);
    });

    basinSelect.addEventListener("change", () => {
      state.basinFilter = basinSelect.value;
      setActiveDay(state.activeDay);
    });

    scenarioSelect.addEventListener("change", () => {
      state.scenario = scenarioSelect.value;
      setActiveDay(state.activeDay);
    });

    searchInput.addEventListener("input", () => {
      state.searchQuery = searchInput.value.trim();
      setActiveDay(state.activeDay);
    });

    refreshBtn.addEventListener("click", () => {
      loadHydroData(true);
    });

    const minorToggle = document.getElementById("toggle-minor-waters");
    if (minorToggle) {
      minorToggle.addEventListener("change", (e) => {
        state.showMinorWaters = e.target.checked;
        setActiveDay(state.activeDay);
      });
    }

    document.getElementById("toggle-stations").addEventListener("change", (e) => {
      state.showStations = e.target.checked;
      renderStationMarkers();
    });

    document.getElementById("toggle-labels").addEventListener("change", (e) => {
      state.showLabels = e.target.checked;
      renderStationMarkers();
    });

    document.getElementById("toggle-basemap").addEventListener("change", (e) => {
      state.showBasemap = e.target.checked;
      updateBasemapTheme();
    });

    const basemapSelect = document.getElementById("basemap-source");
    if (basemapSelect) {
      basemapSelect.addEventListener("change", () => {
        state.basemapSource = basemapSelect.value;
        state.showBasemap = state.basemapSource !== "none";
        document.getElementById("toggle-basemap").checked = state.showBasemap;
        updateBasemapTheme();
      });
    }

    const darkMql = window.matchMedia("(prefers-color-scheme: dark)");
    darkMql.addEventListener("change", (e) => {
      if (!document.documentElement.hasAttribute("data-theme")) {
        state.darkMode = e.matches;
        updateBasemapTheme();
      }
    });

    themeBtn.addEventListener("click", () => {
      state.darkMode = !state.darkMode;
      document.documentElement.setAttribute("data-theme", state.darkMode ? "dark" : "light");
      updateBasemapTheme();
    });
  }

  // Boot Application
  initMap();
  initControls();
  loadHydroData(false);
})();
