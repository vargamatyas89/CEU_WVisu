"""
Bulgaria (BG) — Catchments and Hydrological Gauging Stations
(OVF / hydroinfo.hu 84xxxx + ИАППД / appd-bg.org live Danube data + НИМХ / hydro.bg live national river network + GloFAS v4)
Standalone country source file (42 Bulgarian stations: 28 main rivers/lakes + 14 smaller rivers and tributaries)
"""

COUNTRY_META = {
    "code": "BG",
    "name": "Bulgária (BG)",
    "flag": "🇧🇬",
    "border_color": "#fb923c",
    "bounds": [[41.23, 22.34], [44.23, 28.61]],
}

CATCHMENTS = {
    "bg_danube_north": {
        "name": "Észak-bulgáriai Duna-medence (Vidin–Rusze–Szilisztra, Iszkar, Jantra, Oszam, Vit)",
        "lat": 43.45,
        "lon": 24.85,
        "response_factor": 2.8,
        "lag_days": 2,
    },
    "bg_maritsa_thrace": {
        "name": "Trák-alföld és Rodope (Marica, Tundzsa, Arda — Plovdiv–Szvilengrad)",
        "lat": 42.15,
        "lon": 25.35,
        "response_factor": 3.3,
        "lag_days": 1,
    },
    "bg_struma_mesta_west": {
        "name": "Nyugat-Bulgária, Rila és Pirin (Sztruma, Meszta, Felső-Iszkar)",
        "lat": 42.02,
        "lon": 23.22,
        "response_factor": 3.6,
        "lag_days": 1,
    },
    "bg_black_sea_east": {
        "name": "Fekete-tengeri vízgyűjtő (Kamcsija, Provadijszka, Ropotamo, Burgaszi-tavak)",
        "lat": 42.85,
        "lon": 27.35,
        "response_factor": 3.1,
        "lag_days": 1,
    },
}

STATIONS = [
    # =========================================================================
    # 1. MAIN RIVERS AND LAKES (28 stations — live APPD, hydroinfo.hu 84xxxx & NIMH)
    # =========================================================================
    # --- LOWER DANUBE / ДУНАВ (8 live stations: Novo Selo → Silistra) ---
    {
        "code": "842070", "appd_key": "ново село", "country": "BG", "name": "Novo Szelo (Ново село)", "river": "Duna", "basin": "duna", "catchment": "bg_danube_north",
        "reach_name": "Duna (Дунав) – Timok-torkolat – Novo Szelo (fkm 833,6)", "lat": 44.162, "lon": 22.785, "fkm": 833.6,
        "thresholds": {"lkv": 30, "low": 100, "deg1": 580, "deg2": 680, "deg3": 760, "lnv": 865},
        "default_level": 182, "default_diff24h": 0, "default_discharge": 3909.0, "default_temp": 10.2,
        "downstream_order": 1
    },
    {
        "code": "BG_APPD_VIDIN", "appd_key": "видин", "country": "BG", "name": "Vidin (Видин)", "river": "Duna", "basin": "duna", "catchment": "bg_danube_north",
        "reach_name": "Duna (Дунав) – Vidin–Calafat híd – Vidin kikötő (fkm 790,3)", "lat": 43.992, "lon": 22.883, "fkm": 790.3,
        "thresholds": {"lkv": 40, "low": 120, "deg1": 650, "deg2": 750, "deg3": 840, "lnv": 979},
        "default_level": 224, "default_diff24h": 0, "default_discharge": 3950.0, "default_temp": 11.2,
        "downstream_order": 2
    },
    {
        "code": "842073", "appd_key": "лом", "country": "BG", "name": "Lom (Лом)", "river": "Duna", "basin": "duna", "catchment": "bg_danube_north",
        "reach_name": "Duna (Дунав) – Arcsar – Lom (Lom-torkolat, fkm 743,3)", "lat": 43.828, "lon": 23.237, "fkm": 743.3,
        "thresholds": {"lkv": 50, "low": 130, "deg1": 680, "deg2": 770, "deg3": 850, "lnv": 985},
        "default_level": 232, "default_diff24h": 0, "default_discharge": 3980.0, "default_temp": 11.6,
        "downstream_order": 3
    },
    {
        "code": "842075", "appd_key": "оряхово", "country": "BG", "name": "Orjahovo (Оряхово)", "river": "Duna", "basin": "duna", "catchment": "bg_danube_north",
        "reach_name": "Duna (Дунав) – Kozloduj – Ogoszta-torkolat – Orjahovo (fkm 678,0)", "lat": 43.738, "lon": 23.962, "fkm": 678.0,
        "thresholds": {"lkv": -10, "low": 60, "deg1": 560, "deg2": 650, "deg3": 730, "lnv": 855},
        "default_level": 114, "default_diff24h": 0, "default_discharge": 3175.0, "default_temp": 12.9,
        "downstream_order": 4
    },
    {
        "code": "BG_APPD_NIKOPOL", "appd_key": "никопол", "country": "BG", "name": "Nikopol (Никопол)", "river": "Duna", "basin": "duna", "catchment": "bg_danube_north",
        "reach_name": "Duna (Дунав) – Iszkar- és Vit-torkolat – Nikopol (fkm 597,5)", "lat": 43.706, "lon": 24.896, "fkm": 597.5,
        "thresholds": {"lkv": 30, "low": 100, "deg1": 600, "deg2": 690, "deg3": 770, "lnv": 890},
        "default_level": 180, "default_diff24h": 0, "default_discharge": 3886.0, "default_temp": 12.3,
        "downstream_order": 5
    },
    {
        "code": "842078", "appd_key": "свищов", "country": "BG", "name": "Szvistov (Свищов)", "river": "Duna", "basin": "duna", "catchment": "bg_danube_north",
        "reach_name": "Duna (Дунав) – Belene-sziget – Szvistov – Jantra-torkolat (fkm 554,3)", "lat": 43.621, "lon": 25.351, "fkm": 554.3,
        "thresholds": {"lkv": -10, "low": 60, "deg1": 560, "deg2": 650, "deg3": 730, "lnv": 845},
        "default_level": 108, "default_diff24h": 0, "default_discharge": 3112.0, "default_temp": 11.2,
        "downstream_order": 6
    },
    {
        "code": "842080", "appd_key": "русе", "country": "BG", "name": "Rusze (Русе)", "river": "Duna", "basin": "duna", "catchment": "bg_danube_north",
        "reach_name": "Duna (Дунав) – Rusze (Ruszenszki Lom torkolat) – Duna-híd (fkm 495,6)", "lat": 43.856, "lon": 25.955, "fkm": 495.6,
        "thresholds": {"lkv": -55, "low": 15, "deg1": 600, "deg2": 700, "deg3": 790, "lnv": 906},
        "default_level": 47, "default_diff24h": 0, "default_discharge": 2500.0, "default_temp": 12.0,
        "downstream_order": 7
    },
    {
        "code": "842083", "appd_key": "силистра", "country": "BG", "name": "Szilisztra (Силистра)", "river": "Duna", "basin": "duna", "catchment": "bg_danube_north",
        "reach_name": "Duna (Дунав) – Tutrakan – Szilisztra (román–bolgár határ, fkm 375,5)", "lat": 44.122, "lon": 27.265, "fkm": 375.5,
        "thresholds": {"lkv": -60, "low": 0, "deg1": 570, "deg2": 660, "deg3": 740, "lnv": 865},
        "default_level": 23, "default_diff24h": 0, "default_discharge": 2270.0, "default_temp": 12.0,
        "downstream_order": 8
    },

    # --- NORTH BULGARIAN DANUBE TRIBUTARIES (8 live NIMH stations) ---
    {
        "code": "BG_NIMH_16850", "nimh_id": "16850", "country": "BG", "name": "Butan (Бутан)", "river": "Ogoszta", "basin": "duna", "catchment": "bg_danube_north",
        "reach_name": "Ogoszta (Огоста) – Montana – Kobiljak – Butan – Duna-torkolat", "lat": 43.647, "lon": 23.751, "fkm": 24.0,
        "thresholds": {"lkv": 15, "low": 40, "deg1": 240, "deg2": 320, "deg3": 400, "lnv": 510},
        "default_level": 69, "default_diff24h": 0, "default_discharge": 15.2, "default_temp": 9.8,
        "downstream_order": 1
    },
    {
        "code": "BG_NIMH_18700", "nimh_id": "18700", "country": "BG", "name": "Novi Iszkar / Szófia (Нови Искър)", "river": "Iszkar", "basin": "duna", "catchment": "bg_struma_mesta_west",
        "reach_name": "Felső-Iszkar (Искър) – Szamokov – Szófiai-medence – Novi Iszkar", "lat": 42.815, "lon": 23.348, "fkm": 238.0,
        "thresholds": {"lkv": -10, "low": 15, "deg1": 210, "deg2": 290, "deg3": 370, "lnv": 480},
        "default_level": 26, "default_diff24h": 0, "default_discharge": 11.6, "default_temp": 9.1,
        "downstream_order": 1
    },
    {
        "code": "BG_NIMH_18800", "nimh_id": "18800", "country": "BG", "name": "Roman (Роман)", "river": "Iszkar", "basin": "duna", "catchment": "bg_danube_north",
        "reach_name": "Iszkar-áttörés (Искърско дефиле) – Mezdra – Roman", "lat": 43.149, "lon": 23.917, "fkm": 124.0,
        "thresholds": {"lkv": 5, "low": 30, "deg1": 260, "deg2": 340, "deg3": 420, "lnv": 530},
        "default_level": 42, "default_diff24h": 0, "default_discharge": 22.3, "default_temp": 9.6,
        "downstream_order": 2
    },
    {
        "code": "BG_NIMH_18850", "nimh_id": "18850", "country": "BG", "name": "Orehovica (Ореховица)", "river": "Iszkar", "basin": "duna", "catchment": "bg_danube_north",
        "reach_name": "Alsó-Iszkar (Искър) – Cserven Brjag – Orehovica – Gigen (Duna-torkolat)", "lat": 43.588, "lon": 24.365, "fkm": 22.0,
        "thresholds": {"lkv": 25, "low": 55, "deg1": 310, "deg2": 400, "deg3": 490, "lnv": 610},
        "default_level": 90, "default_diff24h": 0, "default_discharge": 41.9, "default_temp": 10.1,
        "downstream_order": 3
    },
    {
        "code": "BG_NIMH_21800", "nimh_id": "21800", "country": "BG", "name": "Tarnene / Pleven (Търнене)", "river": "Vit", "basin": "duna", "catchment": "bg_danube_north",
        "reach_name": "Vit (Вит) – Tetevenszki-Balkán – Pleven / Tarnene – Duna-torkolat", "lat": 43.377, "lon": 24.539, "fkm": 48.0,
        "thresholds": {"lkv": 20, "low": 45, "deg1": 240, "deg2": 320, "deg3": 400, "lnv": 500},
        "default_level": 78, "default_diff24h": 0, "default_discharge": 6.0, "default_temp": 9.8,
        "downstream_order": 1
    },
    {
        "code": "BG_NIMH_22750", "nimh_id": "22750", "country": "BG", "name": "Lovecs (Ловеч)", "river": "Oszam", "basin": "duna", "catchment": "bg_danube_north",
        "reach_name": "Oszam (Осъм) – Lovecs – Levszki – Nikopol (Duna-torkolat)", "lat": 43.137, "lon": 24.714, "fkm": 175.0,
        "thresholds": {"lkv": -5, "low": 15, "deg1": 210, "deg2": 290, "deg3": 370, "lnv": 470},
        "default_level": 26, "default_diff24h": 0, "default_discharge": 3.5, "default_temp": 9.7,
        "downstream_order": 1
    },
    {
        "code": "BG_NIMH_23700", "nimh_id": "23700", "country": "BG", "name": "Veliko Tarnovo (Велико Търново)", "river": "Jantra", "basin": "duna", "catchment": "bg_danube_north",
        "reach_name": "Felső-Jantra (Янтра) – Gabrovo – Veliko Tarnovo", "lat": 43.082, "lon": 25.635, "fkm": 146.0,
        "thresholds": {"lkv": 35, "low": 70, "deg1": 310, "deg2": 400, "deg3": 490, "lnv": 610},
        "default_level": 113, "default_diff24h": 0, "default_discharge": 3.5, "default_temp": 9.6,
        "downstream_order": 1
    },
    {
        "code": "BG_NIMH_23850", "nimh_id": "23850", "country": "BG", "name": "Karanci (Каранци)", "river": "Jantra", "basin": "duna", "catchment": "bg_danube_north",
        "reach_name": "Alsó-Jantra (Янтра) – Gorna Orjahovica – Karanci – Biala – Duna-torkolat", "lat": 43.383, "lon": 25.667, "fkm": 74.0,
        "thresholds": {"lkv": 30, "low": 65, "deg1": 330, "deg2": 420, "deg3": 510, "lnv": 640},
        "default_level": 106, "default_diff24h": 0, "default_discharge": 24.9, "default_temp": 10.0,
        "downstream_order": 2
    },

    # --- MARITSA, TUNDZHA, ARDA, STRUMA, MESTA, KAMCHIYA (10 live NIMH stations) ---
    {
        "code": "BG_NIMH_71800", "nimh_id": "71800", "country": "BG", "name": "Pazardzsik (Пазарджик)", "river": "Marica", "basin": "marica_bg", "catchment": "bg_maritsa_thrace",
        "reach_name": "Felső-Marica (Марица) – Rila – Belovo – Pazardzsik", "lat": 42.185, "lon": 24.331, "fkm": 412.0,
        "thresholds": {"lkv": -120, "low": -90, "deg1": 140, "deg2": 220, "deg3": 300, "lnv": 410},
        "default_level": -67, "default_diff24h": -2, "default_discharge": 10.4, "default_temp": 10.5,
        "downstream_order": 1
    },
    {
        "code": "BG_NIMH_72700", "nimh_id": "72700", "country": "BG", "name": "Plovdiv (Пловдив)", "river": "Marica", "basin": "marica_bg", "catchment": "bg_maritsa_thrace",
        "reach_name": "Középső-Marica (Марица) – Plovdiv – Parvomaj", "lat": 42.154, "lon": 24.748, "fkm": 374.0,
        "thresholds": {"lkv": -85, "low": -50, "deg1": 210, "deg2": 290, "deg3": 370, "lnv": 480},
        "default_level": -21, "default_diff24h": 0, "default_discharge": 29.2, "default_temp": 11.2,
        "downstream_order": 2
    },
    {
        "code": "BG_NIMH_73750", "nimh_id": "73750", "country": "BG", "name": "Harmanli (Харманли)", "river": "Marica", "basin": "marica_bg", "catchment": "bg_maritsa_thrace",
        "reach_name": "Marica (Марица) – Dimitrovgrad – Szimeonovgrad – Harmanli", "lat": 41.930, "lon": 25.902, "fkm": 252.0,
        "thresholds": {"lkv": 30, "low": 70, "deg1": 310, "deg2": 400, "deg3": 490, "lnv": 610},
        "default_level": 115, "default_diff24h": -1, "default_discharge": 33.3, "default_temp": 11.8,
        "downstream_order": 3
    },
    {
        "code": "BG_NIMH_73850", "nimh_id": "73850", "country": "BG", "name": "Szvilengrad (Свиленград)", "river": "Marica", "basin": "marica_bg", "catchment": "bg_maritsa_thrace",
        "reach_name": "Alsó-Marica (Марица) – Ljubimec – Szvilengrad (görög–török hármashatár)", "lat": 41.766, "lon": 26.202, "fkm": 218.0,
        "thresholds": {"lkv": 20, "low": 60, "deg1": 330, "deg2": 430, "deg3": 520, "lnv": 640},
        "default_level": 96, "default_diff24h": -1, "default_discharge": 44.0, "default_temp": 12.1,
        "downstream_order": 4
    },
    {
        "code": "BG_NIMH_74850", "nimh_id": "74850", "country": "BG", "name": "Elhovo (Елхово)", "river": "Tundzsa", "basin": "marica_bg", "catchment": "bg_maritsa_thrace",
        "reach_name": "Tundzsa (Тунджа) – Kazanlak – Jambol – Elhovo (török határ)", "lat": 42.172, "lon": 26.567, "fkm": 78.0,
        "thresholds": {"lkv": 15, "low": 45, "deg1": 280, "deg2": 360, "deg3": 440, "lnv": 540},
        "default_level": 73, "default_diff24h": 0, "default_discharge": 5.1, "default_temp": 11.4,
        "downstream_order": 1
    },
    {
        "code": "BG_NIMH_61700", "nimh_id": "61700", "country": "BG", "name": "Vehtino / Kardzsali (Вехтино)", "river": "Arda", "basin": "marica_bg", "catchment": "bg_maritsa_thrace",
        "reach_name": "Arda (Арда) – Rudozem – Vehtino – Kardzsali – Ivajlovgrad", "lat": 41.584, "lon": 25.121, "fkm": 176.0,
        "thresholds": {"lkv": 10, "low": 30, "deg1": 230, "deg2": 310, "deg3": 390, "lnv": 500},
        "default_level": 51, "default_diff24h": 2, "default_discharge": 7.9, "default_temp": 10.6,
        "downstream_order": 1
    },
    {
        "code": "BG_NIMH_51750", "nimh_id": "51750", "country": "BG", "name": "Bobosevo (Бобошево)", "river": "Sztruma", "basin": "marica_bg", "catchment": "bg_struma_mesta_west",
        "reach_name": "Felső-Sztruma (Струма) – Pernik – Kjusztendil – Bobosevo", "lat": 42.153, "lon": 23.001, "fkm": 225.0,
        "thresholds": {"lkv": 20, "low": 45, "deg1": 240, "deg2": 320, "deg3": 400, "lnv": 510},
        "default_level": 77, "default_diff24h": -1, "default_discharge": 6.5, "default_temp": 10.2,
        "downstream_order": 1
    },
    {
        "code": "BG_NIMH_51800", "nimh_id": "51800", "country": "BG", "name": "Kreszna (Кресненско ханче)", "river": "Sztruma", "basin": "marica_bg", "catchment": "bg_struma_mesta_west",
        "reach_name": "Alsó-Sztruma (Струма) – Blagoevgrad – Kreszna-szoros – Szandanszki – Kulata", "lat": 41.745, "lon": 23.153, "fkm": 148.0,
        "thresholds": {"lkv": 10, "low": 35, "deg1": 240, "deg2": 320, "deg3": 400, "lnv": 520},
        "default_level": 57, "default_diff24h": -8, "default_discharge": 20.4, "default_temp": 11.4,
        "downstream_order": 2
    },
    {
        "code": "BG_NIMH_52850", "nimh_id": "52850", "country": "BG", "name": "Hadzsidimovo (Хаджидимово)", "river": "Meszta", "basin": "marica_bg", "catchment": "bg_struma_mesta_west",
        "reach_name": "Meszta (Места) – Razlog – Goce Delcsev – Hadzsidimovo (görög határ)", "lat": 41.522, "lon": 23.868, "fkm": 116.0,
        "thresholds": {"lkv": 25, "low": 55, "deg1": 240, "deg2": 310, "deg3": 390, "lnv": 490},
        "default_level": 90, "default_diff24h": -10, "default_discharge": 26.9, "default_temp": 10.4,
        "downstream_order": 1
    },
    {
        "code": "BG_NIMH_43800", "nimh_id": "43800", "country": "BG", "name": "Grozdjovo (Гроздьово)", "river": "Kamcsija", "basin": "marica_bg", "catchment": "bg_black_sea_east",
        "reach_name": "Kamcsija (Камчия) – Veliki Preszlav – Grozdjovo – Fekete-tengeri torkolat", "lat": 43.028, "lon": 27.536, "fkm": 32.0,
        "thresholds": {"lkv": 15, "low": 40, "deg1": 260, "deg2": 350, "deg3": 440, "lnv": 560},
        "default_level": 74, "default_diff24h": 0, "default_discharge": 5.2, "default_temp": 11.6,
        "downstream_order": 1
    },

    # --- BULGARIAN LARGE RESERVOIR AND COASTAL LAKE (2 stations — basin="tavak") ---
    {
        "code": "BG_95001", "country": "BG", "name": "Iszkar-víztározó (Язовир Искър)", "river": "Iszkar-tó", "basin": "tavak", "catchment": "bg_struma_mesta_west",
        "reach_name": "Iszkar-víztározó (Язовир Искър) – Szófia fő ivóvízbázisa", "lat": 42.470, "lon": 23.590, "fkm": 0.0,
        "thresholds": {"lkv": 45, "low": 75, "deg1": 165, "deg2": 195, "deg3": 225, "lnv": 260},
        "default_level": 112, "default_diff24h": 0, "default_discharge": 12.0, "default_temp": 9.5,
        "transboundary_anchor": "842070", "downstream_order": 1
    },
    {
        "code": "BG_95002", "country": "BG", "name": "Burgaszi-tó (Бургаско езеро)", "river": "Burgaszi-tó", "basin": "tavak", "catchment": "bg_black_sea_east",
        "reach_name": "Burgaszi-tó (Вая / Бургаско езеро) – Fekete-tengeri lagúna", "lat": 42.502, "lon": 27.402, "fkm": 0.0,
        "thresholds": {"lkv": 30, "low": 55, "deg1": 145, "deg2": 175, "deg3": 205, "lnv": 240},
        "default_level": 88, "default_diff24h": 0, "default_discharge": 3.5, "default_temp": 12.2,
        "transboundary_anchor": "842083", "downstream_order": 1
    },

    # =========================================================================
    # 2. SMALLER RIVERS AND TRIBUTARIES (14 live NIMH stations — water_category="minor")
    # =========================================================================
    {
        "code": "BG_NIMH_14840", "nimh_id": "14840", "country": "BG", "water_category": "minor", "name": "Vaszilovci (Василовци)", "river": "Lom folyó", "basin": "duna", "catchment": "bg_danube_north",
        "reach_name": "Lom folyó (Лом) – Csiprovci – Vaszilovci – Lom (Duna-torkolat)", "lat": 43.694, "lon": 23.133, "fkm": 22.0,
        "thresholds": {"lkv": 10, "low": 30, "deg1": 210, "deg2": 280, "deg3": 350, "lnv": 440},
        "default_level": 56, "default_diff24h": 0, "default_discharge": 12.7, "default_temp": 9.8,
        "downstream_order": 1
    },
    {
        "code": "BG_NIMH_18560", "nimh_id": "18560", "country": "BG", "water_category": "minor", "name": "Szvode (Своде)", "river": "Malki Iszkar", "basin": "duna", "catchment": "bg_danube_north",
        "reach_name": "Malki Iszkar (Малки Искър) – Etropole – Szvode – Roman (Iszkar-torkolat)", "lat": 43.012, "lon": 23.866, "fkm": 16.0,
        "thresholds": {"lkv": 10, "low": 30, "deg1": 200, "deg2": 270, "deg3": 340, "lnv": 430},
        "default_level": 56, "default_diff24h": 0, "default_discharge": 10.1, "default_temp": 9.4,
        "downstream_order": 1
    },
    {
        "code": "BG_NIMH_21650", "nimh_id": "21650", "country": "BG", "water_category": "minor", "name": "Teteven (Тетевен)", "river": "Beli Vit", "basin": "duna", "catchment": "bg_danube_north",
        "reach_name": "Beli Vit (Бели Вит) – Középső-Balkán – Teteven – Vit összefolyás", "lat": 42.918, "lon": 24.259, "fkm": 145.0,
        "thresholds": {"lkv": 25, "low": 50, "deg1": 210, "deg2": 280, "deg3": 350, "lnv": 440},
        "default_level": 86, "default_diff24h": 0, "default_discharge": 2.9, "default_temp": 8.9,
        "downstream_order": 1
    },
    {
        "code": "BG_NIMH_22700", "nimh_id": "22700", "country": "BG", "water_category": "minor", "name": "Trojan (Троян)", "river": "Beli Oszam", "basin": "duna", "catchment": "bg_danube_north",
        "reach_name": "Beli Oszam (Бели Осъм) – Trojan-hágó – Trojan – Lovecs felé", "lat": 42.884, "lon": 24.716, "fkm": 265.0,
        "thresholds": {"lkv": -5, "low": 10, "deg1": 180, "deg2": 245, "deg3": 310, "lnv": 400},
        "default_level": 15, "default_diff24h": 0, "default_discharge": 3.3, "default_temp": 8.8,
        "downstream_order": 1
    },
    {
        "code": "BG_NIMH_23500", "nimh_id": "23500", "country": "BG", "water_category": "minor", "name": "Szevlievo (Севлиево)", "river": "Roszica", "basin": "duna", "catchment": "bg_danube_north",
        "reach_name": "Roszica (Росица) – Aprilci – Szevlievo – Polikraiste (Jantra-torkolat)", "lat": 43.026, "lon": 25.095, "fkm": 92.0,
        "thresholds": {"lkv": 20, "low": 45, "deg1": 240, "deg2": 320, "deg3": 400, "lnv": 510},
        "default_level": 80, "default_diff24h": 0, "default_discharge": 3.6, "default_temp": 9.5,
        "downstream_order": 1
    },
    {
        "code": "BG_NIMH_31830", "nimh_id": "31830", "country": "BG", "water_category": "minor", "name": "Bozsicsen (Божичен)", "river": "Ruszenszki Lom", "basin": "duna", "catchment": "bg_danube_north",
        "reach_name": "Ruszenszki Lom (Русенски Лом) – Ivanovo – Bozsicsen – Rusze (Duna)", "lat": 43.719, "lon": 25.959, "fkm": 22.0,
        "thresholds": {"lkv": 60, "low": 100, "deg1": 310, "deg2": 390, "deg3": 470, "lnv": 570},
        "default_level": 164, "default_diff24h": 0, "default_discharge": 2.6, "default_temp": 10.2,
        "downstream_order": 1
    },
    {
        "code": "BG_NIMH_42850", "nimh_id": "42850", "country": "BG", "water_category": "minor", "name": "Szindel (гара Синдел)", "river": "Provadijszka", "basin": "marica_bg", "catchment": "bg_black_sea_east",
        "reach_name": "Provadijszka (Провадийска река) – Provadija – Szindel – Várnai-tó", "lat": 43.118, "lon": 27.599, "fkm": 28.0,
        "thresholds": {"lkv": 60, "low": 105, "deg1": 310, "deg2": 390, "deg3": 470, "lnv": 560},
        "default_level": 166, "default_diff24h": 0, "default_discharge": 0.5, "default_temp": 11.4,
        "downstream_order": 1
    },
    {
        "code": "BG_NIMH_43500", "nimh_id": "43500", "country": "BG", "water_category": "minor", "name": "Beronovo (Бероново)", "river": "Luda Kamcsija", "basin": "marica_bg", "catchment": "bg_black_sea_east",
        "reach_name": "Luda Kamcsija (Луда Камчия) – Kotel – Beronovo – Conevo-tó (Kamcsija)", "lat": 42.839, "lon": 26.688, "fkm": 112.0,
        "thresholds": {"lkv": 30, "low": 60, "deg1": 260, "deg2": 340, "deg3": 420, "lnv": 520},
        "default_level": 102, "default_diff24h": 0, "default_discharge": 0.6, "default_temp": 10.4,
        "downstream_order": 1
    },
    {
        "code": "BG_NIMH_82850", "nimh_id": "82850", "country": "BG", "water_category": "minor", "name": "Zidarovo (Зидарово)", "river": "Fakijszka", "basin": "marica_bg", "catchment": "bg_black_sea_east",
        "reach_name": "Fakijszka (Факийска река) – Sztrandzsa – Zidarovo – Mandrenszko-tó", "lat": 42.345, "lon": 27.402, "fkm": 18.0,
        "thresholds": {"lkv": 15, "low": 35, "deg1": 210, "deg2": 280, "deg3": 350, "lnv": 440},
        "default_level": 64, "default_diff24h": 0, "default_discharge": 0.2, "default_temp": 11.8,
        "downstream_order": 1
    },
    {
        "code": "BG_NIMH_83620", "nimh_id": "83620", "country": "BG", "water_category": "minor", "name": "Veszelie (Веселие)", "river": "Ropotamo", "basin": "marica_bg", "catchment": "bg_black_sea_east",
        "reach_name": "Ropotamo (Ропотамо) – Veszelie – Primorszko (Fekete-tenger)", "lat": 42.328, "lon": 27.624, "fkm": 12.0,
        "thresholds": {"lkv": 20, "low": 45, "deg1": 220, "deg2": 290, "deg3": 360, "lnv": 450},
        "default_level": 84, "default_diff24h": 0, "default_discharge": 0.3, "default_temp": 12.1,
        "downstream_order": 1
    },
    {
        "code": "BG_NIMH_71480", "nimh_id": "71480", "country": "BG", "water_category": "minor", "name": "Poibrene (Поибрене)", "river": "Topolnica", "basin": "marica_bg", "catchment": "bg_maritsa_thrace",
        "reach_name": "Topolnica (Тополница) – Koprivstica – Poibrene – Pazardzsik (Marica)", "lat": 42.495, "lon": 24.000, "fkm": 78.0,
        "thresholds": {"lkv": 5, "low": 20, "deg1": 190, "deg2": 260, "deg3": 330, "lnv": 420},
        "default_level": 35, "default_diff24h": -1, "default_discharge": 1.0, "default_temp": 9.8,
        "downstream_order": 1
    },
    {
        "code": "BG_NIMH_72340", "nimh_id": "72340", "country": "BG", "water_category": "minor", "name": "Devin (Девин)", "river": "Vacsa", "basin": "marica_bg", "catchment": "bg_maritsa_thrace",
        "reach_name": "Vacsa (Въча) – Nyugati-Rodope – Devin – Kricsim – Marica-torkolat", "lat": 41.744, "lon": 24.400, "fkm": 72.0,
        "thresholds": {"lkv": 30, "low": 60, "deg1": 240, "deg2": 310, "deg3": 380, "lnv": 470},
        "default_level": 97, "default_diff24h": 0, "default_discharge": 4.3, "default_temp": 9.1,
        "downstream_order": 1
    },
    {
        "code": "BG_NIMH_73480", "nimh_id": "73480", "country": "BG", "water_category": "minor", "name": "Galabovo (Гълъбово)", "river": "Szazlijka", "basin": "marica_bg", "catchment": "bg_maritsa_thrace",
        "reach_name": "Szazlijka (Сазлийка) – Sztara Zagora – Radnevo – Galabovo – Marica", "lat": 42.142, "lon": 25.862, "fkm": 24.0,
        "thresholds": {"lkv": 30, "low": 60, "deg1": 260, "deg2": 340, "deg3": 420, "lnv": 520},
        "default_level": 101, "default_diff24h": -2, "default_discharge": 3.7, "default_temp": 11.2,
        "downstream_order": 1
    },
    {
        "code": "BG_NIMH_51430", "nimh_id": "51430", "country": "BG", "water_category": "minor", "name": "Dupnica (Дупница)", "river": "Dzserman", "basin": "marica_bg", "catchment": "bg_struma_mesta_west",
        "reach_name": "Dzserman (Джерман) – Rila – Szapareva Banja – Dupnica – Sztruma-torkolat", "lat": 42.266, "lon": 23.118, "fkm": 26.0,
        "thresholds": {"lkv": 5, "low": 20, "deg1": 180, "deg2": 245, "deg3": 310, "lnv": 395},
        "default_level": 32, "default_diff24h": -6, "default_discharge": 2.1, "default_temp": 9.6,
        "downstream_order": 1
    },
]
