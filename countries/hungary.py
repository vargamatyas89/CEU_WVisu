"""
Hungary (HU) — Catchments and Official Hydrological Gauging Stations (OVF hydroinfo.hu & vizugy.hu OperativVizallas)
Standalone country source file (108 Hungarian gauges: 64 main rivers/large lakes + 44 smaller waters, streams, main canals and reservoirs)
"""

COUNTRY_META = {
    "code": "HU",
    "name": "Magyarország",
    "flag": "🇭🇺",
    "border_color": "#fbbf24",
    "bounds": [[45.72, 16.08], [48.60, 22.92]],
}

CATCHMENTS = {
    "upper_duna": {"name": "Felső-Duna és Szigetköz (HU)", "lat": 47.85, "lon": 17.45, "response_factor": 2.4, "lag_days": 1},
    "mid_duna": {"name": "Közép-Duna és Dunakanyar (HU)", "lat": 47.50, "lon": 19.04, "response_factor": 2.8, "lag_days": 2},
    "lower_duna": {"name": "Magyar Alsó-Duna (Paks–Mohács, HU)", "lat": 46.20, "lon": 18.92, "response_factor": 3.0, "lag_days": 3},
    "upper_tisza": {"name": "Felső-Tisza és Szamos-vidék (HU/RO)", "lat": 47.95, "lon": 23.15, "response_factor": 4.2, "lag_days": 1},
    "mid_tisza": {"name": "Közép-Tisza és Tisza-tó (HU)", "lat": 47.50, "lon": 20.62, "response_factor": 3.4, "lag_days": 2},
    "lower_tisza": {"name": "Alsó-Tisza és Maros-torkolat (HU/RO)", "lat": 46.25, "lon": 20.15, "response_factor": 3.1, "lag_days": 3},
    "korosok": {"name": "Körösök és Berettyó vízgyűjtő (HU/RO)", "lat": 46.85, "lon": 21.65, "response_factor": 3.6, "lag_days": 1},
    "west_transdanubia": {"name": "Nyugat-Dunántúl (Rába, Zala, Lajta, HU)", "lat": 47.25, "lon": 16.95, "response_factor": 3.2, "lag_days": 1},
    "drava_mura": {"name": "Dráva, Mura és Dél-Dunántúl (HU)", "lat": 45.95, "lon": 17.45, "response_factor": 2.9, "lag_days": 1},
    "north_hills": {"name": "Északi-középhegység (Sajó, Hernád, Ipoly, Zagyva, HU)", "lat": 48.10, "lon": 20.78, "response_factor": 3.5, "lag_days": 1},
    "lakes_balaton": {"name": "Közép-Dunántúl és Nagy tavak (Balaton, Velencei-tó, Sió, HU)", "lat": 46.90, "lon": 18.05, "response_factor": 0.9, "lag_days": 0},
}

STATIONS = [
    # =========================================================================
    # 1. MAIN RIVERS AND LARGE LAKES (64 stations)
    # =========================================================================
    {
        "code": "442020", "country": "HU", "name": "Rajka", "river": "Duna", "basin": "duna", "catchment": "upper_duna",
        "reach_name": "Duna – Felső-szigetközi határszakasz (Rajka)", "lat": 47.998, "lon": 17.206, "fkm": 1848.4,
        "thresholds": {"lkv": -110, "low": -30, "deg1": 430, "deg2": 520, "deg3": 610, "lnv": 756},
        "default_level": 20, "default_diff24h": 1, "default_discharge": 1280, "default_temp": 7.6, "downstream_order": 1
    },
    {
        "code": "442502", "country": "HU", "name": "Nagybajcs", "river": "Duna", "basin": "duna", "catchment": "upper_duna",
        "reach_name": "Duna – Szigetköz-alsó és Győri-medence (Nagybajcs)", "lat": 47.791, "lon": 17.662, "fkm": 1801.0,
        "thresholds": {"lkv": -20, "low": 20, "deg1": 470, "deg2": 540, "deg3": 610, "lnv": 907},
        "default_level": 32, "default_diff24h": 9, "default_discharge": 1310, "default_temp": 7.8, "downstream_order": 2
    },
    {
        "code": "442521", "country": "HU", "name": "Gönyű", "river": "Duna", "basin": "duna", "catchment": "upper_duna",
        "reach_name": "Duna – Gönyű – Ács szakasz", "lat": 47.737, "lon": 17.831, "fkm": 1791.3,
        "thresholds": {"lkv": -95, "low": -30, "deg1": 480, "deg2": 550, "deg3": 620, "lnv": 872},
        "default_level": -4, "default_diff24h": 5, "default_discharge": 1360, "default_temp": 7.8, "downstream_order": 3
    },
    {
        "code": "442522", "country": "HU", "name": "Komárom", "river": "Duna", "basin": "duna", "catchment": "upper_duna",
        "reach_name": "Duna – Komárom – Almásfüzitő szakasz", "lat": 47.746, "lon": 18.121, "fkm": 1768.3,
        "thresholds": {"lkv": -42, "low": 15, "deg1": 500, "deg2": 640, "deg3": 710, "lnv": 845},
        "default_level": 45, "default_diff24h": 12, "default_discharge": 1410, "default_temp": 7.9, "downstream_order": 4
    },
    {
        "code": "442024", "country": "HU", "name": "Lábatlan", "river": "Duna", "basin": "duna", "catchment": "mid_duna",
        "reach_name": "Duna – Lábatlan – Nyergesújfalu szakasz", "lat": 47.756, "lon": 18.501, "fkm": 1737.8,
        "thresholds": {"lkv": 25, "low": 80, "deg1": 480, "deg2": 560, "deg3": 630, "lnv": 772},
        "default_level": 120, "default_diff24h": 11, "default_discharge": 1440, "default_temp": 8.0, "downstream_order": 5
    },
    {
        "code": "442025", "country": "HU", "name": "Esztergom", "river": "Duna", "basin": "duna", "catchment": "mid_duna",
        "reach_name": "Duna – Esztergom – Garam-torkolati szakasz", "lat": 47.795, "lon": 18.736, "fkm": 1718.5,
        "thresholds": {"lkv": -68, "low": -10, "deg1": 500, "deg2": 580, "deg3": 650, "lnv": 813},
        "default_level": 30, "default_diff24h": 15, "default_discharge": 1490, "default_temp": 8.1, "downstream_order": 6
    },
    {
        "code": "442527", "country": "HU", "name": "Nagymaros", "river": "Duna", "basin": "duna", "catchment": "mid_duna",
        "reach_name": "Duna – Dunakanyar (Szob – Visegrád – Nagymaros)", "lat": 47.791, "lon": 18.958, "fkm": 1694.6,
        "thresholds": {"lkv": -115, "low": -50, "deg1": 480, "deg2": 560, "deg3": 630, "lnv": 751},
        "default_level": -25, "default_diff24h": 14, "default_discharge": 1520, "default_temp": 8.1, "downstream_order": 7
    },
    {
        "code": "442026", "country": "HU", "name": "Vác", "river": "Duna", "basin": "duna", "catchment": "mid_duna",
        "reach_name": "Duna – Váci-Duna-ág és Szentendrei-sziget felső szakasz", "lat": 47.775, "lon": 19.124, "fkm": 1679.5,
        "thresholds": {"lkv": -110, "low": -45, "deg1": 500, "deg2": 580, "deg3": 650, "lnv": 805},
        "default_level": -19, "default_diff24h": 12, "default_discharge": 1530, "default_temp": 8.1, "downstream_order": 8
    },
    {
        "code": "442027", "country": "HU", "name": "Budapest", "river": "Duna", "basin": "duna", "catchment": "mid_duna",
        "reach_name": "Duna – Fővárosi szakasz (Göd – Budapest – Budafok)", "lat": 47.498, "lon": 19.045, "fkm": 1646.5,
        "thresholds": {"lkv": 28, "low": 70, "deg1": 620, "deg2": 700, "deg3": 800, "lnv": 891},
        "default_level": 76, "default_diff24h": 8, "default_discharge": 1560, "default_temp": 8.2, "downstream_order": 9
    },
    {
        "code": "442534", "country": "HU", "name": "Ercsi", "river": "Duna", "basin": "duna", "catchment": "mid_duna",
        "reach_name": "Duna – Ercsi – Adony szakasz", "lat": 47.252, "lon": 18.902, "fkm": 1613.2,
        "thresholds": {"lkv": -125, "low": -65, "deg1": 510, "deg2": 590, "deg3": 660, "lnv": 774},
        "default_level": -57, "default_diff24h": 2, "default_discharge": 1550, "default_temp": 8.3, "downstream_order": 10
    },
    {
        "code": "442028", "country": "HU", "name": "Dunaújváros", "river": "Duna", "basin": "duna", "catchment": "lower_duna",
        "reach_name": "Duna – Tass – Dunaújváros szakasz", "lat": 46.965, "lon": 18.948, "fkm": 1580.6,
        "thresholds": {"lkv": -118, "low": -60, "deg1": 500, "deg2": 580, "deg3": 650, "lnv": 756},
        "default_level": -55, "default_diff24h": -1, "default_discharge": 1540, "default_temp": 8.3, "downstream_order": 11
    },
    {
        "code": "442029", "country": "HU", "name": "Dunaföldvár", "river": "Duna", "basin": "duna", "catchment": "lower_duna",
        "reach_name": "Duna – Dunaföldvár – Solt szakasz", "lat": 46.809, "lon": 18.932, "fkm": 1560.6,
        "thresholds": {"lkv": -220, "low": -160, "deg1": 450, "deg2": 540, "deg3": 630, "lnv": 721},
        "default_level": -175, "default_diff24h": -4, "default_discharge": 1540, "default_temp": 8.3, "downstream_order": 12
    },
    {
        "code": "442030", "country": "HU", "name": "Paks", "river": "Duna", "basin": "duna", "catchment": "lower_duna",
        "reach_name": "Duna – Paks – Kalocsa szakasz", "lat": 46.625, "lon": 18.865, "fkm": 1531.3,
        "thresholds": {"lkv": -135, "low": -70, "deg1": 570, "deg2": 680, "deg3": 780, "lnv": 891},
        "default_level": -59, "default_diff24h": -7, "default_discharge": 1535, "default_temp": 8.4, "downstream_order": 13
    },
    {
        "code": "442031", "country": "HU", "name": "Baja", "river": "Duna", "basin": "duna", "catchment": "lower_duna",
        "reach_name": "Duna – Dombori – Gemenc – Baja szakasz", "lat": 46.182, "lon": 18.926, "fkm": 1478.7,
        "thresholds": {"lkv": 15, "low": 60, "deg1": 700, "deg2": 800, "deg3": 900, "lnv": 989},
        "default_level": 62, "default_diff24h": -11, "default_discharge": 1560, "default_temp": 8.5, "downstream_order": 14
    },
    {
        "code": "442032", "country": "HU", "name": "Mohács", "river": "Duna", "basin": "duna", "catchment": "lower_duna",
        "reach_name": "Duna – Dunaszekcső – Mohács déli határszakasz", "lat": 45.993, "lon": 18.691, "fkm": 1446.9,
        "thresholds": {"lkv": 20, "low": 65, "deg1": 700, "deg2": 800, "deg3": 900, "lnv": 965},
        "default_level": 80, "default_diff24h": -12, "default_discharge": 1570, "default_temp": 8.5, "downstream_order": 15
    },

    # --- DANUBE TRIBUTARIES AND BRANCHES (13 stations) ---
    {
        "code": "442601", "country": "HU", "name": "Bácsa", "river": "Mosoni-Duna", "basin": "duna", "catchment": "upper_duna",
        "reach_name": "Mosoni-Duna – Mosonmagyaróvár – Győr-Bácsa szakasz", "lat": 47.716, "lon": 17.674, "fkm": 14.2,
        "thresholds": {"lkv": 60, "low": 100, "deg1": 420, "deg2": 490, "deg3": 550, "lnv": 652},
        "default_level": 174, "default_diff24h": 2, "default_discharge": 42, "default_temp": 7.6, "downstream_order": 1
    },
    {
        "code": "442602", "country": "HU", "name": "Mosonmagyaróvár duzzasztómű, alvíz", "river": "Lajta", "basin": "duna", "catchment": "west_transdanubia",
        "reach_name": "Lajta – Hegyeshalom – Mosonmagyaróvár szakasz", "lat": 47.874, "lon": 17.272, "fkm": 8.5,
        "thresholds": {"lkv": -30, "low": 0, "deg1": 180, "deg2": 220, "deg3": 260, "lnv": 308},
        "default_level": 11, "default_diff24h": -22, "default_discharge": 9, "default_temp": 7.4, "downstream_order": 1
    },
    {
        "code": "442131", "country": "HU", "name": "Szentgotthárd", "river": "Rába", "basin": "duna", "catchment": "west_transdanubia",
        "reach_name": "Rába – Felső-Rába (Szentgotthárd – Csákánydoroszló)", "lat": 46.956, "lon": 16.275, "fkm": 203.1,
        "thresholds": {"lkv": -180, "low": -120, "deg1": 250, "deg2": 320, "deg3": 380, "lnv": 464},
        "default_level": -107, "default_diff24h": 8, "default_discharge": 18, "default_temp": 7.1, "downstream_order": 1
    },
    {
        "code": "442132", "country": "HU", "name": "Körmend", "river": "Rába", "basin": "duna", "catchment": "west_transdanubia",
        "reach_name": "Rába – Körmend – Molnaszecsőd szakasz", "lat": 47.005, "lon": 16.597, "fkm": 172.4,
        "thresholds": {"lkv": -85, "low": -25, "deg1": 330, "deg2": 390, "deg3": 450, "lnv": 546},
        "default_level": 0, "default_diff24h": 4, "default_discharge": 23, "default_temp": 7.3, "downstream_order": 2
    },
    {
        "code": "442512", "country": "HU", "name": "Sárvár", "river": "Rába", "basin": "duna", "catchment": "west_transdanubia",
        "reach_name": "Rába – Közép-Rába (Rum – Sárvár – Ragyogóhíd)", "lat": 47.258, "lon": 16.945, "fkm": 118.2,
        "thresholds": {"lkv": -190, "low": -145, "deg1": 200, "deg2": 260, "deg3": 320, "lnv": 405},
        "default_level": -136, "default_diff24h": 0, "default_discharge": 26, "default_temp": 7.5, "downstream_order": 3
    },
    {
        "code": "442134", "country": "HU", "name": "Győr", "river": "Rába", "basin": "duna", "catchment": "west_transdanubia",
        "reach_name": "Rába – Alsó-Rába (Árpás – Győr torkolat)", "lat": 47.688, "lon": 17.630, "fkm": 1.8,
        "thresholds": {"lkv": -40, "low": 40, "deg1": 400, "deg2": 480, "deg3": 550, "lnv": 698},
        "default_level": 172, "default_diff24h": 4, "default_discharge": 35, "default_temp": 7.7, "downstream_order": 4
    },
    {
        "code": "442172", "country": "HU", "name": "Balassagyarmat", "river": "Ipoly", "basin": "duna", "catchment": "north_hills",
        "reach_name": "Ipoly – Ipolytarnóc – Nógrádszakál – Balassagyarmat", "lat": 48.081, "lon": 19.291, "fkm": 99.4,
        "thresholds": {"lkv": -120, "low": -70, "deg1": 210, "deg2": 260, "deg3": 310, "lnv": 370},
        "default_level": -56, "default_diff24h": 16, "default_discharge": 11, "default_temp": 6.8, "downstream_order": 1
    },
    {
        "code": "442606", "country": "HU", "name": "Ipolytölgyes", "river": "Ipoly", "basin": "duna", "catchment": "north_hills",
        "reach_name": "Ipoly – Alsó-Ipoly (Ipolyvece – Ipolytölgyes – Szob)", "lat": 47.916, "lon": 18.778, "fkm": 16.5,
        "thresholds": {"lkv": 20, "low": 60, "deg1": 350, "deg2": 420, "deg3": 490, "lnv": 584},
        "default_level": 92, "default_diff24h": 3, "default_discharge": 16, "default_temp": 7.0, "downstream_order": 2
    },
    {
        "code": "442537", "country": "HU", "name": "Kvassay zsilip", "river": "Ráckeve-Soroksári Dunaág", "basin": "duna", "catchment": "mid_duna",
        "reach_name": "Ráckeve-Soroksári Dunaág (Kvassay-zsilip – Ráckeve – Tass)", "lat": 47.345, "lon": 19.015, "fkm": 56.8,
        "thresholds": {"lkv": 90, "low": 120, "deg1": 220, "deg2": 250, "deg3": 280, "lnv": 310},
        "default_level": 149, "default_diff24h": 4, "default_discharge": 30, "default_temp": 8.0, "downstream_order": 1
    },
    {
        "code": "442543", "country": "HU", "name": "Zalaapáti", "river": "Zala", "basin": "duna", "catchment": "west_transdanubia",
        "reach_name": "Zala – Zalaegerszeg – Zalabér – Zalaapáti – Kis-Balaton", "lat": 46.742, "lon": 17.118, "fkm": 22.4,
        "thresholds": {"lkv": -10, "low": 40, "deg1": 260, "deg2": 310, "deg3": 360, "lnv": 412},
        "default_level": 99, "default_diff24h": 2, "default_discharge": 8, "default_temp": 7.4, "downstream_order": 1
    },
    {
        "code": "442181", "country": "HU", "name": "Simontornya", "river": "Sió", "basin": "duna", "catchment": "lakes_balaton",
        "reach_name": "Sió – Felső- és Közép-Sió (Siófok – Ozora – Simontornya)", "lat": 46.752, "lon": 18.555, "fkm": 60.2,
        "thresholds": {"lkv": -45, "low": 15, "deg1": 310, "deg2": 370, "deg3": 420, "lnv": 482},
        "default_level": 113, "default_diff24h": -8, "default_discharge": 19, "default_temp": 7.6, "downstream_order": 1
    },
    {
        "code": "442557", "country": "HU", "name": "Szekszárd (Palánk)", "river": "Sió", "basin": "duna", "catchment": "lower_duna",
        "reach_name": "Sió – Alsó-Sió (Szekszárd-Palánk – Sió-árvízkapu)", "lat": 46.402, "lon": 18.718, "fkm": 17.5,
        "thresholds": {"lkv": 50, "low": 120, "deg1": 520, "deg2": 600, "deg3": 680, "lnv": 775},
        "default_level": 268, "default_diff24h": 5, "default_discharge": 24, "default_temp": 7.9, "downstream_order": 2
    },
    {
        "code": "442555", "country": "HU", "name": "Kurd", "river": "Kapos", "basin": "duna", "catchment": "lakes_balaton",
        "reach_name": "Kapos – Kaposvár – Dombóvár – Kurd – Pincehely", "lat": 46.445, "lon": 18.318, "fkm": 48.0,
        "thresholds": {"lkv": -20, "low": 20, "deg1": 260, "deg2": 310, "deg3": 360, "lnv": 410},
        "default_level": 60, "default_diff24h": 3, "default_discharge": 6, "default_temp": 7.5, "downstream_order": 1
    },

    # --- DRAVA AND MURA (4 stations) ---
    {
        "code": "446501", "country": "HU", "name": "Letenye", "river": "Mura", "basin": "drava", "catchment": "drava_mura",
        "reach_name": "Mura – Murarátka – Letenye – Murakeresztúr", "lat": 46.418, "lon": 16.715, "fkm": 22.8,
        "thresholds": {"lkv": -40, "low": 25, "deg1": 330, "deg2": 380, "deg3": 430, "lnv": 554},
        "default_level": 87, "default_diff24h": -1, "default_discharge": 145, "default_temp": 7.8, "downstream_order": 1
    },
    {
        "code": "446198", "country": "HU", "name": "Őrtilos", "river": "Dráva", "basin": "drava", "catchment": "drava_mura",
        "reach_name": "Dráva – Mura-torkolat – Őrtilos – Vízvár szakasz", "lat": 46.278, "lon": 16.925, "fkm": 235.6,
        "thresholds": {"lkv": -210, "low": -140, "deg1": 280, "deg2": 350, "deg3": 410, "lnv": 496},
        "default_level": -127, "default_diff24h": 6, "default_discharge": 410, "default_temp": 8.0, "downstream_order": 1
    },
    {
        "code": "446199", "country": "HU", "name": "Barcs", "river": "Dráva", "basin": "drava", "catchment": "drava_mura",
        "reach_name": "Dráva – Babócsa – Barcs – Szentborbás szakasz", "lat": 45.952, "lon": 17.458, "fkm": 152.5,
        "thresholds": {"lkv": -240, "low": -170, "deg1": 300, "deg2": 380, "deg3": 450, "lnv": 618},
        "default_level": -179, "default_diff24h": -9, "default_discharge": 430, "default_temp": 8.1, "downstream_order": 2
    },
    {
        "code": "446503", "country": "HU", "name": "Drávaszabolcs", "river": "Dráva", "basin": "drava", "catchment": "drava_mura",
        "reach_name": "Dráva – Alsó-Dráva (Drávatamási – Drávaszabolcs)", "lat": 45.798, "lon": 18.202, "fkm": 77.7,
        "thresholds": {"lkv": -130, "low": -65, "deg1": 350, "deg2": 420, "deg3": 490, "lnv": 596},
        "default_level": -50, "default_diff24h": -3, "default_discharge": 455, "default_temp": 8.2, "downstream_order": 3
    },

    # --- TISZA MAIN STEM (10 Hungarian stations) ---
    {
        "code": "444226", "country": "HU", "name": "Tiszabecs", "river": "Tisza", "basin": "tisza", "catchment": "upper_tisza",
        "reach_name": "Tisza – Felső-Tisza belépő szakasz (Tiszabecs – Tivadar)", "lat": 48.103, "lon": 22.828, "fkm": 744.2,
        "thresholds": {"lkv": -145, "low": -70, "deg1": 300, "deg2": 400, "deg3": 500, "lnv": 725},
        "default_level": 18, "default_diff24h": -116, "default_discharge": 185, "default_temp": 6.4, "downstream_order": 2
    },
    {
        "code": "444227", "country": "HU", "name": "Vásárosnamény", "river": "Tisza", "basin": "tisza", "catchment": "upper_tisza",
        "reach_name": "Tisza – Szamos- és Kraszna-torkolati szakasz (Vásárosnamény)", "lat": 48.128, "lon": 22.338, "fkm": 684.8,
        "thresholds": {"lkv": -210, "low": -110, "deg1": 550, "deg2": 650, "deg3": 750, "lnv": 941},
        "default_level": 297, "default_diff24h": 165, "default_discharge": 420, "default_temp": 6.8, "downstream_order": 3
    },
    {
        "code": "444510", "country": "HU", "name": "Záhony", "river": "Tisza", "basin": "tisza", "catchment": "upper_tisza",
        "reach_name": "Tisza – Felső-Tiszakanyar (Záhony – Dombrád)", "lat": 48.412, "lon": 22.178, "fkm": 628.2,
        "thresholds": {"lkv": -295, "low": -180, "deg1": 450, "deg2": 540, "deg3": 610, "lnv": 754},
        "default_level": 118, "default_diff24h": 284, "default_discharge": 450, "default_temp": 7.0, "downstream_order": 4
    },
    {
        "code": "444228", "country": "HU", "name": "Tokaj", "river": "Tisza", "basin": "tisza", "catchment": "upper_tisza",
        "reach_name": "Tisza – Tiszabercel – Tokaj – Bodrog-torkolati szakasz", "lat": 48.126, "lon": 21.412, "fkm": 543.5,
        "thresholds": {"lkv": 15, "low": 150, "deg1": 650, "deg2": 750, "deg3": 810, "lnv": 926},
        "default_level": 499, "default_diff24h": 22, "default_discharge": 510, "default_temp": 7.2, "downstream_order": 5
    },
    {
        "code": "444530", "country": "HU", "name": "Tiszapalkonya", "river": "Tisza", "basin": "tisza", "catchment": "mid_tisza",
        "reach_name": "Tisza – Tiszalök – Sajó-torkolat – Tiszapalkonya – Tiszakeszi", "lat": 47.882, "lon": 21.055, "fkm": 470.5,
        "thresholds": {"lkv": -130, "low": -30, "deg1": 480, "deg2": 580, "deg3": 650, "lnv": 782},
        "default_level": 206, "default_diff24h": 71, "default_discharge": 530, "default_temp": 7.5, "downstream_order": 6
    },
    {
        "code": "444536", "country": "HU", "name": "Kisköre felső", "river": "Tisza-tó", "basin": "tavak", "catchment": "mid_tisza",
        "reach_name": "Tisza-tó és Kiskörei vízlépcső (Tiszafüred – Kisköre)", "lat": 47.502, "lon": 20.518, "fkm": 404.0,
        "thresholds": {"lkv": 520, "low": 610, "deg1": 780, "deg2": 840, "deg3": 900, "lnv": 1018},
        "default_level": 680, "default_diff24h": 6, "default_discharge": 525, "default_temp": 7.7, "downstream_order": 7
    },
    {
        "code": "444229", "country": "HU", "name": "Szolnok", "river": "Tisza", "basin": "tisza", "catchment": "mid_tisza",
        "reach_name": "Tisza – Közép-Tisza (Tiszaroff – Szolnok – Zagyva-torkolat)", "lat": 47.171, "lon": 20.197, "fkm": 334.6,
        "thresholds": {"lkv": -291, "low": -180, "deg1": 650, "deg2": 750, "deg3": 800, "lnv": 1041},
        "default_level": -32, "default_diff24h": 22, "default_discharge": 490, "default_temp": 7.9, "downstream_order": 8
    },
    {
        "code": "444550", "country": "HU", "name": "Tiszaug", "river": "Tisza", "basin": "tisza", "catchment": "mid_tisza",
        "reach_name": "Tisza – Martfű – Tiszaug szakasz", "lat": 46.852, "lon": 20.062, "fkm": 257.4,
        "thresholds": {"lkv": -280, "low": -180, "deg1": 550, "deg2": 650, "deg3": 740, "lnv": 932},
        "default_level": -108, "default_diff24h": 21, "default_discharge": 495, "default_temp": 8.0, "downstream_order": 9
    },
    {
        "code": "444230", "country": "HU", "name": "Csongrád", "river": "Tisza", "basin": "tisza", "catchment": "lower_tisza",
        "reach_name": "Tisza – Körös-torkolat – Csongrád – Mindszent szakasz", "lat": 46.712, "lon": 20.160, "fkm": 246.2,
        "thresholds": {"lkv": -275, "low": -160, "deg1": 600, "deg2": 700, "deg3": 800, "lnv": 1037},
        "default_level": -16, "default_diff24h": 26, "default_discharge": 590, "default_temp": 8.1, "downstream_order": 10
    },
    {
        "code": "444231", "country": "HU", "name": "Szeged", "river": "Tisza", "basin": "tisza", "catchment": "lower_tisza",
        "reach_name": "Tisza – Alsó-Tisza (Algyő – Maros-torkolat – Szeged)", "lat": 46.251, "lon": 20.153, "fkm": 173.6,
        "thresholds": {"lkv": -248, "low": -100, "deg1": 650, "deg2": 750, "deg3": 850, "lnv": 1009},
        "default_level": 143, "default_diff24h": 7, "default_discharge": 670, "default_temp": 8.3, "downstream_order": 11
    },

    # --- TISZA TRIBUTARIES IN HUNGARY (18 stations) ---
    {
        "code": "444244", "country": "HU", "name": "Csenger", "river": "Szamos", "basin": "tisza", "catchment": "upper_tisza",
        "reach_name": "Szamos – Magyarországi alsó szakasz (Csenger – Olcsvaapáti)", "lat": 47.838, "lon": 22.685, "fkm": 48.2,
        "thresholds": {"lkv": -175, "low": -80, "deg1": 400, "deg2": 550, "deg3": 700, "lnv": 906},
        "default_level": 80, "default_diff24h": 30, "default_discharge": 95, "default_temp": 6.7, "downstream_order": 4
    },
    {
        "code": "444507", "country": "HU", "name": "Ágerdőmajor", "river": "Kraszna", "basin": "tisza", "catchment": "upper_tisza",
        "reach_name": "Kraszna – Ágerdőmajor – Nagyecsed – Kocsord", "lat": 47.795, "lon": 22.412, "fkm": 32.0,
        "thresholds": {"lkv": -40, "low": 20, "deg1": 380, "deg2": 450, "deg3": 510, "lnv": 612},
        "default_level": 146, "default_diff24h": 0, "default_discharge": 12, "default_temp": 6.9, "downstream_order": 2
    },
    {
        "code": "444502", "country": "HU", "name": "Sonkád", "river": "Túr", "basin": "tisza", "catchment": "upper_tisza",
        "reach_name": "Túr – Garbolc – Sonkád – Túristvándi", "lat": 48.038, "lon": 22.742, "fkm": 27.5,
        "thresholds": {"lkv": -50, "low": 20, "deg1": 340, "deg2": 400, "deg3": 460, "lnv": 540},
        "default_level": 171, "default_diff24h": 21, "default_discharge": 16, "default_temp": 6.6, "downstream_order": 2
    },
    {
        "code": "444283", "country": "HU", "name": "Sárospatak", "river": "Bodrog", "basin": "tisza", "catchment": "north_hills",
        "reach_name": "Bodrog – Felsőberecki – Sárospatak – Tokaj", "lat": 48.322, "lon": 21.572, "fkm": 29.4,
        "thresholds": {"lkv": 60, "low": 140, "deg1": 480, "deg2": 560, "deg3": 620, "lnv": 758},
        "default_level": 335, "default_diff24h": 18, "default_discharge": 88, "default_temp": 7.1, "downstream_order": 1
    },
    {
        "code": "444323", "country": "HU", "name": "Gesztely", "river": "Hernád", "basin": "tisza", "catchment": "north_hills",
        "reach_name": "Hernád – Hidasnémeti – Gibárt – Gesztely – Bőcs", "lat": 48.105, "lon": 20.962, "fkm": 19.8,
        "thresholds": {"lkv": -110, "low": -50, "deg1": 280, "deg2": 340, "deg3": 400, "lnv": 496},
        "default_level": -18, "default_diff24h": 1, "default_discharge": 26, "default_temp": 6.8, "downstream_order": 1
    },
    {
        "code": "444293", "country": "HU", "name": "Felsőzsolca", "river": "Sajó", "basin": "tisza", "catchment": "north_hills",
        "reach_name": "Sajó – Sajópüspöki – Sajószentpéter – Felsőzsolca – Ónod", "lat": 48.104, "lon": 20.848, "fkm": 28.5,
        "thresholds": {"lkv": -90, "low": -30, "deg1": 240, "deg2": 310, "deg3": 370, "lnv": 464},
        "default_level": 12, "default_diff24h": 7, "default_discharge": 31, "default_temp": 6.9, "downstream_order": 1
    },
    {
        "code": "444311", "country": "HU", "name": "Szendrő", "river": "Bódva", "basin": "tisza", "catchment": "north_hills",
        "reach_name": "Bódva – Hidvégardó – Szendrő – Edelény", "lat": 48.402, "lon": 20.725, "fkm": 38.0,
        "thresholds": {"lkv": -110, "low": -70, "deg1": 180, "deg2": 220, "deg3": 260, "lnv": 335},
        "default_level": -59, "default_diff24h": 1, "default_discharge": 7, "default_temp": 6.5, "downstream_order": 1
    },
    {
        "code": "444548", "country": "HU", "name": "Jásztelek", "river": "Zagyva", "basin": "tisza", "catchment": "north_hills",
        "reach_name": "Zagyva – Pásztó – Hatvan – Jászberény – Jásztelek – Szolnok", "lat": 47.482, "lon": 20.005, "fkm": 46.2,
        "thresholds": {"lkv": 30, "low": 80, "deg1": 350, "deg2": 420, "deg3": 480, "lnv": 572},
        "default_level": 179, "default_diff24h": 7, "default_discharge": 12, "default_temp": 7.4, "downstream_order": 1
    },
    {
        "code": "444654", "country": "HU", "name": "Tarnaörs", "river": "Tarna", "basin": "tisza", "catchment": "north_hills",
        "reach_name": "Tarna – Verpelét – Tarnaméra – Tarnaörs", "lat": 47.602, "lon": 20.060, "fkm": 12.4,
        "thresholds": {"lkv": 20, "low": 70, "deg1": 300, "deg2": 360, "deg3": 420, "lnv": 485},
        "default_level": 136, "default_diff24h": -4, "default_discharge": 5, "default_temp": 7.2, "downstream_order": 1
    },
    {
        "code": "444566", "country": "HU", "name": "Szeghalom", "river": "Berettyó", "basin": "tisza", "catchment": "korosok",
        "reach_name": "Berettyó – Pocsaj – Berettyóújfalu – Szeghalom", "lat": 47.022, "lon": 21.178, "fkm": 12.8,
        "thresholds": {"lkv": -60, "low": 40, "deg1": 400, "deg2": 470, "deg3": 540, "lnv": 642},
        "default_level": 207, "default_diff24h": 2, "default_discharge": 24, "default_temp": 7.6, "downstream_order": 3
    },
    {
        "code": "444567", "country": "HU", "name": "Körösladány", "river": "Sebes-Körös", "basin": "tisza", "catchment": "korosok",
        "reach_name": "Sebes-Körös – Körösszakál – Körösladány", "lat": 46.965, "lon": 21.082, "fkm": 21.5,
        "thresholds": {"lkv": -110, "low": 20, "deg1": 420, "deg2": 500, "deg3": 580, "lnv": 698},
        "default_level": 188, "default_diff24h": 55, "default_discharge": 48, "default_temp": 7.7, "downstream_order": 3
    },
    {
        "code": "444554", "country": "HU", "name": "Sarkad-Malomfok", "river": "Fekete-Körös", "basin": "tisza", "catchment": "korosok",
        "reach_name": "Fekete-Körös – Ant – Sarkad-Malomfok – Remete", "lat": 46.725, "lon": 21.402, "fkm": 15.6,
        "thresholds": {"lkv": -150, "low": -30, "deg1": 520, "deg2": 620, "deg3": 720, "lnv": 864},
        "default_level": 298, "default_diff24h": 74, "default_discharge": 55, "default_temp": 7.8, "downstream_order": 4
    },
    {
        "code": "444552", "country": "HU", "name": "Gyula", "river": "Fehér-Körös", "basin": "tisza", "catchment": "korosok",
        "reach_name": "Fehér-Körös – Gyula határszakasz", "lat": 46.652, "lon": 21.285, "fkm": 9.8,
        "thresholds": {"lkv": -140, "low": -30, "deg1": 450, "deg2": 550, "deg3": 650, "lnv": 798},
        "default_level": 100, "default_diff24h": -41, "default_discharge": 36, "default_temp": 7.9, "downstream_order": 3
    },
    {
        "code": "444361", "country": "HU", "name": "Békés", "river": "Kettős-Körös", "basin": "tisza", "catchment": "korosok",
        "reach_name": "Kettős-Körös – Doboz – Békés – Köröstarcsa", "lat": 46.775, "lon": 21.135, "fkm": 22.0,
        "thresholds": {"lkv": -110, "low": 20, "deg1": 550, "deg2": 650, "deg3": 750, "lnv": 904},
        "default_level": 351, "default_diff24h": 191, "default_discharge": 92, "default_temp": 7.8, "downstream_order": 1
    },
    {
        "code": "444371", "country": "HU", "name": "Gyoma", "river": "Hármas-Körös", "basin": "tisza", "catchment": "korosok",
        "reach_name": "Hármas-Körös – Felső szakasz (Gyomaendrőd – Szarvas)", "lat": 46.938, "lon": 20.825, "fkm": 71.2,
        "thresholds": {"lkv": -60, "low": 60, "deg1": 550, "deg2": 650, "deg3": 750, "lnv": 918},
        "default_level": 392, "default_diff24h": 35, "default_discharge": 135, "default_temp": 7.9, "downstream_order": 1
    },
    {
        "code": "444372", "country": "HU", "name": "Kunszentmárton", "river": "Hármas-Körös", "basin": "tisza", "catchment": "korosok",
        "reach_name": "Hármas-Körös – Alsó szakasz (Békésszentandrás – Kunszentmárton – Csongrád)", "lat": 46.835, "lon": 20.285, "fkm": 24.5,
        "thresholds": {"lkv": -210, "low": -80, "deg1": 600, "deg2": 700, "deg3": 800, "lnv": 982},
        "default_level": 127, "default_diff24h": 107, "default_discharge": 145, "default_temp": 8.0, "downstream_order": 2
    },
    {
        "code": "444568", "country": "HU", "name": "Mezőtúr árvízkapu alsó", "river": "Hortobágy-Berettyó", "basin": "tisza", "catchment": "korosok",
        "reach_name": "Hortobágy-Berettyó főcsatorna (Ecsegfalva – Mezőtúr)", "lat": 47.002, "lon": 20.635, "fkm": 14.0,
        "thresholds": {"lkv": 40, "low": 120, "deg1": 480, "deg2": 540, "deg3": 600, "lnv": 685},
        "default_level": 407, "default_diff24h": 13, "default_discharge": 28, "default_temp": 7.7, "downstream_order": 1
    },
    {
        "code": "444396", "country": "HU", "name": "Makó", "river": "Maros", "basin": "tisza", "catchment": "lower_tisza",
        "reach_name": "Maros – Magyarországi alsó szakasz (Apátfalva – Makó – Szeged)", "lat": 46.201, "lon": 20.472, "fkm": 24.4,
        "thresholds": {"lkv": -135, "low": -65, "deg1": 350, "deg2": 400, "deg3": 450, "lnv": 624},
        "default_level": -24, "default_diff24h": -39, "default_discharge": 115, "default_temp": 8.1, "downstream_order": 7
    },

    # --- HUNGARIAN LARGE LAKES (4 stations) ---
    {
        "code": "442550", "country": "HU", "name": "Siófok", "river": "Balaton", "basin": "tavak", "catchment": "lakes_balaton",
        "reach_name": "Balaton – Keleti-medence (Siófok – Balatonkenese)", "lat": 46.912, "lon": 18.042, "fkm": 0.0,
        "thresholds": {"lkv": 23, "low": 65, "deg1": 115, "deg2": 125, "deg3": 135, "lnv": 152},
        "default_level": 42, "default_diff24h": 1, "default_discharge": 15, "default_temp": 7.3, "downstream_order": 1
    },
    {
        "code": "442633", "country": "HU", "name": "Tihany rév", "river": "Balaton", "basin": "tavak", "catchment": "lakes_balaton",
        "reach_name": "Balaton – Középső- és Nyugati-medence (Tihany – Badacsony – Keszthely)", "lat": 46.889, "lon": 17.892, "fkm": 0.0,
        "thresholds": {"lkv": 23, "low": 65, "deg1": 115, "deg2": 125, "deg3": 135, "lnv": 152},
        "default_level": 40, "default_diff24h": 2, "default_discharge": 15, "default_temp": 8.2, "downstream_order": 2
    },
    {
        "code": "442558", "country": "HU", "name": "Agárd", "river": "Velencei-tó", "basin": "tavak", "catchment": "lakes_balaton",
        "reach_name": "Velencei-tó (Agárd – Gárdony – Pákozd)", "lat": 47.195, "lon": 18.602, "fkm": 0.0,
        "thresholds": {"lkv": 53, "low": 95, "deg1": 165, "deg2": 175, "deg3": 185, "lnv": 205},
        "default_level": 16, "default_diff24h": 2, "default_discharge": 2, "default_temp": 7.4, "downstream_order": 1
    },
    {
        "code": "442613", "country": "HU", "name": "Fertőrákos", "river": "Fertő-tó", "basin": "tavak", "catchment": "west_transdanubia",
        "reach_name": "Fertő-tó magyarországi medence (Fertőrákos – Balf)", "lat": 47.728, "lon": 16.678, "fkm": 0.0,
        "thresholds": {"lkv": -45, "low": -15, "deg1": 40, "deg2": 55, "deg3": 70, "lnv": 92},
        "default_level": -6, "default_diff24h": 0, "default_discharge": 3, "default_temp": 5.1, "downstream_order": 1
    },

    # =========================================================================
    # 2. SMALLER WATERS, STREAMS, MAIN CANALS AND RESERVOIRS (vizugy.hu & OVF — 44 stations)
    # =========================================================================
    {
        "code": "442609", "vizugy_id": "345", "water_category": "minor", "country": "HU",
        "name": "Felsőcsatár", "river": "Pinka", "basin": "duna", "catchment": "west_transdanubia",
        "reach_name": "Pinka-patak – Felsőcsatár – Pornóapáti – Pinkamindszent", "lat": 47.205, "lon": 16.452, "fkm": 33.8,
        "thresholds": {"lkv": 1, "low": 35, "deg1": 320, "deg2": 380, "deg3": 440, "lnv": 506},
        "default_level": 59, "default_diff24h": 19, "default_discharge": 4.2, "default_temp": 7.0, "downstream_order": 1
    },
    {
        "code": "442504", "vizugy_id": "349", "water_category": "minor", "country": "HU",
        "name": "Répcevis", "river": "Répce", "basin": "duna", "catchment": "west_transdanubia",
        "reach_name": "Répce – Répcevis – Bük – Répcelak", "lat": 47.448, "lon": 16.672, "fkm": 76.4,
        "thresholds": {"lkv": -19, "low": 2, "deg1": 250, "deg2": 320, "deg3": 380, "lnv": 470},
        "default_level": 4, "default_diff24h": 4, "default_discharge": 2.8, "default_temp": 7.1, "downstream_order": 1
    },
    {
        "code": "442603", "vizugy_id": "31", "water_category": "minor", "country": "HU",
        "name": "Rábcakapi", "river": "Rábca", "basin": "duna", "catchment": "west_transdanubia",
        "reach_name": "Rábca – Hanság – Rábcakapi – Lébény – Győr", "lat": 47.702, "lon": 17.152, "fkm": 28.2,
        "thresholds": {"lkv": 24, "low": 70, "deg1": 250, "deg2": 310, "deg3": 370, "lnv": 434},
        "default_level": 133, "default_diff24h": 30, "default_discharge": 8.5, "default_temp": 7.3, "downstream_order": 1
    },
    {
        "code": "442518", "vizugy_id": "350", "water_category": "minor", "country": "HU",
        "name": "Karakó", "river": "Marcal", "basin": "duna", "catchment": "west_transdanubia",
        "reach_name": "Marcal – Sümeg – Karakó – Mórichida – Gyirmót", "lat": 47.185, "lon": 17.202, "fkm": 71.3,
        "thresholds": {"lkv": 11, "low": 55, "deg1": 240, "deg2": 290, "deg3": 340, "lnv": 375},
        "default_level": 116, "default_diff24h": -2, "default_discharge": 5.4, "default_temp": 7.4, "downstream_order": 1
    },
    {
        "code": "VIZUGY_3557", "vizugy_id": "3557", "water_category": "minor", "country": "HU",
        "name": "Kőszeg", "river": "Gyöngyös-patak", "basin": "duna", "catchment": "west_transdanubia",
        "reach_name": "Gyöngyös-patak – Kőszeg – Lukácsháza – Szombathely – Sárvár", "lat": 47.388, "lon": 16.542, "fkm": 53.0,
        "thresholds": {"lkv": 26, "low": 35, "deg1": 160, "deg2": 195, "deg3": 225, "lnv": 252},
        "default_level": 44, "default_diff24h": 2, "default_discharge": 3.3, "default_temp": 6.8, "downstream_order": 1
    },
    {
        "code": "VIZUGY_347", "vizugy_id": "347", "water_category": "minor", "country": "HU",
        "name": "Szombathely-Olad", "river": "Arany-patak", "basin": "duna", "catchment": "west_transdanubia",
        "reach_name": "Arany-patak – Rohonc – Dozmat – Szombathely-Olad", "lat": 47.235, "lon": 16.592, "fkm": 1.7,
        "thresholds": {"lkv": 9, "low": 16, "deg1": 165, "deg2": 205, "deg3": 240, "lnv": 278},
        "default_level": 25, "default_diff24h": 1, "default_discharge": 1.4, "default_temp": 7.1, "downstream_order": 1
    },
    {
        "code": "VIZUGY_26", "vizugy_id": "26", "water_category": "minor", "country": "HU",
        "name": "Nagycenk", "river": "Ikva-patak", "basin": "duna", "catchment": "west_transdanubia",
        "reach_name": "Ikva-patak – Sopron – Kópháza – Nagycenk – Fertőszentmiklós", "lat": 47.608, "lon": 16.705, "fkm": 0.6,
        "thresholds": {"lkv": 6, "low": 15, "deg1": 150, "deg2": 185, "deg3": 215, "lnv": 242},
        "default_level": 22, "default_diff24h": 0, "default_discharge": 1.6, "default_temp": 7.0, "downstream_order": 1
    },
    {
        "code": "VIZUGY_3064", "vizugy_id": "3064", "water_category": "minor", "country": "HU",
        "name": "Sorkifalud", "river": "Sorok-Perint", "basin": "duna", "catchment": "west_transdanubia",
        "reach_name": "Sorok-Perint – Szombathely – Sorkifalud – Zsennye", "lat": 47.135, "lon": 16.735, "fkm": 8.8,
        "thresholds": {"lkv": 10, "low": 30, "deg1": 170, "deg2": 210, "deg3": 245, "lnv": 274},
        "default_level": 54, "default_diff24h": 2, "default_discharge": 2.1, "default_temp": 7.2, "downstream_order": 1
    },
    {
        "code": "VIZUGY_4551", "vizugy_id": "4551", "water_category": "minor", "country": "HU",
        "name": "Fertőszéli zsilip", "river": "Hanság-főcsatorna", "basin": "duna", "catchment": "west_transdanubia",
        "reach_name": "Hanság-főcsatorna – Pomogy – Fertőszéli zsilip – Kapuvár – Király-tó", "lat": 47.692, "lon": 16.925, "fkm": 32.3,
        "thresholds": {"lkv": 50, "low": 75, "deg1": 175, "deg2": 205, "deg3": 225, "lnv": 241},
        "default_level": 90, "default_diff24h": 1, "default_discharge": 3.5, "default_temp": 7.1, "downstream_order": 1
    },
    {
        "code": "VIZUGY_4524", "vizugy_id": "4524", "water_category": "minor", "country": "HU",
        "name": "Bajánsenye", "river": "Kerka", "basin": "drava", "catchment": "west_transdanubia",
        "reach_name": "Kerka – Bajánsenye – Lenti – Tormafölde – Muraszemenye", "lat": 46.798, "lon": 16.382, "fkm": 53.2,
        "thresholds": {"lkv": -22, "low": 5, "deg1": 180, "deg2": 215, "deg3": 245, "lnv": 264},
        "default_level": 29, "default_diff24h": 3, "default_discharge": 4.1, "default_temp": 7.3, "downstream_order": 1
    },
    {
        "code": "VIZUGY_4216", "vizugy_id": "4216", "water_category": "minor", "country": "HU",
        "name": "Rédics", "river": "Kebele-patak", "basin": "drava", "catchment": "west_transdanubia",
        "reach_name": "Kebele-patak (Lendva-vízgyűjtő) – Rédics", "lat": 46.625, "lon": 16.485, "fkm": 6.6,
        "thresholds": {"lkv": 21, "low": 30, "deg1": 210, "deg2": 255, "deg3": 295, "lnv": 328},
        "default_level": 37, "default_diff24h": 1, "default_discharge": 1.8, "default_temp": 7.4, "downstream_order": 1
    },
    {
        "code": "VIZUGY_365", "vizugy_id": "365", "water_category": "minor", "country": "HU",
        "name": "Nagykanizsa", "river": "Principális-csatorna", "basin": "drava", "catchment": "drava_mura",
        "reach_name": "Principális-csatorna – Gelse – Nagykanizsa – Murakeresztúr", "lat": 46.452, "lon": 16.985, "fkm": 18.3,
        "thresholds": {"lkv": 38, "low": 50, "deg1": 185, "deg2": 220, "deg3": 250, "lnv": 272},
        "default_level": 68, "default_diff24h": 2, "default_discharge": 3.2, "default_temp": 7.6, "downstream_order": 1
    },
    {
        "code": "VIZUGY_142007", "vizugy_id": "142007", "water_category": "minor", "country": "HU",
        "name": "Apácatorna", "river": "Torna-patak", "basin": "duna", "catchment": "west_transdanubia",
        "reach_name": "Torna-patak – Ajka – Devecser – Apácatorna – Karakó", "lat": 47.122, "lon": 17.305, "fkm": 8.5,
        "thresholds": {"lkv": 17, "low": 40, "deg1": 195, "deg2": 235, "deg3": 275, "lnv": 310},
        "default_level": 73, "default_diff24h": 1, "default_discharge": 2.4, "default_temp": 7.3, "downstream_order": 1
    },
    {
        "code": "VIZUGY_43", "vizugy_id": "43", "water_category": "minor", "country": "HU",
        "name": "Tatabánya", "river": "Által-ér", "basin": "duna", "catchment": "mid_duna",
        "reach_name": "Által-ér – Oroszlány – Tatabánya – Tata – Dunaalmás", "lat": 47.585, "lon": 18.395, "fkm": 21.0,
        "thresholds": {"lkv": -3, "low": 4, "deg1": 95, "deg2": 115, "deg3": 130, "lnv": 140},
        "default_level": 8, "default_diff24h": 0, "default_discharge": 1.9, "default_temp": 7.5, "downstream_order": 1
    },
    {
        "code": "VIZUGY_53", "vizugy_id": "53", "water_category": "minor", "country": "HU",
        "name": "Tata (Öreg-tó)", "river": "Tatai Öreg-tó", "basin": "tavak", "catchment": "mid_duna",
        "reach_name": "Tatai Öreg-tó (Vecserei-zsilip – Tata)", "lat": 47.648, "lon": 18.328, "fkm": 0.0,
        "thresholds": {"lkv": -210, "low": -120, "deg1": 120, "deg2": 160, "deg3": 190, "lnv": 213},
        "default_level": -67, "default_diff24h": 1, "default_discharge": 1.8, "default_temp": 7.2, "downstream_order": 1
    },
    {
        "code": "VIZUGY_39", "vizugy_id": "39", "water_category": "minor", "country": "HU",
        "name": "Bakonybánk", "river": "Cuhai-Bakony-ér", "basin": "duna", "catchment": "mid_duna",
        "reach_name": "Cuhai-Bakony-ér (Concó) – Zirc – Bakonybánk – Gönyű", "lat": 47.465, "lon": 17.895, "fkm": 37.8,
        "thresholds": {"lkv": -5, "low": 2, "deg1": 190, "deg2": 240, "deg3": 280, "lnv": 314},
        "default_level": 6, "default_diff24h": 0, "default_discharge": 1.5, "default_temp": 7.2, "downstream_order": 1
    },
    {
        "code": "VIZUGY_565", "vizugy_id": "565", "water_category": "minor", "country": "HU",
        "name": "Bodajk", "river": "Gaja-patak", "basin": "duna", "catchment": "lakes_balaton",
        "reach_name": "Gaja-patak – Bakonynána – Bodajk – Fehérvárcsurgó – Székesfehérvár", "lat": 47.322, "lon": 18.232, "fkm": 26.7,
        "thresholds": {"lkv": -4, "low": 0, "deg1": 180, "deg2": 225, "deg3": 265, "lnv": 291},
        "default_level": 1, "default_diff24h": 0, "default_discharge": 1.3, "default_temp": 7.3, "downstream_order": 1
    },
    {
        "code": "VIZUGY_140043", "vizugy_id": "140043", "water_category": "minor", "country": "HU",
        "name": "Kisfalud-puszta", "river": "Császár-víz", "basin": "duna", "catchment": "lakes_balaton",
        "reach_name": "Császár-víz – Csákvár – Zámolyi-medence – Kisfalud-puszta (Velencei-tó befolyó)", "lat": 47.235, "lon": 18.525, "fkm": 3.9,
        "thresholds": {"lkv": -2, "low": 0, "deg1": 105, "deg2": 130, "deg3": 148, "lnv": 160},
        "default_level": 1, "default_diff24h": 0, "default_discharge": 0.9, "default_temp": 7.4, "downstream_order": 1
    },
    {
        "code": "442616", "vizugy_id": "567", "water_category": "minor", "country": "HU",
        "name": "Sárszentmihály", "river": "Nádor-csatorna", "basin": "duna", "catchment": "lakes_balaton",
        "reach_name": "Nádor-csatorna (Sárvíz) – Sárszentmihály – Aba – Cece – Sió", "lat": 47.152, "lon": 18.338, "fkm": 95.4,
        "thresholds": {"lkv": -34, "low": 5, "deg1": 130, "deg2": 210, "deg3": 285, "lnv": 360},
        "default_level": 33, "default_diff24h": 26, "default_discharge": 5.8, "default_temp": 7.5, "downstream_order": 1
    },
    {
        "code": "VIZUGY_4375", "vizugy_id": "4375", "water_category": "minor", "country": "HU",
        "name": "Balatonkeresztúr", "river": "Nyugati-övcsatorna", "basin": "tavak", "catchment": "lakes_balaton",
        "reach_name": "Nyugati-övcsatorna – Nagyberek – Marcali – Balatonkeresztúr", "lat": 46.695, "lon": 17.372, "fkm": 1.6,
        "thresholds": {"lkv": -13, "low": -2, "deg1": 85, "deg2": 105, "deg3": 120, "lnv": 131},
        "default_level": 10, "default_diff24h": 1, "default_discharge": 2.2, "default_temp": 7.5, "downstream_order": 1
    },
    {
        "code": "VIZUGY_2895", "vizugy_id": "2895", "water_category": "minor", "country": "HU",
        "name": "Visz", "river": "Tetves-patak", "basin": "tavak", "catchment": "lakes_balaton",
        "reach_name": "Tetves-patak – Visz – Somogybabod – Balatonlelle", "lat": 46.725, "lon": 17.775, "fkm": 9.4,
        "thresholds": {"lkv": 31, "low": 38, "deg1": 115, "deg2": 140, "deg3": 158, "lnv": 169},
        "default_level": 49, "default_diff24h": 1, "default_discharge": 0.8, "default_temp": 7.4, "downstream_order": 1
    },
    {
        "code": "VIZUGY_3061", "vizugy_id": "3061", "water_category": "minor", "country": "HU",
        "name": "Pamuk", "river": "Keleti-Bozót-csatorna", "basin": "tavak", "catchment": "lakes_balaton",
        "reach_name": "Keleti-Bozót-csatorna (Pogányvölgyi-víz) – Somogyvár – Pamuk – Buzsák – Fonyód", "lat": 46.582, "lon": 17.648, "fkm": 24.3,
        "thresholds": {"lkv": 1, "low": 20, "deg1": 145, "deg2": 175, "deg3": 205, "lnv": 221},
        "default_level": 48, "default_diff24h": 2, "default_discharge": 1.9, "default_temp": 7.5, "downstream_order": 1
    },
    {
        "code": "VIZUGY_564", "vizugy_id": "564", "water_category": "minor", "country": "HU",
        "name": "Tamási", "river": "Koppány-patak", "basin": "duna", "catchment": "lakes_balaton",
        "reach_name": "Koppány-patak – Törökkoppány – Tamási – Regöly (Kapos-torkolat)", "lat": 46.632, "lon": 18.288, "fkm": 14.5,
        "thresholds": {"lkv": 18, "low": 55, "deg1": 250, "deg2": 310, "deg3": 355, "lnv": 388},
        "default_level": 138, "default_diff24h": 2, "default_discharge": 2.6, "default_temp": 7.5, "downstream_order": 1
    },
    {
        "code": "VIZUGY_570", "vizugy_id": "570", "water_category": "minor", "country": "HU",
        "name": "Bonyhád", "river": "Völgységi-patak", "basin": "duna", "catchment": "lower_duna",
        "reach_name": "Völgységi-patak – Mecseknádasd – Bonyhád – Bonyhádi-Sió", "lat": 46.302, "lon": 18.532, "fkm": 20.3,
        "thresholds": {"lkv": 82, "low": 115, "deg1": 270, "deg2": 330, "deg3": 375, "lnv": 408},
        "default_level": 152, "default_diff24h": 1, "default_discharge": 1.7, "default_temp": 7.6, "downstream_order": 1
    },
    {
        "code": "VIZUGY_851", "vizugy_id": "851", "water_category": "minor", "country": "HU",
        "name": "Babócsa", "river": "Rinya-patak", "basin": "drava", "catchment": "drava_mura",
        "reach_name": "Rinya (Babócsai- és Lábodi-Rinya) – Nagyatád – Lábod – Babócsa", "lat": 46.042, "lon": 17.345, "fkm": 5.3,
        "thresholds": {"lkv": -30, "low": -5, "deg1": 205, "deg2": 255, "deg3": 295, "lnv": 326},
        "default_level": 6, "default_diff24h": 0, "default_discharge": 2.9, "default_temp": 7.8, "downstream_order": 1
    },
    {
        "code": "VIZUGY_844", "vizugy_id": "844", "water_category": "minor", "country": "HU",
        "name": "Szentlőrinc", "river": "Bükkösdi-víz", "basin": "drava", "catchment": "drava_mura",
        "reach_name": "Bükkösdi-víz – Hetvehely – Bükkösd – Szentlőrinc", "lat": 46.042, "lon": 17.985, "fkm": 6.5,
        "thresholds": {"lkv": 11, "low": 30, "deg1": 225, "deg2": 280, "deg3": 325, "lnv": 357},
        "default_level": 53, "default_diff24h": 2, "default_discharge": 1.6, "default_temp": 7.7, "downstream_order": 1
    },
    {
        "code": "VIZUGY_845", "vizugy_id": "845", "water_category": "minor", "country": "HU",
        "name": "Kémes–Cún", "river": "Fekete-víz", "basin": "drava", "catchment": "drava_mura",
        "reach_name": "Fekete-víz (Ormánság) – Sellye – Kémes – Cún – Drávaszabolcs", "lat": 45.818, "lon": 18.082, "fkm": 7.2,
        "thresholds": {"lkv": -20, "low": 60, "deg1": 330, "deg2": 395, "deg3": 450, "lnv": 485},
        "default_level": 202, "default_diff24h": 4, "default_discharge": 5.2, "default_temp": 7.9, "downstream_order": 1
    },
    {
        "code": "VIZUGY_837", "vizugy_id": "837", "water_category": "minor", "country": "HU",
        "name": "Villány", "river": "Karasica", "basin": "duna", "catchment": "lower_duna",
        "reach_name": "Karasica-patak – Pécsvárad – Szederkény – Villány – Magyarbóly", "lat": 45.868, "lon": 18.458, "fkm": 42.2,
        "thresholds": {"lkv": -2, "low": 20, "deg1": 195, "deg2": 240, "deg3": 280, "lnv": 309},
        "default_level": 35, "default_diff24h": 1, "default_discharge": 2.1, "default_temp": 7.8, "downstream_order": 1
    },
    {
        "code": "VIZUGY_841", "vizugy_id": "841", "water_category": "minor", "country": "HU",
        "name": "Csikóstőttős", "river": "Baranya-csatorna", "basin": "drava", "catchment": "drava_mura",
        "reach_name": "Baranya-csatorna – Sásd – Mágocs – Csikóstőttős – Dombóvár", "lat": 46.332, "lon": 18.158, "fkm": 3.2,
        "thresholds": {"lkv": 5, "low": 25, "deg1": 280, "deg2": 350, "deg3": 410, "lnv": 460},
        "default_level": 43, "default_diff24h": 1, "default_discharge": 1.8, "default_temp": 7.5, "downstream_order": 1
    },
    {
        "code": "VIZUGY_1038", "vizugy_id": "1038", "water_category": "minor", "country": "HU",
        "name": "Szentendre", "river": "Szentendrei-Duna", "basin": "duna", "catchment": "mid_duna",
        "reach_name": "Szentendrei-Duna-ág (Kisoroszi – Tahitótfalu – Szentendre – Békásmegyer)", "lat": 47.668, "lon": 19.082, "fkm": 10.8,
        "thresholds": {"lkv": -114, "low": -50, "deg1": 500, "deg2": 580, "deg3": 650, "lnv": 796},
        "default_level": -32, "default_diff24h": 10, "default_discharge": 310.0, "default_temp": 8.1, "downstream_order": 1
    },
    {
        "code": "VIZUGY_1047", "vizugy_id": "1047", "water_category": "minor", "country": "HU",
        "name": "Bernecebaráti", "river": "Kemence-patak", "basin": "duna", "catchment": "north_hills",
        "reach_name": "Kemence-patak (Börzsöny) – Diósjenő – Kemence – Bernecebaráti", "lat": 48.042, "lon": 18.912, "fkm": 4.4,
        "thresholds": {"lkv": -12, "low": 15, "deg1": 210, "deg2": 270, "deg3": 320, "lnv": 369},
        "default_level": 35, "default_diff24h": 2, "default_discharge": 1.5, "default_temp": 6.6, "downstream_order": 1
    },
    {
        "code": "444686", "vizugy_id": "1055", "water_category": "minor", "country": "HU",
        "name": "Maconkai tározó", "river": "Zagyva-patak", "basin": "tisza", "catchment": "north_hills",
        "reach_name": "Felső-Zagyva és Maconkai-víztározó (Bátonyterenye – Maconka – Pásztó)", "lat": 47.992, "lon": 19.825, "fkm": 133.8,
        "thresholds": {"lkv": 180, "low": 260, "deg1": 450, "deg2": 510, "deg3": 560, "lnv": 615},
        "default_level": 369, "default_diff24h": 2, "default_discharge": 3.4, "default_temp": 6.9, "downstream_order": 1
    },
    {
        "code": "444544", "vizugy_id": "1062", "water_category": "minor", "country": "HU",
        "name": "Hévízgyörk", "river": "Galga-patak", "basin": "tisza", "catchment": "north_hills",
        "reach_name": "Galga-patak – Galgamácsa – Aszód – Hévízgyörk – Tura", "lat": 47.628, "lon": 19.528, "fkm": 18.0,
        "thresholds": {"lkv": 13, "low": 45, "deg1": 210, "deg2": 255, "deg3": 295, "lnv": 321},
        "default_level": 118, "default_diff24h": 4, "default_discharge": 2.3, "default_temp": 7.3, "downstream_order": 1
    },
    {
        "code": "VIZUGY_1755", "vizugy_id": "1755", "water_category": "minor", "country": "HU",
        "name": "Borsodivánka", "river": "Eger-patak", "basin": "tisza", "catchment": "north_hills",
        "reach_name": "Eger-patak (Rima) – Szarvaskő – Almár – Eger – Maklár – Borsodivánka", "lat": 47.702, "lon": 20.648, "fkm": 3.2,
        "thresholds": {"lkv": 3, "low": 40, "deg1": 230, "deg2": 285, "deg3": 335, "lnv": 371},
        "default_level": 143, "default_diff24h": 3, "default_discharge": 3.8, "default_temp": 7.1, "downstream_order": 1
    },
    {
        "code": "VIZUGY_1749", "vizugy_id": "1749", "water_category": "minor", "country": "HU",
        "name": "Bánhorváti", "river": "Bán-patak", "basin": "tisza", "catchment": "north_hills",
        "reach_name": "Bán-patak és Lázbérci-víztározó (Uppony – Dédestapolcsány – Bánhorváti – Sajó)", "lat": 48.222, "lon": 20.515, "fkm": 5.2,
        "thresholds": {"lkv": 3, "low": 10, "deg1": 185, "deg2": 230, "deg3": 270, "lnv": 302},
        "default_level": 15, "default_diff24h": 1, "default_discharge": 1.6, "default_temp": 6.7, "downstream_order": 1
    },
    {
        "code": "444653", "vizugy_id": "1764", "water_category": "minor", "country": "HU",
        "name": "Taktaföldvár", "river": "Takta", "basin": "tisza", "catchment": "north_hills",
        "reach_name": "Takta – Szerencs – Taktaharkány – Taktaföldvár – Taktakenéz", "lat": 48.095, "lon": 21.185, "fkm": 24.4,
        "thresholds": {"lkv": 61, "low": 110, "deg1": 200, "deg2": 280, "deg3": 350, "lnv": 410},
        "default_level": 181, "default_diff24h": 4, "default_discharge": 6.2, "default_temp": 7.1, "downstream_order": 1
    },
    {
        "code": "VIZUGY_1541", "vizugy_id": "1541", "water_category": "minor", "country": "HU",
        "name": "Kótaj", "river": "Lónyay-főcsatorna", "basin": "tisza", "catchment": "upper_tisza",
        "reach_name": "Lónyay-főcsatorna (Nyírség) – Nyírbátor – Kemecse – Kótaj – Gávavencsellő", "lat": 48.062, "lon": 21.725, "fkm": 21.2,
        "thresholds": {"lkv": 460, "low": 510, "deg1": 650, "deg2": 740, "deg3": 820, "lnv": 898},
        "default_level": 606, "default_diff24h": 5, "default_discharge": 7.5, "default_temp": 7.0, "downstream_order": 1
    },
    {
        "code": "444662", "vizugy_id": "2549", "water_category": "minor", "country": "HU",
        "name": "Bakonszeg zsilip felvíz", "river": "Keleti-főcsatorna", "basin": "tisza", "catchment": "mid_tisza",
        "reach_name": "Keleti-főcsatorna – Tiszalök – Hajdúszoboszló – Bakonszeg (Berettyó)", "lat": 47.202, "lon": 21.432, "fkm": 98.2,
        "thresholds": {"lkv": -76, "low": 40, "deg1": 240, "deg2": 265, "deg3": 280, "lnv": 290},
        "default_level": 219, "default_diff24h": 1, "default_discharge": 18.0, "default_temp": 7.5, "downstream_order": 1
    },
    {
        "code": "444670", "vizugy_id": "3416", "water_category": "minor", "country": "HU",
        "name": "Abádszalók felső", "river": "Nagykunsági-főcsatorna", "basin": "tisza", "catchment": "mid_tisza",
        "reach_name": "Nagykunsági-főcsatorna – Abádszalók – Kunhegyes – Karcag – Öcsöd", "lat": 47.412, "lon": 20.648, "fkm": 0.0,
        "thresholds": {"lkv": 414, "low": 580, "deg1": 830, "deg2": 860, "deg3": 890, "lnv": 920},
        "default_level": 810, "default_diff24h": 5, "default_discharge": 20.3, "default_temp": 7.7, "downstream_order": 1
    },
    {
        "code": "444668", "vizugy_id": "2065", "water_category": "minor", "country": "HU",
        "name": "Kisköre felső (Jászsági fcs.)", "river": "Jászsági-főcsatorna", "basin": "tisza", "catchment": "mid_tisza",
        "reach_name": "Jászsági-főcsatorna – Kisköre – Heves – Jászapáti", "lat": 47.542, "lon": 20.382, "fkm": 0.0,
        "thresholds": {"lkv": 598, "low": 680, "deg1": 900, "deg2": 980, "deg3": 1060, "lnv": 1168},
        "default_level": 806, "default_diff24h": 2, "default_discharge": 14.2, "default_temp": 7.6, "downstream_order": 1
    },
    {
        "code": "VIZUGY_130050", "vizugy_id": "130050", "water_category": "minor", "country": "HU",
        "name": "Kecel (Vádei híd)", "river": "Duna-völgyi-főcsatorna", "basin": "duna", "catchment": "lower_duna",
        "reach_name": "Duna-völgyi-főcsatorna – Kunpeszér – Akasztó – Kecel – Baja", "lat": 46.535, "lon": 19.228, "fkm": 50.4,
        "thresholds": {"lkv": 2, "low": 45, "deg1": 180, "deg2": 200, "deg3": 215, "lnv": 222},
        "default_level": 145, "default_diff24h": 2, "default_discharge": 9.4, "default_temp": 8.0, "downstream_order": 1
    },
    {
        "code": "VIZUGY_2561", "vizugy_id": "2561", "water_category": "minor", "country": "HU",
        "name": "Nádudvar", "river": "Kösely-főcsatorna", "basin": "tisza", "catchment": "korosok",
        "reach_name": "Kösely-főcsatorna – Debrecen – Hajdúszoboszló – Nádudvar", "lat": 47.415, "lon": 21.182, "fkm": 6.7,
        "thresholds": {"lkv": 52, "low": 80, "deg1": 220, "deg2": 255, "deg3": 285, "lnv": 305},
        "default_level": 135, "default_diff24h": 3, "default_discharge": 4.8, "default_temp": 7.5, "downstream_order": 1
    },
    {
        "code": "VIZUGY_210206", "vizugy_id": "210206", "water_category": "minor", "country": "HU",
        "name": "Battonya", "river": "Királyhegyesi-Száraz-ér", "basin": "tisza", "catchment": "lower_tisza",
        "reach_name": "Száraz-ér (Királyhegyesi-Szárazéri fcs.) – Battonya – Mezőhegyes – Makó", "lat": 46.282, "lon": 21.018, "fkm": 97.3,
        "thresholds": {"lkv": -10, "low": 10, "deg1": 140, "deg2": 180, "deg3": 215, "lnv": 255},
        "default_level": 34, "default_diff24h": 1, "default_discharge": 2.4, "default_temp": 7.9, "downstream_order": 1
    },
    {
        "code": "VIZUGY_210224", "vizugy_id": "210224", "water_category": "minor", "country": "HU",
        "name": "Szeged-Fehérpart", "river": "Gyálai Holt-Tisza", "basin": "tisza", "catchment": "lower_tisza",
        "reach_name": "Gyálai Holt-Tisza (Szeged-Röszke – Fehérparti-zsilip)", "lat": 46.192, "lon": 20.068, "fkm": 18.0,
        "thresholds": {"lkv": 90, "low": 140, "deg1": 250, "deg2": 285, "deg3": 315, "lnv": 350},
        "default_level": 196, "default_diff24h": 1, "default_discharge": 2.1, "default_temp": 8.2, "downstream_order": 1
    },
]
