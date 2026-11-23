"""
Serbia (RS) — Catchments and Official Hydrological Gauging Stations (RHMZ hidmet.gov.rs / OVF hydroinfo.hu 54xxxx & GloFAS v4)
Standalone country source file (46 Serbian gauges: main rivers, reservoirs/lakes and Vojvodina/Central Serbian smaller waters and canals)
"""

COUNTRY_META = {
    "code": "RS",
    "name": "Szerbia",
    "flag": "🇷🇸",
    "border_color": "#818cf8",
    "bounds": [[42.23, 18.81], [46.19, 23.01]],
}

CATCHMENTS = {
    "rs_vojvodina_danube_tisa": {"name": "Vajdaság: Bácskai és Bánáti Duna-, Tisza- és DTD-vízrendszer (RS)", "lat": 45.45, "lon": 19.95, "response_factor": 2.5, "lag_days": 3},
    "rs_sava_drina_kolubara": {"name": "Száva, Drina, Lim és Kolubara vízgyűjtő (Nyugat-Szerbia és Szerémség, RS)", "lat": 44.55, "lon": 19.65, "response_factor": 3.4, "lag_days": 2},
    "rs_velika_zapadna_morava": {"name": "Nagy-Morava (Velika Morava), Nyugati-Morava és Ibar vízgyűjtő (Közép-Szerbia, RS)", "lat": 43.82, "lon": 20.95, "response_factor": 3.3, "lag_days": 2},
    "rs_juzna_morava_timok": {"name": "Déli-Morava (Južna Morava), Nišava és Timok vízgyűjtő (Dél- és Kelet-Szerbia, RS)", "lat": 43.32, "lon": 21.95, "response_factor": 3.6, "lag_days": 1},
}

STATIONS = [
    # =========================================================================
    # 1. MAIN RIVERS AND LARGE LAKES (31 stations — live RHMZ hidmet.gov.rs & hydroinfo.hu)
    # =========================================================================
    # --- DANUBE AND TISZA (15 stations) ---
    {
        "code": "542010", "rhmz_id": "42010", "country": "RS", "name": "Bezdán (Bezdan)", "river": "Duna", "basin": "duna", "catchment": "rs_vojvodina_danube_tisa",
        "reach_name": "Duna – Bácskai felső szakasz (Bezdán / Bezdan – Ferenc-csatorna zsilip)", "lat": 45.855, "lon": 18.865, "fkm": 1425.5,
        "thresholds": {"lkv": -130, "low": -50, "deg1": 500, "deg2": 700, "deg3": 750, "lnv": 864},
        "default_level": -69, "default_diff24h": -13, "default_discharge": 1100.0, "default_temp": 8.7, "downstream_order": 1
    },
    {
        "code": "RHMZ_42015", "rhmz_id": "42015", "country": "RS", "name": "Apatin", "river": "Duna", "basin": "duna", "catchment": "rs_vojvodina_danube_tisa",
        "reach_name": "Duna – Apatin – Felső-Duna-mente rezervátum", "lat": 45.672, "lon": 18.978, "fkm": 1401.4,
        "thresholds": {"lkv": -90, "low": -15, "deg1": 600, "deg2": 750, "deg3": 800, "lnv": 918},
        "default_level": -6, "default_diff24h": -14, "default_discharge": 1180.0, "default_temp": 9.0, "downstream_order": 2
    },
    {
        "code": "RHMZ_42020", "rhmz_id": "42020", "country": "RS", "name": "Gombos (Bogojevo)", "river": "Duna", "basin": "duna", "catchment": "rs_vojvodina_danube_tisa",
        "reach_name": "Duna – Gombos (Bogojevo) – Dráva-torkolat alatti szakasz", "lat": 45.528, "lon": 19.082, "fkm": 1367.4,
        "thresholds": {"lkv": -95, "low": -20, "deg1": 600, "deg2": 700, "deg3": 780, "lnv": 885},
        "default_level": -15, "default_diff24h": -7, "default_discharge": 1290.0, "default_temp": 9.0, "downstream_order": 3
    },
    {
        "code": "RHMZ_42030", "rhmz_id": "42030", "country": "RS", "name": "Palánka (Bačka Palanka)", "river": "Duna", "basin": "duna", "catchment": "rs_vojvodina_danube_tisa",
        "reach_name": "Duna – Palánka (Bačka Palanka) – Futak", "lat": 45.242, "lon": 19.392, "fkm": 1298.6,
        "thresholds": {"lkv": -75, "low": -5, "deg1": 530, "deg2": 650, "deg3": 720, "lnv": 825},
        "default_level": 5, "default_diff24h": -9, "default_discharge": 1340.0, "default_temp": 9.0, "downstream_order": 4
    },
    {
        "code": "RHMZ_42035", "rhmz_id": "42035", "country": "RS", "name": "Újvidék (Novi Sad)", "river": "Duna", "basin": "duna", "catchment": "rs_vojvodina_danube_tisa",
        "reach_name": "Duna – Újvidék (Novi Sad) – Pétervárad – Karlóca", "lat": 45.252, "lon": 19.855, "fkm": 1255.1,
        "thresholds": {"lkv": -60, "low": 15, "deg1": 450, "deg2": 700, "deg3": 750, "lnv": 845},
        "default_level": 30, "default_diff24h": -1, "default_discharge": 1390.0, "default_temp": 9.2, "downstream_order": 5
    },
    {
        "code": "RHMZ_42040", "rhmz_id": "42040", "country": "RS", "name": "Szalánkemén (Slankamen)", "river": "Duna", "basin": "duna", "catchment": "rs_vojvodina_danube_tisa",
        "reach_name": "Duna – Szalánkemén (Slankamen) – Tisza-torkolat", "lat": 45.142, "lon": 20.258, "fkm": 1215.5,
        "thresholds": {"lkv": 30, "low": 95, "deg1": 500, "deg2": 650, "deg3": 730, "lnv": 830},
        "default_level": 140, "default_diff24h": 6, "default_discharge": 1850.0, "default_temp": 9.3, "downstream_order": 6
    },
    {
        "code": "542045", "rhmz_id": "42045", "country": "RS", "name": "Zimony / Belgrád (Zemun)", "river": "Duna", "basin": "duna", "catchment": "rs_sava_drina_kolubara",
        "reach_name": "Duna – Zimony (Zemun) – Belgrád – Száva-torkolat", "lat": 44.845, "lon": 20.415, "fkm": 1173.0,
        "thresholds": {"lkv": 110, "low": 185, "deg1": 550, "deg2": 650, "deg3": 730, "lnv": 845},
        "default_level": 250, "default_diff24h": 11, "default_discharge": 3350.0, "default_temp": 10.2, "downstream_order": 7
    },
    {
        "code": "RHMZ_42050", "rhmz_id": "42050", "country": "RS", "name": "Pancsova (Pančevo)", "river": "Duna", "basin": "duna", "catchment": "rs_vojvodina_danube_tisa",
        "reach_name": "Duna – Pancsova (Pančevo) – Temes-torkolat", "lat": 44.858, "lon": 20.635, "fkm": 1154.6,
        "thresholds": {"lkv": 140, "low": 210, "deg1": 530, "deg2": 650, "deg3": 720, "lnv": 835},
        "default_level": 282, "default_diff24h": 10, "default_discharge": 3450.0, "default_temp": 10.1, "downstream_order": 8
    },
    {
        "code": "RHMZ_42055", "rhmz_id": "42055", "country": "RS", "name": "Szendrő (Smederevo)", "river": "Duna", "basin": "duna", "catchment": "rs_velika_zapadna_morava",
        "reach_name": "Duna – Szendrő (Smederevo) – Nagy-Morava torkolat", "lat": 44.668, "lon": 20.925, "fkm": 1116.2,
        "thresholds": {"lkv": 310, "low": 385, "deg1": 600, "deg2": 700, "deg3": 780, "lnv": 885},
        "default_level": 460, "default_diff24h": 6, "default_discharge": 3650.0, "default_temp": 10.1, "downstream_order": 9
    },
    {
        "code": "RHMZ_42065", "rhmz_id": "42065", "country": "RS", "name": "Veliko Gradište", "river": "Duna", "basin": "duna", "catchment": "rs_velika_zapadna_morava",
        "reach_name": "Duna – Bánáti-Palánka – Néra- és Karas-torkolat – Veliko Gradište", "lat": 44.768, "lon": 21.518, "fkm": 1059.2,
        "thresholds": {"lkv": 580, "low": 660, "deg1": 800, "deg2": 850, "deg3": 900, "lnv": 965},
        "default_level": 752, "default_diff24h": 2, "default_discharge": 3810.0, "default_temp": 10.0, "downstream_order": 10
    },
    {
        "code": "RHMZ_42095", "rhmz_id": "42095", "country": "RS", "name": "Prahovo (Vaskapu II.)", "river": "Duna", "basin": "duna", "catchment": "rs_juzna_morava_timok",
        "reach_name": "Duna – Kladovo – Vaskapu II. (Đerdap II.) – Prahovo – Timok-torkolat", "lat": 44.295, "lon": 22.585, "fkm": 861.0,
        "thresholds": {"lkv": -40, "low": 25, "deg1": 350, "deg2": 450, "deg3": 550, "lnv": 665},
        "default_level": 97, "default_diff24h": 39, "default_discharge": 3950.0, "default_temp": 10.2, "downstream_order": 11
    },
    {
        "code": "RHMZ_44010", "rhmz_id": "44010", "country": "RS", "name": "Törökkanizsa (Novi Kneževac)", "river": "Tisza", "basin": "tisza", "catchment": "rs_vojvodina_danube_tisa",
        "reach_name": "Tisza (Tisa) – Magyarkanizsa – Törökkanizsa (Novi Kneževac)", "lat": 46.048, "lon": 20.088, "fkm": 140.2,
        "thresholds": {"lkv": 40, "low": 105, "deg1": 500, "deg2": 650, "deg3": 750, "lnv": 895},
        "default_level": 194, "default_diff24h": 8, "default_discharge": 425.0, "default_temp": 8.9, "downstream_order": 1
    },
    {
        "code": "544020", "rhmz_id": "44020", "country": "RS", "name": "Zenta (Senta)", "river": "Tisza", "basin": "tisza", "catchment": "rs_vojvodina_danube_tisa",
        "reach_name": "Tisza (Tisa) – Zenta (Senta) – Ada – Mohol", "lat": 45.932, "lon": 20.095, "fkm": 122.0,
        "thresholds": {"lkv": 90, "low": 160, "deg1": 550, "deg2": 700, "deg3": 780, "lnv": 927},
        "default_level": 256, "default_diff24h": 8, "default_discharge": 445.0, "default_temp": 9.8, "downstream_order": 2
    },
    {
        "code": "544035", "rhmz_id": "44035", "country": "RS", "name": "Törökbecse (Novi Bečej)", "river": "Tisza", "basin": "tisza", "catchment": "rs_vojvodina_danube_tisa",
        "reach_name": "Tisza (Tisa) – Óbecse – Törökbecsei duzzasztó (Novi Bečej)", "lat": 45.595, "lon": 20.125, "fkm": 66.2,
        "thresholds": {"lkv": 250, "low": 325, "deg1": 600, "deg2": 700, "deg3": 780, "lnv": 885},
        "default_level": 411, "default_diff24h": 5, "default_discharge": 465.0, "default_temp": 9.3, "downstream_order": 3
    },
    {
        "code": "544040", "rhmz_id": "44040", "country": "RS", "name": "Titel", "river": "Tisza", "basin": "tisza", "catchment": "rs_vojvodina_danube_tisa",
        "reach_name": "Tisza (Tisa) – Zsablya – Béga-torkolat – Titel – Duna-torkolat", "lat": 45.202, "lon": 20.308, "fkm": 8.9,
        "thresholds": {"lkv": 15, "low": 80, "deg1": 500, "deg2": 650, "deg3": 730, "lnv": 855},
        "default_level": 138, "default_diff24h": 5, "default_discharge": 495.0, "default_temp": 9.4, "downstream_order": 4
    },

    # --- SAVA, DRINA, LIM, MORAVA AND IBAR (13 stations) ---
    {
        "code": "RHMZ_45084", "rhmz_id": "45084", "country": "RS", "name": "Jamena", "river": "Száva", "basin": "duna", "catchment": "rs_sava_drina_kolubara",
        "reach_name": "Száva (Sava) – Jamena – Szerémségi belépő szakasz", "lat": 44.878, "lon": 19.075, "fkm": 195.0,
        "thresholds": {"lkv": 120, "low": 240, "deg1": 750, "deg2": 880, "deg3": 960, "lnv": 1110},
        "default_level": 547, "default_diff24h": 16, "default_discharge": 1370.0, "default_temp": 10.2, "downstream_order": 1
    },
    {
        "code": "RHMZ_45090", "rhmz_id": "45090", "country": "RS", "name": "Szávaszentdemeter (Sremska Mitrovica)", "river": "Száva", "basin": "duna", "catchment": "rs_sava_drina_kolubara",
        "reach_name": "Száva (Sava) – Drina-torkolat – Szávaszentdemeter (Sremska Mitrovica)", "lat": 44.968, "lon": 19.608, "fkm": 136.0,
        "thresholds": {"lkv": 30, "low": 140, "deg1": 650, "deg2": 750, "deg3": 830, "lnv": 916},
        "default_level": 336, "default_diff24h": 21, "default_discharge": 1870.0, "default_temp": 10.3, "downstream_order": 2
    },
    {
        "code": "RHMZ_45094", "rhmz_id": "45094", "country": "RS", "name": "Szabács (Šabac)", "river": "Száva", "basin": "duna", "catchment": "rs_sava_drina_kolubara",
        "reach_name": "Száva (Sava) – Szabács (Šabac) – Beljin", "lat": 44.762, "lon": 19.702, "fkm": 102.6,
        "thresholds": {"lkv": -60, "low": 40, "deg1": 400, "deg2": 500, "deg3": 590, "lnv": 666},
        "default_level": 199, "default_diff24h": 24, "default_discharge": 1910.0, "default_temp": 10.5, "downstream_order": 3
    },
    {
        "code": "RHMZ_45099", "rhmz_id": "45099", "country": "RS", "name": "Belgrád (Beograd-Sava)", "river": "Száva", "basin": "duna", "catchment": "rs_sava_drina_kolubara",
        "reach_name": "Száva (Sava) – Obrenovac – Kolubara-torkolat – Belgrád", "lat": 44.812, "lon": 20.448, "fkm": 2.0,
        "thresholds": {"lkv": 60, "low": 135, "deg1": 500, "deg2": 600, "deg3": 680, "lnv": 798},
        "default_level": 210, "default_diff24h": 12, "default_discharge": 1960.0, "default_temp": 10.4, "downstream_order": 4
    },
    {
        "code": "RHMZ_45865", "rhmz_id": "45865", "country": "RS", "name": "Bajina Bašta", "river": "Drina", "basin": "duna", "catchment": "rs_sava_drina_kolubara",
        "reach_name": "Drina – Perućaci-tározó – Bajina Bašta – Ljubovija", "lat": 43.978, "lon": 19.562, "fkm": 162.0,
        "thresholds": {"lkv": -10, "low": 30, "deg1": 350, "deg2": 450, "deg3": 530, "lnv": 640},
        "default_level": 61, "default_diff24h": -2, "default_discharge": 285.0, "default_temp": 9.8, "downstream_order": 1
    },
    {
        "code": "RHMZ_45882", "rhmz_id": "45882", "country": "RS", "name": "Radalj (Loznica)", "river": "Drina", "basin": "duna", "catchment": "rs_sava_drina_kolubara",
        "reach_name": "Drina – Zvornik – Radalj – Loznica – Badovinci – Száva-torkolat", "lat": 44.415, "lon": 19.155, "fkm": 74.0,
        "thresholds": {"lkv": 50, "low": 110, "deg1": 380, "deg2": 460, "deg3": 540, "lnv": 655},
        "default_level": 158, "default_diff24h": -33, "default_discharge": 342.0, "default_temp": 9.9, "downstream_order": 2
    },
    {
        "code": "RHMZ_45837", "rhmz_id": "45837", "country": "RS", "name": "Prijepolje", "river": "Lim", "basin": "duna", "catchment": "rs_sava_drina_kolubara",
        "reach_name": "Lim – Brodarevo – Prijepolje – Priboj (Délnyugat-Szerbia)", "lat": 43.388, "lon": 19.645, "fkm": 62.0,
        "thresholds": {"lkv": 35, "low": 75, "deg1": 260, "deg2": 320, "deg3": 380, "lnv": 460},
        "default_level": 129, "default_diff24h": 16, "default_discharge": 167.0, "default_temp": 9.7, "downstream_order": 1
    },
    {
        "code": "RHMZ_47030", "rhmz_id": "47030", "country": "RS", "name": "Ćuprija", "river": "Nagy-Morava", "basin": "duna", "catchment": "rs_velika_zapadna_morava",
        "reach_name": "Nagy-Morava (Velika Morava) – Sztalacs – Varvarin – Ćuprija – Jagodina", "lat": 43.928, "lon": 21.368, "fkm": 145.0,
        "thresholds": {"lkv": -140, "low": -95, "deg1": 400, "deg2": 480, "deg3": 560, "lnv": 665},
        "default_level": -60, "default_diff24h": -3, "default_discharge": 130.0, "default_temp": 10.2, "downstream_order": 1
    },
    {
        "code": "RHMZ_47090", "rhmz_id": "47090", "country": "RS", "name": "Požarevac (Ljubičevski most)", "river": "Nagy-Morava", "basin": "duna", "catchment": "rs_velika_zapadna_morava",
        "reach_name": "Nagy-Morava (Velika Morava) – Bagrdan – Požarevac (Ljubičevski most) – Szendrő", "lat": 44.588, "lon": 21.125, "fkm": 35.0,
        "thresholds": {"lkv": -420, "low": -365, "deg1": 150, "deg2": 250, "deg3": 330, "lnv": 435},
        "default_level": -340, "default_diff24h": 12, "default_discharge": 145.0, "default_temp": 10.2, "downstream_order": 2
    },
    {
        "code": "RHMZ_47115", "rhmz_id": "47115", "country": "RS", "name": "Čačak", "river": "Nyugati-Morava", "basin": "duna", "catchment": "rs_velika_zapadna_morava",
        "reach_name": "Nyugati-Morava (Zapadna Morava) – Požega – Ovčar-Kablar – Čačak", "lat": 43.895, "lon": 20.352, "fkm": 148.0,
        "thresholds": {"lkv": -30, "low": 5, "deg1": 280, "deg2": 340, "deg3": 400, "lnv": 485},
        "default_level": 29, "default_diff24h": -6, "default_discharge": 32.0, "default_temp": 10.0, "downstream_order": 1
    },
    {
        "code": "RHMZ_47195", "rhmz_id": "47195", "country": "RS", "name": "Kruševac (Jasika)", "river": "Nyugati-Morava", "basin": "duna", "catchment": "rs_velika_zapadna_morava",
        "reach_name": "Nyugati-Morava (Zapadna Morava) – Kraljevo – Trstenik – Kruševac (Jasika)", "lat": 43.615, "lon": 21.305, "fkm": 28.0,
        "thresholds": {"lkv": -145, "low": -105, "deg1": 250, "deg2": 350, "deg3": 420, "lnv": 515},
        "default_level": -89, "default_diff24h": -13, "default_discharge": 83.0, "default_temp": 10.2, "downstream_order": 2
    },
    {
        "code": "RHMZ_47299", "rhmz_id": "47299", "country": "RS", "name": "Kraljevo", "river": "Ibar", "basin": "duna", "catchment": "rs_velika_zapadna_morava",
        "reach_name": "Ibar – Raška – Ušće – Mataruška Banja – Kraljevo", "lat": 43.722, "lon": 20.692, "fkm": 8.0,
        "thresholds": {"lkv": -25, "low": 10, "deg1": 260, "deg2": 330, "deg3": 390, "lnv": 475},
        "default_level": 30, "default_diff24h": -1, "default_discharge": 48.0, "default_temp": 11.0, "downstream_order": 1
    },
    {
        "code": "RHMZ_47570", "rhmz_id": "47570", "country": "RS", "name": "Aleksinac", "river": "Déli-Morava", "basin": "duna", "catchment": "rs_juzna_morava_timok",
        "reach_name": "Déli-Morava (Južna Morava) – Vranje – Leskovac – Niš – Aleksinac – Mojsinje", "lat": 43.542, "lon": 21.705, "fkm": 52.0,
        "thresholds": {"lkv": -130, "low": -85, "deg1": 280, "deg2": 360, "deg3": 430, "lnv": 515},
        "default_level": -66, "default_diff24h": 26, "default_discharge": 50.4, "default_temp": 11.0, "downstream_order": 1
    },

    # --- SERBIAN LARGE LAKES AND RESERVOIRS (3 stations) ---
    {
        "code": "RHMZ_42070", "rhmz_id": "42070", "country": "RS", "name": "Galambóc / Vaskapu-tó (Golubac)", "river": "Vaskapu-víztározó (Đerdap)", "basin": "tavak", "catchment": "rs_juzna_morava_timok",
        "reach_name": "Vaskapu-víztározó (Đerdapsko jezero – Galambóc / Golubac – Donji Milanovac – Kladovo)", "lat": 44.655, "lon": 21.635, "fkm": 1042.0,
        "thresholds": {"lkv": 540, "low": 610, "deg1": 760, "deg2": 820, "deg3": 870, "lnv": 935},
        "default_level": 683, "default_diff24h": -2, "default_discharge": 3880.0, "default_temp": 10.1, "downstream_order": 1
    },
    {
        "code": "RHMZ_99901", "country": "RS", "name": "Palics (Szabadka / Subotica)", "river": "Palicsi-tó (Palićko jezero)", "basin": "tavak", "catchment": "rs_vojvodina_danube_tisa",
        "reach_name": "Palicsi-tó és Ludasi-tó (Palićko jezero – Szabadka / Subotica)", "lat": 46.088, "lon": 19.758, "fkm": 0.0,
        "thresholds": {"lkv": 95, "low": 125, "deg1": 210, "deg2": 240, "deg3": 270, "lnv": 305},
        "default_level": 152, "default_diff24h": 0, "default_discharge": 0.5, "default_temp": 8.6, "downstream_order": 1
    },
    {
        "code": "RHMZ_99902", "country": "RS", "name": "Vlasina Rid (Surdulica)", "river": "Vlasinai-tó (Vlasinsko jezero)", "basin": "tavak", "catchment": "rs_juzna_morava_timok",
        "reach_name": "Vlasinai-tó (Vlasinsko jezero – Surdulica, Délkelet-Szerbia)", "lat": 42.702, "lon": 22.342, "fkm": 0.0,
        "thresholds": {"lkv": 180, "low": 240, "deg1": 420, "deg2": 480, "deg3": 540, "lnv": 610},
        "default_level": 318, "default_diff24h": 1, "default_discharge": 2.4, "default_temp": 7.8, "downstream_order": 1
    },

    # =========================================================================
    # 2. SMALLER WATERS, CANALS AND TRIBUTARIES (15 stations — live RHMZ hidmet.gov.rs)
    # =========================================================================
    {
        "code": "RHMZ_42401", "rhmz_id": "42401", "country": "RS", "water_category": "minor", "name": "Módos (Jaša Tomić)", "river": "Temes", "basin": "tisza", "catchment": "rs_vojvodina_danube_tisa",
        "reach_name": "Temes (Tamiš) – Módos (Jaša Tomić) – Szécsány – Pancsova (Bánát)", "lat": 45.445, "lon": 20.855, "fkm": 102.0,
        "thresholds": {"lkv": 20, "low": 75, "deg1": 450, "deg2": 600, "deg3": 700, "lnv": 845},
        "default_level": 166, "default_diff24h": 66, "default_discharge": 48.0, "default_temp": 8.8, "downstream_order": 1
    },
    {
        "code": "RHMZ_44211", "rhmz_id": "44211", "country": "RS", "water_category": "minor", "name": "Szerbittabé (Srpski Itebej)", "river": "Béga", "basin": "tisza", "catchment": "rs_vojvodina_danube_tisa",
        "reach_name": "Hajózható Béga (Plovni Begej) – Szerbittabé (Srpski Itebej) – Nagybecskerek (Zrenjanin) – Titel", "lat": 45.568, "lon": 20.715, "fkm": 74.0,
        "thresholds": {"lkv": 240, "low": 310, "deg1": 500, "deg2": 580, "deg3": 650, "lnv": 735},
        "default_level": 397, "default_diff24h": -13, "default_discharge": 18.5, "default_temp": 9.1, "downstream_order": 1
    },
    {
        "code": "RHMZ_44028", "rhmz_id": "44028", "country": "RS", "water_category": "minor", "name": "Egyházaskér (Vrbica)", "river": "Aranka (Zlatica)", "basin": "tisza", "catchment": "rs_vojvodina_danube_tisa",
        "reach_name": "Aranka (Zlatica) – Egyházaskér (Vrbica) – Tiszahegyes – Pádé (Észak-Bánát)", "lat": 46.012, "lon": 20.312, "fkm": 32.0,
        "thresholds": {"lkv": 40, "low": 75, "deg1": 240, "deg2": 300, "deg3": 360, "lnv": 430},
        "default_level": 105, "default_diff24h": 0, "default_discharge": 2.4, "default_temp": 8.9, "downstream_order": 1
    },
    {
        "code": "RHMZ_42480", "rhmz_id": "42480", "country": "RS", "water_category": "minor", "name": "Torontálújfalu (Markovićevo)", "river": "Berzava", "basin": "tisza", "catchment": "rs_vojvodina_danube_tisa",
        "reach_name": "Berzava (Brzava) – Torontálújfalu (Markovićevo) – Konak – Botoš (Közép-Bánát)", "lat": 45.325, "lon": 21.028, "fkm": 22.0,
        "thresholds": {"lkv": -190, "low": -155, "deg1": 180, "deg2": 250, "deg3": 320, "lnv": 410},
        "default_level": -140, "default_diff24h": 2, "default_discharge": 2.3, "default_temp": 7.0, "downstream_order": 1
    },
    {
        "code": "RHMZ_42610", "rhmz_id": "42610", "country": "RS", "water_category": "minor", "name": "Kuštilj (Versec)", "river": "Karas", "basin": "duna", "catchment": "rs_vojvodina_danube_tisa",
        "reach_name": "Karas (Karaš) – Kuštilj – Dobričevo – Bánáti-Palánka (Dél-Bánát)", "lat": 45.035, "lon": 21.378, "fkm": 36.0,
        "thresholds": {"lkv": 30, "low": 80, "deg1": 320, "deg2": 400, "deg3": 470, "lnv": 565},
        "default_level": 147, "default_diff24h": 145, "default_discharge": 8.6, "default_temp": 8.4, "downstream_order": 1
    },
    {
        "code": "RHMZ_42660", "rhmz_id": "42660", "country": "RS", "water_category": "minor", "name": "Kusić (Fehértemplom)", "river": "Néra", "basin": "duna", "catchment": "rs_vojvodina_danube_tisa",
        "reach_name": "Néra (Nera) – Kusić – Fehértemplom (Bela Crkva) – Vračev Gaj", "lat": 44.875, "lon": 21.478, "fkm": 18.0,
        "thresholds": {"lkv": 50, "low": 95, "deg1": 280, "deg2": 340, "deg3": 400, "lnv": 485},
        "default_level": 149, "default_diff24h": 13, "default_discharge": 46.0, "default_temp": 8.0, "downstream_order": 1
    },
    {
        "code": "RHMZ_99903", "country": "RS", "water_category": "minor", "name": "Verbász (Vrbas – DTD)", "river": "Duna–Tisza–Duna-csatorna (DTD)", "basin": "tisza", "catchment": "rs_vojvodina_danube_tisa",
        "reach_name": "Duna–Tisza–Duna-főcsatorna (Ferenc-csatorna / Nagy-Bácskai-csatorna: Bezdán – Zombor – Kúla – Verbász – Óbecse)", "lat": 45.572, "lon": 19.645, "fkm": 58.0,
        "thresholds": {"lkv": 120, "low": 165, "deg1": 310, "deg2": 360, "deg3": 410, "lnv": 475},
        "default_level": 215, "default_diff24h": 0, "default_discharge": 14.5, "default_temp": 9.1, "downstream_order": 1
    },
    {
        "code": "RHMZ_45908", "rhmz_id": "45908", "country": "RS", "water_category": "minor", "name": "Slovac (Valjevo)", "river": "Kolubara", "basin": "duna", "catchment": "rs_sava_drina_kolubara",
        "reach_name": "Kolubara – Valjevo – Slovac – Lazarevac – Draževac – Obrenovac", "lat": 44.342, "lon": 20.068, "fkm": 62.0,
        "thresholds": {"lkv": 40, "low": 80, "deg1": 280, "deg2": 350, "deg3": 420, "lnv": 525},
        "default_level": 122, "default_diff24h": -6, "default_discharge": 3.9, "default_temp": 10.5, "downstream_order": 1
    },
    {
        "code": "RHMZ_45917", "rhmz_id": "45917", "country": "RS", "water_category": "minor", "name": "Koceljeva (Ćemanov most)", "river": "Tamnava", "basin": "duna", "catchment": "rs_sava_drina_kolubara",
        "reach_name": "Tamnava – Koceljeva (Ćemanov most) – Ub – Kolubara-torkolat", "lat": 44.468, "lon": 19.835, "fkm": 38.0,
        "thresholds": {"lkv": 5, "low": 25, "deg1": 220, "deg2": 280, "deg3": 340, "lnv": 415},
        "default_level": 46, "default_diff24h": -3, "default_discharge": 0.92, "default_temp": 9.8, "downstream_order": 1
    },
    {
        "code": "RHMZ_45892", "rhmz_id": "45892", "country": "RS", "water_category": "minor", "name": "Lešnica (Loznica)", "river": "Jadar", "basin": "duna", "catchment": "rs_sava_drina_kolubara",
        "reach_name": "Jadar – Osečina – Zavlaka – Lešnica (Drina-mellékvíz)", "lat": 44.635, "lon": 19.312, "fkm": 12.0,
        "thresholds": {"lkv": -45, "low": -15, "deg1": 220, "deg2": 280, "deg3": 340, "lnv": 425},
        "default_level": -1, "default_diff24h": 4, "default_discharge": 3.58, "default_temp": 9.9, "downstream_order": 1
    },
    {
        "code": "RHMZ_42527", "rhmz_id": "42527", "country": "RS", "water_category": "minor", "name": "Petrovac (Veliko Selo)", "river": "Mlava", "basin": "duna", "catchment": "rs_velika_zapadna_morava",
        "reach_name": "Mlava – Žagubica – Gornjak – Petrovac (Veliko Selo) – Kostolac", "lat": 44.415, "lon": 21.375, "fkm": 48.0,
        "thresholds": {"lkv": 20, "low": 55, "deg1": 270, "deg2": 330, "deg3": 390, "lnv": 475},
        "default_level": 81, "default_diff24h": 29, "default_discharge": 8.4, "default_temp": 10.0, "downstream_order": 1
    },
    {
        "code": "RHMZ_42720", "rhmz_id": "42720", "country": "RS", "water_category": "minor", "name": "Kučevo", "river": "Pek", "basin": "duna", "catchment": "rs_velika_zapadna_morava",
        "reach_name": "Pek – Majdanpek – Kučevo – Veliko Gradište", "lat": 44.478, "lon": 21.668, "fkm": 42.0,
        "thresholds": {"lkv": 20, "low": 52, "deg1": 260, "deg2": 320, "deg3": 380, "lnv": 455},
        "default_level": 74, "default_diff24h": -8, "default_discharge": 6.2, "default_temp": 9.8, "downstream_order": 1
    },
    {
        "code": "RHMZ_42901", "rhmz_id": "42901", "country": "RS", "water_category": "minor", "name": "Zaječar (Čokonjar)", "river": "Timok", "basin": "duna", "catchment": "rs_juzna_morava_timok",
        "reach_name": "Timok (Veliki Timok) – Knjaževac – Zaječar – Čokonjar – Negotin", "lat": 44.018, "lon": 22.345, "fkm": 44.0,
        "thresholds": {"lkv": 30, "low": 75, "deg1": 310, "deg2": 380, "deg3": 450, "lnv": 535},
        "default_level": 118, "default_diff24h": 18, "default_discharge": 8.6, "default_temp": 10.8, "downstream_order": 1
    },
    {
        "code": "RHMZ_47990", "rhmz_id": "47990", "country": "RS", "water_category": "minor", "name": "Niš", "river": "Nišava", "basin": "duna", "catchment": "rs_juzna_morava_timok",
        "reach_name": "Nišava – Dimitrovgrad – Pirot – Bela Palanka – Niš", "lat": 43.325, "lon": 21.898, "fkm": 16.0,
        "thresholds": {"lkv": 25, "low": 65, "deg1": 280, "deg2": 350, "deg3": 410, "lnv": 495},
        "default_level": 98, "default_diff24h": 6, "default_discharge": 34.7, "default_temp": 11.0, "downstream_order": 1
    },
    {
        "code": "RHMZ_47880", "rhmz_id": "47880", "country": "RS", "water_category": "minor", "name": "Prokuplje", "river": "Toplica", "basin": "duna", "catchment": "rs_juzna_morava_timok",
        "reach_name": "Toplica – Kuršumlija – Pepeljevac – Prokuplje – Doljevac", "lat": 43.235, "lon": 21.588, "fkm": 36.0,
        "thresholds": {"lkv": -60, "low": -25, "deg1": 180, "deg2": 240, "deg3": 300, "lnv": 375},
        "default_level": -16, "default_diff24h": -1, "default_discharge": 5.2, "default_temp": 10.6, "downstream_order": 1
    },
]
