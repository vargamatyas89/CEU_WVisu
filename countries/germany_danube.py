"""
German Danube Basin / Bavaria & Baden-Württemberg (DE) — Catchments and Hydrological Gauging Stations
(OVF / hydroinfo.hu 34xxxx + HND Bayern live water levels + HVZ Baden-Württemberg live water levels + GloFAS v4)
Standalone region source file (45 German Danube Basin stations: 28 main rivers/Alpine lakes + 17 smaller tributaries)
"""

COUNTRY_META = {
    "code": "DE",
    "name": "Német Duna-vízgyűjtő (DE)",
    "flag": "🇩🇪",
    "border_color": "#34d399",
    "bounds": [[47.27, 8.15], [49.95, 13.85]],
}

CATCHMENTS = {
    "de_donau_swabia": {
        "name": "Felső-Duna forrásvidéke és Sváb-Alb (Donaueschingen–Ulm–Donauwörth)",
        "lat": 48.28,
        "lon": 9.75,
        "response_factor": 3.1,
        "lag_days": 1,
    },
    "de_donau_bavaria": {
        "name": "Bajor Duna-főág, Altmühl, Naab és Regen (Ingolstadt–Regensburg–Passau)",
        "lat": 48.98,
        "lon": 12.15,
        "response_factor": 2.9,
        "lag_days": 2,
    },
    "de_alps_iller_lech_isar": {
        "name": "Bajor-Alpok előtere (Iller, Lech, Wertach, Isar, Amper, Bajor-tavak)",
        "lat": 47.95,
        "lon": 11.20,
        "response_factor": 3.7,
        "lag_days": 1,
    },
    "de_inn_salzach_bavaria": {
        "name": "Bajor Inn–Salzach–Chiemsee és Bajor-erdő (Wasserburg–Burghausen–Ilz)",
        "lat": 48.18,
        "lon": 12.82,
        "response_factor": 3.5,
        "lag_days": 1,
    },
}

STATIONS = [
    # =========================================================================
    # 1. MAIN RIVERS AND BAVARIAN ALPINE LAKES (28 stations — 100% live official telemetry)
    # =========================================================================
    # --- DANUBE / DONAU MAIN STEM: SOURCE TO PASSAU (15 stations) ---
    {
        "code": "DE_BW_00151", "hvz_id": "00151", "country": "DE", "name": "Donaueschingen", "river": "Duna", "basin": "duna", "catchment": "de_donau_swabia",
        "reach_name": "Duna (Donau) – Fekete-erdő – Donaueschingen (Brigach–Breg összefolyás)", "lat": 47.953, "lon": 8.524, "fkm": 2778.0,
        "thresholds": {"lkv": 45, "low": 80, "deg1": 220, "deg2": 290, "deg3": 360, "lnv": 445},
        "default_level": 117, "default_diff24h": 0, "default_discharge": 16.5, "default_temp": 7.0,
        "downstream_order": 1
    },
    {
        "code": "DE_BW_00026", "hvz_id": "00026", "country": "DE", "name": "Beuron", "river": "Duna", "basin": "duna", "catchment": "de_donau_swabia",
        "reach_name": "Duna (Donau) – Tuttlingen – Felső-Duna áttörés – Beuron", "lat": 48.054, "lon": 8.976, "fkm": 2722.0,
        "thresholds": {"lkv": 65, "low": 100, "deg1": 260, "deg2": 330, "deg3": 400, "lnv": 490},
        "default_level": 143, "default_diff24h": 1, "default_discharge": 24.0, "default_temp": 7.1,
        "downstream_order": 2
    },
    {
        "code": "DE_BW_00084", "hvz_id": "00084", "country": "DE", "name": "Sigmaringen", "river": "Duna", "basin": "duna", "catchment": "de_donau_swabia",
        "reach_name": "Duna (Donau) – Beuron – Sigmaringen – Riedlingen", "lat": 48.090, "lon": 9.222, "fkm": 2694.0,
        "thresholds": {"lkv": 30, "low": 60, "deg1": 240, "deg2": 310, "deg3": 380, "lnv": 465},
        "default_level": 92, "default_diff24h": 0, "default_discharge": 29.5, "default_temp": 7.2,
        "downstream_order": 3
    },
    {
        "code": "DE_BW_00006", "hvz_id": "00006", "country": "DE", "name": "Berg (Ehingen)", "river": "Duna", "basin": "duna", "catchment": "de_donau_swabia",
        "reach_name": "Duna (Donau) – Riedlingen – Ehingen / Berg – Ulm felé", "lat": 48.267, "lon": 9.733, "fkm": 2627.0,
        "thresholds": {"lkv": 35, "low": 60, "deg1": 220, "deg2": 290, "deg3": 360, "lnv": 450},
        "default_level": 87, "default_diff24h": 0, "default_discharge": 38.2, "default_temp": 7.3,
        "downstream_order": 4
    },
    {
        "code": "DE_BY_10026293", "hnd_id": "10026293", "country": "DE", "name": "Neu-Ulm / Ulm", "river": "Duna", "basin": "duna", "catchment": "de_donau_swabia",
        "reach_name": "Duna (Donau) – Ulm / Neu-Ulm (Iller-torkolat) – Günzburg", "lat": 48.395, "lon": 9.997, "fkm": 2586.0,
        "thresholds": {"lkv": 100, "low": 145, "deg1": 340, "deg2": 430, "deg3": 510, "lnv": 605},
        "default_level": 191, "default_diff24h": -2, "default_discharge": 128.0, "default_temp": 7.5,
        "downstream_order": 5
    },
    {
        "code": "DE_BY_10035801", "hnd_id": "10035801", "country": "DE", "name": "Dillingen", "river": "Duna", "basin": "duna", "catchment": "de_donau_swabia",
        "reach_name": "Duna (Donau) – Günzburg – Dillingen – Lauingen", "lat": 48.573, "lon": 10.494, "fkm": 2538.0,
        "thresholds": {"lkv": 150, "low": 210, "deg1": 450, "deg2": 520, "deg3": 590, "lnv": 670},
        "default_level": 278, "default_diff24h": -2, "default_discharge": 165.0, "default_temp": 7.6,
        "downstream_order": 6
    },
    {
        "code": "DE_BY_10039802", "hnd_id": "10039802", "country": "DE", "name": "Donauwörth", "river": "Duna", "basin": "duna", "catchment": "de_donau_swabia",
        "reach_name": "Duna (Donau) – Donauwörth (Wörnitz- és Lech-torkolat) – Neuburg", "lat": 48.716, "lon": 10.781, "fkm": 2508.0,
        "thresholds": {"lkv": 55, "low": 90, "deg1": 330, "deg2": 410, "deg3": 480, "lnv": 575},
        "default_level": 119, "default_diff24h": 4, "default_discharge": 191.0, "default_temp": 7.7,
        "downstream_order": 7
    },
    {
        "code": "342205", "hnd_id": "10046105", "country": "DE", "name": "Ingolstadt", "river": "Duna", "basin": "duna", "catchment": "de_donau_bavaria",
        "reach_name": "Duna (Donau) – Neuburg – Ingolstadt – Vohburg", "lat": 48.757, "lon": 11.426, "fkm": 2458.0,
        "thresholds": {"lkv": 90, "low": 140, "deg1": 400, "deg2": 480, "deg3": 560, "lnv": 675},
        "default_level": 192, "default_diff24h": 4, "default_discharge": 271.0, "default_temp": 7.8,
        "downstream_order": 8
    },
    {
        "code": "DE_BY_10053009", "hnd_id": "10053009", "country": "DE", "name": "Kelheim", "river": "Duna", "basin": "duna", "catchment": "de_donau_bavaria",
        "reach_name": "Duna (Donau) – Weltenburgi áttörés – Kelheim (Altmühl–MDK torkolat)", "lat": 48.917, "lon": 11.865, "fkm": 2414.0,
        "thresholds": {"lkv": 150, "low": 215, "deg1": 460, "deg2": 540, "deg3": 610, "lnv": 710},
        "default_level": 282, "default_diff24h": 1, "default_discharge": 294.0, "default_temp": 7.9,
        "downstream_order": 9
    },
    {
        "code": "342206", "hnd_id": "10056302", "country": "DE", "name": "Oberndorf", "river": "Duna", "basin": "duna", "catchment": "de_donau_bavaria",
        "reach_name": "Duna (Donau) – Kelheim – Bad Abbach – Oberndorf", "lat": 48.947, "lon": 12.015, "fkm": 2397.0,
        "thresholds": {"lkv": 100, "low": 155, "deg1": 420, "deg2": 500, "deg3": 580, "lnv": 695},
        "default_level": 204, "default_diff24h": 4, "default_discharge": 262.0, "default_temp": 7.9,
        "downstream_order": 10
    },
    {
        "code": "342001", "hnd_id": "10062000", "country": "DE", "name": "Regensburg-Schwabelweis", "river": "Duna", "basin": "duna", "catchment": "de_donau_bavaria",
        "reach_name": "Duna (Donau) – Regensburg (Naab- és Regen-torkolat) – Pfatter", "lat": 49.024, "lon": 12.139, "fkm": 2376.0,
        "thresholds": {"lkv": 180, "low": 240, "deg1": 480, "deg2": 560, "deg3": 640, "lnv": 745},
        "default_level": 311, "default_diff24h": 6, "default_discharge": 443.0, "default_temp": 8.0,
        "downstream_order": 11
    },
    {
        "code": "342004", "hnd_id": "10078000", "country": "DE", "name": "Pfelling", "river": "Duna", "basin": "duna", "catchment": "de_donau_bavaria",
        "reach_name": "Duna (Donau) – Straubing – Bogen – Pfelling", "lat": 48.880, "lon": 12.747, "fkm": 2305.0,
        "thresholds": {"lkv": 210, "low": 280, "deg1": 520, "deg2": 600, "deg3": 680, "lnv": 790},
        "default_level": 364, "default_diff24h": 0, "default_discharge": 368.0, "default_temp": 8.1,
        "downstream_order": 12
    },
    {
        "code": "342209", "hnd_id": "10081004", "country": "DE", "name": "Deggendorf", "river": "Duna", "basin": "duna", "catchment": "de_donau_bavaria",
        "reach_name": "Duna (Donau) – Deggendorf (Isar-torkolat) – Niederalteich", "lat": 48.825, "lon": 12.962, "fkm": 2285.0,
        "thresholds": {"lkv": 140, "low": 200, "deg1": 480, "deg2": 560, "deg3": 640, "lnv": 755},
        "default_level": 266, "default_diff24h": -4, "default_discharge": 460.0, "default_temp": 8.1,
        "downstream_order": 13
    },
    {
        "code": "342002", "hnd_id": "10088003", "country": "DE", "name": "Hofkirchen", "river": "Duna", "basin": "duna", "catchment": "de_donau_bavaria",
        "reach_name": "Duna (Donau) – Hofkirchen – Vilshofen (Vils-torkolat)", "lat": 48.677, "lon": 13.115, "fkm": 2257.0,
        "thresholds": {"lkv": 135, "low": 195, "deg1": 460, "deg2": 540, "deg3": 620, "lnv": 730},
        "default_level": 262, "default_diff24h": -6, "default_discharge": 493.0, "default_temp": 8.2,
        "downstream_order": 14
    },
    {
        "code": "342211", "hnd_id": "10092000", "country": "DE", "name": "Passau (Ilzstadt)", "river": "Duna", "basin": "duna", "catchment": "de_donau_bavaria",
        "reach_name": "Duna (Donau) – Passau (Háromfolyó-torkolat: Duna–Inn–Ilz) – Achleiten határ", "lat": 48.575, "lon": 13.478, "fkm": 2224.0,
        "thresholds": {"lkv": 280, "low": 350, "deg1": 700, "deg2": 820, "deg3": 950, "lnv": 1289},
        "default_level": 435, "default_diff24h": -3, "default_discharge": 812.0, "default_temp": 8.2,
        "downstream_order": 15
    },

    # --- MAJOR ALPINE TRIBUTARIES: ILLER, LECH, ISAR, INN, SALZACH (10 stations) ---
    {
        "code": "DE_BY_11402001", "hnd_id": "11402001", "country": "DE", "name": "Kempten", "river": "Iller", "basin": "duna", "catchment": "de_alps_iller_lech_isar",
        "reach_name": "Iller – Oberstdorf – Immenstadt – Kempten – Ulm (Duna-torkolat)", "lat": 47.726, "lon": 10.319, "fkm": 102.0,
        "thresholds": {"lkv": 65, "low": 100, "deg1": 290, "deg2": 360, "deg3": 430, "lnv": 530},
        "default_level": 146, "default_diff24h": -5, "default_discharge": 55.0, "default_temp": 6.8,
        "downstream_order": 1
    },
    {
        "code": "DE_BY_12003001", "hnd_id": "12003001", "country": "DE", "name": "Landsberg am Lech", "river": "Lech", "basin": "duna", "catchment": "de_alps_iller_lech_isar",
        "reach_name": "Lech – Füssen – Forggensee – Schongau – Landsberg am Lech", "lat": 48.049, "lon": 10.876, "fkm": 85.0,
        "thresholds": {"lkv": 60, "low": 95, "deg1": 270, "deg2": 340, "deg3": 410, "lnv": 510},
        "default_level": 132, "default_diff24h": 0, "default_discharge": 65.0, "default_temp": 6.9,
        "downstream_order": 1
    },
    {
        "code": "DE_BY_12006000", "hnd_id": "12006000", "country": "DE", "name": "Augsburg", "river": "Lech", "basin": "duna", "catchment": "de_alps_iller_lech_isar",
        "reach_name": "Lech – Augsburg (Wertach-torkolat) – Rain am Lech (Duna-torkolat)", "lat": 48.404, "lon": 10.896, "fkm": 38.0,
        "thresholds": {"lkv": 25, "low": 55, "deg1": 260, "deg2": 330, "deg3": 400, "lnv": 500},
        "default_level": 83, "default_diff24h": -2, "default_discharge": 94.0, "default_temp": 7.3,
        "downstream_order": 2
    },
    {
        "code": "DE_BY_16003207", "hnd_id": "16003207", "country": "DE", "name": "Bad Tölz", "river": "Isar", "basin": "duna", "catchment": "de_alps_iller_lech_isar",
        "reach_name": "Felső-Isar – Mittenwald – Sylvensteinsee – Bad Tölz", "lat": 47.761, "lon": 11.556, "fkm": 197.0,
        "thresholds": {"lkv": 75, "low": 110, "deg1": 290, "deg2": 360, "deg3": 430, "lnv": 530},
        "default_level": 146, "default_diff24h": 0, "default_discharge": 36.0, "default_temp": 6.5,
        "downstream_order": 1
    },
    {
        "code": "DE_BY_16005701", "hnd_id": "16005701", "country": "DE", "name": "München", "river": "Isar", "basin": "duna", "catchment": "de_alps_iller_lech_isar",
        "reach_name": "Isar – Wolfratshausen – München – Freising", "lat": 48.131, "lon": 11.584, "fkm": 147.0,
        "thresholds": {"lkv": 35, "low": 65, "deg1": 240, "deg2": 320, "deg3": 400, "lnv": 520},
        "default_level": 92, "default_diff24h": 0, "default_discharge": 22.0, "default_temp": 7.2,
        "downstream_order": 2
    },
    {
        "code": "DE_BY_16007004", "hnd_id": "16007004", "country": "DE", "name": "Landshut", "river": "Isar", "basin": "duna", "catchment": "de_alps_iller_lech_isar",
        "reach_name": "Isar – Moosburg (Amper-torkolat) – Landshut – Dingolfing", "lat": 48.537, "lon": 12.152, "fkm": 74.0,
        "thresholds": {"lkv": 40, "low": 70, "deg1": 280, "deg2": 360, "deg3": 440, "lnv": 550},
        "default_level": 100, "default_diff24h": 0, "default_discharge": 67.0, "default_temp": 7.6,
        "downstream_order": 3
    },
    {
        "code": "343999", "hnd_id": "16008506", "country": "DE", "name": "Plattling", "river": "Isar", "basin": "duna", "catchment": "de_alps_iller_lech_isar",
        "reach_name": "Alsó-Isar – Landau – Plattling – Deggendorf (Duna-torkolat)", "lat": 48.776, "lon": 12.874, "fkm": 9.0,
        "thresholds": {"lkv": 75, "low": 115, "deg1": 340, "deg2": 420, "deg3": 500, "lnv": 610},
        "default_level": 154, "default_diff24h": 5, "default_discharge": 98.3, "default_temp": 7.8,
        "downstream_order": 4
    },
    {
        "code": "343101", "hnd_id": "18003004", "country": "DE", "name": "Wasserburg am Inn", "river": "Inn", "basin": "duna", "catchment": "de_inn_salzach_bavaria",
        "reach_name": "Bajor Inn – Kufstein határ – Rosenheim – Wasserburg – Mühldorf", "lat": 48.061, "lon": 12.234, "fkm": 159.0,
        "thresholds": {"lkv": 40, "low": 75, "deg1": 320, "deg2": 420, "deg3": 520, "lnv": 665},
        "default_level": 103, "default_diff24h": 0, "default_discharge": 141.0, "default_temp": 7.0,
        "downstream_order": 1
    },
    {
        "code": "343201", "hnd_id": "18008008", "country": "DE", "name": "Passau-Ingling", "river": "Inn", "basin": "duna", "catchment": "de_inn_salzach_bavaria",
        "reach_name": "Alsó-Inn – Simbach / Braunau – Schärding – Passau-Ingling (Duna-torkolat)", "lat": 48.562, "lon": 13.438, "fkm": 3.0,
        "thresholds": {"lkv": 90, "low": 130, "deg1": 450, "deg2": 580, "deg3": 700, "lnv": 920},
        "default_level": 168, "default_diff24h": -1, "default_discharge": 381.0, "default_temp": 7.4,
        "downstream_order": 2
    },
    {
        "code": "343911", "hnd_id": "18606000", "country": "DE", "name": "Burghausen", "river": "Salzach", "basin": "duna", "catchment": "de_inn_salzach_bavaria",
        "reach_name": "Salzach – Laufen – Tittmoning – Burghausen – Haiming (Inn-torkolat)", "lat": 48.163, "lon": 12.834, "fkm": 11.0,
        "thresholds": {"lkv": 60, "low": 95, "deg1": 350, "deg2": 440, "deg3": 530, "lnv": 675},
        "default_level": 127, "default_diff24h": 3, "default_discharge": 111.0, "default_temp": 6.8,
        "downstream_order": 1
    },

    # --- BAVARIAN ALPINE LAKES (3 stations — HND Bayern live level m ü. NHN -> relative cm) ---
    {
        "code": "DE_BY_18400503", "hnd_id": "18400503", "zero_m_nhn": 517.0, "country": "DE", "name": "Chiemsee (Stock)", "river": "Chiemsee", "basin": "tavak", "catchment": "de_inn_salzach_bavaria",
        "reach_name": "Chiemsee – Bajor-tenger (Prien / Stock – Seebruck, Alz lefolyás)", "lat": 47.855, "lon": 12.362, "fkm": 0.0,
        "thresholds": {"lkv": 45, "low": 65, "deg1": 145, "deg2": 180, "deg3": 215, "lnv": 265},
        "default_level": 83, "default_diff24h": 0, "default_discharge": 20.7, "default_temp": 8.4,
        "downstream_order": 1
    },
    {
        "code": "DE_BY_16663002", "hnd_id": "16663002", "zero_m_nhn": 583.0, "country": "DE", "name": "Starnberger See (Starnberg)", "river": "Starnberger See", "basin": "tavak", "catchment": "de_alps_iller_lech_isar",
        "reach_name": "Starnberger See – Starnberg – Tutzing – Seeshaupt (Würm lefolyás)", "lat": 47.994, "lon": 11.345, "fkm": 0.0,
        "thresholds": {"lkv": 45, "low": 65, "deg1": 135, "deg2": 165, "deg3": 195, "lnv": 235},
        "default_level": 79, "default_diff24h": -1, "default_discharge": 4.5, "default_temp": 8.2,
        "downstream_order": 1
    },
    {
        "code": "DE_BY_16602008", "hnd_id": "16602008", "zero_m_nhn": 532.0, "country": "DE", "name": "Ammersee (Stegen)", "river": "Ammersee", "basin": "tavak", "catchment": "de_alps_iller_lech_isar",
        "reach_name": "Ammersee – Herrsching – Dießen – Stegen (Amper lefolyás)", "lat": 48.075, "lon": 11.135, "fkm": 0.0,
        "thresholds": {"lkv": 50, "low": 70, "deg1": 150, "deg2": 185, "deg3": 220, "lnv": 270},
        "default_level": 84, "default_diff24h": -1, "default_discharge": 13.0, "default_temp": 8.1,
        "downstream_order": 1
    },

    # =========================================================================
    # 2. SMALLER RIVERS AND REGIONAL TRIBUTARIES (17 stations — water_category="minor")
    # =========================================================================
    {
        "code": "DE_BW_00121", "hvz_id": "00121", "country": "DE", "water_category": "minor", "name": "Donaueschingen (Breg)", "river": "Breg", "basin": "duna", "catchment": "de_donau_swabia",
        "reach_name": "Breg (Duna leghosszabb forrásága) – Furtwangen – Donaueschingen", "lat": 47.937, "lon": 8.502, "fkm": 46.0,
        "thresholds": {"lkv": 30, "low": 55, "deg1": 185, "deg2": 240, "deg3": 295, "lnv": 360},
        "default_level": 94, "default_diff24h": 0, "default_discharge": 12.7, "default_temp": 6.8,
        "downstream_order": 1
    },
    {
        "code": "DE_BY_12407000", "hnd_id": "12407000", "country": "DE", "water_category": "minor", "name": "Augsburg-Oberhausen (Wertach)", "river": "Wertach", "basin": "duna", "catchment": "de_alps_iller_lech_isar",
        "reach_name": "Wertach – Kaufbeuren – Türkheim – Augsburg (Lech-torkolat)", "lat": 48.382, "lon": 10.867, "fkm": 4.0,
        "thresholds": {"lkv": 45, "low": 75, "deg1": 240, "deg2": 300, "deg3": 360, "lnv": 430},
        "default_level": 99, "default_diff24h": -7, "default_discharge": 17.0, "default_temp": 7.2,
        "downstream_order": 1
    },
    {
        "code": "DE_BY_11809009", "hnd_id": "11809009", "country": "DE", "water_category": "minor", "name": "Harburg (Wörnitz)", "river": "Wörnitz", "basin": "duna", "catchment": "de_donau_swabia",
        "reach_name": "Wörnitz – Dinkelsbühl – Nördlinger Ries – Harburg – Donauwörth", "lat": 48.786, "lon": 10.688, "fkm": 14.0,
        "thresholds": {"lkv": 55, "low": 90, "deg1": 270, "deg2": 330, "deg3": 390, "lnv": 465},
        "default_level": 135, "default_diff24h": 0, "default_discharge": 5.0, "default_temp": 7.5,
        "downstream_order": 1
    },
    {
        "code": "343612", "hnd_id": "13407902", "country": "DE", "water_category": "minor", "name": "Beilngries (Altmühl)", "river": "Altmühl", "basin": "duna", "catchment": "de_donau_bavaria",
        "reach_name": "Altmühl – Treuchtlingen – Eichstätt – Beilngries – Kelheim (MDK/Duna)", "lat": 49.035, "lon": 11.472, "fkm": 36.0,
        "thresholds": {"lkv": 15, "low": 30, "deg1": 165, "deg2": 220, "deg3": 275, "lnv": 345},
        "default_level": 42, "default_diff24h": 0, "default_discharge": 6.97, "default_temp": 7.6,
        "downstream_order": 1
    },
    {
        "code": "DE_BY_13208000", "hnd_id": "13208000", "country": "DE", "water_category": "minor", "name": "Manching (Paar)", "river": "Paar", "basin": "duna", "catchment": "de_donau_bavaria",
        "reach_name": "Paar – Aichach – Schrobenhausen – Manching – Vohburg (Duna-torkolat)", "lat": 48.718, "lon": 11.495, "fkm": 12.0,
        "thresholds": {"lkv": 25, "low": 45, "deg1": 195, "deg2": 250, "deg3": 305, "lnv": 370},
        "default_level": 65, "default_diff24h": -1, "default_discharge": 4.0, "default_temp": 7.5,
        "downstream_order": 1
    },
    {
        "code": "DE_BY_13322005", "hnd_id": "13322005", "country": "DE", "water_category": "minor", "name": "Abensberg / Aunkofen (Abens)", "river": "Abens", "basin": "duna", "catchment": "de_donau_bavaria",
        "reach_name": "Abens – Hallertau – Mainburg – Abensberg – Neustadt (Duna-torkolat)", "lat": 48.815, "lon": 11.844, "fkm": 9.0,
        "thresholds": {"lkv": 55, "low": 85, "deg1": 225, "deg2": 280, "deg3": 335, "lnv": 400},
        "default_level": 125, "default_diff24h": -3, "default_discharge": 1.6, "default_temp": 7.6,
        "downstream_order": 1
    },
    {
        "code": "DE_BY_14004708", "hnd_id": "14004708", "country": "DE", "water_category": "minor", "name": "Schwandorf (Naab)", "river": "Naab", "basin": "duna", "catchment": "de_donau_bavaria",
        "reach_name": "Felső-Naab – Weiden – Nabburg – Schwandorf", "lat": 49.327, "lon": 12.104, "fkm": 55.0,
        "thresholds": {"lkv": 50, "low": 85, "deg1": 270, "deg2": 340, "deg3": 410, "lnv": 495},
        "default_level": 128, "default_diff24h": -1, "default_discharge": 42.0, "default_temp": 7.4,
        "downstream_order": 1
    },
    {
        "code": "343703", "hnd_id": "14008006", "country": "DE", "water_category": "minor", "name": "Heitzenhofen (Naab)", "river": "Naab", "basin": "duna", "catchment": "de_donau_bavaria",
        "reach_name": "Alsó-Naab – Burglengenfeld – Heitzenhofen – Regensburg (Duna-torkolat)", "lat": 49.118, "lon": 11.984, "fkm": 16.0,
        "thresholds": {"lkv": 55, "low": 90, "deg1": 310, "deg2": 385, "deg3": 460, "lnv": 555},
        "default_level": 147, "default_diff24h": 40, "default_discharge": 71.7, "default_temp": 7.6,
        "downstream_order": 2
    },
    {
        "code": "343799", "hnd_id": "15207507", "country": "DE", "water_category": "minor", "name": "Marienthal (Regen)", "river": "Regen", "basin": "duna", "catchment": "de_donau_bavaria",
        "reach_name": "Regen – Bajor-erdő – Cham – Roding – Marienthal – Regensburg (Duna-torkolat)", "lat": 49.152, "lon": 12.279, "fkm": 32.0,
        "thresholds": {"lkv": 140, "low": 195, "deg1": 400, "deg2": 480, "deg3": 560, "lnv": 665},
        "default_level": 282, "default_diff24h": 19, "default_discharge": 54.7, "default_temp": 7.2,
        "downstream_order": 1
    },
    {
        "code": "DE_BY_16408504", "hnd_id": "16408504", "country": "DE", "water_category": "minor", "name": "Beuerberg (Loisach)", "river": "Loisach", "basin": "duna", "catchment": "de_alps_iller_lech_isar",
        "reach_name": "Loisach – Garmisch-Partenkirchen – Kochelsee – Beuerberg – Wolfratshausen (Isar)", "lat": 47.835, "lon": 11.416, "fkm": 12.0,
        "thresholds": {"lkv": 170, "low": 225, "deg1": 400, "deg2": 470, "deg3": 540, "lnv": 625},
        "default_level": 292, "default_diff24h": -1, "default_discharge": 32.0, "default_temp": 6.7,
        "downstream_order": 1
    },
    {
        "code": "DE_BY_16607001", "hnd_id": "16607001", "country": "DE", "water_category": "minor", "name": "Inkofen (Amper)", "river": "Amper", "basin": "duna", "catchment": "de_alps_iller_lech_isar",
        "reach_name": "Amper – Ammersee – Fürstenfeldbruck – Dachau – Inkofen – Moosburg (Isar)", "lat": 48.474, "lon": 11.898, "fkm": 11.0,
        "thresholds": {"lkv": 20, "low": 40, "deg1": 180, "deg2": 235, "deg3": 290, "lnv": 355},
        "default_level": 60, "default_diff24h": -3, "default_discharge": 28.0, "default_temp": 7.5,
        "downstream_order": 1
    },
    {
        "code": "DE_BY_18209000", "hnd_id": "18209000", "country": "DE", "water_category": "minor", "name": "Rosenheim (Mangfall)", "river": "Mangfall", "basin": "duna", "catchment": "de_inn_salzach_bavaria",
        "reach_name": "Mangfall – Tegernsee – Bad Aibling – Rosenheim (Inn-torkolat)", "lat": 47.848, "lon": 12.126, "fkm": 4.0,
        "thresholds": {"lkv": 30, "low": 55, "deg1": 210, "deg2": 270, "deg3": 330, "lnv": 410},
        "default_level": 75, "default_diff24h": 2, "default_discharge": 7.0, "default_temp": 7.1,
        "downstream_order": 1
    },
    {
        "code": "343991", "hnd_id": "18403002", "country": "DE", "water_category": "minor", "name": "Seebruck (Alz)", "river": "Alz", "basin": "duna", "catchment": "de_inn_salzach_bavaria",
        "reach_name": "Alz – Chiemsee lefolyása – Seebruck – Trostberg – Marktl (Inn-torkolat)", "lat": 47.935, "lon": 12.478, "fkm": 58.0,
        "thresholds": {"lkv": 10, "low": 25, "deg1": 145, "deg2": 190, "deg3": 240, "lnv": 310},
        "default_level": 40, "default_diff24h": 0, "default_discharge": 20.7, "default_temp": 7.8,
        "downstream_order": 1
    },
    {
        "code": "343933", "hnd_id": "18642003", "country": "DE", "water_category": "minor", "name": "Unterjettenberg (Saalach)", "river": "Saalach", "basin": "duna", "catchment": "de_inn_salzach_bavaria",
        "reach_name": "Saalach – Berchtesgadeni-Alpok – Unterjettenberg – Bad Reichenhall (Salzach)", "lat": 47.674, "lon": 12.828, "fkm": 24.0,
        "thresholds": {"lkv": 0, "low": 10, "deg1": 180, "deg2": 240, "deg3": 310, "lnv": 410},
        "default_level": 19, "default_diff24h": 3, "default_discharge": 17.1, "default_temp": 6.4,
        "downstream_order": 1
    },
    {
        "code": "343903", "hnd_id": "17207508", "country": "DE", "water_category": "minor", "name": "Grafenmühle (Vils)", "river": "Vils", "basin": "duna", "catchment": "de_donau_bavaria",
        "reach_name": "Vils – Vilsbiburg – Aldersbach – Grafenmühle – Vilshofen (Duna-torkolat)", "lat": 48.613, "lon": 13.106, "fkm": 11.0,
        "thresholds": {"lkv": 35, "low": 60, "deg1": 240, "deg2": 310, "deg3": 380, "lnv": 470},
        "default_level": 89, "default_diff24h": -3, "default_discharge": 4.07, "default_temp": 7.5,
        "downstream_order": 1
    },
    {
        "code": "DE_BY_18808004", "hnd_id": "18808004", "country": "DE", "water_category": "minor", "name": "Ruhstorf (Rott)", "river": "Rott", "basin": "duna", "catchment": "de_inn_salzach_bavaria",
        "reach_name": "Rott – Eggenfelden – Pfarrkirchen – Ruhstorf – Neuhaus (Inn-torkolat)", "lat": 48.438, "lon": 13.337, "fkm": 8.0,
        "thresholds": {"lkv": 10, "low": 25, "deg1": 210, "deg2": 275, "deg3": 340, "lnv": 430},
        "default_level": 36, "default_diff24h": -1, "default_discharge": 2.0, "default_temp": 7.5,
        "downstream_order": 1
    },
    {
        "code": "343908", "hnd_id": "17406005", "country": "DE", "water_category": "minor", "name": "Kalteneck (Ilz)", "river": "Ilz", "basin": "duna", "catchment": "de_inn_salzach_bavaria",
        "reach_name": "Ilz – Bajor-erdő – Grafenau – Kalteneck – Passau (Duna-torkolat)", "lat": 48.697, "lon": 13.455, "fkm": 22.0,
        "thresholds": {"lkv": 40, "low": 65, "deg1": 250, "deg2": 320, "deg3": 395, "lnv": 490},
        "default_level": 96, "default_diff24h": -16, "default_discharge": 15.8, "default_temp": 6.6,
        "downstream_order": 1
    },
]
