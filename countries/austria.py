"""
Austria (AT) — Catchments and Official Hydrological Gauging Stations (eHYD / OVF hydroinfo.hu 24xxxx & Copernicus GloFAS v4)
Standalone country source file (41 Austrian gauges: Danube main stem, Alpine main rivers, lakes and tributaries)
"""

COUNTRY_META = {
    "code": "AT",
    "name": "Ausztria",
    "flag": "🇦🇹",
    "border_color": "#fb7185",
    "bounds": [[46.37, 9.53], [49.02, 17.16]],
}

CATCHMENTS = {
    "at_upper_danube_inn": {"name": "Felső-Ausztria, Inn, Salzach és Traun vízgyűjtő (AT)", "lat": 48.18, "lon": 13.85, "response_factor": 2.9, "lag_days": 1},
    "at_lower_danube_vienna": {"name": "Alsó-Ausztria, Wachau, Bécsi-medence és Thaya (AT)", "lat": 48.25, "lon": 16.05, "response_factor": 2.6, "lag_days": 2},
    "at_styria_mur_raab": {"name": "Stájerország és Burgenland (Mura, Rába, Lajta, Pinka, AT)", "lat": 47.12, "lon": 15.65, "response_factor": 3.2, "lag_days": 1},
    "at_carinthia_tyrol_drau": {"name": "Karintia és Tirol (Dráva, Gail, Möll, Felső-Inn, AT)", "lat": 46.72, "lon": 13.45, "response_factor": 3.4, "lag_days": 1},
}

STATIONS = [
    # =========================================================================
    # 1. MAIN RIVERS AND ALPINE LAKES (26 stations — live 24xxxx hydroinfo.hu & eHYD/GloFAS)
    # =========================================================================
    # --- AUSTRIAN DANUBE MAIN STEM (9 live 242xxx stations) ---
    {
        "code": "242006", "country": "AT", "name": "Engelhartszell", "river": "Duna", "basin": "duna", "catchment": "at_upper_danube_inn",
        "reach_name": "Duna (Donau) – Passau – Engelhartszell felső-ausztriai belépő szakasz", "lat": 48.502, "lon": 13.732, "fkm": 2201.7,
        "thresholds": {"lkv": 190, "low": 260, "deg1": 620, "deg2": 720, "deg3": 820, "lnv": 1081},
        "default_level": 389, "default_diff24h": 5, "default_discharge": 910, "default_temp": 7.1, "downstream_order": 1
    },
    {
        "code": "242008", "country": "AT", "name": "Linz", "river": "Duna", "basin": "duna", "catchment": "at_upper_danube_inn",
        "reach_name": "Duna (Donau) – Aschach – Linz fővárosi szakasz", "lat": 48.308, "lon": 14.288, "fkm": 2135.2,
        "thresholds": {"lkv": 210, "low": 270, "deg1": 550, "deg2": 650, "deg3": 750, "lnv": 962},
        "default_level": 351, "default_diff24h": -4, "default_discharge": 935, "default_temp": 7.2, "downstream_order": 2
    },
    {
        "code": "242009", "country": "AT", "name": "Mauthausen", "river": "Duna", "basin": "duna", "catchment": "at_upper_danube_inn",
        "reach_name": "Duna (Donau) – Traun- és Enns-torkolat – Mauthausen", "lat": 48.242, "lon": 14.515, "fkm": 2111.1,
        "thresholds": {"lkv": 260, "low": 330, "deg1": 620, "deg2": 710, "deg3": 800, "lnv": 967},
        "default_level": 430, "default_diff24h": 3, "default_discharge": 980, "default_temp": 7.2, "downstream_order": 3
    },
    {
        "code": "242010", "country": "AT", "name": "Ybbs", "river": "Duna", "basin": "duna", "catchment": "at_lower_danube_vienna",
        "reach_name": "Duna (Donau) – Grein – Ybbs-Persenbeug szakasz", "lat": 48.178, "lon": 15.085, "fkm": 2058.8,
        "thresholds": {"lkv": 110, "low": 160, "deg1": 510, "deg2": 600, "deg3": 690, "lnv": 865},
        "default_level": 223, "default_diff24h": 0, "default_discharge": 985, "default_temp": 7.3, "downstream_order": 4
    },
    {
        "code": "242120", "country": "AT", "name": "Melk", "river": "Duna", "basin": "duna", "catchment": "at_lower_danube_vienna",
        "reach_name": "Duna (Donau) – Melk – Wachau kapuja", "lat": 48.228, "lon": 15.328, "fkm": 2036.0,
        "thresholds": {"lkv": 120, "low": 175, "deg1": 540, "deg2": 640, "deg3": 740, "lnv": 910},
        "default_level": 252, "default_diff24h": 14, "default_discharge": 990, "default_temp": 7.3, "downstream_order": 5
    },
    {
        "code": "242011", "country": "AT", "name": "Kienstock (Wachau)", "river": "Duna", "basin": "duna", "catchment": "at_lower_danube_vienna",
        "reach_name": "Duna (Donau) – Wachau (Spitz – Kienstock – Krems)", "lat": 48.385, "lon": 15.462, "fkm": 2015.2,
        "thresholds": {"lkv": 85, "low": 135, "deg1": 580, "deg2": 690, "deg3": 800, "lnv": 1093},
        "default_level": 177, "default_diff24h": 13, "default_discharge": 987, "default_temp": 7.4, "downstream_order": 6
    },
    {
        "code": "242013", "country": "AT", "name": "Korneuburg (Bécs)", "river": "Duna", "basin": "duna", "catchment": "at_lower_danube_vienna",
        "reach_name": "Duna (Donau) – Tulln – Korneuburg – Bécs (Wien)", "lat": 48.338, "lon": 16.322, "fkm": 1941.6,
        "thresholds": {"lkv": 95, "low": 155, "deg1": 540, "deg2": 640, "deg3": 730, "lnv": 809},
        "default_level": 211, "default_diff24h": 6, "default_discharge": 1040, "default_temp": 7.5, "downstream_order": 7
    },
    {
        "code": "242014", "country": "AT", "name": "Wildungsmauer", "river": "Duna", "basin": "duna", "catchment": "at_lower_danube_vienna",
        "reach_name": "Duna (Donau) – Schwechat – Fischamend – Wildungsmauer", "lat": 48.118, "lon": 16.792, "fkm": 1894.7,
        "thresholds": {"lkv": 40, "low": 95, "deg1": 540, "deg2": 640, "deg3": 730, "lnv": 884},
        "default_level": 151, "default_diff24h": 11, "default_discharge": 983, "default_temp": 7.5, "downstream_order": 8
    },
    {
        "code": "242015", "country": "AT", "name": "Hainburg", "river": "Duna", "basin": "duna", "catchment": "at_lower_danube_vienna",
        "reach_name": "Duna (Donau) – Petronell – Hainburg an der Donau (osztrák–szlovák határ)", "lat": 48.148, "lon": 16.942, "fkm": 1883.9,
        "thresholds": {"lkv": 20, "low": 75, "deg1": 560, "deg2": 660, "deg3": 760, "lnv": 944},
        "default_level": 120, "default_diff24h": 12, "default_discharge": 971, "default_temp": 7.5, "downstream_order": 9
    },

    # --- ALPINE MAIN RIVERS (Inn, Salzach, Traun, Enns, Drava, Mur, Rába, Morava — 13 stations) ---
    {
        "code": "249001", "country": "AT", "name": "Innsbruck", "river": "Inn", "basin": "duna", "catchment": "at_carinthia_tyrol_drau",
        "reach_name": "Inn – Felső- és Közép-Inn (Landeck – Innsbruck – Schwaz)", "lat": 47.268, "lon": 11.392, "fkm": 296.0,
        "thresholds": {"lkv": 90, "low": 145, "deg1": 460, "deg2": 530, "deg3": 600, "lnv": 715},
        "default_level": 198, "default_diff24h": -2, "default_discharge": 118.0, "default_temp": 5.6, "downstream_order": 1
    },
    {
        "code": "243102", "country": "AT", "name": "Schärding", "river": "Inn", "basin": "duna", "catchment": "at_upper_danube_inn",
        "reach_name": "Inn – Alsó-Inn (Braunau – Schärding – Passau Duna-torkolat)", "lat": 48.455, "lon": 13.432, "fkm": 16.2,
        "thresholds": {"lkv": 190, "low": 270, "deg1": 580, "deg2": 690, "deg3": 800, "lnv": 1070},
        "default_level": 356, "default_diff24h": 1, "default_discharge": 410.0, "default_temp": 6.8, "downstream_order": 2
    },
    {
        "code": "243111", "country": "AT", "name": "Salzburg", "river": "Salzach", "basin": "duna", "catchment": "at_upper_danube_inn",
        "reach_name": "Salzach – Hallein – Salzburg – Oberndorf", "lat": 47.802, "lon": 13.042, "fkm": 64.5,
        "thresholds": {"lkv": 380, "low": 460, "deg1": 720, "deg2": 790, "deg3": 850, "lnv": 965},
        "default_level": 546, "default_diff24h": 0, "default_discharge": 125.0, "default_temp": 6.4, "downstream_order": 1
    },
    {
        "code": "242210", "country": "AT", "name": "Wels-Lichtenegg", "river": "Traun", "basin": "duna", "catchment": "at_upper_danube_inn",
        "reach_name": "Traun – Gmunden – Lambach – Wels-Lichtenegg – Linz", "lat": 48.155, "lon": 14.018, "fkm": 32.8,
        "thresholds": {"lkv": 60, "low": 100, "deg1": 360, "deg2": 430, "deg3": 500, "lnv": 612},
        "default_level": 139, "default_diff24h": -4, "default_discharge": 68.0, "default_temp": 6.9, "downstream_order": 1
    },
    {
        "code": "242220", "country": "AT", "name": "Steyr", "river": "Enns", "basin": "duna", "catchment": "at_upper_danube_inn",
        "reach_name": "Enns – Admont – Großraming – Steyr – Enns (Duna-torkolat)", "lat": 48.042, "lon": 14.422, "fkm": 30.6,
        "thresholds": {"lkv": 95, "low": 140, "deg1": 420, "deg2": 500, "deg3": 580, "lnv": 715},
        "default_level": 183, "default_diff24h": -16, "default_discharge": 45.0, "default_temp": 6.7, "downstream_order": 1
    },
    {
        "code": "249002", "country": "AT", "name": "Lienz", "river": "Dráva", "basin": "drava", "catchment": "at_carinthia_tyrol_drau",
        "reach_name": "Dráva (Drau) – Kelet-Tirol és Felső-Dráva-völgy (Lienz – Spittal)", "lat": 46.828, "lon": 12.768, "fkm": 635.0,
        "thresholds": {"lkv": 60, "low": 105, "deg1": 310, "deg2": 370, "deg3": 430, "lnv": 525},
        "default_level": 148, "default_diff24h": -1, "default_discharge": 42.0, "default_temp": 6.0, "downstream_order": 1
    },
    {
        "code": "249003", "country": "AT", "name": "Villach", "river": "Dráva", "basin": "drava", "catchment": "at_carinthia_tyrol_drau",
        "reach_name": "Dráva (Drau) – Karintiai-medence (Villach – Ferlach – Völkermarkt)", "lat": 46.615, "lon": 13.852, "fkm": 542.0,
        "thresholds": {"lkv": 80, "low": 135, "deg1": 390, "deg2": 460, "deg3": 530, "lnv": 645},
        "default_level": 195, "default_diff24h": 2, "default_discharge": 145.0, "default_temp": 6.9, "downstream_order": 2
    },
    {
        "code": "249004", "country": "AT", "name": "Lavamünd", "river": "Dráva", "basin": "drava", "catchment": "at_carinthia_tyrol_drau",
        "reach_name": "Dráva (Drau) – Lavant-torkolat – Lavamünd (osztrák–szlovén határ)", "lat": 46.642, "lon": 14.945, "fkm": 456.0,
        "thresholds": {"lkv": 100, "low": 160, "deg1": 450, "deg2": 530, "deg3": 610, "lnv": 740},
        "default_level": 238, "default_diff24h": 4, "default_discharge": 215.0, "default_temp": 7.3, "downstream_order": 3
    },
    {
        "code": "249005", "country": "AT", "name": "Bruck an der Mur", "river": "Mura", "basin": "drava", "catchment": "at_styria_mur_raab",
        "reach_name": "Mura (Mur) – Felső-Mura (Judenburg – Leoben – Bruck an der Mur)", "lat": 47.412, "lon": 15.268, "fkm": 235.0,
        "thresholds": {"lkv": 70, "low": 120, "deg1": 360, "deg2": 430, "deg3": 500, "lnv": 610},
        "default_level": 172, "default_diff24h": 1, "default_discharge": 74.0, "default_temp": 6.5, "downstream_order": 1
    },
    {
        "code": "249006", "country": "AT", "name": "Graz", "river": "Mura", "basin": "drava", "catchment": "at_styria_mur_raab",
        "reach_name": "Mura (Mur) – Stájer fővárosi szakasz (Frohnleiten – Graz – Wildon)", "lat": 47.072, "lon": 15.435, "fkm": 178.0,
        "thresholds": {"lkv": 85, "low": 140, "deg1": 410, "deg2": 480, "deg3": 550, "lnv": 670},
        "default_level": 204, "default_diff24h": 2, "default_discharge": 105.0, "default_temp": 7.0, "downstream_order": 2
    },
    {
        "code": "249007", "country": "AT", "name": "Spielfeld (Bad Radkersburg)", "river": "Mura", "basin": "drava", "catchment": "at_styria_mur_raab",
        "reach_name": "Mura (Mur) – Leibnitz – Spielfeld – Bad Radkersburg", "lat": 46.708, "lon": 15.635, "fkm": 115.0,
        "thresholds": {"lkv": 90, "low": 150, "deg1": 440, "deg2": 520, "deg3": 600, "lnv": 725},
        "default_level": 226, "default_diff24h": 3, "default_discharge": 128.0, "default_temp": 7.4, "downstream_order": 3
    },
    {
        "code": "249008", "country": "AT", "name": "Feldbach (Jennersdorf)", "river": "Rába", "basin": "duna", "catchment": "at_styria_mur_raab",
        "reach_name": "Rába (Raab) – Gleisdorf – Feldbach – Fehring – Jennersdorf (Szentgotthárd előtt)", "lat": 46.952, "lon": 15.888, "fkm": 238.0,
        "thresholds": {"lkv": 30, "low": 70, "deg1": 280, "deg2": 340, "deg3": 400, "lnv": 485},
        "default_level": 114, "default_diff24h": 5, "default_discharge": 14.5, "default_temp": 7.0, "downstream_order": 1
    },
    {
        "code": "249009", "country": "AT", "name": "Angern an der March", "river": "Morva", "basin": "duna", "catchment": "at_lower_danube_vienna",
        "reach_name": "Morva (March) – Hohenau – Dürnkrut – Angern an der March (osztrák–szlovák határ)", "lat": 48.378, "lon": 16.832, "fkm": 32.0,
        "thresholds": {"lkv": 30, "low": 80, "deg1": 410, "deg2": 480, "deg3": 540, "lnv": 625},
        "default_level": 138, "default_diff24h": 8, "default_discharge": 66.0, "default_temp": 7.3, "downstream_order": 1
    },

    # --- AUSTRIAN ALPINE LAKES (4 stations) ---
    {
        "code": "249010", "country": "AT", "name": "Kammer (Attersee)", "river": "Attersee", "basin": "tavak", "catchment": "at_upper_danube_inn",
        "reach_name": "Attersee (Salzkammergut – Kammer – Weyregg)", "lat": 47.925, "lon": 13.552, "fkm": 0.0,
        "thresholds": {"lkv": 80, "low": 120, "deg1": 240, "deg2": 270, "deg3": 300, "lnv": 345},
        "default_level": 158, "default_diff24h": 1, "default_discharge": 18.0, "default_temp": 8.1, "downstream_order": 1
    },
    {
        "code": "249011", "country": "AT", "name": "Gmunden (Traunsee)", "river": "Traunsee", "basin": "tavak", "catchment": "at_upper_danube_inn",
        "reach_name": "Traunsee (Salzkammergut – Gmunden – Ebensee)", "lat": 47.882, "lon": 13.798, "fkm": 0.0,
        "thresholds": {"lkv": 70, "low": 115, "deg1": 250, "deg2": 285, "deg3": 320, "lnv": 370},
        "default_level": 152, "default_diff24h": 0, "default_discharge": 26.0, "default_temp": 7.9, "downstream_order": 1
    },
    {
        "code": "249012", "country": "AT", "name": "Klagenfurt (Wörthersee)", "river": "Wörthersee", "basin": "tavak", "catchment": "at_carinthia_tyrol_drau",
        "reach_name": "Wörthersee (Karintia – Velden – Pörtschach – Klagenfurt)", "lat": 46.628, "lon": 14.158, "fkm": 0.0,
        "thresholds": {"lkv": 65, "low": 105, "deg1": 215, "deg2": 245, "deg3": 275, "lnv": 315},
        "default_level": 138, "default_diff24h": 1, "default_discharge": 9.5, "default_temp": 8.6, "downstream_order": 1
    },
    {
        "code": "249013", "country": "AT", "name": "Bregenz (Bodeni-tó)", "river": "Bodeni-tó (Bodensee)", "basin": "tavak", "catchment": "at_carinthia_tyrol_drau",
        "reach_name": "Bodeni-tó osztrák medence (Bodensee – Bregenz – Hard)", "lat": 47.508, "lon": 9.738, "fkm": 0.0,
        "thresholds": {"lkv": 210, "low": 270, "deg1": 460, "deg2": 500, "deg3": 540, "lnv": 610},
        "default_level": 334, "default_diff24h": 2, "default_discharge": 290.0, "default_temp": 8.4, "downstream_order": 1
    },

    # =========================================================================
    # 2. SMALLER WATERS, ALPINE STREAMS AND TRIBUTARIES (15 stations — eHYD & GloFAS v4)
    # =========================================================================
    {
        "code": "249101", "water_category": "minor", "country": "AT",
        "name": "Bruck an der Leitha", "river": "Lajta", "basin": "duna", "catchment": "at_lower_danube_vienna",
        "reach_name": "Felső- és Közép-Lajta (Leitha) – Wiener Neustadt – Bruck an der Leitha – Gattendorf", "lat": 48.028, "lon": 16.782, "fkm": 42.0,
        "thresholds": {"lkv": 20, "low": 48, "deg1": 195, "deg2": 235, "deg3": 275, "lnv": 330},
        "default_level": 78, "default_diff24h": -4, "default_discharge": 8.2, "default_temp": 7.3, "downstream_order": 1
    },
    {
        "code": "249102", "water_category": "minor", "country": "AT",
        "name": "Bernhardsthal (Laa)", "river": "Thaya", "basin": "duna", "catchment": "at_lower_danube_vienna",
        "reach_name": "Thaya (Dyje) – Raabs – Laa an der Thaya – Bernhardsthal (Morva-torkolat)", "lat": 48.692, "lon": 16.885, "fkm": 18.0,
        "thresholds": {"lkv": 35, "low": 75, "deg1": 290, "deg2": 350, "deg3": 410, "lnv": 495},
        "default_level": 124, "default_diff24h": 3, "default_discharge": 28.0, "default_temp": 7.1, "downstream_order": 1
    },
    {
        "code": "249103", "water_category": "minor", "country": "AT",
        "name": "Stiefern (Zwettl)", "river": "Kamp", "basin": "duna", "catchment": "at_lower_danube_vienna",
        "reach_name": "Kamp (Waldviertel) – Ottenstein-tározó – Gars am Kamp – Stiefern – Grafenwörth", "lat": 48.532, "lon": 15.692, "fkm": 28.0,
        "thresholds": {"lkv": 40, "low": 75, "deg1": 260, "deg2": 320, "deg3": 380, "lnv": 465},
        "default_level": 112, "default_diff24h": 1, "default_discharge": 9.4, "default_temp": 6.6, "downstream_order": 1
    },
    {
        "code": "249104", "water_category": "minor", "country": "AT",
        "name": "St. Pölten", "river": "Traisen", "basin": "duna", "catchment": "at_lower_danube_vienna",
        "reach_name": "Traisen – Lilienfeld – Wilhelmsburg – St. Pölten – Traismauer (Duna)", "lat": 48.205, "lon": 15.635, "fkm": 22.0,
        "thresholds": {"lkv": 30, "low": 65, "deg1": 250, "deg2": 310, "deg3": 370, "lnv": 450},
        "default_level": 98, "default_diff24h": 2, "default_discharge": 11.5, "default_temp": 6.9, "downstream_order": 1
    },
    {
        "code": "249105", "water_category": "minor", "country": "AT",
        "name": "Wieselburg", "river": "Erlauf", "basin": "duna", "catchment": "at_lower_danube_vienna",
        "reach_name": "Erlauf – Scheibbs – Wieselburg – Pöchlarn (Duna)", "lat": 48.135, "lon": 15.138, "fkm": 14.0,
        "thresholds": {"lkv": 25, "low": 58, "deg1": 230, "deg2": 285, "deg3": 340, "lnv": 415},
        "default_level": 86, "default_diff24h": 1, "default_discharge": 8.8, "default_temp": 6.7, "downstream_order": 1
    },
    {
        "code": "249106", "water_category": "minor", "country": "AT",
        "name": "Amstetten (Greinsfurth)", "river": "Ybbs-folyó", "basin": "duna", "catchment": "at_lower_danube_vienna",
        "reach_name": "Ybbs-folyó – Waidhofen an der Ybbs – Amstetten – Ybbs an der Donau", "lat": 48.118, "lon": 14.865, "fkm": 19.0,
        "thresholds": {"lkv": 35, "low": 70, "deg1": 270, "deg2": 330, "deg3": 390, "lnv": 475},
        "default_level": 106, "default_diff24h": -2, "default_discharge": 16.2, "default_temp": 6.8, "downstream_order": 1
    },
    {
        "code": "249107", "water_category": "minor", "country": "AT",
        "name": "Schwechat (Baden)", "river": "Schwechat", "basin": "duna", "catchment": "at_lower_danube_vienna",
        "reach_name": "Schwechat (Bécsi-erdő) – Helenental – Baden – Achau – Schwechat (Duna)", "lat": 48.075, "lon": 16.385, "fkm": 16.0,
        "thresholds": {"lkv": 15, "low": 42, "deg1": 190, "deg2": 240, "deg3": 290, "lnv": 355},
        "default_level": 66, "default_diff24h": 2, "default_discharge": 5.4, "default_temp": 7.4, "downstream_order": 1
    },
    {
        "code": "249108", "water_category": "minor", "country": "AT",
        "name": "Felsőőr (Oberwart)", "river": "Pinka", "basin": "duna", "catchment": "at_styria_mur_raab",
        "reach_name": "Felső-Pinka (Burgenland) – Pinggau – Pinkafeld – Felsőőr (Oberwart) – Burg", "lat": 47.288, "lon": 16.208, "fkm": 68.0,
        "thresholds": {"lkv": 10, "low": 35, "deg1": 210, "deg2": 260, "deg3": 310, "lnv": 380},
        "default_level": 58, "default_diff24h": 6, "default_discharge": 3.1, "default_temp": 6.9, "downstream_order": 1
    },
    {
        "code": "249109", "water_category": "minor", "country": "AT",
        "name": "Fürstenfeld", "river": "Lapincs", "basin": "duna", "catchment": "at_styria_mur_raab",
        "reach_name": "Lapincs (Lafnitz) – Rohrbach – Fürstenfeld – Rábakeresztúr (Heiligenkreuz) – Szentgotthárd", "lat": 47.055, "lon": 16.082, "fkm": 24.0,
        "thresholds": {"lkv": 20, "low": 55, "deg1": 240, "deg2": 300, "deg3": 360, "lnv": 440},
        "default_level": 88, "default_diff24h": 4, "default_discharge": 6.5, "default_temp": 7.0, "downstream_order": 1
    },
    {
        "code": "249110", "water_category": "minor", "country": "AT",
        "name": "Kapfenberg", "river": "Mürz", "basin": "drava", "catchment": "at_styria_mur_raab",
        "reach_name": "Mürz – Mürzzuschlag – Kindberg – Kapfenberg – Bruck an der Mur", "lat": 47.445, "lon": 15.292, "fkm": 6.5,
        "thresholds": {"lkv": 25, "low": 60, "deg1": 230, "deg2": 285, "deg3": 340, "lnv": 415},
        "default_level": 94, "default_diff24h": 1, "default_discharge": 14.8, "default_temp": 6.3, "downstream_order": 1
    },
    {
        "code": "249111", "water_category": "minor", "country": "AT",
        "name": "Wolfsberg", "river": "Lavant", "basin": "drava", "catchment": "at_carinthia_tyrol_drau",
        "reach_name": "Lavant – Bad St. Leonhard – Wolfsberg – St. Andrä – Lavamünd (Dráva)", "lat": 46.838, "lon": 14.842, "fkm": 28.0,
        "thresholds": {"lkv": 20, "low": 52, "deg1": 225, "deg2": 280, "deg3": 335, "lnv": 405},
        "default_level": 82, "default_diff24h": 2, "default_discharge": 9.8, "default_temp": 6.8, "downstream_order": 1
    },
    {
        "code": "249112", "water_category": "minor", "country": "AT",
        "name": "Hermagor (Nötsch)", "river": "Gail", "basin": "drava", "catchment": "at_carinthia_tyrol_drau",
        "reach_name": "Gail (Karnische Alpen) – Kötschach-Mauthen – Hermagor – Villach (Dráva)", "lat": 46.612, "lon": 13.515, "fkm": 32.0,
        "thresholds": {"lkv": 30, "low": 70, "deg1": 270, "deg2": 335, "deg3": 400, "lnv": 485},
        "default_level": 112, "default_diff24h": 3, "default_discharge": 24.5, "default_temp": 6.5, "downstream_order": 1
    },
    {
        "code": "249113", "water_category": "minor", "country": "AT",
        "name": "Winklern (Obervellach)", "river": "Möll", "basin": "drava", "catchment": "at_carinthia_tyrol_drau",
        "reach_name": "Möll (Hohe Tauern / Großglockner) – Heiligenblut – Winklern – Obervellach – Möllbrücke (Dráva)", "lat": 46.918, "lon": 13.115, "fkm": 38.0,
        "thresholds": {"lkv": 25, "low": 60, "deg1": 240, "deg2": 295, "deg3": 350, "lnv": 425},
        "default_level": 92, "default_diff24h": -1, "default_discharge": 15.4, "default_temp": 5.4, "downstream_order": 1
    },
    {
        "code": "249114", "water_category": "minor", "country": "AT",
        "name": "Feldkirch", "river": "Ill", "basin": "duna", "catchment": "at_carinthia_tyrol_drau",
        "reach_name": "Ill (Vorarlberg / Montafon) – Schruns – Bludenz – Feldkirch (Rajna)", "lat": 47.238, "lon": 9.598, "fkm": 8.0,
        "thresholds": {"lkv": 40, "low": 85, "deg1": 280, "deg2": 345, "deg3": 410, "lnv": 495},
        "default_level": 128, "default_diff24h": 2, "default_discharge": 32.0, "default_temp": 6.1, "downstream_order": 1
    },
    {
        "code": "249115", "water_category": "minor", "country": "AT",
        "name": "Kennelbach (Bregenz)", "river": "Bregenzer Ach", "basin": "duna", "catchment": "at_carinthia_tyrol_drau",
        "reach_name": "Bregenzer Ach (Bregenzerwald) – Egg – Kennelbach – Bregenz (Bodeni-tó)", "lat": 47.482, "lon": 9.768, "fkm": 5.5,
        "thresholds": {"lkv": 30, "low": 70, "deg1": 265, "deg2": 325, "deg3": 385, "lnv": 465},
        "default_level": 108, "default_diff24h": 3, "default_discharge": 26.5, "default_temp": 6.3, "downstream_order": 1
    },
]
