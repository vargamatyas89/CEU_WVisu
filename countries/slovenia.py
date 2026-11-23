"""
Slovenia (SI) — Catchments and Official Hydrological Gauging Stations (ARSO hidro_podatki_zadnji.xml / hydroinfo.hu 546102 & GloFAS v4)
Standalone country source file (37 Slovenian gauges: main rivers, Alpine/karst lakes and smaller waters — 100% live ARSO XML telemetry)
"""

COUNTRY_META = {
    "code": "SI",
    "name": "Szlovénia",
    "flag": "🇸🇮",
    "border_color": "#2dd4bf",
    "bounds": [[45.42, 13.38], [46.88, 16.61]],
}

CATCHMENTS = {
    "si_sava_ljubljana": {"name": "Száva-völgy, Gorenjska és Ljubljanai-medence (SI)", "lat": 46.12, "lon": 14.55, "response_factor": 3.5, "lag_days": 1},
    "si_drava_mura_pomurje": {"name": "Dráva, Mura, Savinja és Muravidék (Štajerska / Prekmurje, SI)", "lat": 46.42, "lon": 15.65, "response_factor": 3.1, "lag_days": 1},
    "si_soca_adriatic": {"name": "Soča (Isonzó), Vipava és Adriai-karszt vízgyűjtő (Primorska, SI)", "lat": 46.02, "lon": 13.72, "response_factor": 3.9, "lag_days": 1},
    "si_krka_kolpa_dolenjska": {"name": "Krka, Kolpa (Kupa) és Notranjska karsztvidék (Dolenjska, SI)", "lat": 45.78, "lon": 15.05, "response_factor": 3.4, "lag_days": 1},
}

STATIONS = [
    # =========================================================================
    # 1. MAIN RIVERS AND ALPINE / KARST LAKES (22 stations — live ARSO XML & hydroinfo.hu)
    # =========================================================================
    # --- SAVA (6 stations) ---
    {
        "code": "ARSO_3420", "arso_id": "3420", "country": "SI", "name": "Radovljica", "river": "Száva", "basin": "duna", "catchment": "si_sava_ljubljana",
        "reach_name": "Száva (Sava) – Sava Dolinka és Sava Bohinjka összefolyás – Radovljica", "lat": 46.340, "lon": 14.165, "fkm": 862.0,
        "thresholds": {"lkv": 25, "low": 55, "deg1": 210, "deg2": 265, "deg3": 320, "lnv": 410},
        "default_level": 72, "default_diff24h": 2, "default_discharge": 38.2, "default_temp": 7.8, "downstream_order": 1
    },
    {
        "code": "ARSO_3570", "arso_id": "3570", "country": "SI", "name": "Ljubljana (Šentjakob)", "river": "Száva", "basin": "duna", "catchment": "si_sava_ljubljana",
        "reach_name": "Száva (Sava) – Kranj – Medvode – Ljubljana (Šentjakob)", "lat": 46.084, "lon": 14.583, "fkm": 815.0,
        "thresholds": {"lkv": 190, "low": 250, "deg1": 450, "deg2": 520, "deg3": 590, "lnv": 695},
        "default_level": 304, "default_diff24h": 4, "default_discharge": 77.2, "default_temp": 8.7, "downstream_order": 2
    },
    {
        "code": "ARSO_3660", "arso_id": "3660", "country": "SI", "name": "Litija", "river": "Száva", "basin": "duna", "catchment": "si_sava_ljubljana",
        "reach_name": "Száva (Sava) – Ljubljanica- és Kamniška Bistrica-torkolat – Litija", "lat": 46.057, "lon": 14.829, "fkm": 788.0,
        "thresholds": {"lkv": 40, "low": 90, "deg1": 360, "deg2": 450, "deg3": 530, "lnv": 645},
        "default_level": 140, "default_diff24h": 5, "default_discharge": 264.0, "default_temp": 9.3, "downstream_order": 3
    },
    {
        "code": "ARSO_3725", "arso_id": "3725", "country": "SI", "name": "Hrastnik", "river": "Száva", "basin": "duna", "catchment": "si_sava_ljubljana",
        "reach_name": "Száva (Sava) – Zasavje (Zagorje – Trbovlje – Hrastnik – Zidani Most)", "lat": 46.122, "lon": 15.091, "fkm": 761.0,
        "thresholds": {"lkv": 210, "low": 280, "deg1": 520, "deg2": 620, "deg3": 710, "lnv": 825},
        "default_level": 340, "default_diff24h": 6, "default_discharge": 288.0, "default_temp": 9.6, "downstream_order": 4
    },
    {
        "code": "ARSO_3850", "arso_id": "3850", "country": "SI", "name": "Čatež (Brežice)", "river": "Száva", "basin": "duna", "catchment": "si_krka_kolpa_dolenjska",
        "reach_name": "Száva (Sava) – Krško – Brežice – Krka-torkolat – Čatež", "lat": 45.893, "lon": 15.610, "fkm": 737.0,
        "thresholds": {"lkv": 110, "low": 175, "deg1": 490, "deg2": 580, "deg3": 660, "lnv": 775},
        "default_level": 242, "default_diff24h": 8, "default_discharge": 465.0, "default_temp": 9.5, "downstream_order": 5
    },
    {
        "code": "ARSO_3900", "arso_id": "3900", "country": "SI", "name": "Jesenice na Dolenjskem", "river": "Száva", "basin": "duna", "catchment": "si_krka_kolpa_dolenjska",
        "reach_name": "Száva (Sava) – Jesenice na Dolenjskem (Szlovén–horvát határszakasz)", "lat": 45.860, "lon": 15.693, "fkm": 729.0,
        "thresholds": {"lkv": 85, "low": 145, "deg1": 460, "deg2": 550, "deg3": 630, "lnv": 745},
        "default_level": 195, "default_diff24h": 7, "default_discharge": 448.0, "default_temp": 10.3, "downstream_order": 6
    },

    # --- DRAVA AND MURA (5 stations) ---
    {
        "code": "ARSO_2005", "arso_id": "2005", "country": "SI", "name": "Črneče (Dravograd)", "river": "Dráva", "basin": "drava", "catchment": "si_drava_mura_pomurje",
        "reach_name": "Dráva (Drava) – Karintiai belépő szakasz (Črneče – Dravograd)", "lat": 46.598, "lon": 14.984, "fkm": 415.0,
        "thresholds": {"lkv": 410, "low": 475, "deg1": 670, "deg2": 750, "deg3": 820, "lnv": 935},
        "default_level": 548, "default_diff24h": 2, "default_discharge": 241.0, "default_temp": 7.0, "downstream_order": 1
    },
    {
        "code": "ARSO_2110", "arso_id": "2110", "country": "SI", "name": "Ptuj (Maribor–Ptuj)", "river": "Dráva", "basin": "drava", "catchment": "si_drava_mura_pomurje",
        "reach_name": "Dráva (Drava) – Maribor – Ptuj – Ptuji-víztározó", "lat": 46.417, "lon": 15.868, "fkm": 330.0,
        "thresholds": {"lkv": 330, "low": 395, "deg1": 590, "deg2": 665, "deg3": 730, "lnv": 845},
        "default_level": 451, "default_diff24h": 3, "default_discharge": 331.0, "default_temp": 7.4, "downstream_order": 2
    },
    {
        "code": "ARSO_2160", "arso_id": "2160", "country": "SI", "name": "Zavrč (Ormož)", "river": "Dráva", "basin": "drava", "catchment": "si_drava_mura_pomurje",
        "reach_name": "Dráva (Drava) – Borl – Zavrč – Ormož (Szlovén–horvát határszakasz)", "lat": 46.388, "lon": 16.037, "fkm": 308.0,
        "thresholds": {"lkv": -35, "low": 0, "deg1": 230, "deg2": 300, "deg3": 360, "lnv": 445},
        "default_level": 17, "default_diff24h": 1, "default_discharge": 295.0, "default_temp": 8.4, "downstream_order": 3
    },
    {
        "code": "546102", "arso_id": "1060", "country": "SI", "name": "Gornja Radgona", "river": "Mura", "basin": "drava", "catchment": "si_drava_mura_pomurje",
        "reach_name": "Mura – Gornja Radgona (Osztrák–szlovén határszakasz)", "lat": 46.681, "lon": 15.995, "fkm": 115.0,
        "thresholds": {"lkv": 15, "low": 45, "deg1": 310, "deg2": 390, "deg3": 450, "lnv": 535},
        "default_level": 59, "default_diff24h": -1, "default_discharge": 50.6, "default_temp": 6.6, "downstream_order": 1
    },
    {
        "code": "ARSO_1070", "arso_id": "1070", "country": "SI", "name": "Petanjci (Muraszombat)", "river": "Mura", "basin": "drava", "catchment": "si_drava_mura_pomurje",
        "reach_name": "Mura – Muravidék (Petanjci – Veržej – Lendva-vidék)", "lat": 46.648, "lon": 16.054, "fkm": 103.0,
        "thresholds": {"lkv": 40, "low": 75, "deg1": 340, "deg2": 420, "deg3": 480, "lnv": 565},
        "default_level": 94, "default_diff24h": -1, "default_discharge": 55.1, "default_temp": 6.9, "downstream_order": 2
    },

    # --- LJUBLJANICA, SAVINJA, KRKA, KOLPA AND SOČA (8 stations) ---
    {
        "code": "ARSO_5078", "arso_id": "5078", "country": "SI", "name": "Ljubljana (Moste)", "river": "Ljubljanica", "basin": "duna", "catchment": "si_sava_ljubljana",
        "reach_name": "Ljubljanica – Vrhnika – Ljubljanai-láp – Ljubljana (Moste)", "lat": 46.055, "lon": 14.544, "fkm": 11.0,
        "thresholds": {"lkv": 80, "low": 135, "deg1": 310, "deg2": 370, "deg3": 420, "lnv": 495},
        "default_level": 197, "default_diff24h": 4, "default_discharge": 167.0, "default_temp": 9.4, "downstream_order": 1
    },
    {
        "code": "ARSO_6140", "arso_id": "6140", "country": "SI", "name": "Celje", "river": "Savinja", "basin": "duna", "catchment": "si_drava_mura_pomurje",
        "reach_name": "Savinja – Solčava – Nazarje – Letuš – Celje", "lat": 46.228, "lon": 15.261, "fkm": 22.0,
        "thresholds": {"lkv": 55, "low": 90, "deg1": 340, "deg2": 430, "deg3": 500, "lnv": 615},
        "default_level": 124, "default_diff24h": 2, "default_discharge": 26.1, "default_temp": 8.2, "downstream_order": 1
    },
    {
        "code": "ARSO_6210", "arso_id": "6210", "country": "SI", "name": "Laško (Veliko Širje)", "river": "Savinja", "basin": "duna", "catchment": "si_drava_mura_pomurje",
        "reach_name": "Savinja – Laško – Veliko Širje – Zidani Most (Száva-torkolat)", "lat": 46.092, "lon": 15.192, "fkm": 3.5,
        "thresholds": {"lkv": 110, "low": 155, "deg1": 420, "deg2": 510, "deg3": 590, "lnv": 705},
        "default_level": 201, "default_diff24h": 2, "default_discharge": 31.3, "default_temp": 7.8, "downstream_order": 2
    },
    {
        "code": "ARSO_7060", "arso_id": "7060", "country": "SI", "name": "Soteska (Novo mesto)", "river": "Krka (SI)", "basin": "duna", "catchment": "si_krka_kolpa_dolenjska",
        "reach_name": "Krka (SI) – Podbukovje – Žužemberk – Soteska – Novo mesto", "lat": 45.779, "lon": 15.019, "fkm": 62.0,
        "thresholds": {"lkv": 115, "low": 165, "deg1": 360, "deg2": 430, "deg3": 490, "lnv": 575},
        "default_level": 227, "default_diff24h": 5, "default_discharge": 54.1, "default_temp": 9.8, "downstream_order": 1
    },
    {
        "code": "ARSO_7160", "arso_id": "7160", "country": "SI", "name": "Podbočje (Kostanjevica)", "river": "Krka (SI)", "basin": "duna", "catchment": "si_krka_kolpa_dolenjska",
        "reach_name": "Krka (SI) – Otočec – Kostanjevica na Krki – Podbočje – Brežice", "lat": 45.865, "lon": 15.455, "fkm": 12.0,
        "thresholds": {"lkv": 55, "low": 95, "deg1": 280, "deg2": 340, "deg3": 395, "lnv": 465},
        "default_level": 142, "default_diff24h": 4, "default_discharge": 81.4, "default_temp": 9.8, "downstream_order": 2
    },
    {
        "code": "ARSO_4860", "arso_id": "4860", "country": "SI", "name": "Metlika", "river": "Kolpa", "basin": "duna", "catchment": "si_krka_kolpa_dolenjska",
        "reach_name": "Kolpa (Kupa) – Petrina – Črnomelj – Metlika (Bela krajina)", "lat": 45.635, "lon": 15.323, "fkm": 175.0,
        "thresholds": {"lkv": 55, "low": 105, "deg1": 370, "deg2": 450, "deg3": 520, "lnv": 615},
        "default_level": 171, "default_diff24h": 6, "default_discharge": 166.0, "default_temp": 8.8, "downstream_order": 1
    },
    {
        "code": "ARSO_8080", "arso_id": "8080", "country": "SI", "name": "Kobarid", "river": "Soča (Isonzó)", "basin": "drava", "catchment": "si_soca_adriatic",
        "reach_name": "Soča (Isonzó) – Trenta – Bovec – Kobarid – Tolmin (Júliai-Alpok)", "lat": 46.247, "lon": 13.586, "fkm": 98.0,
        "thresholds": {"lkv": 40, "low": 70, "deg1": 270, "deg2": 340, "deg3": 410, "lnv": 510},
        "default_level": 97, "default_diff24h": 3, "default_discharge": 26.2, "default_temp": 7.6, "downstream_order": 1
    },
    {
        "code": "ARSO_8180", "arso_id": "8180", "country": "SI", "name": "Solkan (Nova Gorica)", "river": "Soča (Isonzó)", "basin": "drava", "catchment": "si_soca_adriatic",
        "reach_name": "Soča (Isonzó) – Kanal ob Soči – Solkan – Nova Gorica", "lat": 45.982, "lon": 13.655, "fkm": 52.0,
        "thresholds": {"lkv": 190, "low": 250, "deg1": 520, "deg2": 620, "deg3": 710, "lnv": 845},
        "default_level": 313, "default_diff24h": 8, "default_discharge": 139.0, "default_temp": 9.4, "downstream_order": 2
    },

    # --- SLOVENIAN LARGE LAKES (3 stations) ---
    {
        "code": "ARSO_3350", "arso_id": "3350", "country": "SI", "name": "Bledi-tó (Mlino)", "river": "Bledi-tó (Blejsko jezero)", "basin": "tavak", "catchment": "si_sava_ljubljana",
        "reach_name": "Bledi-tó (Blejsko jezero – Mlino / Bled)", "lat": 46.360, "lon": 14.099, "fkm": 0.0,
        "thresholds": {"lkv": 10, "low": 25, "deg1": 95, "deg2": 120, "deg3": 145, "lnv": 175},
        "default_level": 44, "default_diff24h": 0, "default_discharge": 0.6, "default_temp": 10.9, "downstream_order": 1
    },
    {
        "code": "ARSO_3280", "arso_id": "3280", "country": "SI", "name": "Bohinji-tó (Sveti Duh)", "river": "Bohinji-tó (Bohinjsko jezero)", "basin": "tavak", "catchment": "si_sava_ljubljana",
        "reach_name": "Bohinji-tó (Bohinjsko jezero – Ukanc – Sveti Duh – Ribčev Laz)", "lat": 46.279, "lon": 13.865, "fkm": 0.0,
        "thresholds": {"lkv": 5, "low": 22, "deg1": 120, "deg2": 155, "deg3": 190, "lnv": 235},
        "default_level": 38, "default_diff24h": 1, "default_discharge": 7.9, "default_temp": 8.1, "downstream_order": 1
    },
    {
        "code": "ARSO_5680", "arso_id": "5680", "country": "SI", "name": "Cerknicai-tó (Dolenje Jezero)", "river": "Cerknicai-tó (Cerkniško jezero)", "basin": "tavak", "catchment": "si_krka_kolpa_dolenjska",
        "reach_name": "Cerknicai-karszttó (Cerkniško jezero / Stržen – Dolenje Jezero)", "lat": 45.766, "lon": 14.361, "fkm": 0.0,
        "thresholds": {"lkv": 180, "low": 290, "deg1": 520, "deg2": 580, "deg3": 640, "lnv": 715},
        "default_level": 431, "default_diff24h": 4, "default_discharge": 12.0, "default_temp": 8.3, "downstream_order": 1
    },

    # =========================================================================
    # 2. SMALLER WATERS, ALPINE AND KARST STREAMS (15 stations — live ARSO XML)
    # =========================================================================
    {
        "code": "ARSO_3060", "arso_id": "3060", "country": "SI", "water_category": "minor", "name": "Jesenice", "river": "Sava Dolinka", "basin": "duna", "catchment": "si_sava_ljubljana",
        "reach_name": "Sava Dolinka – Kranjska Gora – Jesenice – Blejski most", "lat": 46.434, "lon": 14.054, "fkm": 32.0,
        "thresholds": {"lkv": 25, "low": 48, "deg1": 190, "deg2": 240, "deg3": 290, "lnv": 360},
        "default_level": 68, "default_diff24h": 1, "default_discharge": 5.5, "default_temp": 7.5, "downstream_order": 1
    },
    {
        "code": "ARSO_3250", "arso_id": "3250", "country": "SI", "water_category": "minor", "name": "Bodešče (Bohinj)", "river": "Sava Bohinjka", "basin": "duna", "catchment": "si_sava_ljubljana",
        "reach_name": "Sava Bohinjka – Bohinjska Bistrica – Bodešče – Radovljica", "lat": 46.342, "lon": 14.142, "fkm": 6.0,
        "thresholds": {"lkv": 35, "low": 65, "deg1": 240, "deg2": 300, "deg3": 360, "lnv": 445},
        "default_level": 93, "default_diff24h": 2, "default_discharge": 18.4, "default_temp": 7.9, "downstream_order": 1
    },
    {
        "code": "ARSO_4200", "arso_id": "4200", "country": "SI", "water_category": "minor", "name": "Škofja Loka (Suha)", "river": "Sora", "basin": "duna", "catchment": "si_sava_ljubljana",
        "reach_name": "Sora (Poljanska & Selška Sora) – Škofja Loka – Suha – Medvode", "lat": 46.162, "lon": 14.326, "fkm": 11.0,
        "thresholds": {"lkv": 50, "low": 85, "deg1": 290, "deg2": 360, "deg3": 420, "lnv": 510},
        "default_level": 127, "default_diff24h": 3, "default_discharge": 24.4, "default_temp": 9.6, "downstream_order": 1
    },
    {
        "code": "ARSO_4400", "arso_id": "4400", "country": "SI", "water_category": "minor", "name": "Kamnik", "river": "Kamniška Bistrica", "basin": "duna", "catchment": "si_sava_ljubljana",
        "reach_name": "Kamniška Bistrica – Kamniki-Alpok – Kamnik – Domžale – Vir", "lat": 46.224, "lon": 14.613, "fkm": 20.0,
        "thresholds": {"lkv": 25, "low": 50, "deg1": 210, "deg2": 265, "deg3": 320, "lnv": 410},
        "default_level": 71, "default_diff24h": 1, "default_discharge": 8.2, "default_temp": 8.3, "downstream_order": 1
    },
    {
        "code": "ARSO_4155", "arso_id": "4155", "country": "SI", "water_category": "minor", "name": "Kranj", "river": "Kokra", "basin": "duna", "catchment": "si_sava_ljubljana",
        "reach_name": "Kokra – Jezersko – Kokra-szurdok – Kranj", "lat": 46.243, "lon": 14.360, "fkm": 2.5,
        "thresholds": {"lkv": 35, "low": 60, "deg1": 210, "deg2": 260, "deg3": 310, "lnv": 385},
        "default_level": 85, "default_diff24h": 1, "default_discharge": 5.5, "default_temp": 7.5, "downstream_order": 1
    },
    {
        "code": "ARSO_1260", "arso_id": "1260", "country": "SI", "water_category": "minor", "name": "Csente (Čentiba / Lendva)", "river": "Ledva (Ledava)", "basin": "drava", "catchment": "si_drava_mura_pomurje",
        "reach_name": "Ledva (Ledava) – Muraszombat – Lendva – Csente (Čentiba)", "lat": 46.535, "lon": 16.478, "fkm": 12.0,
        "thresholds": {"lkv": 45, "low": 85, "deg1": 260, "deg2": 320, "deg3": 380, "lnv": 455},
        "default_level": 125, "default_diff24h": 0, "default_discharge": 1.5, "default_temp": 8.6, "downstream_order": 1
    },
    {
        "code": "ARSO_1355", "arso_id": "1355", "country": "SI", "water_category": "minor", "name": "Őrihodos (Hodoš)", "river": "Nagy-Kerka (Velika Krka)", "basin": "drava", "catchment": "si_drava_mura_pomurje",
        "reach_name": "Nagy-Kerka (Velika Krka) – Goričko – Őrihodos (Hodoš) – Őrség", "lat": 46.814, "lon": 16.333, "fkm": 58.0,
        "thresholds": {"lkv": -15, "low": 2, "deg1": 160, "deg2": 210, "deg3": 260, "lnv": 320},
        "default_level": 8, "default_diff24h": 0, "default_discharge": 0.1, "default_temp": 6.6, "downstream_order": 1
    },
    {
        "code": "ARSO_2250", "arso_id": "2250", "country": "SI", "water_category": "minor", "name": "Otiški Vrh (Dravograd)", "river": "Meža", "basin": "drava", "catchment": "si_drava_mura_pomurje",
        "reach_name": "Meža – Črna na Koroškem – Ravne – Otiški Vrh (Dravograd)", "lat": 46.578, "lon": 15.026, "fkm": 4.0,
        "thresholds": {"lkv": 20, "low": 42, "deg1": 220, "deg2": 280, "deg3": 340, "lnv": 430},
        "default_level": 59, "default_diff24h": 0, "default_discharge": 6.2, "default_temp": 6.8, "downstream_order": 1
    },
    {
        "code": "ARSO_2652", "arso_id": "2652", "country": "SI", "water_category": "minor", "name": "Videm (Ptuj)", "river": "Dravinja", "basin": "drava", "catchment": "si_drava_mura_pomurje",
        "reach_name": "Dravinja – Slovenske Konjice – Makole – Videm pri Ptuju", "lat": 46.368, "lon": 15.903, "fkm": 5.5,
        "thresholds": {"lkv": 40, "low": 75, "deg1": 270, "deg2": 330, "deg3": 390, "lnv": 465},
        "default_level": 106, "default_diff24h": -1, "default_discharge": 3.3, "default_temp": 7.8, "downstream_order": 1
    },
    {
        "code": "ARSO_2900", "arso_id": "2900", "country": "SI", "water_category": "minor", "name": "Zamušani", "river": "Pesnica", "basin": "drava", "catchment": "si_drava_mura_pomurje",
        "reach_name": "Pesnica – Slovenske gorice – Gočova – Zamušani – Ormož", "lat": 46.414, "lon": 16.034, "fkm": 11.0,
        "thresholds": {"lkv": 35, "low": 68, "deg1": 260, "deg2": 320, "deg3": 380, "lnv": 455},
        "default_level": 94, "default_diff24h": 0, "default_discharge": 1.3, "default_temp": 7.1, "downstream_order": 1
    },
    {
        "code": "ARSO_4750", "arso_id": "4750", "country": "SI", "water_category": "minor", "name": "Rakovec (Rogaška)", "river": "Sotla", "basin": "duna", "catchment": "si_drava_mura_pomurje",
        "reach_name": "Sotla (Sutla) – Rogatec – Podčetrtek – Rakovec (Szlovén–horvát határfolyó)", "lat": 45.921, "lon": 15.704, "fkm": 14.0,
        "thresholds": {"lkv": 5, "low": 22, "deg1": 230, "deg2": 290, "deg3": 350, "lnv": 425},
        "default_level": 34, "default_diff24h": -1, "default_discharge": 3.0, "default_temp": 7.5, "downstream_order": 1
    },
    {
        "code": "ARSO_8450", "arso_id": "8450", "country": "SI", "water_category": "minor", "name": "Hotešk (Idrija)", "river": "Idrijca", "basin": "drava", "catchment": "si_soca_adriatic",
        "reach_name": "Idrijca – Idrija – Podroteja – Hotešk – Most na Soči", "lat": 46.128, "lon": 13.794, "fkm": 6.5,
        "thresholds": {"lkv": 30, "low": 60, "deg1": 260, "deg2": 330, "deg3": 400, "lnv": 495},
        "default_level": 89, "default_diff24h": 3, "default_discharge": 32.6, "default_temp": 8.9, "downstream_order": 1
    },
    {
        "code": "ARSO_8601", "arso_id": "8601", "country": "SI", "water_category": "minor", "name": "Miren (Ajdovščina)", "river": "Vipava", "basin": "drava", "catchment": "si_soca_adriatic",
        "reach_name": "Vipava – Ajdovščina – Zalošče – Miren (Vipava-völgy)", "lat": 45.894, "lon": 13.608, "fkm": 4.0,
        "thresholds": {"lkv": 65, "low": 120, "deg1": 360, "deg2": 430, "deg3": 490, "lnv": 575},
        "default_level": 196, "default_diff24h": 6, "default_discharge": 53.0, "default_temp": 10.4, "downstream_order": 1
    },
    {
        "code": "ARSO_9050", "arso_id": "9050", "country": "SI", "water_category": "minor", "name": "Škocjan (Cerkvenikov mlin)", "river": "Reka (Škocjan)", "basin": "drava", "catchment": "si_soca_adriatic",
        "reach_name": "Reka – Ilirska Bistrica – Cerkvenikov mlin – Škocjan-barlang", "lat": 45.655, "lon": 14.061, "fkm": 12.0,
        "thresholds": {"lkv": 85, "low": 140, "deg1": 370, "deg2": 440, "deg3": 510, "lnv": 615},
        "default_level": 233, "default_diff24h": 5, "default_discharge": 27.7, "default_temp": 9.3, "downstream_order": 1
    },
    {
        "code": "ARSO_9300", "arso_id": "9300", "country": "SI", "water_category": "minor", "name": "Podkaštel (Piran)", "river": "Dragonja", "basin": "drava", "catchment": "si_soca_adriatic",
        "reach_name": "Dragonja – Szlovén-Isztria – Podkaštel – Sečovlje (Adriai-tenger)", "lat": 45.453, "lon": 13.654, "fkm": 6.0,
        "thresholds": {"lkv": 35, "low": 65, "deg1": 230, "deg2": 290, "deg3": 350, "lnv": 425},
        "default_level": 99, "default_diff24h": 2, "default_discharge": 3.0, "default_temp": 11.5, "downstream_order": 1
    },
]
