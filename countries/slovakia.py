"""
Slovakia (SK) — Catchments and Official Hydrological Gauging Stations (SHMÚ / OVF hydroinfo.hu 14xxxx & GloFAS v4)
Standalone country source file (45 Slovak gauges: main rivers, reservoirs and Carpathian smaller waters)
"""

COUNTRY_META = {
    "code": "SK",
    "name": "Szlovákia",
    "flag": "🇸🇰",
    "border_color": "#22d3ee",
    "bounds": [[47.73, 16.83], [49.62, 22.57]],
}

CATCHMENTS = {
    "sk_danube_morava": {"name": "Pozsonyi-medence, Csallóköz és Morva-vidék (SK)", "lat": 48.14, "lon": 17.11, "response_factor": 2.6, "lag_days": 2},
    "sk_vah_nitra": {"name": "Vág, Árva és Nyitra vízgyűjtő (Nyugat-Kárpátok, SK)", "lat": 48.95, "lon": 18.65, "response_factor": 3.6, "lag_days": 1},
    "sk_hron_ipel": {"name": "Garam és Ipoly vízgyűjtő (Közép-Szlovákia, SK)", "lat": 48.55, "lon": 19.15, "response_factor": 3.5, "lag_days": 1},
    "sk_east_bodrog_hornad": {"name": "Kelet-Szlovákia (Hernád, Sajó, Bodrog, Laborc, Ung, SK)", "lat": 48.72, "lon": 21.25, "response_factor": 3.8, "lag_days": 1},
}

STATIONS = [
    # =========================================================================
    # 1. MAIN RIVERS AND RESERVOIRS (27 stations — live 14xxxx SHMÚ / hydroinfo.hu)
    # =========================================================================
    # --- DANUBE AND MORAVA (8 stations) ---
    {
        "code": "142301", "country": "SK", "name": "Dévény (Devín)", "river": "Duna", "basin": "duna", "catchment": "sk_danube_morava",
        "reach_name": "Duna – Dévényi-kapu (Morva-torkolat – Dévény / Devín)", "lat": 48.173, "lon": 16.978, "fkm": 1879.8,
        "thresholds": {"lkv": 40, "low": 100, "deg1": 650, "deg2": 750, "deg3": 850, "lnv": 994},
        "default_level": 134, "default_diff24h": 12, "default_discharge": 1180, "default_temp": 7.5, "downstream_order": 1
    },
    {
        "code": "142302", "country": "SK", "name": "Pozsony (Bratislava)", "river": "Duna", "basin": "duna", "catchment": "sk_danube_morava",
        "reach_name": "Duna – Pozsonyi fővárosi szakasz (Pozsony / Bratislava)", "lat": 48.138, "lon": 17.108, "fkm": 1868.8,
        "thresholds": {"lkv": 180, "low": 240, "deg1": 650, "deg2": 750, "deg3": 850, "lnv": 1034},
        "default_level": 292, "default_diff24h": 8, "default_discharge": 1220, "default_temp": 7.6, "downstream_order": 2
    },
    {
        "code": "142304", "country": "SK", "name": "Bős (Gabčíkovo)", "river": "Duna", "basin": "duna", "catchment": "sk_danube_morava",
        "reach_name": "Duna – Csallóközi-felvízcsatorna és Bősi vízlépcső (Gabčíkovo)", "lat": 47.882, "lon": 17.538, "fkm": 1819.0,
        "thresholds": {"lkv": 20, "low": 60, "deg1": 520, "deg2": 600, "deg3": 680, "lnv": 810},
        "default_level": 95, "default_diff24h": 0, "default_discharge": 1190, "default_temp": 7.7, "downstream_order": 3
    },
    {
        "code": "142306", "country": "SK", "name": "Medve (Medveďov)", "river": "Duna", "basin": "duna", "catchment": "sk_danube_morava",
        "reach_name": "Duna – Medve (Medveďov) – Vámosszabadi határszakasz", "lat": 47.795, "lon": 17.658, "fkm": 1806.3,
        "thresholds": {"lkv": -30, "low": 25, "deg1": 550, "deg2": 650, "deg3": 750, "lnv": 949},
        "default_level": 55, "default_diff24h": -12, "default_discharge": 1310, "default_temp": 7.8, "downstream_order": 4
    },
    {
        "code": "142308", "country": "SK", "name": "Révkomárom (Komárno)", "river": "Duna", "basin": "duna", "catchment": "sk_danube_morava",
        "reach_name": "Duna – Vág-torkolat – Révkomárom (Komárno)", "lat": 47.752, "lon": 18.128, "fkm": 1767.8,
        "thresholds": {"lkv": 5, "low": 55, "deg1": 550, "deg2": 640, "deg3": 720, "lnv": 890},
        "default_level": 94, "default_diff24h": -1, "default_discharge": 1415, "default_temp": 7.9, "downstream_order": 5
    },
    {
        "code": "142310", "country": "SK", "name": "Párkány (Štúrovo)", "river": "Duna", "basin": "duna", "catchment": "sk_hron_ipel",
        "reach_name": "Duna – Párkány (Štúrovo) – Garam- és Ipoly-torkolat", "lat": 47.798, "lon": 18.725, "fkm": 1718.8,
        "thresholds": {"lkv": -60, "low": 0, "deg1": 500, "deg2": 580, "deg3": 650, "lnv": 815},
        "default_level": 34, "default_diff24h": 1, "default_discharge": 1490, "default_temp": 8.0, "downstream_order": 6
    },
    {
        "code": "142132", "country": "SK", "name": "Morvaszentjános", "river": "Morva", "basin": "duna", "catchment": "sk_danube_morava",
        "reach_name": "Morva (Morava) – Morvaszentjános (Moravský Svätý Ján)", "lat": 48.588, "lon": 16.942, "fkm": 67.2,
        "thresholds": {"lkv": 45, "low": 95, "deg1": 420, "deg2": 490, "deg3": 550, "lnv": 635},
        "default_level": 160, "default_diff24h": -6, "default_discharge": 62.0, "default_temp": 7.2, "downstream_order": 1
    },
    {
        "code": "142134", "country": "SK", "name": "Magyarfalu (Záhorská Ves)", "river": "Morva", "basin": "duna", "catchment": "sk_danube_morava",
        "reach_name": "Morva (Morava) – Magyarfalu (Záhorská Ves) – Dévény", "lat": 48.382, "lon": 16.842, "fkm": 32.5,
        "thresholds": {"lkv": -10, "low": 35, "deg1": 400, "deg2": 470, "deg3": 530, "lnv": 618},
        "default_level": 62, "default_diff24h": 14, "default_discharge": 68.0, "default_temp": 7.3, "downstream_order": 2
    },

    # --- VÁH, NITRA, HRON AND IPEĽ (10 stations) ---
    {
        "code": "142406", "country": "SK", "name": "Liptószentmiklós", "river": "Vág", "basin": "duna", "catchment": "sk_vah_nitra",
        "reach_name": "Vág (Váh) – Liptói-medence (Liptóújvár – Liptószentmiklós / Liptovský Mikuláš)", "lat": 49.085, "lon": 19.612, "fkm": 342.0,
        "thresholds": {"lkv": 40, "low": 75, "deg1": 240, "deg2": 300, "deg3": 360, "lnv": 445},
        "default_level": 109, "default_diff24h": 0, "default_discharge": 28.0, "default_temp": 5.8, "downstream_order": 1
    },
    {
        "code": "142444", "country": "SK", "name": "Sztrecsény (Strečno)", "river": "Vág", "basin": "duna", "catchment": "sk_vah_nitra",
        "reach_name": "Vág (Váh) – Rózsahegy – Árva-torkolat – Sztrecsény (Strečno) – Zsolna", "lat": 49.175, "lon": 18.862, "fkm": 265.0,
        "thresholds": {"lkv": 10, "low": 40, "deg1": 310, "deg2": 380, "deg3": 450, "lnv": 560},
        "default_level": 61, "default_diff24h": 2, "default_discharge": 84.0, "default_temp": 6.3, "downstream_order": 2
    },
    {
        "code": "142479", "country": "SK", "name": "Vágsellye (Šaľa)", "river": "Vág", "basin": "duna", "catchment": "sk_vah_nitra",
        "reach_name": "Vág (Váh) – Trencsén – Pöstyén – Szered – Vágsellye (Šaľa)", "lat": 48.152, "lon": 17.878, "fkm": 48.5,
        "thresholds": {"lkv": 30, "low": 80, "deg1": 420, "deg2": 500, "deg3": 580, "lnv": 710},
        "default_level": 132, "default_diff24h": 2, "default_discharge": 135.0, "default_temp": 7.1, "downstream_order": 3
    },
    {
        "code": "142481", "country": "SK", "name": "Gúta (Kolárovo)", "river": "Vág", "basin": "duna", "catchment": "sk_vah_nitra",
        "reach_name": "Vág (Váh) és Kis-Duna torkolat – Gúta (Kolárovo) – Révkomárom", "lat": 47.918, "lon": 17.995, "fkm": 22.0,
        "thresholds": {"lkv": 25, "low": 75, "deg1": 450, "deg2": 540, "deg3": 620, "lnv": 765},
        "default_level": 135, "default_diff24h": 35, "default_discharge": 152.0, "default_temp": 7.4, "downstream_order": 4
    },
    {
        "code": "142494", "country": "SK", "name": "Nyitraszerdahely", "river": "Nyitra", "basin": "duna", "catchment": "sk_vah_nitra",
        "reach_name": "Nyitra (Nitra) – Simony – Nagytapolcsány – Nyitraszerdahely", "lat": 48.522, "lon": 18.175, "fkm": 98.0,
        "thresholds": {"lkv": 5, "low": 30, "deg1": 280, "deg2": 340, "deg3": 400, "lnv": 485},
        "default_level": 46, "default_diff24h": -4, "default_discharge": 14.5, "default_temp": 6.9, "downstream_order": 1
    },
    {
        "code": "142498", "country": "SK", "name": "Érsekújvár (Nové Zámky)", "river": "Nyitra", "basin": "duna", "catchment": "sk_vah_nitra",
        "reach_name": "Nyitra (Nitra) – Nyitra – Érsekújvár (Nové Zámky) – Komárom", "lat": 47.988, "lon": 18.165, "fkm": 26.0,
        "thresholds": {"lkv": 60, "low": 120, "deg1": 410, "deg2": 480, "deg3": 550, "lnv": 665},
        "default_level": 195, "default_diff24h": -8, "default_discharge": 22.0, "default_temp": 7.3, "downstream_order": 2
    },
    {
        "code": "142516", "country": "SK", "name": "Besztercebánya", "river": "Garam", "basin": "duna", "catchment": "sk_hron_ipel",
        "reach_name": "Garam (Hron) – Breznóbánya – Besztercebánya (Banská Bystrica) – Zólyom", "lat": 48.735, "lon": 19.145, "fkm": 178.0,
        "thresholds": {"lkv": 35, "low": 70, "deg1": 290, "deg2": 350, "deg3": 410, "lnv": 505},
        "default_level": 101, "default_diff24h": -9, "default_discharge": 28.5, "default_temp": 6.4, "downstream_order": 1
    },
    {
        "code": "142521", "country": "SK", "name": "Garamszentkereszt", "river": "Garam", "basin": "duna", "catchment": "sk_hron_ipel",
        "reach_name": "Garam (Hron) – Garamszentkereszt (Žiar nad Hronom) – Újbánya – Léva", "lat": 48.582, "lon": 18.855, "fkm": 132.0,
        "thresholds": {"lkv": 40, "low": 80, "deg1": 330, "deg2": 400, "deg3": 470, "lnv": 580},
        "default_level": 119, "default_diff24h": -5, "default_discharge": 38.0, "default_temp": 6.7, "downstream_order": 2
    },
    {
        "code": "142538", "country": "SK", "name": "Kéménd (Kamenín)", "river": "Garam", "basin": "duna", "catchment": "sk_hron_ipel",
        "reach_name": "Garam (Hron) – Alsó-Garam (Zselíz – Kéménd / Kamenín – Párkány)", "lat": 47.888, "lon": 18.645, "fkm": 16.5,
        "thresholds": {"lkv": 30, "low": 75, "deg1": 380, "deg2": 450, "deg3": 520, "lnv": 635},
        "default_level": 114, "default_diff24h": -3, "default_discharge": 48.0, "default_temp": 7.2, "downstream_order": 3
    },
    {
        "code": "142622", "country": "SK", "name": "Szalka (Salka)", "river": "Ipoly", "basin": "duna", "catchment": "sk_hron_ipel",
        "reach_name": "Ipoly (Ipeľ) – Ipolyság – Szalka (Salka) – Szob", "lat": 47.888, "lon": 18.758, "fkm": 12.2,
        "thresholds": {"lkv": 15, "low": 55, "deg1": 340, "deg2": 410, "deg3": 480, "lnv": 575},
        "default_level": 84, "default_diff24h": 10, "default_discharge": 17.5, "default_temp": 7.0, "downstream_order": 1
    },

    # --- EASTERN SLOVAKIA (Tisza basin: Hornád, Slaná, Bodrog, Latorica, Laborec, Uh — 6 stations) ---
    {
        "code": "144318", "country": "SK", "name": "Sároskőszeg (Kysak)", "river": "Hernád", "basin": "tisza", "catchment": "sk_east_bodrog_hornad",
        "reach_name": "Hernád (Hornád) – Igló – Sároskőszeg (Kysak) – Kassa (Košice) – Hernádzsadány", "lat": 48.852, "lon": 21.222, "fkm": 82.0,
        "thresholds": {"lkv": 40, "low": 80, "deg1": 310, "deg2": 380, "deg3": 450, "lnv": 560},
        "default_level": 117, "default_diff24h": 3, "default_discharge": 24.0, "default_temp": 6.5, "downstream_order": 1
    },
    {
        "code": "144204", "country": "SK", "name": "Rozsnyó (Rožňava)", "river": "Sajó", "basin": "tisza", "catchment": "sk_east_bodrog_hornad",
        "reach_name": "Sajó (Slaná) – Dobsina – Rozsnyó (Rožňava) – Pelsőc – Tornalja", "lat": 48.652, "lon": 20.532, "fkm": 112.0,
        "thresholds": {"lkv": -10, "low": 15, "deg1": 210, "deg2": 265, "deg3": 320, "lnv": 395},
        "default_level": 32, "default_diff24h": 4, "default_discharge": 11.5, "default_temp": 6.4, "downstream_order": 1
    },
    {
        "code": "144140", "country": "SK", "name": "Bodrogszerdahely", "river": "Bodrog", "basin": "tisza", "catchment": "sk_east_bodrog_hornad",
        "reach_name": "Bodrog – Latorca–Ondava egyesülése – Bodrogszerdahely (Streda nad Bodrogom)", "lat": 48.378, "lon": 21.765, "fkm": 55.2,
        "thresholds": {"lkv": 140, "low": 230, "deg1": 650, "deg2": 750, "deg3": 850, "lnv": 995},
        "default_level": 443, "default_diff24h": 14, "default_discharge": 92.0, "default_temp": 7.0, "downstream_order": 1
    },
    {
        "code": "144101", "country": "SK", "name": "Nagykapos", "river": "Latorca", "basin": "tisza", "catchment": "sk_east_bodrog_hornad",
        "reach_name": "Latorca (Latorica) – Кіralyhelmec – Nagykapos (Veľké Kapušany) – Zemplén", "lat": 48.515, "lon": 22.065, "fkm": 28.4,
        "thresholds": {"lkv": 150, "low": 240, "deg1": 580, "deg2": 660, "deg3": 740, "lnv": 865},
        "default_level": 441, "default_diff24h": 8, "default_discharge": 48.0, "default_temp": 6.9, "downstream_order": 1
    },
    {
        "code": "144116", "country": "SK", "name": "Nagymihály (Michalovce)", "river": "Laborc", "basin": "tisza", "catchment": "sk_east_bodrog_hornad",
        "reach_name": "Laborc (Laborec) – Homonna – Nagymihály (Michalovce) – Iske", "lat": 48.752, "lon": 21.915, "fkm": 42.0,
        "thresholds": {"lkv": 50, "low": 105, "deg1": 350, "deg2": 420, "deg3": 490, "lnv": 595},
        "default_level": 177, "default_diff24h": 16, "default_discharge": 26.0, "default_temp": 6.8, "downstream_order": 1
    },
    {
        "code": "144120", "country": "SK", "name": "Lakárd (Lekárovce)", "river": "Ung", "basin": "tisza", "catchment": "sk_east_bodrog_hornad",
        "reach_name": "Ung (Uh) – Ungvár – Lakárd (Lekárovce) – Laborc-torkolat", "lat": 48.608, "lon": 22.158, "fkm": 19.5,
        "thresholds": {"lkv": 80, "low": 150, "deg1": 560, "deg2": 660, "deg3": 760, "lnv": 910},
        "default_level": 243, "default_diff24h": 43, "default_discharge": 39.0, "default_temp": 6.8, "downstream_order": 1
    },

    # --- SLOVAK LARGE RESERVOIRS / LAKES (3 stations) ---
    {
        "code": "142427", "country": "SK", "name": "Turdossin (Tvrdošín)", "river": "Árvai-víztározó", "basin": "tavak", "catchment": "sk_vah_nitra",
        "reach_name": "Árvai-víztározó (Oravská priehrada – Námesztó – Turdossin)", "lat": 49.385, "lon": 19.545, "fkm": 0.0,
        "thresholds": {"lkv": 120, "low": 210, "deg1": 480, "deg2": 540, "deg3": 600, "lnv": 680},
        "default_level": 335, "default_diff24h": 1, "default_discharge": 22.0, "default_temp": 6.1, "downstream_order": 1
    },
    {
        "code": "149001", "country": "SK", "name": "Szentmária (Liptovská Mara)", "river": "Szentmáriai-víztározó", "basin": "tavak", "catchment": "sk_vah_nitra",
        "reach_name": "Szentmáriai-víztározó (Liptovská Mara – Liptószentmiklós)", "lat": 49.098, "lon": 19.488, "fkm": 0.0,
        "thresholds": {"lkv": 150, "low": 240, "deg1": 520, "deg2": 580, "deg3": 640, "lnv": 715},
        "default_level": 372, "default_diff24h": 2, "default_discharge": 31.0, "default_temp": 6.2, "downstream_order": 1
    },
    {
        "code": "149002", "country": "SK", "name": "Kaluža (Nagymihály)", "river": "Széles-tó (Zemplínska šírava)", "basin": "tavak", "catchment": "sk_east_bodrog_hornad",
        "reach_name": "Széles-tó (Zemplínska šírava – Vihorlát – Nagymihály)", "lat": 48.788, "lon": 22.015, "fkm": 0.0,
        "thresholds": {"lkv": 80, "low": 160, "deg1": 410, "deg2": 460, "deg3": 510, "lnv": 575},
        "default_level": 265, "default_diff24h": 3, "default_discharge": 14.0, "default_temp": 7.1, "downstream_order": 1
    },

    # =========================================================================
    # 2. SMALLER WATERS, CARPATHIAN STREAMS AND TRIBUTARIES (18 live 14xxxx stations)
    # =========================================================================
    {
        "code": "142405", "water_category": "minor", "country": "SK",
        "name": "Liptóújvár (Liptovský Hrádok)", "river": "Béla-patak", "basin": "duna", "catchment": "sk_vah_nitra",
        "reach_name": "Béla-patak (Belá) – Magas-Tátra – Podbanszkó – Liptóújvár (Vág)", "lat": 49.042, "lon": 19.725, "fkm": 3.5,
        "thresholds": {"lkv": 50, "low": 80, "deg1": 210, "deg2": 260, "deg3": 310, "lnv": 385},
        "default_level": 117, "default_diff24h": 0, "default_discharge": 7.5, "default_temp": 5.2, "downstream_order": 1
    },
    {
        "code": "142434", "water_category": "minor", "country": "SK",
        "name": "Dierová (Kralován)", "river": "Árva", "basin": "duna", "catchment": "sk_vah_nitra",
        "reach_name": "Árva (Orava) – Alsókubin (Dolný Kubín) – Dierová – Kralován (Vág)", "lat": 49.162, "lon": 19.148, "fkm": 6.2,
        "thresholds": {"lkv": 55, "low": 85, "deg1": 250, "deg2": 310, "deg3": 370, "lnv": 455},
        "default_level": 123, "default_diff24h": -1, "default_discharge": 26.0, "default_temp": 6.0, "downstream_order": 1
    },
    {
        "code": "142440", "water_category": "minor", "country": "SK",
        "name": "Túrócszentmárton (Martin)", "river": "Túróc", "basin": "duna", "catchment": "sk_vah_nitra",
        "reach_name": "Túróc (Turiec) – Stubnyafürdő – Túrócszentmárton (Martin) – Ruttka", "lat": 49.068, "lon": 18.918, "fkm": 10.5,
        "thresholds": {"lkv": 45, "low": 75, "deg1": 220, "deg2": 270, "deg3": 320, "lnv": 395},
        "default_level": 108, "default_diff24h": 4, "default_discharge": 12.0, "default_temp": 6.1, "downstream_order": 1
    },
    {
        "code": "142451", "water_category": "minor", "country": "SK",
        "name": "Kiszucaújhely", "river": "Kiszuca", "basin": "duna", "catchment": "sk_vah_nitra",
        "reach_name": "Kiszuca (Kysuca) – Csáca (Čadca) – Kiszucaújhely – Zsolna", "lat": 49.298, "lon": 18.785, "fkm": 8.4,
        "thresholds": {"lkv": 70, "low": 115, "deg1": 310, "deg2": 370, "deg3": 430, "lnv": 515},
        "default_level": 159, "default_diff24h": -6, "default_discharge": 16.5, "default_temp": 6.2, "downstream_order": 1
    },
    {
        "code": "142453", "water_category": "minor", "country": "SK",
        "name": "Szentistvánpatak (Bytčica)", "river": "Rajcsánka", "basin": "duna", "catchment": "sk_vah_nitra",
        "reach_name": "Rajcsánka (Rajčanka) – Rajecfürdő – Zsolna (Žilina)", "lat": 49.188, "lon": 18.725, "fkm": 4.8,
        "thresholds": {"lkv": 55, "low": 85, "deg1": 210, "deg2": 255, "deg3": 300, "lnv": 365},
        "default_level": 119, "default_diff24h": 4, "default_discharge": 5.8, "default_temp": 6.3, "downstream_order": 1
    },
    {
        "code": "142492", "water_category": "minor", "country": "SK",
        "name": "Nadlány (Nadlice)", "river": "Bebrava", "basin": "duna", "catchment": "sk_vah_nitra",
        "reach_name": "Bebrava – Bán (Bánovce nad Bebravou) – Nadlány – Simony (Nyitra)", "lat": 48.642, "lon": 18.238, "fkm": 9.2,
        "thresholds": {"lkv": 5, "low": 20, "deg1": 185, "deg2": 230, "deg3": 275, "lnv": 335},
        "default_level": 35, "default_diff24h": -2, "default_discharge": 4.2, "default_temp": 6.8, "downstream_order": 1
    },
    {
        "code": "142497", "water_category": "minor", "country": "SK",
        "name": "Barskisfalud (Vieska)", "river": "Zsitva", "basin": "duna", "catchment": "sk_vah_nitra",
        "reach_name": "Zsitva (Žitava) – Aranyosmarót – Verebély – Ógyalla", "lat": 48.318, "lon": 18.352, "fkm": 42.0,
        "thresholds": {"lkv": 60, "low": 105, "deg1": 280, "deg2": 335, "deg3": 390, "lnv": 465},
        "default_level": 154, "default_diff24h": -10, "default_discharge": 5.1, "default_temp": 7.1, "downstream_order": 1
    },
    {
        "code": "142518", "water_category": "minor", "country": "SK",
        "name": "Zólyom (Zvolen)", "river": "Szalatna", "basin": "duna", "catchment": "sk_hron_ipel",
        "reach_name": "Szalatna (Slatina) – Gyetva (Detva) – Zólyom (Zvolen – Garam)", "lat": 48.572, "lon": 19.145, "fkm": 4.5,
        "thresholds": {"lkv": 5, "low": 22, "deg1": 195, "deg2": 245, "deg3": 295, "lnv": 360},
        "default_level": 39, "default_diff24h": -9, "default_discharge": 6.4, "default_temp": 6.6, "downstream_order": 1
    },
    {
        "code": "142604", "water_category": "minor", "country": "SK",
        "name": "Ipolygalsa (Holiša)", "river": "Ipoly", "basin": "duna", "catchment": "sk_hron_ipel",
        "reach_name": "Felső-Ipoly (Ipeľ) – Poltár – Losonc – Ipolygalsa (Holiša) – Fülek", "lat": 48.302, "lon": 19.742, "fkm": 162.0,
        "thresholds": {"lkv": -10, "low": 10, "deg1": 190, "deg2": 240, "deg3": 290, "lnv": 355},
        "default_level": 21, "default_diff24h": -1, "default_discharge": 3.8, "default_temp": 6.7, "downstream_order": 1
    },
    {
        "code": "144206", "water_category": "minor", "country": "SK",
        "name": "Csetnek (Štítnik)", "river": "Csetnek-patak", "basin": "tisza", "catchment": "sk_east_bodrog_hornad",
        "reach_name": "Csetnek-patak (Štítnik) – Gömör – Csetnek – Pelsőc (Sajó)", "lat": 48.658, "lon": 20.365, "fkm": 14.0,
        "thresholds": {"lkv": 5, "low": 22, "deg1": 175, "deg2": 215, "deg3": 255, "lnv": 310},
        "default_level": 39, "default_diff24h": -5, "default_discharge": 2.9, "default_temp": 6.5, "downstream_order": 1
    },
    {
        "code": "144219", "water_category": "minor", "country": "SK",
        "name": "Rimaszombat", "river": "Rima", "basin": "tisza", "catchment": "sk_east_bodrog_hornad",
        "reach_name": "Rima (Rimava) – Tiszolc – Nyustya – Rimaszombat – Feled – Sajó", "lat": 48.382, "lon": 20.018, "fkm": 32.0,
        "thresholds": {"lkv": 10, "low": 32, "deg1": 220, "deg2": 275, "deg3": 330, "lnv": 410},
        "default_level": 54, "default_diff24h": -5, "default_discharge": 7.4, "default_temp": 6.8, "downstream_order": 1
    },
    {
        "code": "144224", "water_category": "minor", "country": "SK",
        "name": "Torna (Turňa nad Bodvou)", "river": "Bódva", "basin": "tisza", "catchment": "sk_east_bodrog_hornad",
        "reach_name": "Felső-Bódva (Bodva) – Mecenzéf – Szepsi – Torna – Hidvégardó", "lat": 48.598, "lon": 20.878, "fkm": 62.0,
        "thresholds": {"lkv": 25, "low": 50, "deg1": 210, "deg2": 255, "deg3": 300, "lnv": 365},
        "default_level": 79, "default_diff24h": 1, "default_discharge": 4.6, "default_temp": 6.5, "downstream_order": 1
    },
    {
        "code": "144310", "water_category": "minor", "country": "SK",
        "name": "Jekelfalva (Jaklovce)", "river": "Gölnic", "basin": "tisza", "catchment": "sk_east_bodrog_hornad",
        "reach_name": "Gölnic (Hnilec) – Sztracena – Svedlér – Gölnicbánya – Jekelfalva (Hernád)", "lat": 48.872, "lon": 20.992, "fkm": 6.5,
        "thresholds": {"lkv": 75, "low": 115, "deg1": 270, "deg2": 325, "deg3": 380, "lnv": 455},
        "default_level": 159, "default_diff24h": 3, "default_discharge": 9.2, "default_temp": 6.2, "downstream_order": 1
    },
    {
        "code": "144321", "water_category": "minor", "country": "SK",
        "name": "Eperjes (Prešov)", "river": "Tarca", "basin": "tisza", "catchment": "sk_east_bodrog_hornad",
        "reach_name": "Tarca (Torysa) – Héthárs – Kisszeben – Eperjes (Prešov) – Kassa (Hernád)", "lat": 48.995, "lon": 21.238, "fkm": 52.0,
        "thresholds": {"lkv": 40, "low": 75, "deg1": 260, "deg2": 320, "deg3": 380, "lnv": 465},
        "default_level": 109, "default_diff24h": 1, "default_discharge": 11.8, "default_temp": 6.4, "downstream_order": 1
    },
    {
        "code": "144128", "water_category": "minor", "country": "SK",
        "name": "Sztropkó (Stropkov)", "river": "Ondava", "basin": "tisza", "catchment": "sk_east_bodrog_hornad",
        "reach_name": "Ondava – Felsővízköz – Sztropkó – Varannó – Hór (Bodrog)", "lat": 49.205, "lon": 21.652, "fkm": 88.0,
        "thresholds": {"lkv": 20, "low": 48, "deg1": 230, "deg2": 285, "deg3": 340, "lnv": 415},
        "default_level": 73, "default_diff24h": -1, "default_discharge": 13.5, "default_temp": 6.3, "downstream_order": 1
    },
    {
        "code": "144134", "water_category": "minor", "country": "SK",
        "name": "Bártfa (Bardejov)", "river": "Tapoly", "basin": "tisza", "catchment": "sk_east_bodrog_hornad",
        "reach_name": "Tapoly (Topľa) – Bártfa (Bardejov) – Girált – Tapolyhanusfalva – Varannó", "lat": 49.292, "lon": 21.278, "fkm": 94.0,
        "thresholds": {"lkv": 55, "low": 90, "deg1": 250, "deg2": 310, "deg3": 370, "lnv": 450},
        "default_level": 131, "default_diff24h": 0, "default_discharge": 10.4, "default_temp": 6.2, "downstream_order": 1
    },
    {
        "code": "144108", "water_category": "minor", "country": "SK",
        "name": "Szinna (Snina)", "river": "Ciroka", "basin": "tisza", "catchment": "sk_east_bodrog_hornad",
        "reach_name": "Ciroka (Cirocha) – Sztarina-tározó – Szinna (Snina) – Homonna (Laborc)", "lat": 48.988, "lon": 22.152, "fkm": 16.0,
        "thresholds": {"lkv": 15, "low": 40, "deg1": 195, "deg2": 245, "deg3": 295, "lnv": 360},
        "default_level": 68, "default_diff24h": -18, "default_discharge": 6.8, "default_temp": 6.4, "downstream_order": 1
    },
    {
        "code": "149101", "water_category": "minor", "country": "SK",
        "name": "Poprád (Poprad)", "river": "Poprád", "basin": "tisza", "catchment": "sk_vah_nitra",
        "reach_name": "Poprád (Poprad) – Csorba – Poprád – Késmárk – Ólubló", "lat": 49.055, "lon": 20.298, "fkm": 115.0,
        "thresholds": {"lkv": 20, "low": 45, "deg1": 210, "deg2": 265, "deg3": 320, "lnv": 395},
        "default_level": 72, "default_diff24h": 2, "default_discharge": 14.5, "default_temp": 5.6, "downstream_order": 1
    },
]
