"""
Croatia (HR) — Catchments and Official Hydrological Gauging Stations (DHMZ hidro.dhz.hr / OVF hydroinfo.hu 54xxxx & GloFAS v4)
Standalone country source file (45 Croatian gauges: main rivers, karst lakes and Slavonian/karst smaller waters)
"""

COUNTRY_META = {
    "code": "HR",
    "name": "Horvátország",
    "flag": "🇭🇷",
    "border_color": "#a3e635",
    "bounds": [[42.38, 13.48], [46.56, 19.45]],
}

CATCHMENTS = {
    "hr_danube_drava_mura": {"name": "Dráva, Mura és Baranya-Szlavóniai Duna-szakasz (HR)", "lat": 45.65, "lon": 18.25, "response_factor": 2.8, "lag_days": 2},
    "hr_sava_posavina": {"name": "Száva-völgy, Zágrábi-medence és Szlavóniai-Posavina (HR)", "lat": 45.35, "lon": 16.95, "response_factor": 3.2, "lag_days": 2},
    "hr_kupa_una_karst": {"name": "Kulpa (Kupa), Korana, Dobra és Una vízgyűjtő (Károlyváros / Gorski kotar, HR)", "lat": 45.42, "lon": 15.55, "response_factor": 3.7, "lag_days": 1},
    "hr_adriatic_dalmatia": {"name": "Adriai-parti karsztfolyók és tavak (Isztria, Lika, Dalmácia: Krka, Cetina, Neretva, HR)", "lat": 43.75, "lon": 16.15, "response_factor": 3.5, "lag_days": 1},
}

STATIONS = [
    # =========================================================================
    # 1. MAIN RIVERS AND LARGE LAKES (27 stations — live DHMZ hidro.dhz.hr & hydroinfo.hu)
    # =========================================================================
    # --- DANUBE, MURA AND DRAVA (12 stations) ---
    {
        "code": "DHMZ_5170", "dhmz_id": "5170", "country": "HR", "name": "Kiskőszeg (Batina)", "river": "Duna", "basin": "duna", "catchment": "hr_danube_drava_mura",
        "reach_name": "Duna – Drávaszögi felső szakasz (Kiskőszeg / Batina)", "lat": 45.845, "lon": 18.852, "fkm": 1424.8,
        "thresholds": {"lkv": -110, "low": -35, "deg1": 500, "deg2": 650, "deg3": 750, "lnv": 865},
        "default_level": -60, "default_diff24h": -8, "default_discharge": 1120.0, "default_temp": 8.7, "downstream_order": 1
    },
    {
        "code": "542017", "dhmz_id": "5001", "country": "HR", "name": "Almás (Aljmaš)", "river": "Duna", "basin": "duna", "catchment": "hr_danube_drava_mura",
        "reach_name": "Duna – Dráva-torkolat – Almás (Aljmaš) – Erdőd", "lat": 45.532, "lon": 18.952, "fkm": 1380.2,
        "thresholds": {"lkv": -90, "low": -15, "deg1": 550, "deg2": 700, "deg3": 800, "lnv": 925},
        "default_level": -17, "default_diff24h": -10, "default_discharge": 1460.0, "default_temp": 8.9, "forecast_key": "duna almás", "downstream_order": 2
    },
    {
        "code": "DHMZ_5070", "dhmz_id": "5070", "country": "HR", "name": "Vukovár (Vukovar)", "river": "Duna", "basin": "duna", "catchment": "hr_danube_drava_mura",
        "reach_name": "Duna – Vukovár (Vukovar) – Vuka-torkolat", "lat": 45.355, "lon": 19.005, "fkm": 1333.1,
        "thresholds": {"lkv": -95, "low": -20, "deg1": 530, "deg2": 630, "deg3": 720, "lnv": 835},
        "default_level": -20, "default_diff24h": -8, "default_discharge": 1510.0, "default_temp": 9.0, "downstream_order": 3
    },
    {
        "code": "542030", "dhmz_id": "5024", "country": "HR", "name": "Újlak (Ilok)", "river": "Duna", "basin": "duna", "catchment": "hr_danube_drava_mura",
        "reach_name": "Duna – Újlak (Ilok) – Szerémségi határszakasz", "lat": 45.225, "lon": 19.375, "fkm": 1301.5,
        "thresholds": {"lkv": -85, "low": -10, "deg1": 520, "deg2": 620, "deg3": 710, "lnv": 825},
        "default_level": -2, "default_diff24h": -7, "default_discharge": 1540.0, "default_temp": 9.0, "downstream_order": 4
    },
    {
        "code": "DHMZ_5044", "dhmz_id": "5044", "country": "HR", "name": "Muraszerdahely", "river": "Mura", "basin": "drava", "catchment": "hr_danube_drava_mura",
        "reach_name": "Mura – Muraközi felső szakasz (Muraszerdahely / Mursko Središće)", "lat": 46.515, "lon": 16.438, "fkm": 79.0,
        "thresholds": {"lkv": 30, "low": 75, "deg1": 360, "deg2": 440, "deg3": 500, "lnv": 585},
        "default_level": 135, "default_diff24h": -3, "default_discharge": 105.0, "default_temp": 7.6, "downstream_order": 1
    },
    {
        "code": "DHMZ_5035", "dhmz_id": "5035", "country": "HR", "name": "Muracsány (Goričan)", "river": "Mura", "basin": "drava", "catchment": "hr_danube_drava_mura",
        "reach_name": "Mura – Muracsány (Goričan) – Kotoriba – Légrád torkolat", "lat": 46.412, "lon": 16.685, "fkm": 24.5,
        "thresholds": {"lkv": 5, "low": 45, "deg1": 350, "deg2": 430, "deg3": 490, "lnv": 565},
        "default_level": 85, "default_diff24h": -4, "default_discharge": 115.0, "default_temp": 7.8, "downstream_order": 2
    },
    {
        "code": "DHMZ_5066", "dhmz_id": "5066", "country": "HR", "name": "Varasd (Varaždin)", "river": "Dráva", "basin": "drava", "catchment": "hr_danube_drava_mura",
        "reach_name": "Dráva (Drava) – Varasdi-medence és víztározó-rendszer (Varaždin)", "lat": 46.325, "lon": 16.362, "fkm": 288.4,
        "thresholds": {"lkv": 60, "low": 115, "deg1": 320, "deg2": 390, "deg3": 450, "lnv": 545},
        "default_level": 165, "default_diff24h": 4, "default_discharge": 265.0, "default_temp": 8.2, "downstream_order": 1
    },
    {
        "code": "546060", "dhmz_id": "5008", "country": "HR", "name": "Botovo (Kapronca)", "river": "Dráva", "basin": "drava", "catchment": "hr_danube_drava_mura",
        "reach_name": "Dráva (Drava) – Mura-torkolat – Légrád – Botovo (Kapronca)", "lat": 46.242, "lon": 16.938, "fkm": 226.8,
        "thresholds": {"lkv": -110, "low": -35, "deg1": 400, "deg2": 500, "deg3": 570, "lnv": 675},
        "default_level": -4, "default_diff24h": 6, "default_discharge": 385.0, "default_temp": 8.4, "downstream_order": 2
    },
    {
        "code": "546070", "dhmz_id": "5063", "country": "HR", "name": "Trézenföld (Terezino Polje)", "river": "Dráva", "basin": "drava", "catchment": "hr_danube_drava_mura",
        "reach_name": "Dráva (Drava) – Verőce / Trézenföld (Terezino Polje) – Barcs", "lat": 45.942, "lon": 17.462, "fkm": 152.3,
        "thresholds": {"lkv": -450, "low": -395, "deg1": 150, "deg2": 230, "deg3": 300, "lnv": 385},
        "default_level": -378, "default_diff24h": 2, "default_discharge": 410.0, "default_temp": 8.6, "downstream_order": 3
    },
    {
        "code": "DHMZ_5150", "dhmz_id": "5150", "country": "HR", "name": "Alsómiholjác (Donji Miholjac)", "river": "Dráva", "basin": "drava", "catchment": "hr_danube_drava_mura",
        "reach_name": "Dráva (Drava) – Alsómiholjác (Donji Miholjac) – Drávaszabolcs", "lat": 45.778, "lon": 18.185, "fkm": 77.7,
        "thresholds": {"lkv": -210, "low": -150, "deg1": 350, "deg2": 430, "deg3": 500, "lnv": 595},
        "default_level": -136, "default_diff24h": 0, "default_discharge": 435.0, "default_temp": 8.8, "downstream_order": 4
    },
    {
        "code": "DHMZ_5005", "dhmz_id": "5005", "country": "HR", "name": "Belistye (Belišće)", "river": "Dráva", "basin": "drava", "catchment": "hr_danube_drava_mura",
        "reach_name": "Dráva (Drava) – Belistye (Belišće) – Valpó", "lat": 45.692, "lon": 18.415, "fkm": 46.2,
        "thresholds": {"lkv": -70, "low": -15, "deg1": 380, "deg2": 460, "deg3": 530, "lnv": 635},
        "default_level": 7, "default_diff24h": -2, "default_discharge": 445.0, "default_temp": 8.9, "downstream_order": 5
    },
    {
        "code": "546090", "dhmz_id": "5053", "country": "HR", "name": "Eszék (Osijek)", "river": "Dráva", "basin": "drava", "catchment": "hr_danube_drava_mura",
        "reach_name": "Dráva (Drava) – Eszék (Osijek) – Kopácsi-rét – Duna-torkolat", "lat": 45.562, "lon": 18.685, "fkm": 19.8,
        "thresholds": {"lkv": -240, "low": -185, "deg1": 350, "deg2": 450, "deg3": 500, "lnv": 615},
        "default_level": -175, "default_diff24h": -5, "default_discharge": 455.0, "default_temp": 9.0, "downstream_order": 6
    },

    # --- SAVA, KUPA, UNA AND ADRIATIC MAIN RIVERS (12 stations) ---
    {
        "code": "DHMZ_3121", "dhmz_id": "3121", "country": "HR", "name": "Zágráb (Zagreb)", "river": "Száva", "basin": "duna", "catchment": "hr_sava_posavina",
        "reach_name": "Száva (Sava) – Zágrábi fővárosi szakasz (Podsused – Zagreb – Rugvica)", "lat": 45.785, "lon": 15.965, "fkm": 700.0,
        "thresholds": {"lkv": -280, "low": -160, "deg1": 350, "deg2": 450, "deg3": 550, "lnv": 665},
        "default_level": -64, "default_diff24h": 14, "default_discharge": 265.0, "default_temp": 8.9, "downstream_order": 1
    },
    {
        "code": "DHMZ_3020", "dhmz_id": "3020", "country": "HR", "name": "Sziszek (Crnac / Sisak)", "river": "Száva", "basin": "duna", "catchment": "hr_sava_posavina",
        "reach_name": "Száva (Sava) – Sziszek (Sisak / Crnac) – Kulpa-torkolat – Lonja-mező", "lat": 45.442, "lon": 16.418, "fkm": 596.0,
        "thresholds": {"lkv": -80, "low": 60, "deg1": 550, "deg2": 670, "deg3": 760, "lnv": 845},
        "default_level": 314, "default_diff24h": 18, "default_discharge": 495.0, "default_temp": 9.3, "downstream_order": 2
    },
    {
        "code": "DHMZ_3219", "dhmz_id": "3219", "country": "HR", "name": "Jasenovac", "river": "Száva", "basin": "duna", "catchment": "hr_sava_posavina",
        "reach_name": "Száva (Sava) – Jasenovac – Una- és Lonja-torkolat", "lat": 45.265, "lon": 16.912, "fkm": 514.2,
        "thresholds": {"lkv": -40, "low": 120, "deg1": 650, "deg2": 800, "deg3": 870, "lnv": 935},
        "default_level": 451, "default_diff24h": 22, "default_discharge": 740.0, "default_temp": 9.5, "downstream_order": 3
    },
    {
        "code": "DHMZ_3104", "dhmz_id": "3104", "country": "HR", "name": "Ógradiska (Stara Gradiška)", "river": "Száva", "basin": "duna", "catchment": "hr_sava_posavina",
        "reach_name": "Száva (Sava) – Ógradiska (Stara Gradiška) – Davor", "lat": 45.148, "lon": 17.245, "fkm": 465.0,
        "thresholds": {"lkv": -60, "low": 90, "deg1": 630, "deg2": 750, "deg3": 830, "lnv": 905},
        "default_level": 363, "default_diff24h": 19, "default_discharge": 885.0, "default_temp": 9.6, "downstream_order": 4
    },
    {
        "code": "DHMZ_3098", "dhmz_id": "3098", "country": "HR", "name": "Bród (Slavonski Brod)", "river": "Száva", "basin": "duna", "catchment": "hr_sava_posavina",
        "reach_name": "Száva (Sava) – Bród (Slavonski Brod) – Slavonski Šamac", "lat": 45.152, "lon": 18.012, "fkm": 375.5,
        "thresholds": {"lkv": -80, "low": 75, "deg1": 650, "deg2": 780, "deg3": 860, "lnv": 945},
        "default_level": 330, "default_diff24h": 16, "default_discharge": 1020.0, "default_temp": 9.8, "downstream_order": 5
    },
    {
        "code": "DHMZ_3211", "dhmz_id": "3211", "country": "HR", "name": "Zsupanya (Županja)", "river": "Száva", "basin": "duna", "catchment": "hr_sava_posavina",
        "reach_name": "Száva (Sava) – Zsupanya (Županja) – Gunja kelet-szlavóniai szakasz", "lat": 45.068, "lon": 18.688, "fkm": 262.0,
        "thresholds": {"lkv": -60, "low": 95, "deg1": 750, "deg2": 880, "deg3": 980, "lnv": 1110},
        "default_level": 369, "default_diff24h": 18, "default_discharge": 1240.0, "default_temp": 10.0, "downstream_order": 6
    },
    {
        "code": "DHMZ_4111", "dhmz_id": "4111", "country": "HR", "name": "Károlyváros (Karlovac)", "river": "Kulpa", "basin": "duna", "catchment": "hr_kupa_una_karst",
        "reach_name": "Kulpa (Kupa) – Károlyváros (Karlovac) – Korana- és Dobra-torkolat", "lat": 45.495, "lon": 15.555, "fkm": 130.5,
        "thresholds": {"lkv": -40, "low": 60, "deg1": 600, "deg2": 750, "deg3": 830, "lnv": 895},
        "default_level": 415, "default_diff24h": 28, "default_discharge": 185.0, "default_temp": 9.4, "downstream_order": 1
    },
    {
        "code": "DHMZ_4010", "dhmz_id": "4010", "country": "HR", "name": "Farkašić (Petrinja)", "river": "Kulpa", "basin": "duna", "catchment": "hr_kupa_una_karst",
        "reach_name": "Kulpa (Kupa) – Farkašić – Petrinja – Sziszeki torkolat", "lat": 45.475, "lon": 16.152, "fkm": 37.5,
        "thresholds": {"lkv": 80, "low": 180, "deg1": 720, "deg2": 860, "deg3": 940, "lnv": 1015},
        "default_level": 579, "default_diff24h": 24, "default_discharge": 235.0, "default_temp": 9.5, "downstream_order": 2
    },
    {
        "code": "DHMZ_3217", "dhmz_id": "3217", "country": "HR", "name": "Kosztajnica (Kostajnica)", "river": "Una", "basin": "duna", "catchment": "hr_kupa_una_karst",
        "reach_name": "Una – Kosztajnica (Hrvatska Kostajnica) – Hrvatska Dubica – Jasenovac", "lat": 45.225, "lon": 16.542, "fkm": 34.0,
        "thresholds": {"lkv": 20, "low": 70, "deg1": 340, "deg2": 400, "deg3": 450, "lnv": 535},
        "default_level": 168, "default_diff24h": 9, "default_discharge": 165.0, "default_temp": 9.6, "downstream_order": 1
    },
    {
        "code": "DHMZ_7095", "dhmz_id": "7095", "country": "HR", "name": "Skradinski buk (Krka)", "river": "Krka", "basin": "drava", "catchment": "hr_adriatic_dalmatia",
        "reach_name": "Krka – Knin – Roški slap – Skradinski buk (Krka Nemzeti Park)", "lat": 43.805, "lon": 15.965, "fkm": 16.0,
        "thresholds": {"lkv": 20, "low": 55, "deg1": 210, "deg2": 260, "deg3": 310, "lnv": 385},
        "default_level": 90, "default_diff24h": 4, "default_discharge": 54.0, "default_temp": 13.4, "downstream_order": 1
    },
    {
        "code": "DHMZ_7232", "dhmz_id": "7232", "country": "HR", "name": "Omiš / Tisne Stine (Cetina)", "river": "Cetina", "basin": "drava", "catchment": "hr_adriatic_dalmatia",
        "reach_name": "Cetina – Sinj – Trilj – Tisne Stine – Omiši-szurdok", "lat": 43.445, "lon": 16.725, "fkm": 14.0,
        "thresholds": {"lkv": 35, "low": 75, "deg1": 260, "deg2": 320, "deg3": 380, "lnv": 455},
        "default_level": 117, "default_diff24h": 5, "default_discharge": 82.0, "default_temp": 11.8, "downstream_order": 1
    },
    {
        "code": "DHMZ_7052", "dhmz_id": "7052", "country": "HR", "name": "Metković", "river": "Neretva", "basin": "drava", "catchment": "hr_adriatic_dalmatia",
        "reach_name": "Neretva – Metković – Opuzen – Neretva-delta", "lat": 43.055, "lon": 17.648, "fkm": 20.5,
        "thresholds": {"lkv": 40, "low": 95, "deg1": 300, "deg2": 360, "deg3": 400, "lnv": 465},
        "default_level": 174, "default_diff24h": 6, "default_discharge": 285.0, "default_temp": 10.8, "downstream_order": 1
    },

    # --- CROATIAN LARGE LAKES (3 stations) ---
    {
        "code": "DHMZ_4109", "dhmz_id": "4109", "country": "HR", "name": "Plitvicei-tavak (Kozjak-tó)", "river": "Plitvicei-tavak (Kozjak-tó)", "basin": "tavak", "catchment": "hr_kupa_una_karst",
        "reach_name": "Plitvicei-tavak – Kozjak-tó és Prošćansko-tó (Plitvička jezera)", "lat": 44.882, "lon": 15.608, "fkm": 0.0,
        "thresholds": {"lkv": 75, "low": 100, "deg1": 185, "deg2": 215, "deg3": 245, "lnv": 280},
        "default_level": 125, "default_diff24h": 1, "default_discharge": 4.2, "default_temp": 10.5, "downstream_order": 1
    },
    {
        "code": "DHMZ_7078", "dhmz_id": "7078", "country": "HR", "name": "Vranai-tó (Prosika / Pakoštane)", "river": "Vranai-tó (Vransko jezero)", "basin": "tavak", "catchment": "hr_adriatic_dalmatia",
        "reach_name": "Vranai-tó (Vransko jezero – Pakoštane / Biograd na Moru)", "lat": 43.895, "lon": 15.582, "fkm": 0.0,
        "thresholds": {"lkv": 25, "low": 45, "deg1": 140, "deg2": 175, "deg3": 210, "lnv": 245},
        "default_level": 64, "default_diff24h": 0, "default_discharge": 1.8, "default_temp": 13.8, "downstream_order": 1
    },
    {
        "code": "DHMZ_7136", "dhmz_id": "7136", "country": "HR", "name": "Baćinai-tavak (Ploče)", "river": "Baćinai-tavak (Baćinska jezera)", "basin": "tavak", "catchment": "hr_adriatic_dalmatia",
        "reach_name": "Baćinai-tavak (Baćinska jezera – Šipak / Ploče)", "lat": 43.078, "lon": 17.422, "fkm": 0.0,
        "thresholds": {"lkv": 140, "low": 185, "deg1": 340, "deg2": 390, "deg3": 440, "lnv": 495},
        "default_level": 249, "default_diff24h": 2, "default_discharge": 2.4, "default_temp": 13.2, "downstream_order": 1
    },

    # =========================================================================
    # 2. SMALLER WATERS, STREAMS AND TRIBUTARIES (18 stations — live DHMZ hidro.dhz.hr)
    # =========================================================================
    {
        "code": "DHMZ_5089", "dhmz_id": "5089", "country": "HR", "water_category": "minor", "name": "Ludbreg", "river": "Bednja", "basin": "drava", "catchment": "hr_danube_drava_mura",
        "reach_name": "Bednja – Lepoglava – Tuhovec – Ludbreg (Dráva-mellékvíz)", "lat": 46.255, "lon": 16.615, "fkm": 18.5,
        "thresholds": {"lkv": -45, "low": -15, "deg1": 240, "deg2": 300, "deg3": 350, "lnv": 420},
        "default_level": -6, "default_diff24h": -2, "default_discharge": 6.4, "default_temp": 8.1, "downstream_order": 1
    },
    {
        "code": "DHMZ_5179", "dhmz_id": "5179", "country": "HR", "water_category": "minor", "name": "Krkanec (Varasd)", "river": "Plitvica-patak", "basin": "drava", "catchment": "hr_danube_drava_mura",
        "reach_name": "Plitvica-patak – Krkanec – Vidovićev Mlin (Varasdi-síkság)", "lat": 46.262, "lon": 16.295, "fkm": 22.0,
        "thresholds": {"lkv": 5, "low": 22, "deg1": 180, "deg2": 230, "deg3": 270, "lnv": 330},
        "default_level": 38, "default_diff24h": 1, "default_discharge": 2.8, "default_temp": 8.0, "downstream_order": 1
    },
    {
        "code": "DHMZ_3054", "dhmz_id": "3054", "country": "HR", "water_category": "minor", "name": "Kupljenovo (Zaprešić)", "river": "Krapina", "basin": "duna", "catchment": "hr_sava_posavina",
        "reach_name": "Krapina – Zlatar Bistrica – Zabok – Kupljenovo (Zagorje)", "lat": 45.915, "lon": 15.815, "fkm": 14.0,
        "thresholds": {"lkv": 15, "low": 40, "deg1": 310, "deg2": 380, "deg3": 440, "lnv": 525},
        "default_level": 69, "default_diff24h": -3, "default_discharge": 11.5, "default_temp": 8.2, "downstream_order": 1
    },
    {
        "code": "DHMZ_3127", "dhmz_id": "3127", "country": "HR", "water_category": "minor", "name": "Zelenjak (Klanjec)", "river": "Sutla", "basin": "duna", "catchment": "hr_sava_posavina",
        "reach_name": "Sutla – Zelenjak – Klanjec (Horvát–szlovén határfolyó)", "lat": 46.038, "lon": 15.728, "fkm": 28.0,
        "thresholds": {"lkv": 25, "low": 55, "deg1": 280, "deg2": 350, "deg3": 410, "lnv": 485},
        "default_level": 78, "default_diff24h": -2, "default_discharge": 7.2, "default_temp": 8.1, "downstream_order": 1
    },
    {
        "code": "DHMZ_3062", "dhmz_id": "3062", "country": "HR", "water_category": "minor", "name": "Lonjica (Vrbovec)", "river": "Lonja", "basin": "duna", "catchment": "hr_sava_posavina",
        "reach_name": "Lonja – Lonjica – Ivanić-Grad – Lonjsko polje", "lat": 45.845, "lon": 16.365, "fkm": 46.0,
        "thresholds": {"lkv": -10, "low": 18, "deg1": 240, "deg2": 300, "deg3": 360, "lnv": 430},
        "default_level": 39, "default_diff24h": 0, "default_discharge": 5.8, "default_temp": 8.7, "downstream_order": 1
    },
    {
        "code": "DHMZ_3072", "dhmz_id": "3072", "country": "HR", "water_category": "minor", "name": "Narta (Belovár)", "river": "Česma", "basin": "duna", "catchment": "hr_sava_posavina",
        "reach_name": "Česma – Pavlovac – Narta – Csázma (Čazma)", "lat": 45.825, "lon": 16.752, "fkm": 48.0,
        "thresholds": {"lkv": 60, "low": 115, "deg1": 360, "deg2": 430, "deg3": 490, "lnv": 575},
        "default_level": 191, "default_diff24h": 3, "default_discharge": 9.4, "default_temp": 8.8, "downstream_order": 1
    },
    {
        "code": "DHMZ_3115", "dhmz_id": "3115", "country": "HR", "water_category": "minor", "name": "Veliko Vukovje (Garešnica)", "river": "Ilova", "basin": "duna", "catchment": "hr_sava_posavina",
        "reach_name": "Ilova – Maslenjača – Garešnica – Veliko Vukovje", "lat": 45.542, "lon": 16.925, "fkm": 32.0,
        "thresholds": {"lkv": 30, "low": 75, "deg1": 290, "deg2": 350, "deg3": 410, "lnv": 485},
        "default_level": 135, "default_diff24h": 2, "default_discharge": 6.8, "default_temp": 8.9, "downstream_order": 1
    },
    {
        "code": "DHMZ_3393", "dhmz_id": "3393", "country": "HR", "water_category": "minor", "name": "Janja Lipa (Pakrác)", "river": "Pakra", "basin": "duna", "catchment": "hr_sava_posavina",
        "reach_name": "Pakra – Pakrác – Lipik – Janja Lipa", "lat": 45.455, "lon": 16.968, "fkm": 19.0,
        "thresholds": {"lkv": -10, "low": 20, "deg1": 250, "deg2": 310, "deg3": 370, "lnv": 445},
        "default_level": 51, "default_diff24h": -1, "default_discharge": 4.2, "default_temp": 9.0, "downstream_order": 1
    },
    {
        "code": "DHMZ_3397", "dhmz_id": "3397", "country": "HR", "water_category": "minor", "name": "Frkljevci (Pozsega)", "river": "Orljava", "basin": "duna", "catchment": "hr_sava_posavina",
        "reach_name": "Orljava – Pozsega (Požega) – Pleternica – Frkljevci", "lat": 45.265, "lon": 17.812, "fkm": 24.0,
        "thresholds": {"lkv": -5, "low": 22, "deg1": 260, "deg2": 320, "deg3": 380, "lnv": 455},
        "default_level": 52, "default_diff24h": 1, "default_discharge": 6.1, "default_temp": 9.1, "downstream_order": 1
    },
    {
        "code": "DHMZ_3346", "dhmz_id": "3346", "country": "HR", "water_category": "minor", "name": "Vinkovce (Vinkovci)", "river": "Bosut", "basin": "duna", "catchment": "hr_sava_posavina",
        "reach_name": "Bosut – Cerna (Biđ) – Vinkovce (Vinkovci) – Nijemci", "lat": 45.288, "lon": 18.805, "fkm": 68.0,
        "thresholds": {"lkv": 15, "low": 42, "deg1": 240, "deg2": 300, "deg3": 360, "lnv": 430},
        "default_level": 67, "default_diff24h": 0, "default_discharge": 7.5, "default_temp": 9.4, "downstream_order": 1
    },
    {
        "code": "DHMZ_5169", "dhmz_id": "5169", "country": "HR", "water_category": "minor", "name": "Beketinci (Eszék–Vukovár)", "river": "Vuka", "basin": "duna", "catchment": "hr_danube_drava_mura",
        "reach_name": "Vuka – Bračevci – Beketinci – Vukovár", "lat": 45.442, "lon": 18.495, "fkm": 42.0,
        "thresholds": {"lkv": -10, "low": 15, "deg1": 210, "deg2": 260, "deg3": 310, "lnv": 385},
        "default_level": 36, "default_diff24h": 0, "default_discharge": 3.2, "default_temp": 9.1, "downstream_order": 1
    },
    {
        "code": "DHMZ_4026", "dhmz_id": "4026", "country": "HR", "water_category": "minor", "name": "Károlyváros (Karlovac-Korana)", "river": "Korana", "basin": "duna", "catchment": "hr_kupa_una_karst",
        "reach_name": "Korana – Szluin (Slunj) – Veljun – Károlyváros (Karlovac)", "lat": 45.475, "lon": 15.568, "fkm": 3.5,
        "thresholds": {"lkv": 80, "low": 165, "deg1": 620, "deg2": 730, "deg3": 780, "lnv": 855},
        "default_level": 393, "default_diff24h": 18, "default_discharge": 62.0, "default_temp": 9.9, "downstream_order": 1
    },
    {
        "code": "DHMZ_4042", "dhmz_id": "4042", "country": "HR", "water_category": "minor", "name": "Duga Resa (Mrzlo Polje)", "river": "Mrežnica", "basin": "duna", "catchment": "hr_kupa_una_karst",
        "reach_name": "Mrežnica – Juzbašići – Duga Resa (Mrzlo Polje)", "lat": 45.458, "lon": 15.512, "fkm": 6.5,
        "thresholds": {"lkv": 35, "low": 75, "deg1": 310, "deg2": 370, "deg3": 420, "lnv": 495},
        "default_level": 157, "default_diff24h": 7, "default_discharge": 34.0, "default_temp": 9.6, "downstream_order": 1
    },
    {
        "code": "DHMZ_4061", "dhmz_id": "4061", "country": "HR", "water_category": "minor", "name": "Stative Donje (Ogulin)", "river": "Dobra", "basin": "duna", "catchment": "hr_kupa_una_karst",
        "reach_name": "Dobra – Ogulin – Lešće – Stative Donje", "lat": 45.518, "lon": 15.465, "fkm": 11.0,
        "thresholds": {"lkv": 55, "low": 105, "deg1": 340, "deg2": 400, "deg3": 460, "lnv": 535},
        "default_level": 206, "default_diff24h": 8, "default_discharge": 29.0, "default_temp": 9.3, "downstream_order": 1
    },
    {
        "code": "DHMZ_4013", "dhmz_id": "4013", "country": "HR", "water_category": "minor", "name": "Glina", "river": "Glina", "basin": "duna", "catchment": "hr_kupa_una_karst",
        "reach_name": "Glina – Široka Rijeka – Vranovina – Glina", "lat": 45.338, "lon": 16.088, "fkm": 24.0,
        "thresholds": {"lkv": 40, "low": 95, "deg1": 420, "deg2": 500, "deg3": 560, "lnv": 635},
        "default_level": 235, "default_diff24h": 11, "default_discharge": 18.5, "default_temp": 9.4, "downstream_order": 1
    },
    {
        "code": "DHMZ_6026", "dhmz_id": "6026", "country": "HR", "water_category": "minor", "name": "Motovun (Portonski most)", "river": "Mirna", "basin": "drava", "catchment": "hr_adriatic_dalmatia",
        "reach_name": "Mirna – Buzet – Motovun (Portonski most) – Novigrad (Isztria)", "lat": 45.352, "lon": 13.738, "fkm": 14.5,
        "thresholds": {"lkv": 40, "low": 85, "deg1": 380, "deg2": 460, "deg3": 520, "lnv": 610},
        "default_level": 179, "default_diff24h": 4, "default_discharge": 14.2, "default_temp": 14.5, "downstream_order": 1
    },
    {
        "code": "DHMZ_8016", "dhmz_id": "8016", "country": "HR", "water_category": "minor", "name": "Čovići (Otočac)", "river": "Gacka", "basin": "drava", "catchment": "hr_adriatic_dalmatia",
        "reach_name": "Gacka – Izvor Gacke – Otočac – Čovići (Lika-medence)", "lat": 44.845, "lon": 15.292, "fkm": 16.0,
        "thresholds": {"lkv": 80, "low": 125, "deg1": 280, "deg2": 330, "deg3": 380, "lnv": 440},
        "default_level": 187, "default_diff24h": 2, "default_discharge": 12.8, "default_temp": 9.8, "downstream_order": 1
    },
    {
        "code": "DHMZ_7219", "dhmz_id": "7219", "country": "HR", "water_category": "minor", "name": "Obrovac", "river": "Zrmanja", "basin": "drava", "catchment": "hr_adriatic_dalmatia",
        "reach_name": "Zrmanja – Mokro Polje – Žegar – Obrovac (Velebit-karszt)", "lat": 44.202, "lon": 15.682, "fkm": 11.5,
        "thresholds": {"lkv": 45, "low": 90, "deg1": 270, "deg2": 320, "deg3": 370, "lnv": 435},
        "default_level": 181, "default_diff24h": 6, "default_discharge": 36.0, "default_temp": 9.8, "downstream_order": 1
    },
]
