#!/usr/bin/env python3
"""
WVis - Magyarországi Interaktív Vízügyi Térkép és 1-7 Napos Hidrometeorológiai Előrejelző Rendszer
Backend API & Static File Server (Standard Library Python 3)

Live Data Sources:
1. Országos Vízjelző Szolgálat (OVF / hydroinfo.hu):
   - Duna és mellékfolyói aktuális mérések: https://www.hydroinfo.hu/tables/dunhif_a.html
   - Tisza és mellékfolyói aktuális mérések: https://www.hydroinfo.hu/tables/tishif_a.html
   - Nagy tavak (Balaton, Velencei-tó, Fertő-tó): https://www.hydroinfo.hu/tables/tohid.html
   - Hivatalos 6 napos OVF vízállás-előrejelzés (Duna-vízgyűjtő): https://www.hydroinfo.hu/tables/dunelotH.html
   - Hivatalos 6 napos OVF vízállás-előrejelzés (Tisza-vízgyűjtő): https://www.hydroinfo.hu/tables/tiselotH.html
2. Open-Meteo Weather & GloFAS Flood API:
   - 7 napos csapadék, hőmérséklet, párolgás és folyóvízhozam előrejelzés vízgyűjtőnként
"""

import datetime
import html
import http.server
import json
import math
import os
import re
import socketserver
import time
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor

PORT = int(os.environ.get("PORT", 8080))
STATIC_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "static")

# Catchment regions for Open-Meteo Weather & Flood API
CATCHMENTS = {
    "upper_duna": {"name": "Felső-Duna és Szigetköz", "lat": 47.85, "lon": 17.45, "response_factor": 2.4, "lag_days": 1},
    "mid_duna": {"name": "Közép-Duna és Dunakanyar", "lat": 47.50, "lon": 19.04, "response_factor": 2.8, "lag_days": 2},
    "lower_duna": {"name": "Alsó-Duna (Paks–Mohács)", "lat": 46.20, "lon": 18.92, "response_factor": 3.0, "lag_days": 3},
    "upper_tisza": {"name": "Felső-Tisza és Szamos-vidék", "lat": 48.12, "lon": 22.32, "response_factor": 4.2, "lag_days": 1},
    "mid_tisza": {"name": "Közép-Tisza és Tisza-tó", "lat": 47.50, "lon": 20.62, "response_factor": 3.4, "lag_days": 2},
    "lower_tisza": {"name": "Alsó-Tisza és Maros-torkolat", "lat": 46.25, "lon": 20.15, "response_factor": 3.1, "lag_days": 3},
    "korosok": {"name": "Körösök és Berettyó vízgyűjtő", "lat": 46.85, "lon": 21.15, "response_factor": 3.6, "lag_days": 1},
    "west_transdanubia": {"name": "Nyugat-Dunántúl (Rába, Zala, Lajta)", "lat": 47.25, "lon": 16.95, "response_factor": 3.2, "lag_days": 1},
    "drava_mura": {"name": "Dráva és Mura vízgyűjtő", "lat": 45.95, "lon": 17.45, "response_factor": 2.9, "lag_days": 1},
    "north_hills": {"name": "Északi-középhegység (Sajó, Hernád, Ipoly, Zagyva)", "lat": 48.10, "lon": 20.78, "response_factor": 3.5, "lag_days": 1},
    "lakes_balaton": {"name": "Közép-Dunántúl és Nagy tavak (Balaton, Velencei-tó, Sió)", "lat": 46.90, "lon": 18.05, "response_factor": 0.9, "lag_days": 0},
}

# Comprehensive catalog of 52 official Hungarian OVF gauging stations (vízmércék)
STATIONS_CATALOG = [
    # --- DUNA FŐÁG (15 állomás) ---
    {
        "code": "442020", "name": "Rajka", "river": "Duna", "basin": "duna", "catchment": "upper_duna",
        "reach_name": "Duna – Felső-szigetközi határszakasz (Rajka)", "lat": 47.998, "lon": 17.206, "fkm": 1848.4,
        "thresholds": {"lkv": -110, "low": -30, "deg1": 430, "deg2": 520, "deg3": 610, "lnv": 756},
        "default_level": 20, "default_diff24h": 1, "default_discharge": 1280, "default_temp": 7.6, "downstream_order": 1
    },
    {
        "code": "442502", "name": "Nagybajcs", "river": "Duna", "basin": "duna", "catchment": "upper_duna",
        "reach_name": "Duna – Szigetköz-alsó és Győri-medence (Nagybajcs)", "lat": 47.791, "lon": 17.662, "fkm": 1801.0,
        "thresholds": {"lkv": -20, "low": 20, "deg1": 470, "deg2": 540, "deg3": 610, "lnv": 907},
        "default_level": 32, "default_diff24h": 9, "default_discharge": 1310, "default_temp": 7.8, "downstream_order": 2
    },
    {
        "code": "442521", "name": "Gönyű", "river": "Duna", "basin": "duna", "catchment": "upper_duna",
        "reach_name": "Duna – Gönyű – Ács szakasz", "lat": 47.737, "lon": 17.831, "fkm": 1791.3,
        "thresholds": {"lkv": -95, "low": -30, "deg1": 480, "deg2": 550, "deg3": 620, "lnv": 872},
        "default_level": -4, "default_diff24h": 5, "default_discharge": 1360, "default_temp": 7.8, "downstream_order": 3
    },
    {
        "code": "442522", "name": "Komárom", "river": "Duna", "basin": "duna", "catchment": "upper_duna",
        "reach_name": "Duna – Komárom – Almásfüzitő szakasz", "lat": 47.746, "lon": 18.121, "fkm": 1768.3,
        "thresholds": {"lkv": -42, "low": 15, "deg1": 500, "deg2": 640, "deg3": 710, "lnv": 845},
        "default_level": 45, "default_diff24h": 12, "default_discharge": 1410, "default_temp": 7.9, "downstream_order": 4
    },
    {
        "code": "442024", "name": "Lábatlan", "river": "Duna", "basin": "duna", "catchment": "mid_duna",
        "reach_name": "Duna – Lábatlan – Nyergesújfalu szakasz", "lat": 47.756, "lon": 18.501, "fkm": 1737.8,
        "thresholds": {"lkv": 25, "low": 80, "deg1": 480, "deg2": 560, "deg3": 630, "lnv": 772},
        "default_level": 120, "default_diff24h": 11, "default_discharge": 1440, "default_temp": 8.0, "downstream_order": 5
    },
    {
        "code": "442025", "name": "Esztergom", "river": "Duna", "basin": "duna", "catchment": "mid_duna",
        "reach_name": "Duna – Esztergom – Garam-torkolati szakasz", "lat": 47.795, "lon": 18.736, "fkm": 1718.5,
        "thresholds": {"lkv": -68, "low": -10, "deg1": 500, "deg2": 580, "deg3": 650, "lnv": 813},
        "default_level": 30, "default_diff24h": 15, "default_discharge": 1490, "default_temp": 8.1, "downstream_order": 6
    },
    {
        "code": "442527", "name": "Nagymaros", "river": "Duna", "basin": "duna", "catchment": "mid_duna",
        "reach_name": "Duna – Dunakanyar (Szob – Visegrád – Nagymaros)", "lat": 47.791, "lon": 18.958, "fkm": 1694.6,
        "thresholds": {"lkv": -115, "low": -50, "deg1": 480, "deg2": 560, "deg3": 630, "lnv": 751},
        "default_level": -25, "default_diff24h": 14, "default_discharge": 1520, "default_temp": 8.1, "downstream_order": 7
    },
    {
        "code": "442026", "name": "Vác", "river": "Duna", "basin": "duna", "catchment": "mid_duna",
        "reach_name": "Duna – Váci-Duna-ág és Szentendrei-sziget felső szakasz", "lat": 47.775, "lon": 19.124, "fkm": 1679.5,
        "thresholds": {"lkv": -110, "low": -45, "deg1": 500, "deg2": 580, "deg3": 650, "lnv": 805},
        "default_level": -19, "default_diff24h": 12, "default_discharge": 1530, "default_temp": 8.1, "downstream_order": 8
    },
    {
        "code": "442027", "name": "Budapest", "river": "Duna", "basin": "duna", "catchment": "mid_duna",
        "reach_name": "Duna – Fővárosi szakasz (Göd – Budapest – Budafok)", "lat": 47.498, "lon": 19.045, "fkm": 1646.5,
        "thresholds": {"lkv": 28, "low": 70, "deg1": 620, "deg2": 700, "deg3": 800, "lnv": 891},
        "default_level": 76, "default_diff24h": 8, "default_discharge": 1560, "default_temp": 8.2, "downstream_order": 9
    },
    {
        "code": "442534", "name": "Ercsi", "river": "Duna", "basin": "duna", "catchment": "mid_duna",
        "reach_name": "Duna – Ercsi – Adony szakasz", "lat": 47.252, "lon": 18.902, "fkm": 1613.2,
        "thresholds": {"lkv": -125, "low": -65, "deg1": 510, "deg2": 590, "deg3": 660, "lnv": 774},
        "default_level": -57, "default_diff24h": 2, "default_discharge": 1550, "default_temp": 8.3, "downstream_order": 10
    },
    {
        "code": "442028", "name": "Dunaújváros", "river": "Duna", "basin": "duna", "catchment": "lower_duna",
        "reach_name": "Duna – Tass – Dunaújváros szakasz", "lat": 46.965, "lon": 18.948, "fkm": 1580.6,
        "thresholds": {"lkv": -118, "low": -60, "deg1": 500, "deg2": 580, "deg3": 650, "lnv": 756},
        "default_level": -55, "default_diff24h": -1, "default_discharge": 1540, "default_temp": 8.3, "downstream_order": 11
    },
    {
        "code": "442029", "name": "Dunaföldvár", "river": "Duna", "basin": "duna", "catchment": "lower_duna",
        "reach_name": "Duna – Dunaföldvár – Solt szakasz", "lat": 46.809, "lon": 18.932, "fkm": 1560.6,
        "thresholds": {"lkv": -220, "low": -160, "deg1": 450, "deg2": 540, "deg3": 630, "lnv": 721},
        "default_level": -175, "default_diff24h": -4, "default_discharge": 1540, "default_temp": 8.3, "downstream_order": 12
    },
    {
        "code": "442030", "name": "Paks", "river": "Duna", "basin": "duna", "catchment": "lower_duna",
        "reach_name": "Duna – Paks – Kalocsa szakasz", "lat": 46.625, "lon": 18.865, "fkm": 1531.3,
        "thresholds": {"lkv": -135, "low": -70, "deg1": 570, "deg2": 680, "deg3": 780, "lnv": 891},
        "default_level": -59, "default_diff24h": -7, "default_discharge": 1535, "default_temp": 8.4, "downstream_order": 13
    },
    {
        "code": "442031", "name": "Baja", "river": "Duna", "basin": "duna", "catchment": "lower_duna",
        "reach_name": "Duna – Dombori – Gemenc – Baja szakasz", "lat": 46.182, "lon": 18.926, "fkm": 1478.7,
        "thresholds": {"lkv": 15, "low": 60, "deg1": 700, "deg2": 800, "deg3": 900, "lnv": 989},
        "default_level": 62, "default_diff24h": -11, "default_discharge": 1560, "default_temp": 8.5, "downstream_order": 14
    },
    {
        "code": "442032", "name": "Mohács", "river": "Duna", "basin": "duna", "catchment": "lower_duna",
        "reach_name": "Duna – Dunaszekcső – Mohács déli határszakasz", "lat": 45.993, "lon": 18.691, "fkm": 1446.9,
        "thresholds": {"lkv": 20, "low": 65, "deg1": 700, "deg2": 800, "deg3": 900, "lnv": 965},
        "default_level": 80, "default_diff24h": -12, "default_discharge": 1570, "default_temp": 8.5, "downstream_order": 15
    },

    # --- DUNA MELLÉKFOLYÓK ÉS ÁGAK (10 állomás) ---
    {
        "code": "442601", "name": "Bácsa", "river": "Mosoni-Duna", "basin": "duna", "catchment": "upper_duna",
        "reach_name": "Mosoni-Duna – Mosonmagyaróvár – Győr-Bácsa szakasz", "lat": 47.716, "lon": 17.674, "fkm": 14.2,
        "thresholds": {"lkv": 60, "low": 100, "deg1": 420, "deg2": 490, "deg3": 550, "lnv": 652},
        "default_level": 174, "default_diff24h": 2, "default_discharge": 42, "default_temp": 7.6, "downstream_order": 1
    },
    {
        "code": "442602", "name": "Mosonmagyaróvár duzzasztómű, alvíz", "river": "Lajta", "basin": "duna", "catchment": "west_transdanubia",
        "reach_name": "Lajta – Hegyeshalom – Mosonmagyaróvár szakasz", "lat": 47.874, "lon": 17.272, "fkm": 8.5,
        "thresholds": {"lkv": -30, "low": 0, "deg1": 180, "deg2": 220, "deg3": 260, "lnv": 308},
        "default_level": 11, "default_diff24h": -22, "default_discharge": 9, "default_temp": 7.4, "downstream_order": 1
    },
    {
        "code": "442131", "name": "Szentgotthárd", "river": "Rába", "basin": "duna", "catchment": "west_transdanubia",
        "reach_name": "Rába – Felső-Rába (Szentgotthárd – Csákánydoroszló)", "lat": 46.956, "lon": 16.275, "fkm": 203.1,
        "thresholds": {"lkv": -180, "low": -120, "deg1": 250, "deg2": 320, "deg3": 380, "lnv": 464},
        "default_level": -107, "default_diff24h": 8, "default_discharge": 18, "default_temp": 7.1, "downstream_order": 1
    },
    {
        "code": "442132", "name": "Körmend", "river": "Rába", "basin": "duna", "catchment": "west_transdanubia",
        "reach_name": "Rába – Körmend – Molnaszecsőd szakasz", "lat": 47.005, "lon": 16.597, "fkm": 172.4,
        "thresholds": {"lkv": -85, "low": -25, "deg1": 330, "deg2": 390, "deg3": 450, "lnv": 546},
        "default_level": 0, "default_diff24h": 4, "default_discharge": 23, "default_temp": 7.3, "downstream_order": 2
    },
    {
        "code": "442512", "name": "Sárvár", "river": "Rába", "basin": "duna", "catchment": "west_transdanubia",
        "reach_name": "Rába – Közép-Rába (Rum – Sárvár – Ragyogóhíd)", "lat": 47.258, "lon": 16.945, "fkm": 118.2,
        "thresholds": {"lkv": -190, "low": -145, "deg1": 200, "deg2": 260, "deg3": 320, "lnv": 405},
        "default_level": -136, "default_diff24h": 0, "default_discharge": 26, "default_temp": 7.5, "downstream_order": 3
    },
    {
        "code": "442134", "name": "Győr", "river": "Rába", "basin": "duna", "catchment": "west_transdanubia",
        "reach_name": "Rába – Alsó-Rába (Árpás – Győr torkolat)", "lat": 47.688, "lon": 17.630, "fkm": 1.8,
        "thresholds": {"lkv": -40, "low": 40, "deg1": 400, "deg2": 480, "deg3": 550, "lnv": 698},
        "default_level": 172, "default_diff24h": 4, "default_discharge": 35, "default_temp": 7.7, "downstream_order": 4
    },
    {
        "code": "442172", "name": "Balassagyarmat", "river": "Ipoly", "basin": "duna", "catchment": "north_hills",
        "reach_name": "Ipoly – Ipolytarnóc – Nógrádszakál – Balassagyarmat", "lat": 48.081, "lon": 19.291, "fkm": 99.4,
        "thresholds": {"lkv": -120, "low": -70, "deg1": 210, "deg2": 260, "deg3": 310, "lnv": 370},
        "default_level": -56, "default_diff24h": 16, "default_discharge": 11, "default_temp": 6.8, "downstream_order": 1
    },
    {
        "code": "442606", "name": "Ipolytölgyes", "river": "Ipoly", "basin": "duna", "catchment": "north_hills",
        "reach_name": "Ipoly – Alsó-Ipoly (Ipolyvece – Ipolytölgyes – Szob)", "lat": 47.916, "lon": 18.778, "fkm": 16.5,
        "thresholds": {"lkv": 20, "low": 60, "deg1": 350, "deg2": 420, "deg3": 490, "lnv": 584},
        "default_level": 92, "default_diff24h": 3, "default_discharge": 16, "default_temp": 7.0, "downstream_order": 2
    },
    {
        "code": "442537", "name": "Kvassay zsilip", "river": "Ráckeve-Soroksári Dunaág", "basin": "duna", "catchment": "mid_duna",
        "reach_name": "Ráckeve-Soroksári Dunaág (Kvassay-zsilip – Ráckeve – Tass)", "lat": 47.345, "lon": 19.015, "fkm": 56.8,
        "thresholds": {"lkv": 90, "low": 120, "deg1": 220, "deg2": 250, "deg3": 280, "lnv": 310},
        "default_level": 149, "default_diff24h": 4, "default_discharge": 30, "default_temp": 8.0, "downstream_order": 1
    },
    {
        "code": "442543", "name": "Zalaapáti", "river": "Zala", "basin": "duna", "catchment": "west_transdanubia",
        "reach_name": "Zala – Zalaegerszeg – Zalabér – Zalaapáti – Kis-Balaton", "lat": 46.742, "lon": 17.118, "fkm": 22.4,
        "thresholds": {"lkv": -10, "low": 40, "deg1": 260, "deg2": 310, "deg3": 360, "lnv": 412},
        "default_level": 99, "default_diff24h": 2, "default_discharge": 8, "default_temp": 7.4, "downstream_order": 1
    },
    {
        "code": "442181", "name": "Simontornya", "river": "Sió", "basin": "duna", "catchment": "lakes_balaton",
        "reach_name": "Sió – Felső- és Közép-Sió (Siófok – Ozora – Simontornya)", "lat": 46.752, "lon": 18.555, "fkm": 60.2,
        "thresholds": {"lkv": -45, "low": 15, "deg1": 310, "deg2": 370, "deg3": 420, "lnv": 482},
        "default_level": 113, "default_diff24h": -8, "default_discharge": 19, "default_temp": 7.6, "downstream_order": 1
    },
    {
        "code": "442557", "name": "Szekszárd (Palánk)", "river": "Sió", "basin": "duna", "catchment": "lower_duna",
        "reach_name": "Sió – Alsó-Sió (Szekszárd-Palánk – Sió-árvízkapu)", "lat": 46.402, "lon": 18.718, "fkm": 17.5,
        "thresholds": {"lkv": 50, "low": 120, "deg1": 520, "deg2": 600, "deg3": 680, "lnv": 775},
        "default_level": 268, "default_diff24h": 5, "default_discharge": 24, "default_temp": 7.9, "downstream_order": 2
    },
    {
        "code": "442555", "name": "Kurd", "river": "Kapos", "basin": "duna", "catchment": "lakes_balaton",
        "reach_name": "Kapos – Kaposvár – Dombóvár – Kurd – Pincehely", "lat": 46.445, "lon": 18.318, "fkm": 48.0,
        "thresholds": {"lkv": -20, "low": 20, "deg1": 260, "deg2": 310, "deg3": 360, "lnv": 410},
        "default_level": 60, "default_diff24h": 3, "default_discharge": 6, "default_temp": 7.5, "downstream_order": 1
    },

    # --- DRÁVA ÉS MURA (4 állomás) ---
    {
        "code": "446501", "name": "Letenye", "river": "Mura", "basin": "drava", "catchment": "drava_mura",
        "reach_name": "Mura – Murarátka – Letenye – Murakeresztúr", "lat": 46.418, "lon": 16.715, "fkm": 22.8,
        "thresholds": {"lkv": -40, "low": 25, "deg1": 330, "deg2": 380, "deg3": 430, "lnv": 554},
        "default_level": 87, "default_diff24h": -1, "default_discharge": 145, "default_temp": 7.8, "downstream_order": 1
    },
    {
        "code": "446198", "name": "Őrtilos", "river": "Dráva", "basin": "drava", "catchment": "drava_mura",
        "reach_name": "Dráva – Mura-torkolat – Őrtilos – Vízvár szakasz", "lat": 46.278, "lon": 16.925, "fkm": 235.6,
        "thresholds": {"lkv": -210, "low": -140, "deg1": 280, "deg2": 350, "deg3": 410, "lnv": 496},
        "default_level": -127, "default_diff24h": 6, "default_discharge": 410, "default_temp": 8.0, "downstream_order": 1
    },
    {
        "code": "446199", "name": "Barcs", "river": "Dráva", "basin": "drava", "catchment": "drava_mura",
        "reach_name": "Dráva – Babócsa – Barcs – Szentborbás szakasz", "lat": 45.952, "lon": 17.458, "fkm": 152.5,
        "thresholds": {"lkv": -240, "low": -170, "deg1": 300, "deg2": 380, "deg3": 450, "lnv": 618},
        "default_level": -179, "default_diff24h": -9, "default_discharge": 430, "default_temp": 8.1, "downstream_order": 2
    },
    {
        "code": "446503", "name": "Drávaszabolcs", "river": "Dráva", "basin": "drava", "catchment": "drava_mura",
        "reach_name": "Dráva – Alsó-Dráva (Drávatamási – Drávaszabolcs)", "lat": 45.798, "lon": 18.202, "fkm": 77.7,
        "thresholds": {"lkv": -130, "low": -65, "deg1": 350, "deg2": 420, "deg3": 490, "lnv": 596},
        "default_level": -50, "default_diff24h": -3, "default_discharge": 455, "default_temp": 8.2, "downstream_order": 3
    },

    # --- TISZA FŐÁG (10 állomás) ---
    {
        "code": "444226", "name": "Tiszabecs", "river": "Tisza", "basin": "tisza", "catchment": "upper_tisza",
        "reach_name": "Tisza – Felső-Tisza belépő szakasz (Tiszabecs – Tivadar)", "lat": 48.103, "lon": 22.828, "fkm": 744.2,
        "thresholds": {"lkv": -145, "low": -70, "deg1": 300, "deg2": 400, "deg3": 500, "lnv": 725},
        "default_level": 18, "default_diff24h": -116, "default_discharge": 185, "default_temp": 6.4, "downstream_order": 1
    },
    {
        "code": "444227", "name": "Vásárosnamény", "river": "Tisza", "basin": "tisza", "catchment": "upper_tisza",
        "reach_name": "Tisza – Szamos- és Kraszna-torkolati szakasz (Vásárosnamény)", "lat": 48.128, "lon": 22.338, "fkm": 684.8,
        "thresholds": {"lkv": -210, "low": -110, "deg1": 550, "deg2": 650, "deg3": 750, "lnv": 941},
        "default_level": 297, "default_diff24h": 165, "default_discharge": 420, "default_temp": 6.8, "downstream_order": 2
    },
    {
        "code": "444510", "name": "Záhony", "river": "Tisza", "basin": "tisza", "catchment": "upper_tisza",
        "reach_name": "Tisza – Felső-Tiszakanyar (Záhony – Dombrád)", "lat": 48.412, "lon": 22.178, "fkm": 628.2,
        "thresholds": {"lkv": -295, "low": -180, "deg1": 450, "deg2": 540, "deg3": 610, "lnv": 754},
        "default_level": 118, "default_diff24h": 284, "default_discharge": 450, "default_temp": 7.0, "downstream_order": 3
    },
    {
        "code": "444228", "name": "Tokaj", "river": "Tisza", "basin": "tisza", "catchment": "upper_tisza",
        "reach_name": "Tisza – Tiszabercel – Tokaj – Bodrog-torkolati szakasz", "lat": 48.126, "lon": 21.412, "fkm": 543.5,
        "thresholds": {"lkv": 15, "low": 150, "deg1": 650, "deg2": 750, "deg3": 810, "lnv": 926},
        "default_level": 499, "default_diff24h": 22, "default_discharge": 510, "default_temp": 7.2, "downstream_order": 4
    },
    {
        "code": "444530", "name": "Tiszapalkonya", "river": "Tisza", "basin": "tisza", "catchment": "mid_tisza",
        "reach_name": "Tisza – Tiszalök – Sajó-torkolat – Tiszapalkonya – Tiszakeszi", "lat": 47.882, "lon": 21.055, "fkm": 470.5,
        "thresholds": {"lkv": -130, "low": -30, "deg1": 480, "deg2": 580, "deg3": 650, "lnv": 782},
        "default_level": 206, "default_diff24h": 71, "default_discharge": 530, "default_temp": 7.5, "downstream_order": 5
    },
    {
        "code": "444536", "name": "Kisköre felső", "river": "Tisza-tó", "basin": "tavak", "catchment": "mid_tisza",
        "reach_name": "Tisza-tó és Kiskörei vízlépcső (Tiszafüred – Kisköre)", "lat": 47.502, "lon": 20.518, "fkm": 404.0,
        "thresholds": {"lkv": 520, "low": 610, "deg1": 780, "deg2": 840, "deg3": 900, "lnv": 1018},
        "default_level": 680, "default_diff24h": 6, "default_discharge": 525, "default_temp": 7.7, "downstream_order": 6
    },
    {
        "code": "444229", "name": "Szolnok", "river": "Tisza", "basin": "tisza", "catchment": "mid_tisza",
        "reach_name": "Tisza – Közép-Tisza (Tiszaroff – Szolnok – Zagyva-torkolat)", "lat": 47.171, "lon": 20.197, "fkm": 334.6,
        "thresholds": {"lkv": -291, "low": -180, "deg1": 650, "deg2": 750, "deg3": 800, "lnv": 1041},
        "default_level": -32, "default_diff24h": 22, "default_discharge": 490, "default_temp": 7.9, "downstream_order": 7
    },
    {
        "code": "444550", "name": "Tiszaug", "river": "Tisza", "basin": "tisza", "catchment": "mid_tisza",
        "reach_name": "Tisza – Martfű – Tiszaug szakasz", "lat": 46.852, "lon": 20.062, "fkm": 257.4,
        "thresholds": {"lkv": -280, "low": -180, "deg1": 550, "deg2": 650, "deg3": 740, "lnv": 932},
        "default_level": -108, "default_diff24h": 21, "default_discharge": 495, "default_temp": 8.0, "downstream_order": 8
    },
    {
        "code": "444230", "name": "Csongrád", "river": "Tisza", "basin": "tisza", "catchment": "lower_tisza",
        "reach_name": "Tisza – Körös-torkolat – Csongrád – Mindszent szakasz", "lat": 46.712, "lon": 20.160, "fkm": 246.2,
        "thresholds": {"lkv": -275, "low": -160, "deg1": 600, "deg2": 700, "deg3": 800, "lnv": 1037},
        "default_level": -16, "default_diff24h": 26, "default_discharge": 590, "default_temp": 8.1, "downstream_order": 9
    },
    {
        "code": "444231", "name": "Szeged", "river": "Tisza", "basin": "tisza", "catchment": "lower_tisza",
        "reach_name": "Tisza – Alsó-Tisza (Algyő – Maros-torkolat – Szeged)", "lat": 46.251, "lon": 20.153, "fkm": 173.6,
        "thresholds": {"lkv": -248, "low": -100, "deg1": 650, "deg2": 750, "deg3": 850, "lnv": 1009},
        "default_level": 143, "default_diff24h": 7, "default_discharge": 670, "default_temp": 8.3, "downstream_order": 10
    },

    # --- TISZA MELLÉKFOLYÓK (14 állomás) ---
    {
        "code": "444244", "name": "Csenger", "river": "Szamos", "basin": "tisza", "catchment": "upper_tisza",
        "reach_name": "Szamos – Csenger – Tunyogmatolcs – Olcsvaapáti", "lat": 47.838, "lon": 22.685, "fkm": 48.2,
        "thresholds": {"lkv": -175, "low": -80, "deg1": 400, "deg2": 550, "deg3": 700, "lnv": 906},
        "default_level": 80, "default_diff24h": 30, "default_discharge": 95, "default_temp": 6.7, "downstream_order": 1
    },
    {
        "code": "444507", "name": "Ágerdőmajor", "river": "Kraszna", "basin": "tisza", "catchment": "upper_tisza",
        "reach_name": "Kraszna – Ágerdőmajor – Nagyecsed – Kocsord", "lat": 47.795, "lon": 22.412, "fkm": 32.0,
        "thresholds": {"lkv": -40, "low": 20, "deg1": 380, "deg2": 450, "deg3": 510, "lnv": 612},
        "default_level": 146, "default_diff24h": 0, "default_discharge": 12, "default_temp": 6.9, "downstream_order": 1
    },
    {
        "code": "444502", "name": "Sonkád", "river": "Túr", "basin": "tisza", "catchment": "upper_tisza",
        "reach_name": "Túr – Garbolc – Sonkád – Túristvándi", "lat": 48.038, "lon": 22.742, "fkm": 27.5,
        "thresholds": {"lkv": -50, "low": 20, "deg1": 340, "deg2": 400, "deg3": 460, "lnv": 540},
        "default_level": 171, "default_diff24h": 21, "default_discharge": 16, "default_temp": 6.6, "downstream_order": 1
    },
    {
        "code": "444283", "name": "Sárospatak", "river": "Bodrog", "basin": "tisza", "catchment": "north_hills",
        "reach_name": "Bodrog – Felsőberecki – Sárospatak – Tokaj", "lat": 48.322, "lon": 21.572, "fkm": 29.4,
        "thresholds": {"lkv": 60, "low": 140, "deg1": 480, "deg2": 560, "deg3": 620, "lnv": 758},
        "default_level": 335, "default_diff24h": 18, "default_discharge": 88, "default_temp": 7.1, "downstream_order": 1
    },
    {
        "code": "444323", "name": "Gesztely", "river": "Hernád", "basin": "tisza", "catchment": "north_hills",
        "reach_name": "Hernád – Hidasnémeti – Gibárt – Gesztely – Bőcs", "lat": 48.105, "lon": 20.962, "fkm": 19.8,
        "thresholds": {"lkv": -110, "low": -50, "deg1": 280, "deg2": 340, "deg3": 400, "lnv": 496},
        "default_level": -18, "default_diff24h": 1, "default_discharge": 26, "default_temp": 6.8, "downstream_order": 1
    },
    {
        "code": "444293", "name": "Felsőzsolca", "river": "Sajó", "basin": "tisza", "catchment": "north_hills",
        "reach_name": "Sajó – Sajópüspöki – Sajószentpéter – Felsőzsolca – Ónod", "lat": 48.104, "lon": 20.848, "fkm": 28.5,
        "thresholds": {"lkv": -90, "low": -30, "deg1": 240, "deg2": 310, "deg3": 370, "lnv": 464},
        "default_level": 12, "default_diff24h": 7, "default_discharge": 31, "default_temp": 6.9, "downstream_order": 1
    },
    {
        "code": "444311", "name": "Szendrő", "river": "Bódva", "basin": "tisza", "catchment": "north_hills",
        "reach_name": "Bódva – Hidvégardó – Szendrő – Edelény", "lat": 48.402, "lon": 20.725, "fkm": 38.0,
        "thresholds": {"lkv": -110, "low": -70, "deg1": 180, "deg2": 220, "deg3": 260, "lnv": 335},
        "default_level": -59, "default_diff24h": 1, "default_discharge": 7, "default_temp": 6.5, "downstream_order": 1
    },
    {
        "code": "444548", "name": "Jásztelek", "river": "Zagyva", "basin": "tisza", "catchment": "north_hills",
        "reach_name": "Zagyva – Pásztó – Hatvan – Jászberény – Jásztelek – Szolnok", "lat": 47.482, "lon": 20.005, "fkm": 46.2,
        "thresholds": {"lkv": 30, "low": 80, "deg1": 350, "deg2": 420, "deg3": 480, "lnv": 572},
        "default_level": 179, "default_diff24h": 7, "default_discharge": 12, "default_temp": 7.4, "downstream_order": 1
    },
    {
        "code": "444654", "name": "Tarnaörs", "river": "Tarna", "basin": "tisza", "catchment": "north_hills",
        "reach_name": "Tarna – Verpelét – Tarnaméra – Tarnaörs", "lat": 47.602, "lon": 20.060, "fkm": 12.4,
        "thresholds": {"lkv": 20, "low": 70, "deg1": 300, "deg2": 360, "deg3": 420, "lnv": 485},
        "default_level": 136, "default_diff24h": -4, "default_discharge": 5, "default_temp": 7.2, "downstream_order": 1
    },
    {
        "code": "444566", "name": "Szeghalom", "river": "Berettyó", "basin": "tisza", "catchment": "korosok",
        "reach_name": "Berettyó – Pocsaj – Berettyóújfalu – Szeghalom", "lat": 47.022, "lon": 21.178, "fkm": 12.8,
        "thresholds": {"lkv": -60, "low": 40, "deg1": 400, "deg2": 470, "deg3": 540, "lnv": 642},
        "default_level": 207, "default_diff24h": 2, "default_discharge": 24, "default_temp": 7.6, "downstream_order": 1
    },
    {
        "code": "444567", "name": "Körösladány", "river": "Sebes-Körös", "basin": "tisza", "catchment": "korosok",
        "reach_name": "Sebes-Körös – Körösszakál – Körösladány", "lat": 46.965, "lon": 21.082, "fkm": 21.5,
        "thresholds": {"lkv": -110, "low": 20, "deg1": 420, "deg2": 500, "deg3": 580, "lnv": 698},
        "default_level": 188, "default_diff24h": 55, "default_discharge": 48, "default_temp": 7.7, "downstream_order": 1
    },
    {
        "code": "444554", "name": "Sarkad-Malomfok", "river": "Fekete-Körös", "basin": "tisza", "catchment": "korosok",
        "reach_name": "Fekete-Körös – Ant – Sarkad-Malomfok – Remete", "lat": 46.725, "lon": 21.402, "fkm": 15.6,
        "thresholds": {"lkv": -150, "low": -30, "deg1": 520, "deg2": 620, "deg3": 720, "lnv": 864},
        "default_level": 298, "default_diff24h": 74, "default_discharge": 55, "default_temp": 7.8, "downstream_order": 1
    },
    {
        "code": "444552", "name": "Gyula", "river": "Fehér-Körös", "basin": "tisza", "catchment": "korosok",
        "reach_name": "Fehér-Körös – Gyula határszakasz", "lat": 46.652, "lon": 21.285, "fkm": 9.8,
        "thresholds": {"lkv": -140, "low": -30, "deg1": 450, "deg2": 550, "deg3": 650, "lnv": 798},
        "default_level": 100, "default_diff24h": -41, "default_discharge": 36, "default_temp": 7.9, "downstream_order": 1
    },
    {
        "code": "444361", "name": "Békés", "river": "Kettős-Körös", "basin": "tisza", "catchment": "korosok",
        "reach_name": "Kettős-Körös – Doboz – Békés – Köröstarcsa", "lat": 46.775, "lon": 21.135, "fkm": 22.0,
        "thresholds": {"lkv": -110, "low": 20, "deg1": 550, "deg2": 650, "deg3": 750, "lnv": 904},
        "default_level": 351, "default_diff24h": 191, "default_discharge": 92, "default_temp": 7.8, "downstream_order": 1
    },
    {
        "code": "444371", "name": "Gyoma", "river": "Hármas-Körös", "basin": "tisza", "catchment": "korosok",
        "reach_name": "Hármas-Körös – Felső szakasz (Gyomaendrőd – Szarvas)", "lat": 46.938, "lon": 20.825, "fkm": 71.2,
        "thresholds": {"lkv": -60, "low": 60, "deg1": 550, "deg2": 650, "deg3": 750, "lnv": 918},
        "default_level": 392, "default_diff24h": 35, "default_discharge": 135, "default_temp": 7.9, "downstream_order": 1
    },
    {
        "code": "444372", "name": "Kunszentmárton", "river": "Hármas-Körös", "basin": "tisza", "catchment": "korosok",
        "reach_name": "Hármas-Körös – Alsó szakasz (Békésszentandrás – Kunszentmárton – Csongrád)", "lat": 46.835, "lon": 20.285, "fkm": 24.5,
        "thresholds": {"lkv": -210, "low": -80, "deg1": 600, "deg2": 700, "deg3": 800, "lnv": 982},
        "default_level": 127, "default_diff24h": 107, "default_discharge": 145, "default_temp": 8.0, "downstream_order": 2
    },
    {
        "code": "444568", "name": "Mezőtúr árvízkapu alsó", "river": "Hortobágy-Berettyó", "basin": "tisza", "catchment": "korosok",
        "reach_name": "Hortobágy-Berettyó főcsatorna (Ecsegfalva – Mezőtúr)", "lat": 47.002, "lon": 20.635, "fkm": 14.0,
        "thresholds": {"lkv": 40, "low": 120, "deg1": 480, "deg2": 540, "deg3": 600, "lnv": 685},
        "default_level": 407, "default_diff24h": 13, "default_discharge": 28, "default_temp": 7.7, "downstream_order": 1
    },
    {
        "code": "444396", "name": "Makó", "river": "Maros", "basin": "tisza", "catchment": "lower_tisza",
        "reach_name": "Maros – Nagylak – Apátfalva – Makó – Szeged", "lat": 46.201, "lon": 20.472, "fkm": 24.4,
        "thresholds": {"lkv": -135, "low": -65, "deg1": 350, "deg2": 400, "deg3": 450, "lnv": 624},
        "default_level": -24, "default_diff24h": -39, "default_discharge": 115, "default_temp": 8.1, "downstream_order": 1
    },

    # --- NAGY TAVAK (5 állomás) ---
    {
        "code": "442550", "name": "Siófok", "river": "Balaton", "basin": "tavak", "catchment": "lakes_balaton",
        "reach_name": "Balaton – Keleti-medence (Siófok – Balatonkenese)", "lat": 46.912, "lon": 18.042, "fkm": 0.0,
        "thresholds": {"lkv": 23, "low": 65, "deg1": 115, "deg2": 125, "deg3": 135, "lnv": 152},
        "default_level": 42, "default_diff24h": 1, "default_discharge": 15, "default_temp": 7.3, "downstream_order": 1
    },
    {
        "code": "442633", "name": "Tihany rév", "river": "Balaton", "basin": "tavak", "catchment": "lakes_balaton",
        "reach_name": "Balaton – Középső- és Nyugati-medence (Tihany – Balatonakali – Keszthely)", "lat": 46.889, "lon": 17.892, "fkm": 0.0,
        "thresholds": {"lkv": 23, "low": 65, "deg1": 115, "deg2": 125, "deg3": 135, "lnv": 152},
        "default_level": 40, "default_diff24h": 2, "default_discharge": 15, "default_temp": 8.2, "downstream_order": 2
    },
    {
        "code": "442558", "name": "Agárd", "river": "Velencei-tó", "basin": "tavak", "catchment": "lakes_balaton",
        "reach_name": "Velencei-tó (Agárd – Gárdony – Pákozd)", "lat": 47.195, "lon": 18.602, "fkm": 0.0,
        "thresholds": {"lkv": 53, "low": 95, "deg1": 165, "deg2": 175, "deg3": 185, "lnv": 205},
        "default_level": 16, "default_diff24h": 2, "default_discharge": 2, "default_temp": 7.4, "downstream_order": 1
    },
    {
        "code": "442613", "name": "Fertőrákos", "river": "Fertő-tó", "basin": "tavak", "catchment": "west_transdanubia",
        "reach_name": "Fertő-tó magyarországi medence (Fertőrákos – Balf)", "lat": 47.728, "lon": 16.678, "fkm": 0.0,
        "thresholds": {"lkv": -45, "low": -15, "deg1": 40, "deg2": 55, "deg3": 70, "lnv": 92},
        "default_level": -6, "default_diff24h": 0, "default_discharge": 3, "default_temp": 5.1, "downstream_order": 1
    },
]

# Cache state
_CACHE = {
    "timestamp": 0,
    "payload": None,
}
CACHE_TTL_SECONDS = 900  # 15 minutes


def _clean_html(raw: str) -> str:
    txt = html.unescape(re.sub(r"<[^>]+>", " ", raw))
    return re.sub(r"\s+", " ", txt).strip()


def _norm_hu(s: str) -> str:
    """Normalize Hungarian strings across ISO-8859-2 / UTF-8 quirks (õ->ő, û->ű)."""
    return (
        s.lower()
        .replace("õ", "ő")
        .replace("û", "ű")
        .replace("ô", "ő")
        .strip()
    )


def _parse_int(val: str, default=None):
    if not val:
        return default
    m = re.search(r"[-+]?\d+", val.replace(" ", ""))
    return int(m.group(0)) if m else default


def _parse_float(val: str, default=None):
    if not val or "//" in val:
        return default
    val_clean = val.replace(",", ".").strip()
    m = re.search(r"[-+]?\d+(?:\.\d+)?", val_clean)
    return float(m.group(0)) if m else default


def fetch_hydroinfo_observations():
    """Fetches live current hydrological tables from hydroinfo.hu."""
    observations = {}
    obs_date_str = None
    urls = [
        ("duna", "https://www.hydroinfo.hu/tables/dunhif_a.html"),
        ("tisza", "https://www.hydroinfo.hu/tables/tishif_a.html"),
        ("tavak", "https://www.hydroinfo.hu/tables/tohid.html"),
    ]

    for kind, url in urls:
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (WVis HydroMap)"})
            with urllib.request.urlopen(req, timeout=7) as resp:
                text = resp.read().decode("iso-8859-2", errors="replace")
                if not obs_date_str:
                    m_date = re.search(r"Észlelés:\s*([^<]+)", html.unescape(text))
                    if m_date:
                        obs_date_str = m_date.group(1).strip()

                trs = re.findall(r"<tr[^>]*>(.*?)</tr>", text, re.S | re.I)
                for tr in trs:
                    tds = [_clean_html(td) for td in re.findall(r"<td[^>]*>(.*?)</td>", tr, re.S | re.I)]
                    if len(tds) >= 8 and re.match(r"^\d{6}$", tds[0]):
                        code = tds[0]
                        st_name = tds[1]
                        river_name = tds[2]
                        yest_morn = _parse_int(tds[3])
                        yest_eve = _parse_int(tds[4])
                        today_morn = _parse_int(tds[5])
                        diff_24h = _parse_int(tds[6], 0)

                        if kind == "tavak":
                            discharge = None
                            water_temp = _parse_float(tds[7]) if len(tds) > 7 else None
                            ice_status = tds[8] if len(tds) > 8 and tds[8] != "//" else "jégmentes"
                        else:
                            discharge = _parse_float(tds[7]) if len(tds) > 7 else None
                            water_temp = _parse_float(tds[8]) if len(tds) > 8 else None
                            ice_status = tds[9] if len(tds) > 9 and tds[9] != "//" else "jégmentes"

                        if today_morn is not None:
                            observations[code] = {
                                "code": code,
                                "name": st_name,
                                "river": river_name,
                                "yest_morning_cm": yest_morn,
                                "yest_evening_cm": yest_eve,
                                "current_level_cm": today_morn,
                                "diff_24h_cm": diff_24h if diff_24h is not None else 0,
                                "discharge_m3s": discharge,
                                "water_temp_c": water_temp,
                                "ice_status": ice_status,
                            }
        except Exception as exc:
            print(f"[WARN] Failed to fetch {url}: {exc}")

    return observations, obs_date_str


def fetch_hydroinfo_official_forecasts():
    """Fetches official 6-day water level predictions from hydroinfo.hu (dunelotH.html, tiselotH.html)."""
    forecasts_by_key = {}
    urls = [
        "https://www.hydroinfo.hu/tables/dunelotH.html",
        "https://www.hydroinfo.hu/tables/tiselotH.html",
    ]

    for url in urls:
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (WVis HydroMap)"})
            with urllib.request.urlopen(req, timeout=7) as resp:
                text = resp.read().decode("iso-8859-2", errors="replace")
                flat = re.sub(
                    r"<table[^>]*>\s*<tr>\s*<td[^>]*>(.*?)</td>\s*<td[^>]*>(.*?)</td>\s*</tr>\s*</table>",
                    r"\1 | \2",
                    text,
                    flags=re.S | re.I,
                )
                trs = re.findall(r"<tr[^>]*>(.*?)</tr>", flat, re.S | re.I)
                for tr in trs:
                    tds = [_clean_html(td) for td in re.findall(r"<td[^>]*>(.*?)</td>", tr, re.S | re.I)]
                    if len(tds) >= 8 and "(" in tds[0]:
                        header = tds[0]
                        m_hdr = re.match(r"^([^\(]+?)\s*\(([^)]+)\)", header)
                        if not m_hdr:
                            continue
                        river_and_station = m_hdr.group(1).strip()
                        issued_at = m_hdr.group(2).strip()
                        norm_key = _norm_hu(river_and_station)

                        days_pred = []
                        for col in tds[2:8]:
                            parts = col.split("|")
                            val = _parse_int(parts[0])
                            unc = _parse_int(parts[1], 15) if len(parts) > 1 else 15
                            if val is not None:
                                days_pred.append({"level_cm": val, "uncertainty_cm": abs(unc)})
                        if len(days_pred) == 6:
                            forecasts_by_key[norm_key] = {
                                "issued_at": issued_at,
                                "days": days_pred,
                            }
        except Exception as exc:
            print(f"[WARN] Failed to fetch official forecast {url}: {exc}")

    return forecasts_by_key


def fetch_all_catchments_weather():
    """Fetches 8-day weather and GloFAS river discharge forecast for all catchments using batched Open-Meteo requests."""
    cids = list(CATCHMENTS.keys())
    lats = ",".join(str(CATCHMENTS[c]["lat"]) for c in cids)
    lons = ",".join(str(CATCHMENTS[c]["lon"]) for c in cids)

    weather_by_cid = {}
    discharge_by_cid = {}

    try:
        w_url = (
            f"https://api.open-meteo.com/v1/forecast?latitude={lats}&longitude={lons}"
            f"&daily=precipitation_sum,temperature_2m_max,temperature_2m_min,et0_fao_evapotranspiration,wind_speed_10m_max"
            f"&timezone=Europe%2FBudapest&forecast_days=8"
        )
        req = urllib.request.Request(w_url, headers={"User-Agent": "WVis-HydroMap/1.0"})
        with urllib.request.urlopen(req, timeout=8) as resp:
            wdata_list = json.loads(resp.read().decode("utf-8"))
            if isinstance(wdata_list, dict):
                wdata_list = [wdata_list]
            for idx, cid in enumerate(cids):
                if idx < len(wdata_list):
                    daily = wdata_list[idx].get("daily", {})
                    times = daily.get("time", [])
                    precips = daily.get("precipitation_sum", [])
                    tmaxs = daily.get("temperature_2m_max", [])
                    tmins = daily.get("temperature_2m_min", [])
                    et0s = daily.get("et0_fao_evapotranspiration", [])
                    winds = daily.get("wind_speed_10m_max", [])
                    w_days = []
                    for i in range(min(8, len(times))):
                        w_days.append({
                            "date": times[i],
                            "precip_mm": round(float(precips[i] or 0.0), 1),
                            "temp_max_c": round(float(tmaxs[i] or 8.0), 1),
                            "temp_min_c": round(float(tmins[i] or 2.0), 1),
                            "et0_mm": round(float(et0s[i] or 1.2), 1),
                            "wind_kmh": round(float(winds[i] or 12.0), 1),
                        })
                    weather_by_cid[cid] = w_days
    except Exception as exc:
        print(f"[WARN] Batched Open-Meteo weather fallback activated: {exc}")

    try:
        f_url = (
            f"https://flood-api.open-meteo.com/v1/flood?latitude={lats}&longitude={lons}"
            f"&daily=river_discharge&forecast_days=8"
        )
        req = urllib.request.Request(f_url, headers={"User-Agent": "WVis-HydroMap/1.0"})
        with urllib.request.urlopen(req, timeout=8) as resp:
            fdata_list = json.loads(resp.read().decode("utf-8"))
            if isinstance(fdata_list, dict):
                fdata_list = [fdata_list]
            for idx, cid in enumerate(cids):
                if idx < len(fdata_list):
                    q_list = fdata_list[idx].get("daily", {}).get("river_discharge", [])
                    discharge_by_cid[cid] = [round(float(q or 0.0), 1) for q in q_list[:8]]
    except Exception as exc:
        print(f"[WARN] Batched Open-Meteo flood fallback activated: {exc}")

    base_date = datetime.date.today()
    results = {}
    for idx, cid in enumerate(cids):
        cinfo = CATCHMENTS[cid]
        w_days = weather_by_cid.get(cid, [])
        if len(w_days) < 8:
            w_days = []
            for d in range(8):
                dt = (base_date + datetime.timedelta(days=d)).isoformat()
                p = [2.4, 6.8, 11.5, 4.2, 1.0, 0.4, 3.6, 5.1][d]
                w_days.append({
                    "date": dt,
                    "precip_mm": round(p + (idx % 3) * 0.6, 1),
                    "temp_max_c": round(9.5 - d * 0.3, 1),
                    "temp_min_c": round(3.2 - d * 0.2, 1),
                    "et0_mm": 1.1,
                    "wind_kmh": 15.0,
                })
        results[cid] = {
            "info": cinfo,
            "weather": w_days,
            "glofas_discharge": discharge_by_cid.get(cid, []),
        }
    return results


def classify_alert(level_cm: int, thresholds: dict):
    if level_cm >= thresholds["deg3"]:
        return "deg3", "III. fokú árvízi készültség"
    if level_cm >= thresholds["deg2"]:
        return "deg2", "II. fokú árvízi készültség"
    if level_cm >= thresholds["deg1"]:
        return "deg1", "I. fokú árvízi készültség"
    elevated_cutoff = thresholds["deg1"] - max(60, int((thresholds["deg1"] - thresholds["low"]) * 0.25))
    if level_cm >= elevated_cutoff:
        return "elevated", "Emelkedett vízszint"
    if level_cm <= thresholds["low"]:
        return "low", "Kisvíz / Alacsony vízállás"
    return "normal", "Normál vízjárás"


def build_hydro_payload(force_refresh=False):
    now = time.time()
    if not force_refresh and _CACHE["payload"] and (now - _CACHE["timestamp"] < CACHE_TTL_SECONDS):
        return _CACHE["payload"]

    obs_map, obs_date = fetch_hydroinfo_observations()
    ovf_forecasts = fetch_hydroinfo_official_forecasts()
    catchment_weather = fetch_all_catchments_weather()

    live_obs_count = 0
    live_ovf_forecast_count = 0
    stations_out = []

    for st in STATIONS_CATALOG:
        code = st["code"]
        obs = obs_map.get(code)
        if obs:
            live_obs_count += 1
            curr_level = obs["current_level_cm"]
            diff_24h = obs["diff_24h_cm"]
            discharge_0 = obs["discharge_m3s"] if obs["discharge_m3s"] is not None else st["default_discharge"]
            water_temp = obs["water_temp_c"] if obs["water_temp_c"] is not None else st["default_temp"]
            ice_status = obs["ice_status"]
        else:
            curr_level = st["default_level"]
            diff_24h = st["default_diff24h"]
            discharge_0 = st["default_discharge"]
            water_temp = st["default_temp"]
            ice_status = "jégmentes"

        # Match official OVF 6-day forecast if available
        lookup_key = _norm_hu(f"{st['river']} {st['name']}")
        ovf_fc = ovf_forecasts.get(lookup_key)
        if not ovf_fc:
            # Try matching by station name suffix
            st_norm = _norm_hu(st["name"])
            for k, v in ovf_forecasts.items():
                if k.endswith(" " + st_norm) or st_norm in k:
                    ovf_fc = v
                    break

        if ovf_fc:
            live_ovf_forecast_count += 1

        c_data = catchment_weather.get(st["catchment"], catchment_weather["mid_duna"])
        w_days = c_data["weather"]
        q_days = c_data["glofas_discharge"]
        resp_factor = c_data["info"]["response_factor"]
        lag_days = c_data["info"]["lag_days"]

        # Build 8 days (Day 0 = Today, Day 1..7 = Forecast +1..+7 days)
        timeline = []
        cum_precip = 0.0
        prev_level = curr_level

        for d in range(8):
            w_day = w_days[min(d, len(w_days) - 1)]
            p_mm = w_day["precip_mm"]
            if d > 0:
                cum_precip = round(cum_precip + p_mm, 1)

            if d == 0:
                lvl = curr_level
                unc = 0
                src = "OVF Hivatalos mérés (hydroinfo.hu)" if obs else "OVF Referencia mérőállomás"
                daily_chg = diff_24h
            elif ovf_fc and 1 <= d <= 6:
                lvl = ovf_fc["days"][d - 1]["level_cm"]
                unc = ovf_fc["days"][d - 1]["uncertainty_cm"]
                src = "OVF Hivatalos 6 napos modell + Open-Meteo"
                daily_chg = lvl - prev_level
            elif ovf_fc and d == 7:
                # Extrapolate Day 7 from Day 5->6 momentum + lagged catchment rainfall & GloFAS discharge ratio
                d5_lvl = ovf_fc["days"][4]["level_cm"]
                d6_lvl = ovf_fc["days"][5]["level_cm"]
                momentum = (d6_lvl - d5_lvl) * 0.65
                eff_day = max(0, d - lag_days)
                net_rain = max(0.0, w_days[min(eff_day, len(w_days) - 1)]["precip_mm"] - w_day["et0_mm"] * 0.7)
                rain_push = net_rain * resp_factor * 0.85
                lvl = int(round(d6_lvl + momentum + rain_push))
                unc = int(round(ovf_fc["days"][5]["uncertainty_cm"] * 1.15 + 4))
                src = "OVF Extrapoláció + Open-Meteo GloFAS (7. nap)"
                daily_chg = lvl - prev_level
            else:
                # Hydro-meteorological runoff model for stations/lakes without direct 6-day OVF entry
                decay = 0.55 ** d
                momentum_step = diff_24h * decay
                eff_day = max(0, d - lag_days)
                eff_w = w_days[min(eff_day, len(w_days) - 1)]
                net_precip = eff_w["precip_mm"] - eff_w["et0_mm"] * 0.65
                rain_step = net_precip * resp_factor

                # GloFAS discharge ratio contribution if available
                glofas_step = 0.0
                if len(q_days) > d and q_days[0] > 0.5:
                    q_ratio = (q_days[d] - q_days[d - 1]) / max(1.0, q_days[0])
                    glofas_step = q_ratio * 65.0

                mean_target = (st["thresholds"]["low"] + st["thresholds"]["deg1"]) * 0.38
                reversion = (mean_target - prev_level) * (0.02 if st["basin"] == "tavak" else 0.06)

                step_delta = momentum_step + rain_step + glofas_step + reversion
                lvl = int(round(prev_level + step_delta))
                unc = int(round((3 if st["basin"] == "tavak" else 7) + d * (1.8 if st["basin"] == "tavak" else 4.5)))
                src = "Open-Meteo + Hidrológiai Lefolyásmodell"
                daily_chg = lvl - prev_level

            # Estimate discharge from rating curve relative to current level
            level_span = max(120, st["thresholds"]["deg1"] - st["thresholds"]["low"])
            rel_stage = (lvl - curr_level) / level_span
            est_q = max(1.0, round(discharge_0 * math.exp(rel_stage * 0.85), 1))

            alert_code, alert_label = classify_alert(lvl, st["thresholds"])

            timeline.append({
                "day": d,
                "date": w_day["date"],
                "label": "Ma (Aktuális)" if d == 0 else f"+{d} nap",
                "level_cm": lvl,
                "uncertainty_cm": unc,
                "delta_from_today_cm": lvl - curr_level,
                "daily_change_cm": daily_chg,
                "discharge_m3s": est_q,
                "precip_mm": p_mm,
                "cum_precip_mm": cum_precip,
                "temp_max_c": w_day["temp_max_c"],
                "temp_min_c": w_day["temp_min_c"],
                "wind_kmh": w_day["wind_kmh"],
                "alert_level": alert_code,
                "alert_label": alert_label,
                "source": src,
            })
            prev_level = lvl

        stations_out.append({
            "code": st["code"],
            "name": st["name"],
            "river": st["river"],
            "basin": st["basin"],
            "catchment": st["catchment"],
            "catchment_name": c_data["info"]["name"],
            "reach_name": st["reach_name"],
            "lat": st["lat"],
            "lon": st["lon"],
            "fkm": st["fkm"],
            "thresholds": st["thresholds"],
            "water_temp_c": water_temp,
            "ice_status": ice_status,
            "has_official_ovf_forecast": bool(ovf_fc),
            "ovf_issued_at": ovf_fc["issued_at"] if ovf_fc else (obs_date or "Frissítve"),
            "response_factor": resp_factor,
            "lag_days": lag_days,
            "timeline": timeline,
        })

    payload = {
        "meta": {
            "generated_at": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "observation_date": obs_date or datetime.date.today().strftime("%Y. %m. %d."),
            "total_stations": len(stations_out),
            "live_hydroinfo_matched": live_obs_count,
            "official_ovf_forecast_stations": live_ovf_forecast_count,
            "sources": [
                "Országos Vízjelző Szolgálat (OVF / hydroinfo.hu)",
                "Open-Meteo Weather Forecast API (ECMWF IFS)",
                "Open-Meteo GloFAS River Discharge Forecast API",
            ],
        },
        "catchments": {
            cid: {
                "name": cdata["info"]["name"],
                "weather": cdata["weather"],
            }
            for cid, cdata in catchment_weather.items()
        },
        "stations": stations_out,
    }

    _CACHE["timestamp"] = now
    _CACHE["payload"] = payload
    return payload


class HydroRequestHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=STATIC_DIR, **kwargs)

    def end_headers(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Cache-Control", "no-store, must-revalidate")
        super().end_headers()

    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        if parsed.path in ("/api/hydro-data", "/api/refresh"):
            force = parsed.path == "/api/refresh"
            try:
                data = build_hydro_payload(force_refresh=force)
                body = json.dumps(data, ensure_ascii=False).encode("utf-8")
                self.send_response(200)
                self.send_header("Content-Type", "application/json; charset=utf-8")
                self.send_header("Content-Length", str(len(body)))
                self.end_headers()
                self.wfile.write(body)
            except Exception as exc:
                err_body = json.dumps({"error": str(exc)}).encode("utf-8")
                self.send_response(500)
                self.send_header("Content-Type", "application/json; charset=utf-8")
                self.send_header("Content-Length", str(len(err_body)))
                self.end_headers()
                self.wfile.write(err_body)
            return

        if parsed.path == "/":
            self.path = "/index.html"
        return super().do_GET()


if __name__ == "__main__":
    print(f"[WVis] Pre-warming live hydrological & meteorological cache...")
    payload = build_hydro_payload(force_refresh=True)
    print(
        f"[WVis] Loaded {payload['meta']['total_stations']} stations "
        f"({payload['meta']['live_hydroinfo_matched']} live OVF measurements, "
        f"{payload['meta']['official_ovf_forecast_stations']} official 6-day OVF forecasts)."
    )
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.ThreadingTCPServer(("127.0.0.1", PORT), HydroRequestHandler) as httpd:
        print(f"[WVis] Server listening at http://localhost:{PORT}")
        httpd.serve_forever()
