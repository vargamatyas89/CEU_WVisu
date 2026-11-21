"""
Románia (RO) — Vízgyűjtők és Hivatalos Vízügyi Mérőállomások (INHGA / OVF hydroinfo.hu 74xxxx & Copernicus GloFAS v4 5km)
Különálló ország-forrásfájl (78 romániai vízmérce: 56 főfolyó/nagy tó + 22 kisvízfolyás, hegyi folyó és mellékág)
"""

COUNTRY_META = {
    "code": "RO",
    "name": "Románia",
    "flag": "🇷🇴",
    "border_color": "#c084fc",
    "bounds": [[43.60, 20.22], [48.28, 29.72]],
}

CATCHMENTS = {
    "transylvania_maros": {"name": "Erdélyi-medence, Maros és Küküllő vízgyűjtő (RO)", "lat": 46.15, "lon": 23.85, "response_factor": 3.7, "lag_days": 1},
    "banat_temes": {"name": "Bánság (Temes, Béga és Vaskapu-Duna, RO)", "lat": 45.45, "lon": 21.35, "response_factor": 3.3, "lag_days": 1},
    "olt_basin": {"name": "Olt vízgyűjtő (Csíki-medence – Vöröstorony – Havasalföld, RO)", "lat": 45.10, "lon": 24.36, "response_factor": 3.4, "lag_days": 1},
    "wallachia_south": {"name": "Havasalföld (Zsil, Argeș, Ialomița és Alsó-Duna, RO)", "lat": 44.35, "lon": 25.10, "response_factor": 3.1, "lag_days": 2},
    "moldova_siret_prut": {"name": "Moldva és Keleti-Kárpátok (Szeret, Beszterce, Prut, RO)", "lat": 46.55, "lon": 26.95, "response_factor": 3.8, "lag_days": 1},
    "lower_danube_delta": {"name": "Dobrudzsa és Duna-delta (Brăila – Tulcea – Sulina, RO)", "lat": 45.18, "lon": 28.80, "response_factor": 2.2, "lag_days": 3},
}

STATIONS = [
    # =========================================================================
    # 1. FŐFOLYÓK ÉS NAGY TAVAK (56 állomás)
    # =========================================================================
    # --- ERDÉLY, MÁRAMAROS, SZATMÁR, PARTIUM (Tisza-vízgyűjtő Romániában - 18 élő állomás) ---
    {
        "code": "744102", "country": "RO", "name": "Máramarossziget", "river": "Tisza", "basin": "tisza", "catchment": "upper_tisza",
        "reach_name": "Tisza – Máramarosi felső szakasz (Máramarossziget / Sighetu Marmației)", "lat": 47.935, "lon": 23.888, "fkm": 804.0,
        "thresholds": {"lkv": -190, "low": -125, "deg1": 220, "deg2": 320, "deg3": 420, "lnv": 590},
        "default_level": -101, "default_diff24h": 17, "default_discharge": 108, "default_temp": 8.2, "downstream_order": 1
    },
    {
        "code": "744119", "country": "RO", "name": "Visóbeszterce", "river": "Visó", "basin": "tisza", "catchment": "upper_tisza",
        "reach_name": "Visó (Vișeu) – Felső-Visó – Visóbeszterce (Bistra)", "lat": 47.868, "lon": 24.182, "fkm": 12.0,
        "thresholds": {"lkv": 10, "low": 65, "deg1": 290, "deg2": 370, "deg3": 450, "lnv": 560},
        "default_level": 129, "default_diff24h": 12, "default_discharge": 88.7, "default_temp": 6.1, "downstream_order": 1
    },
    {
        "code": "744149", "country": "RO", "name": "Farkasrév", "river": "Iza", "basin": "tisza", "catchment": "upper_tisza",
        "reach_name": "Iza – Iza-völgy – Farkasrév (Vadu Izei)", "lat": 47.882, "lon": 23.942, "fkm": 6.0,
        "thresholds": {"lkv": 40, "low": 95, "deg1": 310, "deg2": 380, "deg3": 450, "lnv": 540},
        "default_level": 232, "default_diff24h": 51, "default_discharge": 67.0, "default_temp": 6.5, "downstream_order": 1
    },
    {
        "code": "744188", "country": "RO", "name": "Túrterebes", "river": "Túr", "basin": "tisza", "catchment": "upper_tisza",
        "reach_name": "Túr (Tur) – Avas-medence – Túrterebes (Turulung)", "lat": 47.926, "lon": 23.082, "fkm": 46.0,
        "thresholds": {"lkv": 15, "low": 65, "deg1": 320, "deg2": 390, "deg3": 450, "lnv": 530},
        "default_level": 134, "default_diff24h": -39, "default_discharge": 3.1, "default_temp": 6.8, "downstream_order": 1
    },
    {
        "code": "744212", "country": "RO", "name": "Dés", "river": "Szamos", "basin": "tisza", "catchment": "upper_tisza",
        "reach_name": "Szamos (Someș) – Nagy- és Kis-Szamos egyesülése (Dés / Dej)", "lat": 47.142, "lon": 23.875, "fkm": 208.0,
        "thresholds": {"lkv": 10, "low": 80, "deg1": 450, "deg2": 550, "deg3": 650, "lnv": 820},
        "default_level": 206, "default_diff24h": -42, "default_discharge": 90.4, "default_temp": 6.9, "downstream_order": 1
    },
    {
        "code": "744216", "country": "RO", "name": "Sülelmed", "river": "Szamos", "basin": "tisza", "catchment": "upper_tisza",
        "reach_name": "Szamos (Someș) – Zsibó – Sülelmed (Ulmeni) szakasz", "lat": 47.465, "lon": 23.302, "fkm": 132.0,
        "thresholds": {"lkv": -160, "low": -90, "deg1": 380, "deg2": 480, "deg3": 580, "lnv": 740},
        "default_level": -43, "default_diff24h": -27, "default_discharge": 75.6, "default_temp": 7.0, "downstream_order": 2
    },
    {
        "code": "744220", "country": "RO", "name": "Szatmárnémeti", "river": "Szamos", "basin": "tisza", "catchment": "upper_tisza",
        "reach_name": "Szamos (Someș) – Szatmári-síkság (Szatmárnémeti / Satu Mare)", "lat": 47.792, "lon": 22.875, "fkm": 68.0,
        "thresholds": {"lkv": -160, "low": -70, "deg1": 450, "deg2": 580, "deg3": 700, "lnv": 885},
        "default_level": 47, "default_diff24h": 12, "default_discharge": 223.0, "default_temp": 7.2, "downstream_order": 3
    },
    {
        "code": "744360", "country": "RO", "name": "Hagymáslápos", "river": "Lápos", "basin": "tisza", "catchment": "upper_tisza",
        "reach_name": "Lápos (Lăpuș) – Nagybányai-medence – Hagymáslápos (Lăpușel)", "lat": 47.618, "lon": 23.482, "fkm": 14.0,
        "thresholds": {"lkv": -20, "low": 40, "deg1": 310, "deg2": 390, "deg3": 460, "lnv": 580},
        "default_level": 141, "default_diff24h": -94, "default_discharge": 51.0, "default_temp": 6.7, "downstream_order": 1
    },
    {
        "code": "744392", "country": "RO", "name": "Domahida", "river": "Kraszna", "basin": "tisza", "catchment": "upper_tisza",
        "reach_name": "Kraszna (Crasna) – Szilágysomlyó – Domahida (Domănești)", "lat": 47.738, "lon": 22.582, "fkm": 48.0,
        "thresholds": {"lkv": 10, "low": 70, "deg1": 360, "deg2": 430, "deg3": 500, "lnv": 610},
        "default_level": 223, "default_diff24h": 7, "default_discharge": 3.9, "default_temp": 7.1, "downstream_order": 1
    },
    {
        "code": "744573", "country": "RO", "name": "Szilágynagyfalu", "river": "Berettyó", "basin": "tisza", "catchment": "korosok",
        "reach_name": "Berettyó (Barcău) – Felső-Berettyó (Szilágynagyfalu / Nușfalău)", "lat": 47.198, "lon": 22.725, "fkm": 115.0,
        "thresholds": {"lkv": -45, "low": 5, "deg1": 240, "deg2": 310, "deg3": 380, "lnv": 465},
        "default_level": 23, "default_diff24h": -5, "default_discharge": 1.2, "default_temp": 7.3, "downstream_order": 1
    },
    {
        "code": "744580", "country": "RO", "name": "Szalárd", "river": "Berettyó", "basin": "tisza", "catchment": "korosok",
        "reach_name": "Berettyó (Barcău) – Margitta – Szalárd (Sălard) szakasz", "lat": 47.218, "lon": 22.042, "fkm": 52.0,
        "thresholds": {"lkv": -20, "low": 40, "deg1": 340, "deg2": 410, "deg3": 480, "lnv": 590},
        "default_level": 195, "default_diff24h": 61, "default_discharge": 3.6, "default_temp": 7.5, "downstream_order": 2
    },
    {
        "code": "744519", "country": "RO", "name": "Csucsa", "river": "Sebes-Körös", "basin": "tisza", "catchment": "korosok",
        "reach_name": "Sebes-Körös (Crișul Repede) – Bánffyhunyad – Csucsa (Ciucea) – Révi-szoros", "lat": 46.952, "lon": 22.815, "fkm": 138.0,
        "thresholds": {"lkv": -60, "low": -10, "deg1": 240, "deg2": 310, "deg3": 380, "lnv": 475},
        "default_level": 19, "default_diff24h": 21, "default_discharge": 9.2, "default_temp": 6.8, "downstream_order": 1
    },
    {
        "code": "744524", "country": "RO", "name": "Nagyvárad", "river": "Sebes-Körös", "basin": "tisza", "catchment": "korosok",
        "reach_name": "Sebes-Körös (Crișul Repede) – Élesd – Nagyvárad (Oradea)", "lat": 47.058, "lon": 21.932, "fkm": 74.0,
        "thresholds": {"lkv": -65, "low": -5, "deg1": 310, "deg2": 390, "deg3": 470, "lnv": 585},
        "default_level": 32, "default_diff24h": -1, "default_discharge": 14.5, "default_temp": 7.4, "downstream_order": 2
    },
    {
        "code": "744453", "country": "RO", "name": "Belényes", "river": "Fekete-Körös", "basin": "tisza", "catchment": "korosok",
        "reach_name": "Fekete-Körös (Crișul Negru) – Belényesi-medence (Belényes / Beiuș)", "lat": 46.668, "lon": 22.352, "fkm": 112.0,
        "thresholds": {"lkv": 15, "low": 65, "deg1": 310, "deg2": 380, "deg3": 450, "lnv": 560},
        "default_level": 137, "default_diff24h": 6, "default_discharge": 26.4, "default_temp": 7.1, "downstream_order": 1
    },
    {
        "code": "744455", "country": "RO", "name": "Tenke", "river": "Fekete-Körös", "basin": "tisza", "catchment": "korosok",
        "reach_name": "Fekete-Körös (Crișul Negru) – Tenke (Tinca) szakasz", "lat": 46.775, "lon": 21.932, "fkm": 64.0,
        "thresholds": {"lkv": -10, "low": 60, "deg1": 370, "deg2": 450, "deg3": 530, "lnv": 650},
        "default_level": 184, "default_diff24h": -138, "default_discharge": 56.3, "default_temp": 7.5, "downstream_order": 2
    },
    {
        "code": "744459", "country": "RO", "name": "Nagyzerénd", "river": "Fekete-Körös", "basin": "tisza", "catchment": "korosok",
        "reach_name": "Fekete-Körös (Crișul Negru) – Nagyzerénd (Zerind)", "lat": 46.625, "lon": 21.518, "fkm": 22.0,
        "thresholds": {"lkv": -30, "low": 70, "deg1": 520, "deg2": 620, "deg3": 720, "lnv": 850},
        "default_level": 422, "default_diff24h": 94, "default_discharge": 99.4, "default_temp": 7.7, "downstream_order": 3
    },
    {
        "code": "744405", "country": "RO", "name": "Honctő", "river": "Fehér-Körös", "basin": "tisza", "catchment": "korosok",
        "reach_name": "Fehér-Körös (Crișul Alb) – Brád – Honctő (Gurahonț)", "lat": 46.272, "lon": 22.345, "fkm": 128.0,
        "thresholds": {"lkv": -60, "low": -5, "deg1": 280, "deg2": 360, "deg3": 440, "lnv": 550},
        "default_level": 31, "default_diff24h": -39, "default_discharge": 22.0, "default_temp": 7.2, "downstream_order": 1
    },
    {
        "code": "744409", "country": "RO", "name": "Kisjenő", "river": "Fehér-Körös", "basin": "tisza", "catchment": "korosok",
        "reach_name": "Fehér-Körös (Crișul Alb) – Kisjenő (Chișineu-Criș)", "lat": 46.522, "lon": 21.518, "fkm": 32.0,
        "thresholds": {"lkv": -40, "low": 50, "deg1": 480, "deg2": 580, "deg3": 680, "lnv": 815},
        "default_level": 432, "default_diff24h": 213, "default_discharge": 47.0, "default_temp": 7.7, "downstream_order": 2
    },

    # --- MAROS, KÜKÜLLŐ ÉS SZTRIGY (Erdélyi-medence - 8 állomás) ---
    {
        "code": "749001", "country": "RO", "name": "Marosvásárhely", "river": "Maros", "basin": "tisza", "catchment": "transylvania_maros",
        "reach_name": "Maros (Mureș) – Felső-Maros (Szászrégen – Marosvásárhely / Târgu Mureș)", "lat": 46.545, "lon": 24.558, "fkm": 535.0,
        "thresholds": {"lkv": -55, "low": 10, "deg1": 320, "deg2": 400, "deg3": 480, "lnv": 610},
        "default_level": 68, "default_diff24h": 14, "default_discharge": 54.0, "default_temp": 6.8, "downstream_order": 1
    },
    {
        "code": "749002", "country": "RO", "name": "Medgyes", "river": "Nagy-Küküllő", "basin": "tisza", "catchment": "transylvania_maros",
        "reach_name": "Nagy-Küküllő (Târnava Mare) – Segesvár – Medgyes (Mediaș) – Balázsfalva", "lat": 46.165, "lon": 24.352, "fkm": 68.0,
        "thresholds": {"lkv": -40, "low": 20, "deg1": 290, "deg2": 360, "deg3": 430, "lnv": 545},
        "default_level": 84, "default_diff24h": 19, "default_discharge": 28.0, "default_temp": 7.0, "downstream_order": 1
    },
    {
        "code": "744612", "country": "RO", "name": "Gyulafehérvár", "river": "Maros", "basin": "tisza", "catchment": "transylvania_maros",
        "reach_name": "Maros (Mureș) – Küküllő- és Aranyos-torkolat – Gyulafehérvár (Alba Iulia)", "lat": 46.068, "lon": 23.585, "fkm": 412.0,
        "thresholds": {"lkv": -95, "low": -25, "deg1": 380, "deg2": 470, "deg3": 560, "lnv": 715},
        "default_level": 22, "default_diff24h": 97, "default_discharge": 151.0, "default_temp": 7.4, "downstream_order": 2
    },
    {
        "code": "744834", "country": "RO", "name": "Petrény", "river": "Sztrigy", "basin": "tisza", "catchment": "transylvania_maros",
        "reach_name": "Sztrigy (Strei) – Hátszegi-medence – Petrény (Petreni)", "lat": 45.775, "lon": 23.018, "fkm": 18.0,
        "thresholds": {"lkv": -20, "low": 25, "deg1": 250, "deg2": 310, "deg3": 370, "lnv": 455},
        "default_level": 63, "default_diff24h": 3, "default_discharge": 26.8, "default_temp": 7.1, "downstream_order": 1
    },
    {
        "code": "744616", "country": "RO", "name": "Branyicska", "river": "Maros", "basin": "tisza", "catchment": "transylvania_maros",
        "reach_name": "Maros (Mureș) – Déva – Branyicska (Brănișca) szakasz", "lat": 45.915, "lon": 22.782, "fkm": 315.0,
        "thresholds": {"lkv": -130, "low": -60, "deg1": 360, "deg2": 450, "deg3": 540, "lnv": 690},
        "default_level": -32, "default_diff24h": 28, "default_discharge": 139.0, "default_temp": 7.6, "downstream_order": 3
    },
    {
        "code": "744618", "country": "RO", "name": "Soborsin", "river": "Maros", "basin": "tisza", "catchment": "transylvania_maros",
        "reach_name": "Maros (Mureș) – Marosillye – Soborsin (Săvârșin)", "lat": 46.012, "lon": 22.235, "fkm": 235.0,
        "thresholds": {"lkv": -90, "low": -20, "deg1": 370, "deg2": 460, "deg3": 550, "lnv": 680},
        "default_level": 37, "default_diff24h": -5, "default_discharge": 117.0, "default_temp": 7.8, "downstream_order": 4
    },
    {
        "code": "744622", "country": "RO", "name": "Arad", "river": "Maros", "basin": "tisza", "catchment": "lower_tisza",
        "reach_name": "Maros (Mureș) – Arad szakasz", "lat": 46.172, "lon": 21.322, "fkm": 98.0,
        "thresholds": {"lkv": -115, "low": -40, "deg1": 350, "deg2": 430, "deg3": 510, "lnv": 645},
        "default_level": 17, "default_diff24h": -12, "default_discharge": 110.0, "default_temp": 8.0, "downstream_order": 5
    },
    {
        "code": "744624", "country": "RO", "name": "Nagylak", "river": "Maros", "basin": "tisza", "catchment": "lower_tisza",
        "reach_name": "Maros (Mureș) – Pécska – Nagylak (Nădlac) határszakasz", "lat": 46.155, "lon": 20.752, "fkm": 52.0,
        "thresholds": {"lkv": -120, "low": -45, "deg1": 360, "deg2": 440, "deg3": 520, "lnv": 650},
        "default_level": 5, "default_diff24h": -29, "default_discharge": 125.0, "default_temp": 8.1, "downstream_order": 6
    },

    # --- BÁNSÁG (Béga és Temes - 2 állomás) ---
    {
        "code": "749003", "country": "RO", "name": "Temesvár", "river": "Béga", "basin": "tisza", "catchment": "banat_temes",
        "reach_name": "Béga (Bega) – Facsád – Temesvár (Timișoara) – Ótelek", "lat": 45.748, "lon": 21.228, "fkm": 114.0,
        "thresholds": {"lkv": -30, "low": 25, "deg1": 240, "deg2": 300, "deg3": 360, "lnv": 440},
        "default_level": 92, "default_diff24h": 6, "default_discharge": 18.5, "default_temp": 8.1, "downstream_order": 1
    },
    {
        "code": "749004", "country": "RO", "name": "Lugos", "river": "Temes", "basin": "duna", "catchment": "banat_temes",
        "reach_name": "Temes (Timiș) – Karánsebes – Lugos (Lugoj) – Temesmóra", "lat": 45.688, "lon": 21.902, "fkm": 162.0,
        "thresholds": {"lkv": -45, "low": 20, "deg1": 330, "deg2": 410, "deg3": 490, "lnv": 610},
        "default_level": 78, "default_diff24h": 11, "default_discharge": 42.0, "default_temp": 8.0, "downstream_order": 1
    },

    # --- AL-DUNA ÉS DUNA-DELTA (Romániai Duna-főág - 14 élő 742xxx állomás) ---
    {
        "code": "742001", "country": "RO", "name": "Báziás", "river": "Duna", "basin": "duna", "catchment": "banat_temes",
        "reach_name": "Al-Duna (Dunărea) – Báziás (Baziaș) – Néra-torkolat", "lat": 44.812, "lon": 21.392, "fkm": 1072.4,
        "thresholds": {"lkv": 280, "low": 420, "deg1": 780, "deg2": 860, "deg3": 940, "lnv": 1050},
        "default_level": 574, "default_diff24h": 4, "default_discharge": 3650, "default_temp": 8.8, "downstream_order": 16
    },
    {
        "code": "742002", "country": "RO", "name": "Ómoldova", "river": "Duna", "basin": "duna", "catchment": "banat_temes",
        "reach_name": "Al-Duna (Dunărea) – Ómoldova (Moldova Veche) – Drenkó", "lat": 44.718, "lon": 21.622, "fkm": 1048.0,
        "thresholds": {"lkv": 420, "low": 560, "deg1": 900, "deg2": 980, "deg3": 1050, "lnv": 1160},
        "default_level": 720, "default_diff24h": 2, "default_discharge": 3710, "default_temp": 8.8, "downstream_order": 17
    },
    {
        "code": "742005", "country": "RO", "name": "Orsova", "river": "Duna", "basin": "duna", "catchment": "banat_temes",
        "reach_name": "Al-Duna (Dunărea) – Kazán-szoros – Orsova (Orșova / Vaskapu-tározó)", "lat": 44.722, "lon": 22.398, "fkm": 954.0,
        "thresholds": {"lkv": 2100, "low": 2300, "deg1": 2750, "deg2": 2850, "deg3": 2950, "lnv": 3120},
        "default_level": 2522, "default_diff24h": -3, "default_discharge": 3820, "default_temp": 8.9, "downstream_order": 18
    },
    {
        "code": "742008", "country": "RO", "name": "Szörényvár", "river": "Duna", "basin": "duna", "catchment": "wallachia_south",
        "reach_name": "Al-Duna (Dunărea) – Vaskapu I. – Szörényvár (Drobeta-Turnu Severin)", "lat": 44.622, "lon": 22.655, "fkm": 931.0,
        "thresholds": {"lkv": 250, "low": 420, "deg1": 920, "deg2": 1020, "deg3": 1120, "lnv": 1240},
        "default_level": 742, "default_diff24h": 16, "default_discharge": 3850, "default_temp": 9.0, "downstream_order": 19
    },
    {
        "code": "742013", "country": "RO", "name": "Calafat", "river": "Duna", "basin": "duna", "catchment": "wallachia_south",
        "reach_name": "Al-Duna (Dunărea) – Gruia – Cetate – Calafat szakasz", "lat": 43.992, "lon": 22.932, "fkm": 795.0,
        "thresholds": {"lkv": -120, "low": -30, "deg1": 550, "deg2": 650, "deg3": 750, "lnv": 885},
        "default_level": 23, "default_diff24h": 49, "default_discharge": 3920, "default_temp": 9.1, "downstream_order": 20
    },
    {
        "code": "742018", "country": "RO", "name": "Corabia", "river": "Duna", "basin": "duna", "catchment": "wallachia_south",
        "reach_name": "Al-Duna (Dunărea) – Bechet – Zsil-torkolat – Corabia szakasz", "lat": 43.772, "lon": 24.502, "fkm": 630.0,
        "thresholds": {"lkv": -150, "low": -50, "deg1": 520, "deg2": 620, "deg3": 720, "lnv": 850},
        "default_level": -26, "default_diff24h": 33, "default_discharge": 4080, "default_temp": 9.2, "downstream_order": 21
    },
    {
        "code": "742024", "country": "RO", "name": "Turnu Magurele", "river": "Duna", "basin": "duna", "catchment": "wallachia_south",
        "reach_name": "Al-Duna (Dunărea) – Olt-torkolat – Turnu Măgurele – Zimnicea", "lat": 43.738, "lon": 24.868, "fkm": 597.0,
        "thresholds": {"lkv": -140, "low": -45, "deg1": 540, "deg2": 640, "deg3": 740, "lnv": 870},
        "default_level": -15, "default_diff24h": 28, "default_discharge": 4290, "default_temp": 9.2, "downstream_order": 22
    },
    {
        "code": "742027", "country": "RO", "name": "Gyurgyevó", "river": "Duna", "basin": "duna", "catchment": "wallachia_south",
        "reach_name": "Al-Duna (Dunărea) – Gyurgyevó (Giurgiu) – Rusze – Oltenița", "lat": 43.885, "lon": 25.965, "fkm": 493.0,
        "thresholds": {"lkv": -190, "low": -110, "deg1": 560, "deg2": 660, "deg3": 760, "lnv": 890},
        "default_level": -95, "default_diff24h": 19, "default_discharge": 4380, "default_temp": 9.3, "downstream_order": 23
    },
    {
        "code": "742034", "country": "RO", "name": "Calarasi", "river": "Duna", "basin": "duna", "catchment": "wallachia_south",
        "reach_name": "Al-Duna (Dunărea) – Călărași – Borcea-ág szakasz", "lat": 44.195, "lon": 27.332, "fkm": 370.0,
        "thresholds": {"lkv": -210, "low": -120, "deg1": 520, "deg2": 620, "deg3": 720, "lnv": 845},
        "default_level": -104, "default_diff24h": 7, "default_discharge": 4450, "default_temp": 9.4, "downstream_order": 24
    },
    {
        "code": "742038", "country": "RO", "name": "Cernavoda", "river": "Duna", "basin": "duna", "catchment": "lower_danube_delta",
        "reach_name": "Al-Duna (Dunărea) – Fetești – Cernavodă – Hârșova szakasz", "lat": 44.342, "lon": 28.028, "fkm": 300.0,
        "thresholds": {"lkv": -250, "low": -175, "deg1": 500, "deg2": 600, "deg3": 700, "lnv": 825},
        "default_level": -169, "default_diff24h": 2, "default_discharge": 4520, "default_temp": 9.4, "downstream_order": 25
    },
    {
        "code": "742051", "country": "RO", "name": "Braila", "river": "Duna", "basin": "duna", "catchment": "lower_danube_delta",
        "reach_name": "Al-Duna (Dunărea) – Brăilai-láp és folyamág (Brăila)", "lat": 45.268, "lon": 27.975, "fkm": 170.0,
        "thresholds": {"lkv": -110, "low": -20, "deg1": 540, "deg2": 620, "deg3": 700, "lnv": 812},
        "default_level": 12, "default_diff24h": -1, "default_discharge": 4620, "default_temp": 9.5, "downstream_order": 26
    },
    {
        "code": "742052", "country": "RO", "name": "Galac", "river": "Duna", "basin": "duna", "catchment": "lower_danube_delta",
        "reach_name": "Al-Duna (Dunărea) – Szeret- és Prut-torkolat – Galac (Galați) – Isaccea", "lat": 45.432, "lon": 28.055, "fkm": 150.0,
        "thresholds": {"lkv": -95, "low": 0, "deg1": 560, "deg2": 640, "deg3": 720, "lnv": 835},
        "default_level": 36, "default_diff24h": -1, "default_discharge": 4980, "default_temp": 9.5, "downstream_order": 27
    },
    {
        "code": "742057", "country": "RO", "name": "Tulcea", "river": "Duna", "basin": "duna", "catchment": "lower_danube_delta",
        "reach_name": "Duna-delta (Delta Dunării) – Tulcea – Chilia / Szent György-ág", "lat": 45.182, "lon": 28.802, "fkm": 71.0,
        "thresholds": {"lkv": -60, "low": 5, "deg1": 360, "deg2": 420, "deg3": 480, "lnv": 565},
        "default_level": 26, "default_diff24h": 2, "default_discharge": 5050, "default_temp": 9.6, "downstream_order": 28
    },
    {
        "code": "742060", "country": "RO", "name": "Sulina", "river": "Duna", "basin": "duna", "catchment": "lower_danube_delta",
        "reach_name": "Duna-delta (Delta Dunării) – Sulinai-főág – Fekete-tengeri torkolat (Sulina)", "lat": 45.158, "lon": 29.658, "fkm": 0.0,
        "thresholds": {"lkv": -20, "low": 25, "deg1": 210, "deg2": 260, "deg3": 310, "lnv": 385},
        "default_level": 60, "default_diff24h": 5, "default_discharge": 5100, "default_temp": 9.8, "downstream_order": 29
    },

    # --- OLT, ZSIL, ARGEȘ, IALOMIȚA, BODZA (Kárpátokon túli déli vízgyűjtők - 7 állomás) ---
    {
        "code": "749005", "country": "RO", "name": "Sepsiszentgyörgy", "river": "Olt", "basin": "olt_siret", "catchment": "olt_basin",
        "reach_name": "Olt – Csíki- és Háromszéki-medence (Csíkszereda – Sepsiszentgyörgy – Fogaras)", "lat": 45.862, "lon": 25.795, "fkm": 540.0,
        "thresholds": {"lkv": -40, "low": 15, "deg1": 280, "deg2": 350, "deg3": 420, "lnv": 530},
        "default_level": 64, "default_diff24h": 9, "default_discharge": 32.0, "default_temp": 6.4, "downstream_order": 1
    },
    {
        "code": "749006", "country": "RO", "name": "Râmnicu Vâlcea", "river": "Olt", "basin": "olt_siret", "catchment": "olt_basin",
        "reach_name": "Olt – Vöröstoronyi-szoros – Râmnicu Vâlcea – Drăgășani", "lat": 45.102, "lon": 24.375, "fkm": 235.0,
        "thresholds": {"lkv": -30, "low": 35, "deg1": 360, "deg2": 440, "deg3": 520, "lnv": 645},
        "default_level": 118, "default_diff24h": 15, "default_discharge": 128.0, "default_temp": 7.8, "downstream_order": 2
    },
    {
        "code": "749007", "country": "RO", "name": "Slatina", "river": "Olt", "basin": "olt_siret", "catchment": "olt_basin",
        "reach_name": "Olt – Alsó-Olt (Slatina – Caracal – Islaz Duna-torkolat)", "lat": 44.428, "lon": 24.355, "fkm": 112.0,
        "thresholds": {"lkv": -20, "low": 45, "deg1": 390, "deg2": 470, "deg3": 550, "lnv": 680},
        "default_level": 142, "default_diff24h": 12, "default_discharge": 175.0, "default_temp": 8.4, "downstream_order": 3
    },
    {
        "code": "749008", "country": "RO", "name": "Craiova (Podari)", "river": "Zsil", "basin": "olt_siret", "catchment": "wallachia_south",
        "reach_name": "Zsil (Jiu) – Zsilvásárhely (Târgu Jiu) – Filiași – Craiova – Bechet", "lat": 44.252, "lon": 23.778, "fkm": 118.0,
        "thresholds": {"lkv": -45, "low": 25, "deg1": 350, "deg2": 430, "deg3": 510, "lnv": 635},
        "default_level": 95, "default_diff24h": 14, "default_discharge": 86.0, "default_temp": 8.3, "downstream_order": 1
    },
    {
        "code": "749009", "country": "RO", "name": "Pitești", "river": "Argeș", "basin": "olt_siret", "catchment": "wallachia_south",
        "reach_name": "Argeș – Curtea de Argeș – Pitești – Bukarest déli előtér – Oltenița", "lat": 44.855, "lon": 24.885, "fkm": 210.0,
        "thresholds": {"lkv": -35, "low": 20, "deg1": 320, "deg2": 390, "deg3": 460, "lnv": 575},
        "default_level": 76, "default_diff24h": 8, "default_discharge": 62.0, "default_temp": 8.1, "downstream_order": 1
    },
    {
        "code": "749010", "country": "RO", "name": "Slobozia", "river": "Ialomița", "basin": "olt_siret", "catchment": "wallachia_south",
        "reach_name": "Ialomița – Târgoviște – Urziceni – Slobozia – Țăndărei", "lat": 44.558, "lon": 27.365, "fkm": 86.0,
        "thresholds": {"lkv": -40, "low": 15, "deg1": 310, "deg2": 380, "deg3": 450, "lnv": 550},
        "default_level": 68, "default_diff24h": 5, "default_discharge": 44.0, "default_temp": 8.5, "downstream_order": 1
    },
    {
        "code": "749011", "country": "RO", "name": "Bodzavásár (Buzău)", "river": "Bodza", "basin": "olt_siret", "catchment": "moldova_siret_prut",
        "reach_name": "Bodza (Buzău) – Bodzai-szoros – Bodzavásár (Buzău) – Szeret-torkolat", "lat": 45.158, "lon": 26.828, "fkm": 110.0,
        "thresholds": {"lkv": -30, "low": 20, "deg1": 300, "deg2": 370, "deg3": 440, "lnv": 540},
        "default_level": 72, "default_diff24h": 7, "default_discharge": 29.0, "default_temp": 7.9, "downstream_order": 1
    },

    # --- MOLDVA (Szeret / Siret, Beszterce / Bistrița, Prut - 4 állomás) ---
    {
        "code": "749012", "country": "RO", "name": "Roman", "river": "Szeret", "basin": "olt_siret", "catchment": "moldova_siret_prut",
        "reach_name": "Szeret (Siret) – Felső- és Közép-Szeret (Suceava – Pașcani – Roman – Bákó)", "lat": 46.918, "lon": 26.928, "fkm": 295.0,
        "thresholds": {"lkv": -50, "low": 25, "deg1": 380, "deg2": 460, "deg3": 540, "lnv": 675},
        "default_level": 112, "default_diff24h": 18, "default_discharge": 135.0, "default_temp": 7.0, "downstream_order": 1
    },
    {
        "code": "749013", "country": "RO", "name": "Lungoci (Focșani)", "river": "Szeret", "basin": "olt_siret", "catchment": "moldova_siret_prut",
        "reach_name": "Szeret (Siret) – Alsó-Szeret (Adjud – Focșani / Lungoci – Galac)", "lat": 45.558, "lon": 27.495, "fkm": 78.0,
        "thresholds": {"lkv": -60, "low": 30, "deg1": 420, "deg2": 510, "deg3": 600, "lnv": 745},
        "default_level": 148, "default_diff24h": 21, "default_discharge": 240.0, "default_temp": 7.8, "downstream_order": 2
    },
    {
        "code": "749014", "country": "RO", "name": "Karácsonkő (Piatra Neamț)", "river": "Beszterce", "basin": "olt_siret", "catchment": "moldova_siret_prut",
        "reach_name": "Aranyos-Beszterce (Bistrița) – Békás – Karácsonkő (Piatra Neamț) – Bákó", "lat": 46.925, "lon": 26.372, "fkm": 92.0,
        "thresholds": {"lkv": -25, "low": 30, "deg1": 310, "deg2": 380, "deg3": 450, "lnv": 560},
        "default_level": 88, "default_diff24h": 11, "default_discharge": 58.0, "default_temp": 6.6, "downstream_order": 1
    },
    {
        "code": "749015", "country": "RO", "name": "Ungheni (Jászvásár)", "river": "Prut", "basin": "olt_siret", "catchment": "moldova_siret_prut",
        "reach_name": "Prut – Stânca-Costești – Jászvásár (Iași / Ungheni) – Fălciu – Galac", "lat": 47.205, "lon": 27.785, "fkm": 385.0,
        "thresholds": {"lkv": -40, "low": 35, "deg1": 390, "deg2": 480, "deg3": 570, "lnv": 710},
        "default_level": 116, "default_diff24h": 9, "default_discharge": 92.0, "default_temp": 7.3, "downstream_order": 1
    },

    # --- ROMÁNIAI NAGY TAVAK (3 állomás) ---
    {
        "code": "749016", "country": "RO", "name": "Jurilovca", "river": "Razim-tó", "basin": "tavak", "catchment": "lower_danube_delta",
        "reach_name": "Razim–Sinoe-tórendszer (Lacul Razim / Razelm – Babadag – Jurilovca)", "lat": 44.765, "lon": 28.915, "fkm": 0.0,
        "thresholds": {"lkv": -10, "low": 25, "deg1": 120, "deg2": 145, "deg3": 170, "lnv": 210},
        "default_level": 56, "default_diff24h": 2, "default_discharge": 28.0, "default_temp": 9.6, "downstream_order": 1
    },
    {
        "code": "749017", "country": "RO", "name": "Békási-gát (Bicaz)", "river": "Békási-tó", "basin": "tavak", "catchment": "moldova_siret_prut",
        "reach_name": "Békási-víztározó (Lacul Izvorul Muntelui / Bicaz – Ceahlău)", "lat": 46.968, "lon": 26.075, "fkm": 0.0,
        "thresholds": {"lkv": 120, "low": 240, "deg1": 520, "deg2": 580, "deg3": 640, "lnv": 710},
        "default_level": 365, "default_diff24h": 4, "default_discharge": 42.0, "default_temp": 6.8, "downstream_order": 1
    },
    {
        "code": "749018", "country": "RO", "name": "Vidraru-gát", "river": "Vidraru-tó", "basin": "tavak", "catchment": "olt_basin",
        "reach_name": "Vidraru-víztározó (Lacul Vidraru – Fogarasi-havasok / Argeș)", "lat": 45.378, "lon": 24.632, "fkm": 0.0,
        "thresholds": {"lkv": 140, "low": 260, "deg1": 550, "deg2": 610, "deg3": 670, "lnv": 740},
        "default_level": 388, "default_diff24h": 3, "default_discharge": 24.0, "default_temp": 6.5, "downstream_order": 1
    },

    # =========================================================================
    # 2. KISVÍZFOLYÁSOK, HEGYI PATAKOK ÉS MELLÉKFOLYÓK (OVF 74xxxx & GloFAS v4 5km — 22 állomás)
    # =========================================================================
    {
        "code": "744390", "water_category": "minor", "country": "RO",
        "name": "Alsószopor", "river": "Kraszna", "basin": "tisza", "catchment": "upper_tisza",
        "reach_name": "Felső-Kraszna (Crasna) – Szilágysomlyó – Alsószopor (Supuru de Jos)", "lat": 47.462, "lon": 22.785, "fkm": 92.0,
        "thresholds": {"lkv": -10, "low": 20, "deg1": 250, "deg2": 320, "deg3": 380, "lnv": 465},
        "default_level": 33, "default_diff24h": 5, "default_discharge": 8.8, "default_temp": 6.9, "downstream_order": 1
    },
    {
        "code": "744575", "water_category": "minor", "country": "RO",
        "name": "Márkaszék", "river": "Berettyó", "basin": "tisza", "catchment": "korosok",
        "reach_name": "Berettyó (Barcău) – Márkaszék (Marca) – Bisztraterebes", "lat": 47.212, "lon": 22.532, "fkm": 88.0,
        "thresholds": {"lkv": -15, "low": 35, "deg1": 280, "deg2": 350, "deg3": 410, "lnv": 495},
        "default_level": 101, "default_diff24h": -13, "default_discharge": 2.4, "default_temp": 7.3, "downstream_order": 2
    },
    {
        "code": "744457", "water_category": "minor", "country": "RO",
        "name": "Talpas", "river": "Fekete-Körös", "basin": "tisza", "catchment": "korosok",
        "reach_name": "Fekete-Körös (Crișul Negru) – Talpas (Talpoș) szakasz", "lat": 46.678, "lon": 21.718, "fkm": 42.0,
        "thresholds": {"lkv": -20, "low": 65, "deg1": 450, "deg2": 540, "deg3": 630, "lnv": 760},
        "default_level": 351, "default_diff24h": -211, "default_discharge": 67.8, "default_temp": 7.6, "downstream_order": 3
    },
    {
        "code": "744408", "water_category": "minor", "country": "RO",
        "name": "Borosjenő", "river": "Fehér-Körös", "basin": "tisza", "catchment": "korosok",
        "reach_name": "Fehér-Körös (Crișul Alb) – Borosjenő (Ineu) – Csigér-torkolat", "lat": 46.425, "lon": 21.835, "fkm": 68.0,
        "thresholds": {"lkv": -45, "low": 35, "deg1": 380, "deg2": 460, "deg3": 540, "lnv": 670},
        "default_level": 255, "default_diff24h": 30, "default_discharge": 62.8, "default_temp": 7.5, "downstream_order": 2
    },
    {
        "code": "744444", "water_category": "minor", "country": "RO",
        "name": "Kurtakér", "river": "Csigér", "basin": "tisza", "catchment": "korosok",
        "reach_name": "Csigér-patak (Cigher) – Tauț-tározó – Kurtakér (Chier) – Borosjenő", "lat": 46.332, "lon": 21.892, "fkm": 14.0,
        "thresholds": {"lkv": 15, "low": 60, "deg1": 280, "deg2": 340, "deg3": 400, "lnv": 485},
        "default_level": 153, "default_diff24h": -11, "default_discharge": 1.2, "default_temp": 7.4, "downstream_order": 1
    },
    {
        "code": "744620", "water_category": "minor", "country": "RO",
        "name": "Máriaradna", "river": "Maros", "basin": "tisza", "catchment": "lower_tisza",
        "reach_name": "Maros (Mureș) – Lippa – Máriaradna (Radna) szoros", "lat": 46.095, "lon": 21.688, "fkm": 142.0,
        "thresholds": {"lkv": -110, "low": -45, "deg1": 350, "deg2": 430, "deg3": 510, "lnv": 640},
        "default_level": -28, "default_diff24h": -8, "default_discharge": 108.0, "default_temp": 7.9, "downstream_order": 5
    },
    {
        "code": "749101", "water_category": "minor", "country": "RO",
        "name": "Kolozsvár (Cluj)", "river": "Kis-Szamos", "basin": "tisza", "catchment": "upper_tisza",
        "reach_name": "Kis-Szamos (Someșul Mic) – Gyalu – Kolozsvár (Cluj-Napoca) – Szamosújvár – Dés", "lat": 46.772, "lon": 23.592, "fkm": 54.0,
        "thresholds": {"lkv": -20, "low": 25, "deg1": 240, "deg2": 310, "deg3": 370, "lnv": 455},
        "default_level": 74, "default_diff24h": 4, "default_discharge": 18.6, "default_temp": 6.7, "downstream_order": 1
    },
    {
        "code": "749102", "water_category": "minor", "country": "RO",
        "name": "Beszterce (Bistrița)", "river": "Nagy-Szamos", "basin": "tisza", "catchment": "upper_tisza",
        "reach_name": "Nagy-Szamos (Someșul Mare) – Radna – Naszód – Bethlen – Dés", "lat": 47.185, "lon": 24.185, "fkm": 42.0,
        "thresholds": {"lkv": -25, "low": 20, "deg1": 260, "deg2": 330, "deg3": 400, "lnv": 490},
        "default_level": 68, "default_diff24h": 6, "default_discharge": 34.2, "default_temp": 6.4, "downstream_order": 1
    },
    {
        "code": "749103", "water_category": "minor", "country": "RO",
        "name": "Torda (Turda)", "river": "Aranyos", "basin": "tisza", "catchment": "transylvania_maros",
        "reach_name": "Aranyos (Arieș) – Topánfalva – Torda (Turda) – Aranyosgyéres (Maros)", "lat": 46.565, "lon": 23.785, "fkm": 26.0,
        "thresholds": {"lkv": -30, "low": 15, "deg1": 270, "deg2": 340, "deg3": 410, "lnv": 510},
        "default_level": 82, "default_diff24h": 9, "default_discharge": 45.5, "default_temp": 6.6, "downstream_order": 1
    },
    {
        "code": "749104", "water_category": "minor", "country": "RO",
        "name": "Dicsőszentmárton", "river": "Kis-Küküllő", "basin": "tisza", "catchment": "transylvania_maros",
        "reach_name": "Kis-Küküllő (Târnava Mică) – Szováta – Erdőszentgyörgy – Dicsőszentmárton – Balázsfalva", "lat": 46.328, "lon": 24.288, "fkm": 38.0,
        "thresholds": {"lkv": -25, "low": 18, "deg1": 250, "deg2": 310, "deg3": 370, "lnv": 460},
        "default_level": 64, "default_diff24h": 7, "default_discharge": 14.8, "default_temp": 6.9, "downstream_order": 1
    },
    {
        "code": "749105", "water_category": "minor", "country": "RO",
        "name": "Kézdivásárhely", "river": "Feketeügy", "basin": "olt_siret", "catchment": "olt_basin",
        "reach_name": "Feketeügy (Râul Negru) – Kézdivásárhely – Kovászna – Prázsmár (Olt)", "lat": 45.965, "lon": 26.085, "fkm": 24.0,
        "thresholds": {"lkv": -15, "low": 15, "deg1": 210, "deg2": 265, "deg3": 320, "lnv": 395},
        "default_level": 48, "default_diff24h": 3, "default_discharge": 6.4, "default_temp": 6.3, "downstream_order": 1
    },
    {
        "code": "749106", "water_category": "minor", "country": "RO",
        "name": "Nagyszeben (Sibiu)", "river": "Cibin", "basin": "olt_siret", "catchment": "olt_basin",
        "reach_name": "Cibin (Szeben-folyó) – Szebeni-havasok – Nagyszeben (Sibiu) –Talmacs (Olt)", "lat": 45.795, "lon": 24.162, "fkm": 22.0,
        "thresholds": {"lkv": -10, "low": 20, "deg1": 220, "deg2": 275, "deg3": 330, "lnv": 410},
        "default_level": 52, "default_diff24h": 4, "default_discharge": 11.2, "default_temp": 6.8, "downstream_order": 1
    },
    {
        "code": "749107", "water_category": "minor", "country": "RO",
        "name": "Szászsebes (Sebeș)", "river": "Sebes", "basin": "tisza", "catchment": "transylvania_maros",
        "reach_name": "Sebes (Sebeș) – Oașa-tározó – Szászsebes (Sebeș) – Maros-torkolat", "lat": 45.955, "lon": 23.568, "fkm": 14.0,
        "thresholds": {"lkv": -15, "low": 20, "deg1": 230, "deg2": 285, "deg3": 340, "lnv": 420},
        "default_level": 58, "default_diff24h": 2, "default_discharge": 16.5, "default_temp": 6.9, "downstream_order": 1
    },
    {
        "code": "749108", "water_category": "minor", "country": "RO",
        "name": "Resicabánya (Reșița)", "river": "Berzava", "basin": "duna", "catchment": "banat_temes",
        "reach_name": "Berzava (Bârzava) – Resicabánya – Boksánbánya – Gátalja – Detta", "lat": 45.308, "lon": 21.882, "fkm": 64.0,
        "thresholds": {"lkv": -20, "low": 15, "deg1": 220, "deg2": 275, "deg3": 330, "lnv": 405},
        "default_level": 49, "default_diff24h": 5, "default_discharge": 7.8, "default_temp": 7.7, "downstream_order": 1
    },
    {
        "code": "749109", "water_category": "minor", "country": "RO",
        "name": "Varadia (Oravica)", "river": "Karas", "basin": "duna", "catchment": "banat_temes",
        "reach_name": "Karas (Caraș) – Krassóvár – Varadia – Fehértemplom (Duna)", "lat": 45.082, "lon": 21.545, "fkm": 42.0,
        "thresholds": {"lkv": -15, "low": 15, "deg1": 215, "deg2": 270, "deg3": 325, "lnv": 395},
        "default_level": 44, "default_diff24h": 3, "default_discharge": 6.9, "default_temp": 7.9, "downstream_order": 1
    },
    {
        "code": "749110", "water_category": "minor", "country": "RO",
        "name": "Herkulesfürdő", "river": "Cserna", "basin": "duna", "catchment": "banat_temes",
        "reach_name": "Cserna (Cerna) – Cserna-völgy – Herkulesfürdő (Băile Herculane) – Orsova", "lat": 44.878, "lon": 22.415, "fkm": 16.0,
        "thresholds": {"lkv": -10, "low": 20, "deg1": 230, "deg2": 285, "deg3": 340, "lnv": 415},
        "default_level": 56, "default_diff24h": 4, "default_discharge": 14.2, "default_temp": 7.6, "downstream_order": 1
    },
    {
        "code": "749111", "water_category": "minor", "country": "RO",
        "name": "Bukarest (București)", "river": "Dâmbovița", "basin": "olt_siret", "catchment": "wallachia_south",
        "reach_name": "Dâmbovița – Târgoviște – Bukarest (Lacul Morii) – Budești (Argeș)", "lat": 44.428, "lon": 26.102, "fkm": 45.0,
        "thresholds": {"lkv": -15, "low": 20, "deg1": 240, "deg2": 295, "deg3": 350, "lnv": 430},
        "default_level": 62, "default_diff24h": 2, "default_discharge": 12.4, "default_temp": 8.4, "downstream_order": 1
    },
    {
        "code": "749112", "water_category": "minor", "country": "RO",
        "name": "Ploiești (Adâncata)", "river": "Prahova", "basin": "olt_siret", "catchment": "wallachia_south",
        "reach_name": "Prahova – Sinaia – Câmpina – Ploiești – Adâncata (Ialomița)", "lat": 44.782, "lon": 26.185, "fkm": 38.0,
        "thresholds": {"lkv": -20, "low": 15, "deg1": 250, "deg2": 310, "deg3": 370, "lnv": 455},
        "default_level": 58, "default_diff24h": 4, "default_discharge": 19.5, "default_temp": 8.1, "downstream_order": 1
    },
    {
        "code": "749113", "water_category": "minor", "country": "RO",
        "name": "Alexandria", "river": "Vedea", "basin": "olt_siret", "catchment": "wallachia_south",
        "reach_name": "Vedea – Roșiorii de Vede – Alexandria – Teleorman – Duna", "lat": 43.968, "lon": 25.332, "fkm": 54.0,
        "thresholds": {"lkv": -25, "low": 15, "deg1": 240, "deg2": 300, "deg3": 360, "lnv": 440},
        "default_level": 51, "default_diff24h": 3, "default_discharge": 11.8, "default_temp": 8.6, "downstream_order": 1
    },
    {
        "code": "749114", "water_category": "minor", "country": "RO",
        "name": "Ónfalva (Onești)", "river": "Tatros", "basin": "olt_siret", "catchment": "moldova_siret_prut",
        "reach_name": "Tatros (Trotuș) – Gyimes – Kománfalva – Ónfalva (Onești) – Adjud (Szeret)", "lat": 46.252, "lon": 26.775, "fkm": 36.0,
        "thresholds": {"lkv": -20, "low": 20, "deg1": 265, "deg2": 330, "deg3": 395, "lnv": 485},
        "default_level": 74, "default_diff24h": 8, "default_discharge": 31.0, "default_temp": 7.1, "downstream_order": 1
    },
    {
        "code": "749115", "water_category": "minor", "country": "RO",
        "name": "Bârlad (Vaslui)", "river": "Bârlad", "basin": "olt_siret", "catchment": "moldova_siret_prut",
        "reach_name": "Bârlad – Vaslui – Bârlad – Tecuci (Szeret)", "lat": 46.228, "lon": 27.672, "fkm": 85.0,
        "thresholds": {"lkv": -25, "low": 15, "deg1": 245, "deg2": 305, "deg3": 365, "lnv": 450},
        "default_level": 56, "default_diff24h": 4, "default_discharge": 9.6, "default_temp": 7.6, "downstream_order": 1
    },
    {
        "code": "749116", "water_category": "minor", "country": "RO",
        "name": "Suceava", "river": "Suceava", "basin": "olt_siret", "catchment": "moldova_siret_prut",
        "reach_name": "Suceava – Radóc (Rădăuți) – Suceava – Liteni (Szeret)", "lat": 47.652, "lon": 26.265, "fkm": 42.0,
        "thresholds": {"lkv": -20, "low": 20, "deg1": 260, "deg2": 325, "deg3": 390, "lnv": 480},
        "default_level": 68, "default_diff24h": 7, "default_discharge": 26.4, "default_temp": 6.8, "downstream_order": 1
    },
]
