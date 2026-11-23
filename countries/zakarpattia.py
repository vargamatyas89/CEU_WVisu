"""
Kárpátalja / Zakarpattia (UA) — Catchments and Hydrological Reference Stations
(Copernicus GloFAS v4 5 km + Open-Meteo IFS + live cross-border OVF/SHMÚ/INHGA calibration)
Standalone region source file (24 Zakarpattia stations: Upper Tisza headwaters, Latorytsia, Uzh, Borzhava, Rika, Lake Synevyr and smaller waters)
"""

COUNTRY_META = {
    "code": "UA",
    "name": "Kárpátalja (UA)",
    "flag": "🇺🇦",
    "border_color": "#e879f9",
    "bounds": [[47.89, 22.13], [49.09, 24.64]],
}

CATCHMENTS = {
    "ua_upper_tisza_rakhiv": {"name": "Felső-Tisza forrásvidéke (Rahó, Fekete- és Fehér-Tisza, Kárpátalja)", "lat": 48.12, "lon": 24.25, "response_factor": 4.1, "lag_days": 1},
    "ua_mid_tisza_khust": {"name": "Középső-Kárpátalja (Técső, Huszt, Tarac, Talabor, Nagyág, Borzsa)", "lat": 48.24, "lon": 23.38, "response_factor": 3.8, "lag_days": 1},
    "ua_latorca_ung_bereg": {"name": "Ung–Latorca–Beregi-síkság (Ungvár, Munkács, Beregszász, Csap)", "lat": 48.48, "lon": 22.62, "response_factor": 3.3, "lag_days": 1},
}

STATIONS = [
    # =========================================================================
    # 1. MAIN RIVERS AND CARPATHIAN LAKE (15 stations — GloFAS v4 + live cross-border calibration)
    # =========================================================================
    # --- BLACK TISZA, WHITE TISZA AND UPPER TISZA (7 stations) ---
    {
        "code": "UA_94001", "country": "UA", "name": "Kőrösmező (Ясіня)", "river": "Fekete-Tisza", "basin": "tisza", "catchment": "ua_upper_tisza_rakhiv",
        "reach_name": "Fekete-Tisza (Чорна Тиса) – Tatár-hágó – Kőrösmező (Yasinia) – Rahó", "lat": 48.268, "lon": 24.358, "fkm": 958.0,
        "thresholds": {"lkv": 35, "low": 75, "deg1": 240, "deg2": 310, "deg3": 380, "lnv": 465},
        "default_level": 118, "default_diff24h": 4, "default_discharge": 18.5, "default_temp": 6.2,
        "transboundary_anchor": "744102", "downstream_order": 1
    },
    {
        "code": "UA_94002", "country": "UA", "name": "Bogdán (Богдан)", "river": "Fehér-Tisza", "basin": "tisza", "catchment": "ua_upper_tisza_rakhiv",
        "reach_name": "Fehér-Tisza (Біла Тиса) – Hoverla – Bogdán (Bohdan) – Rahó", "lat": 48.038, "lon": 24.345, "fkm": 952.0,
        "thresholds": {"lkv": 30, "low": 65, "deg1": 220, "deg2": 290, "deg3": 350, "lnv": 435},
        "default_level": 102, "default_diff24h": 3, "default_discharge": 15.2, "default_temp": 6.0,
        "transboundary_anchor": "744102", "downstream_order": 1
    },
    {
        "code": "UA_94003", "country": "UA", "name": "Rahó (Рахів)", "river": "Tisza", "basin": "tisza", "catchment": "ua_upper_tisza_rakhiv",
        "reach_name": "Felső-Tisza (Тиса) – Rahó (Rakhiv) – Terebesfejérpatak", "lat": 48.055, "lon": 24.202, "fkm": 941.0,
        "thresholds": {"lkv": 45, "low": 90, "deg1": 320, "deg2": 400, "deg3": 470, "lnv": 575},
        "default_level": 145, "default_diff24h": 5, "default_discharge": 42.0, "default_temp": 6.5,
        "transboundary_anchor": "744102", "downstream_order": 1
    },
    {
        "code": "UA_94004", "country": "UA", "name": "Técső (Тячів)", "river": "Tisza", "basin": "tisza", "catchment": "ua_mid_tisza_khust",
        "reach_name": "Felső-Tisza (Тиса) – Nagybocskó – Tarac-torkolat – Técső (Tiachiv)", "lat": 48.008, "lon": 23.572, "fkm": 848.0,
        "thresholds": {"lkv": 20, "low": 75, "deg1": 380, "deg2": 470, "deg3": 550, "lnv": 675},
        "default_level": 136, "default_diff24h": 6, "default_discharge": 145.0, "default_temp": 7.1,
        "transboundary_anchor": "444226", "downstream_order": 2
    },
    {
        "code": "UA_94005", "country": "UA", "name": "Huszt (Хуст)", "river": "Tisza", "basin": "tisza", "catchment": "ua_mid_tisza_khust",
        "reach_name": "Felső-Tisza (Тиса) – Visk – Nagyág-torkolat – Huszt (Khust)", "lat": 48.165, "lon": 23.298, "fkm": 815.0,
        "thresholds": {"lkv": 40, "low": 100, "deg1": 400, "deg2": 500, "deg3": 590, "lnv": 715},
        "default_level": 172, "default_diff24h": 8, "default_discharge": 195.0, "default_temp": 7.3,
        "transboundary_anchor": "444226", "downstream_order": 3
    },
    {
        "code": "UA_94006", "country": "UA", "name": "Tiszaújlak (Вилок)", "river": "Tisza", "basin": "tisza", "catchment": "ua_mid_tisza_khust",
        "reach_name": "Felső-Tisza (Тиса) – Nagyszőlős – Tiszaújlak (Vylok) – Tiszabecs belépő", "lat": 48.112, "lon": 22.838, "fkm": 768.0,
        "thresholds": {"lkv": -120, "low": -45, "deg1": 300, "deg2": 420, "deg3": 520, "lnv": 665},
        "default_level": 28, "default_diff24h": 10, "default_discharge": 235.0, "default_temp": 7.5,
        "transboundary_anchor": "444226", "downstream_order": 4
    },
    {
        "code": "UA_94007", "country": "UA", "name": "Csap (Чоп)", "river": "Tisza", "basin": "tisza", "catchment": "ua_latorca_ung_bereg",
        "reach_name": "Tisza (Тиса) – Bátyú – Csap (Chop) – Záhony hármashatár", "lat": 48.425, "lon": 22.212, "fkm": 635.0,
        "thresholds": {"lkv": -180, "low": -90, "deg1": 550, "deg2": 720, "deg3": 850, "lnv": 1015},
        "default_level": 112, "default_diff24h": 14, "default_discharge": 310.0, "default_temp": 7.8,
        "transboundary_anchor": "444510", "downstream_order": 5
    },

    # --- LATORYTSIA, UZH, BORZHAVA, RIKA AND LAKE SYNEVYR (8 stations) ---
    {
        "code": "UA_94008", "country": "UA", "name": "Szolyva (Свалява)", "river": "Latorca", "basin": "tisza", "catchment": "ua_latorca_ung_bereg",
        "reach_name": "Latorca (Латориця) – Vereckei-hágó – Szolyva (Svaliava)", "lat": 48.548, "lon": 22.988, "fkm": 134.0,
        "thresholds": {"lkv": 25, "low": 60, "deg1": 240, "deg2": 310, "deg3": 370, "lnv": 455},
        "default_level": 96, "default_diff24h": 4, "default_discharge": 19.5, "default_temp": 6.8,
        "transboundary_anchor": "144101", "downstream_order": 1
    },
    {
        "code": "UA_94009", "country": "UA", "name": "Munkács (Мукачево)", "river": "Latorca", "basin": "tisza", "catchment": "ua_latorca_ung_bereg",
        "reach_name": "Latorca (Латориця) – Munkács (Mukachevo) – Kárpátaljai-síkság", "lat": 48.438, "lon": 22.718, "fkm": 94.0,
        "thresholds": {"lkv": -60, "low": -10, "deg1": 290, "deg2": 370, "deg3": 450, "lnv": 565},
        "default_level": 48, "default_diff24h": 6, "default_discharge": 34.0, "default_temp": 7.2,
        "transboundary_anchor": "144101", "downstream_order": 2
    },
    {
        "code": "UA_94010", "country": "UA", "name": "Csap–Latorca (Чоп)", "river": "Latorca", "basin": "tisza", "catchment": "ua_latorca_ung_bereg",
        "reach_name": "Latorca (Латориця) – Nagydobrony – Csap (Chop) – szlovák határ", "lat": 48.458, "lon": 22.228, "fkm": 48.0,
        "thresholds": {"lkv": 80, "low": 160, "deg1": 520, "deg2": 620, "deg3": 700, "lnv": 795},
        "default_level": 245, "default_diff24h": 8, "default_discharge": 44.5, "default_temp": 7.5,
        "transboundary_anchor": "144101", "downstream_order": 3
    },
    {
        "code": "UA_94011", "country": "UA", "name": "Nagyberezna (Великий Березний)", "river": "Ung", "basin": "tisza", "catchment": "ua_latorca_ung_bereg",
        "reach_name": "Ung (Уж) – Uzsoki-hágó – Nagyberezna (Velykyi Bereznyi)", "lat": 48.892, "lon": 22.458, "fkm": 74.0,
        "thresholds": {"lkv": 20, "low": 55, "deg1": 230, "deg2": 300, "deg3": 360, "lnv": 445},
        "default_level": 88, "default_diff24h": 2, "default_discharge": 16.0, "default_temp": 6.6,
        "transboundary_anchor": "144120", "downstream_order": 1
    },
    {
        "code": "UA_94012", "country": "UA", "name": "Ungvár (Ужгород)", "river": "Ung", "basin": "tisza", "catchment": "ua_latorca_ung_bereg",
        "reach_name": "Ung (Уж) – Perecseny – Ungvár (Uzhhorod) – szlovák határ", "lat": 48.622, "lon": 22.298, "fkm": 32.0,
        "thresholds": {"lkv": -110, "low": -65, "deg1": 180, "deg2": 260, "deg3": 340, "lnv": 435},
        "default_level": -24, "default_diff24h": 3, "default_discharge": 29.5, "default_temp": 7.2,
        "transboundary_anchor": "144120", "downstream_order": 2
    },
    {
        "code": "UA_94013", "country": "UA", "name": "Dolha / Salánk (Довге–Боржава)", "river": "Borzsa", "basin": "tisza", "catchment": "ua_mid_tisza_khust",
        "reach_name": "Borzsa (Боржава) – Dolha – Ilosva – Salánk – Vári (Tisza-torkolat)", "lat": 48.275, "lon": 22.985, "fkm": 38.0,
        "thresholds": {"lkv": 15, "low": 65, "deg1": 360, "deg2": 450, "deg3": 530, "lnv": 635},
        "default_level": 124, "default_diff24h": 5, "default_discharge": 22.0, "default_temp": 7.4,
        "transboundary_anchor": "444226", "downstream_order": 1
    },
    {
        "code": "UA_94014", "country": "UA", "name": "Ökörmező / Huszt (Міжгір'я–Ріка)", "river": "Nagyág (Rika)", "basin": "tisza", "catchment": "ua_mid_tisza_khust",
        "reach_name": "Nagyág (Ріка / Rika) – Ökörmező – Iza – Huszt (Tisza-torkolat)", "lat": 48.425, "lon": 23.495, "fkm": 42.0,
        "thresholds": {"lkv": 25, "low": 65, "deg1": 270, "deg2": 340, "deg3": 410, "lnv": 510},
        "default_level": 108, "default_diff24h": 4, "default_discharge": 28.5, "default_temp": 6.7,
        "transboundary_anchor": "444226", "downstream_order": 1
    },
    {
        "code": "UA_94015", "country": "UA", "name": "Szinevéri-tó (Синевир)", "river": "Szinevéri-tó (Synevyr)", "basin": "tavak", "catchment": "ua_mid_tisza_khust",
        "reach_name": "Szinevéri-tó (Озеро Синевир – Gorgánok, Kárpátalja)", "lat": 48.617, "lon": 23.684, "fkm": 0.0,
        "thresholds": {"lkv": 110, "low": 145, "deg1": 240, "deg2": 275, "deg3": 310, "lnv": 355},
        "default_level": 182, "default_diff24h": 0, "default_discharge": 0.8, "default_temp": 6.4,
        "transboundary_anchor": "444226", "downstream_order": 1
    },

    # =========================================================================
    # 2. SMALLER WATERS, CARPATHIAN STREAMS AND BEREG CANALS (9 stations)
    # =========================================================================
    {
        "code": "UA_94101", "country": "UA", "water_category": "minor", "name": "Dombó / Taracköz (Тересва)", "river": "Tarac (Teresva)", "basin": "tisza", "catchment": "ua_upper_tisza_rakhiv",
        "reach_name": "Tarac (Тересва / Teresva) – Királymező – Dombó – Taracköz", "lat": 48.165, "lon": 23.815, "fkm": 24.0,
        "thresholds": {"lkv": 20, "low": 55, "deg1": 250, "deg2": 320, "deg3": 390, "lnv": 480},
        "default_level": 94, "default_diff24h": 3, "default_discharge": 26.0, "default_temp": 6.5,
        "transboundary_anchor": "744102", "downstream_order": 1
    },
    {
        "code": "UA_94102", "country": "UA", "water_category": "minor", "name": "Alsókalocsa / Bustyaháza (Теребля)", "river": "Talabor (Tereblia)", "basin": "tisza", "catchment": "ua_mid_tisza_khust",
        "reach_name": "Talabor (Теребля / Tereblia) – Szinevér – Alsókalocsa – Bustyaháza", "lat": 48.245, "lon": 23.595, "fkm": 28.0,
        "thresholds": {"lkv": 15, "low": 50, "deg1": 240, "deg2": 300, "deg3": 360, "lnv": 445},
        "default_level": 86, "default_diff24h": 3, "default_discharge": 18.0, "default_temp": 6.6,
        "transboundary_anchor": "444226", "downstream_order": 1
    },
    {
        "code": "UA_94103", "country": "UA", "water_category": "minor", "name": "Kaszómező (Косівська)", "river": "Kaszó-patak (Kosivska)", "basin": "tisza", "catchment": "ua_upper_tisza_rakhiv",
        "reach_name": "Kaszó-patak (Косівська) – Kaszómező – Gyertyánliget – Tisza-torkolat", "lat": 48.015, "lon": 24.055, "fkm": 8.0,
        "thresholds": {"lkv": 15, "low": 40, "deg1": 190, "deg2": 240, "deg3": 290, "lnv": 360},
        "default_level": 68, "default_diff24h": 2, "default_discharge": 6.4, "default_temp": 6.1,
        "transboundary_anchor": "744102", "downstream_order": 1
    },
    {
        "code": "UA_94104", "country": "UA", "water_category": "minor", "name": "Turjaremete / Perecseny (Тур'я)", "river": "Turja (Turia)", "basin": "tisza", "catchment": "ua_latorca_ung_bereg",
        "reach_name": "Turja (Тур'я / Turia) – Polonina Runa – Turjaremete – Perecseny (Ung-mellékvíz)", "lat": 48.725, "lon": 22.588, "fkm": 14.0,
        "thresholds": {"lkv": 15, "low": 45, "deg1": 210, "deg2": 270, "deg3": 330, "lnv": 405},
        "default_level": 74, "default_diff24h": 2, "default_discharge": 9.2, "default_temp": 6.8,
        "transboundary_anchor": "144120", "downstream_order": 1
    },
    {
        "code": "UA_94105", "country": "UA", "water_category": "minor", "name": "Volóc / Vezérszállás (Віча)", "river": "Vicsa (Vicha)", "basin": "tisza", "catchment": "ua_latorca_ung_bereg",
        "reach_name": "Vicsa (Віча / Vicha) – Volóc – Hársfalva – Szolyva (Latorca-mellékvíz)", "lat": 48.665, "lon": 23.165, "fkm": 16.0,
        "thresholds": {"lkv": 15, "low": 42, "deg1": 195, "deg2": 250, "deg3": 305, "lnv": 375},
        "default_level": 70, "default_diff24h": 2, "default_discharge": 7.5, "default_temp": 6.5,
        "transboundary_anchor": "144101", "downstream_order": 1
    },
    {
        "code": "UA_94106", "country": "UA", "water_category": "minor", "name": "Feketeardó / Magosliget (Батар)", "river": "Batár-patak", "basin": "tisza", "catchment": "ua_mid_tisza_khust",
        "reach_name": "Batár-patak (Батар) – Tiszabökény – Feketeardó – Magosliget határ", "lat": 48.075, "lon": 22.925, "fkm": 18.0,
        "thresholds": {"lkv": 10, "low": 35, "deg1": 180, "deg2": 235, "deg3": 285, "lnv": 345},
        "default_level": 64, "default_diff24h": 1, "default_discharge": 3.8, "default_temp": 7.6,
        "transboundary_anchor": "444226", "downstream_order": 1
    },
    {
        "code": "UA_94107", "country": "UA", "water_category": "minor", "name": "Beregszász (Берегове)", "river": "Vérke-csatorna", "basin": "tisza", "catchment": "ua_latorca_ung_bereg",
        "reach_name": "Vérke-csatorna (Верке) – Borzsa-leágazás – Beregszász (Berehove) – Szernye", "lat": 48.205, "lon": 22.645, "fkm": 16.0,
        "thresholds": {"lkv": 30, "low": 65, "deg1": 210, "deg2": 260, "deg3": 310, "lnv": 375},
        "default_level": 104, "default_diff24h": 1, "default_discharge": 2.9, "default_temp": 7.9,
        "transboundary_anchor": "444510", "downstream_order": 1
    },
    {
        "code": "UA_94108", "country": "UA", "water_category": "minor", "name": "Bátyú / Kisdobrony (Серне)", "river": "Szernye-csatorna", "basin": "tisza", "catchment": "ua_latorca_ung_bereg",
        "reach_name": "Szernye-csatorna (Серне) – Szernye-mocsár – Bátyú – Latorca-zsilip", "lat": 48.365, "lon": 22.415, "fkm": 12.0,
        "thresholds": {"lkv": 40, "low": 80, "deg1": 240, "deg2": 295, "deg3": 350, "lnv": 420},
        "default_level": 126, "default_diff24h": 1, "default_discharge": 4.2, "default_temp": 7.8,
        "transboundary_anchor": "444510", "downstream_order": 1
    },
    {
        "code": "UA_94109", "country": "UA", "water_category": "minor", "name": "Szerednye (Середнє)", "river": "Sztara-patak", "basin": "tisza", "catchment": "ua_latorca_ung_bereg",
        "reach_name": "Sztara-patak (Стара) – Makarja-hegység – Szerednye – Latorca", "lat": 48.538, "lon": 22.505, "fkm": 14.0,
        "thresholds": {"lkv": 10, "low": 35, "deg1": 180, "deg2": 230, "deg3": 280, "lnv": 345},
        "default_level": 58, "default_diff24h": 1, "default_discharge": 2.4, "default_temp": 7.4,
        "transboundary_anchor": "144101", "downstream_order": 1
    },
]
