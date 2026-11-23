/**
 * Hungary's Top 10 Water Retention and Storage Plans — Interactive Leaflet Layer
 * Hover card + 5-second explanatory hydrological cross-section animation for each plan
 */
(() => {
  "use strict";

  const ANIM_DURATION_MS = 5000; // 5.0-second animation cycle

  const RETENTION_PLANS = [
    {
      id: 1,
      shortName: "Flood-MAR (Homokhátság & Nyírség)",
      title: "Flood-MAR — Irányított Felszín Alatti Víztározás",
      region: "Duna–Tisza közi Homokhátság (Kecskemét–Kiskunhalas) & Nyírség",
      lat: 46.62,
      lon: 19.55,
      radiusMeters: 28000,
      secondaryZones: [{ lat: 47.88, lon: 21.95, radiusMeters: 20000, label: "Nyírségi Flood-MAR zóna" }],
      color: "#38bdf8",
      volume: "1,5–3,0 Mrd m³",
      evap: "~0% (Föld alatt)",
      precedent: "Kalifornia (Central Valley Flood-MAR)",
      neighborImpact: "Pozitív (Szerbia / Észak-Bácska talajvízszintjét is emeli)",
      desc: "A nyílt víztározók 1000 mm/év párolgási vesztesége helyett a tavaszi/nyár eleji árhullámok többletvizét homokos beszivárogtató mezőkre és buckaközi mélyedésekbe vezetjük, feltöltve a 2–6 métert süllyedt felszín alatti vízadó rétegeket.",
      phases: [
        "1/3 (0–1.7s): Árhullám-többlet kivezetése a homokhátsági beszivárogtató mezőre",
        "2/3 (1.7–3.5s): Mélybeszivárgás a porózus homokrétegbe — 0% párolgási veszteség!",
        "3/3 (3.5–5.0s): A talajvízszint 3–4 métert emelkedik és alulról eléri a gyökérzónát",
      ],
    },
    {
      id: 2,
      shortName: "Szivacstalaj & Erdősávok",
      title: "Országos „Szivacstalaj”, Regeneratív Művelés és Mezővédő Erdősávok",
      region: "Országos szántóföldek (Csanádi-hát, Békés, Nagykunság, Mezőföld — 4,3 M ha)",
      lat: 46.56,
      lon: 20.68,
      radiusMeters: 24000,
      secondaryZones: [{ lat: 46.95, lon: 18.52, radiusMeters: 19000, label: "Mezőföldi szivacstalaj-zóna" }],
      color: "#fbbf24",
      volume: "650–850 M m³/év",
      evap: "-35–40% (Mulcs + Erdősáv)",
      precedent: "Kína (Loess Plateau) & USA (No-Till)",
      neighborImpact: "100% Semleges (helyi csapadékot tart meg, csökkenti a hordalékot)",
      desc: "A legnagyobb víztározó maga a termőtalaj: a forgatás nélküli művelés (no-till), az eketalp-megszüntetés, a takarónövények és a mezővédő erdősávok +1% humusz-növekedéssel hektáronként 150–200 m³ vizet tartanak a gyökérzónában.",
      phases: [
        "1/3 (0–1.7s): Záporeső érkezik — balra hagyományos eketalpas, jobbra mulcsos szivacstalaj",
        "2/3 (1.7–3.5s): A mezővédő erdősáv megtöri a szárító szelet, a humusz beszívja a vizet",
        "3/3 (3.5–5.0s): Aszályban a szivacstalaj +200 m³/ha saját vízkészletből táplálja a növényt",
      ],
    },
    {
      id: 3,
      shortName: "Fok-gazdálkodás 2.0 (Tisza)",
      title: "Fok-gazdálkodás 2.0 és Mélyártéri Vízkormányzás",
      region: "Tisza-völgy (Felső-, Közép-, Alsó-Tisza) és a Körösök ártéri tározói",
      lat: 47.38,
      lon: 20.52,
      radiusMeters: 25000,
      secondaryZones: [{ lat: 46.92, lon: 20.85, radiusMeters: 18000, label: "Körös-völgyi holtágak" }],
      color: "#38bdf8",
      volume: "500–900 M m³/év",
      evap: "Mikroklíma-hűtő párolgás",
      precedent: "Hollandia (Room for the River)",
      neighborImpact: "Pozitív (Szerbia felé lapítja az árhullámot, nyáron növeli a kisvizet)",
      desc: "A Vásárhelyi-terv (VTT) tározóinak és a levágott holtágaknak rendszeres feltöltése minden tavaszi és kora nyári árhullámból. A víz szétterül a mélyártereken, lehűti a tájat és feltölti a Tisza-völgy talajvizét.",
      phases: [
        "1/3 (0–1.7s): Tavaszi/nyár eleji árhullám érkezik a Tisza gátak közé szorított medrében",
        "2/3 (1.7–3.5s): A modern fok-zsilip kinyílik: a többletvíz betölti a holtágakat és a mélyárteret",
        "3/3 (3.5–5.0s): A zsilip zár: vizes élőhely, páradús mikroklíma és 20 km-es talajvíz-emelkedés",
      ],
    },
    {
      id: 4,
      shortName: "Kétirányú Csatornahálózat",
      title: "42 000 km Belvízcsatorna Kétirányúsítása és Altalaj-nedvesítés",
      region: "Nagykunsági-, Jászsági-, Duna-völgyi-, Keleti- és Békési-főcsatornák",
      lat: 47.12,
      lon: 20.78,
      radiusMeters: 22000,
      secondaryZones: [{ lat: 46.68, lon: 21.18, radiusMeters: 17000, label: "Békési csatornahálózat" }],
      color: "#34d399",
      volume: "400–600 M m³/év",
      evap: "Alacsony (Altalaj-szivárgás)",
      precedent: "Hollandia (Delta Programme Fresh Water)",
      neighborImpact: "Semleges (belső belvizeket tart vissza, alaplefolyást nem érint)",
      desc: "A térképen zölddel jelölt főcsatornák és a 42 000 km-es belvízhálózat ma kivezeti a vizet. Automatizált billenőzsilipekkel a vizet visszaduzzasztjuk a medrekben, ahonnan oldalirányban (sub-irrigation) a szántók alá szivárog.",
      phases: [
        "1/3 (0–1.7s): A nyitott belvízcsatorna elvezeti a vizet, a szántó alatt kiszárad a talaj",
        "2/3 (1.7–3.5s): Az okos billenőzsilip lezár és magasra duzzasztja a csatorna vízszintjét",
        "3/3 (3.5–5.0s): Oldalirányú altalaj-nedvesítés (sub-irrigation) táplálja a növények gyökerét",
      ],
    },
    {
      id: 5,
      shortName: "Szennyvíz + SDI + Agro-PV",
      title: "Tisztított Szennyvíz Visszaforgatás + Felszín Alatti Csepegtetés (SDI) + Agrivoltaics",
      region: "Budapest, Szeged, Debrecen, Kecskemét, Győr, Pécs 30 km-es agrárgyűrűi",
      lat: 47.25,
      lon: 19.32,
      radiusMeters: 20000,
      secondaryZones: [{ lat: 46.28, lon: 20.12, radiusMeters: 16000, label: "Szegedi agrárgyűrű" }],
      color: "#fbbf24",
      volume: "300–450 M m³/év",
      evap: "<10% (Föld alatti SDI)",
      precedent: "Izrael (90% szennyvíz-visszaforgatás)",
      neighborImpact: "Pozitív (zéró folyóvíz-elvonás, tisztább határmetszeti folyóvíz)",
      desc: "Évi ~500 millió m³ tisztított városi szennyvizet engedünk el a folyókon. UV/membrános utótisztítással, felszín alatti csepegtető öntözéssel (SDI) és a növényeket árnyékoló agro-napelemekkel (Agrivoltaics) zárt vízciklust építünk.",
      phases: [
        "1/3 (0–1.7s): A városi tisztított víz a folyóba engedés helyett UV-szűrőn át az agrárgyűrűbe jut",
        "2/3 (1.7–3.5s): Magasított agro-napelemek árnyékolnak (-40% párolgás), a föld alatt SDI csepegtet",
        "3/3 (3.5–5.0s): 95%-os vízhasznosulás + helyben megtermelt tiszta szivattyúzási energia",
      ],
    },
    {
      id: 6,
      shortName: "Duna–Homokhátság Átemelés",
      title: "Duna–Tisza Közi Napelemes Gerinc-Vízpótlás (Dunai Zöldár-Átemelés)",
      region: "RSD & Duna-völgyi-főcsatorna → Homokhátsági gerinc (Kiskőrös–Soltvadkert–Kecskemét)",
      lat: 46.68,
      lon: 19.14,
      radiusMeters: 21000,
      color: "#34d399",
      volume: "200–350 M m³/év",
      evap: "Alacsony (Zárt nyomócső)",
      precedent: "Ausztria (Marchfeldkanal)",
      neighborImpact: "Semleges (a Duna nyári zöldárjának <0,7%-át emeli át)",
      desc: "A Duna alpesi olvadékvízből fakadó május–júliusi „zöldárja” egybeesik a hazai naperőművek nyári túltermelési csúcsával. Ingyenes napenergiával zárt csöveken +35 m-re felnyomjuk a vizet a Homokhátság gerincére, onnan gravitációsan osztjuk szét.",
      phases: [
        "1/3 (0–1.7s): Júniusi magas „zöldár” a Dunán + déli napsütésben csúcsra járó naperőművek",
        "2/3 (1.7–3.5s): Napelemes szivattyúk zárt csövön +35 m magasra nyomják a vizet a hátságra",
        "3/3 (3.5–5.0s): A gerincről a víz gravitációsan tölti a Kolon-tavat, szikes tavakat és tározókat",
      ],
    },
    {
      id: 7,
      shortName: "1000 Kistározó Kaszkád",
      title: "Dunántúli és Hegyaljai „1000 Kistározó” Völgyzárógátas Kaszkád",
      region: "Kapos, Koppány, Sió, Sárvíz, Zala és Északi-középhegység dombvidéki patakjai",
      lat: 46.48,
      lon: 17.95,
      radiusMeters: 24000,
      secondaryZones: [{ lat: 47.82, lon: 19.95, radiusMeters: 17000, label: "Mátra–Bükk előtéri patakok" }],
      color: "#38bdf8",
      volume: "150–250 M m³/év",
      evap: "Közepes (Erdősített völgyek)",
      precedent: "Csehország & Bajorország kisvízfolyás-program",
      neighborImpact: "100% Semleges (tisztán belső dombvidéki vízgyűjtők)",
      desc: "A dombvidéki patakokon a nyári felhőszakadások vize ma villámárvízként órák alatt lefut. Kis völgyzárógátas záportározók és hódgát-analóg fenékküszöbök (beaver dam analogues) láncával megfogjuk a vizet a völgyekben.",
      phases: [
        "1/3 (0–1.7s): Hirtelen nyári felhőszakadás — villámárvíz és talajerózió indul a dombvidéken",
        "2/3 (1.7–3.5s): A 3 lépcsős völgyzárógátas és rőzsegátas kaszkád megfogja az árhullámot",
        "3/3 (3.5–5.0s): A lépcsőzetes kistavak egész nyáron nedvesen tartják a völgyi termőföldeket",
      ],
    },
    {
      id: 8,
      shortName: "Ős-Dráva & Szigetköz–Hanság",
      title: "Ős-Dráva, Szigetköz–Mosoni-Duna és Hanság–Rábaköz Belső Vízpótlása",
      region: "Dráva–Ormánság (DNY) és Szigetköz–Hanság–Rába (ÉNY)",
      lat: 45.86,
      lon: 17.85,
      radiusMeters: 21000,
      secondaryZones: [{ lat: 47.76, lon: 17.28, radiusMeters: 21000, label: "Szigetköz–Hanság–Rábaköz" }],
      color: "#34d399",
      volume: "150–200 M m³/év",
      evap: "Alacsony–Közepes",
      precedent: "Szigetközi fenékküszöb & mellékág-rehabilitáció",
      neighborImpact: "Pozitív (Ausztria/Seewinkel és Horvátország/Dráva talajvizét is védi)",
      desc: "A határmenti bővizű folyók (Dráva, Mura, Duna/Mosoni-Duna, Rába) árhullámaiból az Ormánság kiszáradó holtágainak (Ős-Dráva program) és a Hansági-főcsatorna / Rábaköz talajvízrendszerének célzott feltöltése.",
      phases: [
        "1/3 (0–1.7s): Bővizű határfolyó (Dráva / Duna) mellett kiszáradó belső holtágak és láprétek",
        "2/3 (1.7–3.5s): Fenékküszöb és oldalzsilip átvezeti az árhullám-többletet a belső mellékágakba",
        "3/3 (3.5–5.0s): Az Ormánság és a Hanság holtágai megtelnek, a határmenti talajvíz helyreáll",
      ],
    },
    {
      id: 9,
      shortName: "Civaqua+ Észak-Alföldi Vízkör",
      title: "Civaqua+ és Észak-Alföldi Vízkör (Tisza → Debrecen → Erdőspuszták → Berettyó)",
      region: "Tiszalök → Keleti-főcsatorna → Hajdúhát → Debrecen Nagyerdő → Berettyó",
      lat: 47.55,
      lon: 21.58,
      radiusMeters: 22000,
      color: "#34d399",
      volume: "120–180 M m³/év",
      evap: "Közepes (Erdőspusztai tavak)",
      precedent: "Civaqua I. ütem továbbfejlesztése",
      neighborImpact: "100% Semleges (zárt belső Tisza–Berettyó–Körös–Tisza vízkör)",
      desc: "A térképen Tiszalöktől délre futó zöld Keleti-főcsatornából a vizet szivattyúkkal és gravitációs vezetékekkel átvezetjük a Hajdúháton a debreceni Nagyerdőbe, a kiszáradt Erdőspusztai tavakba (Vekeri-, Fancsika-tó) és a Dél-Nyírségbe.",
      phases: [
        "1/3 (0–1.7s): Tiszalöknél a Tisza vize belép a zölddel jelölt Keleti-főcsatornába",
        "2/3 (1.7–3.5s): A Civaqua+ rendszer felvezeti a vizet a Nagyerdőbe és az Erdőspusztai tavakba",
        "3/3 (3.5–5.0s): A Vekeri- és Fancsikai-tavak megtelnek, a többlet a Berettyón át visszatér",
      ],
    },
    {
      id: 10,
      shortName: "AI Hidrológiai Digitális Iker",
      title: "Országos Hidrológiai „Digitális Iker” (Digital Twin) és AI Okos-Zsilip Vezérlés",
      region: "Budapest központ + a térkép összes kék és zöld vízügyi csomópontja",
      lat: 47.49,
      lon: 19.04,
      radiusMeters: 18000,
      color: "#fbbf24",
      volume: "+25–35% Rendszerhatásfok",
      evap: "Optimalizált vízelosztás",
      precedent: "Hollandia (Smart Water Management Digital Twin)",
      neighborImpact: "Pozitív (garantálja a nemzetközi egyezmények szerinti határhozamokat)",
      desc: "A térképen fehér-kék és fehér-zöld körökkel jelölt több száz vízügyi csomópont összekötése Sentinel műholdas talajnedvesség-adatokkal és meteorológiai radarral. Az AI 48–72 órával az eső előtt vezérli a zsilipeket.",
      phases: [
        "1/3 (0–1.7s): Sentinel műhold és radar észleli a közeledő esőzónát és árhullámot (T-48h)",
        "2/3 (1.7–3.5s): Az AI vezérlő automatikusan lezárja a levezető és megnyitja a tározó-zsilipeket",
        "3/3 (3.5–5.0s): +30% extra megtartott víz az országban, stabil határmetszeti vízhozamok",
      ],
    },
  ];

  let animFrameId = null;
  let activeAnimStart = 0;

  // Drawing helpers for the 5-second expressive canvas animations
  function drawSun(ctx, x, y, r, pulse) {
    ctx.save();
    const grad = ctx.createRadialGradient(x, y, r * 0.2, x, y, r * (1.5 + pulse * 0.2));
    grad.addColorStop(0, "#fde047");
    grad.addColorStop(0.6, "#f59e0b");
    grad.addColorStop(1, "rgba(245, 158, 11, 0)");
    ctx.fillStyle = grad;
    ctx.beginPath();
    ctx.arc(x, y, r * 1.7, 0, Math.PI * 2);
    ctx.fill();
    ctx.fillStyle = "#fef08a";
    ctx.beginPath();
    ctx.arc(x, y, r * 0.75, 0, Math.PI * 2);
    ctx.fill();
    ctx.restore();
  }

  function drawTree(ctx, x, y, scale, greenness) {
    ctx.save();
    ctx.translate(x, y);
    ctx.scale(scale, scale);
    ctx.fillStyle = "#78350f";
    ctx.fillRect(-2.5, -12, 5, 12);
    const r = Math.round(130 - greenness * 96);
    const g = Math.round(115 + greenness * 82);
    const b = Math.round(50 + greenness * 44);
    ctx.fillStyle = `rgb(${r},${g},${b})`;
    ctx.beginPath();
    ctx.arc(0, -18, 10, 0, Math.PI * 2);
    ctx.arc(-6, -14, 7, 0, Math.PI * 2);
    ctx.arc(6, -14, 7, 0, Math.PI * 2);
    ctx.fill();
    ctx.restore();
  }

  function drawCrop(ctx, x, y, growth, health) {
    ctx.save();
    ctx.translate(x, y);
    const h = 10 + growth * 17;
    const r = Math.round(180 - health * 145);
    const g = Math.round(130 + health * 85);
    const b = Math.round(45 + health * 35);
    ctx.strokeStyle = `rgb(${r},${g},${b})`;
    ctx.lineWidth = 2.2;
    ctx.beginPath();
    ctx.moveTo(0, 0);
    ctx.lineTo(0, -h);
    ctx.stroke();
    ctx.beginPath();
    ctx.moveTo(0, -h * 0.5);
    ctx.quadraticCurveTo(-8 * health, -h * 0.7, -10, -h * 0.45);
    ctx.moveTo(0, -h * 0.7);
    ctx.quadraticCurveTo(8 * health, -h * 0.9, 10, -h * 0.65);
    ctx.stroke();
    ctx.restore();
  }

  function drawArrow(ctx, x1, y1, x2, y2, color) {
    ctx.save();
    ctx.strokeStyle = color;
    ctx.fillStyle = color;
    ctx.lineWidth = 2;
    ctx.beginPath();
    ctx.moveTo(x1, y1);
    ctx.lineTo(x2, y2);
    ctx.stroke();
    const ang = Math.atan2(y2 - y1, x2 - x1);
    ctx.beginPath();
    ctx.moveTo(x2, y2);
    ctx.lineTo(x2 - 7 * Math.cos(ang - 0.45), y2 - 7 * Math.sin(ang - 0.45));
    ctx.lineTo(x2 - 7 * Math.cos(ang + 0.45), y2 - 7 * Math.sin(ang + 0.45));
    ctx.closePath();
    ctx.fill();
    ctx.restore();
  }

  function drawPlanFrame(canvas, phaseEl, timerEl, barEl, plan, now) {
    if (!canvas || !canvas.isConnected) return false;
    const ctx = canvas.getContext("2d");
    const elapsed = (now - activeAnimStart) % ANIM_DURATION_MS;
    const p = elapsed / ANIM_DURATION_MS;
    const sec = (elapsed / 1000).toFixed(1);

    if (timerEl) timerEl.textContent = `${sec}s / 5.0s`;
    if (barEl) barEl.style.width = `${(p * 100).toFixed(1)}%`;
    if (phaseEl) {
      const idx = p < 0.34 ? 0 : p < 0.7 ? 1 : 2;
      phaseEl.textContent = plan.phases[idx];
    }

    const W = canvas.width;
    const H = canvas.height;
    ctx.clearRect(0, 0, W, H);

    const sky = ctx.createLinearGradient(0, 0, 0, H * 0.55);
    sky.addColorStop(0, "#0f172a");
    sky.addColorStop(1, "#1e293b");
    ctx.fillStyle = sky;
    ctx.fillRect(0, 0, W, H);

    const s1 = Math.min(1, p / 0.34);
    const s2 = Math.max(0, Math.min(1, (p - 0.25) / 0.45));
    const s3 = Math.max(0, Math.min(1, (p - 0.62) / 0.38));

    switch (plan.id) {
      case 1: {
        drawSun(ctx, 305, 24, 12, Math.sin(p * Math.PI * 4));
        ctx.fillStyle = "#78350f";
        ctx.fillRect(0, 74, W, H - 74);
        ctx.fillStyle = "#1e293b";
        ctx.beginPath();
        ctx.moveTo(30, 74);
        ctx.quadraticCurveTo(95, 102, 160, 74);
        ctx.closePath();
        ctx.fill();
        ctx.fillStyle = "rgba(56, 189, 248, 0.85)";
        ctx.beginPath();
        ctx.moveTo(36, 75);
        ctx.quadraticCurveTo(95, 75 + s1 * 24, 154, 75);
        ctx.closePath();
        ctx.fill();
        const gwY = 138 - s2 * 40;
        ctx.fillStyle = "rgba(14, 165, 233, 0.85)";
        ctx.fillRect(0, gwY, W, H - gwY);
        if (p > 0.15 && p < 0.85) {
          for (let i = 0; i < 4; i++) {
            const dx = 60 + i * 22;
            const dy = 88 + ((p * 150 + i * 15) % Math.max(10, gwY - 86));
            drawArrow(ctx, dx, dy, dx, dy + 10, "#38bdf8");
          }
        }
        for (let i = 0; i < 4; i++) {
          drawCrop(ctx, 195 + i * 35, 74, 0.3 + s3 * 0.7, 0.25 + s2 * 0.75);
        }
        ctx.fillStyle = "#7dd3fc";
        ctx.font = "bold 10px sans-serif";
        ctx.fillText(`MAR talajvíz-emelkedés: +${(s2 * 3.8).toFixed(1)} m • 0% párolgás`, 12, 132);
        break;
      }
      case 2: {
        ctx.fillStyle = "#78350f";
        ctx.fillRect(0, 82, W / 2, H - 82);
        ctx.fillStyle = "#451a03";
        ctx.fillRect(W / 2, 82, W / 2, H - 82);
        ctx.fillStyle = "#ef4444";
        ctx.fillRect(0, 100, W / 2 - 4, 4);
        ctx.fillStyle = "#84cc16";
        ctx.fillRect(W / 2 + 4, 79, W / 2 - 8, 4);
        ctx.fillStyle = `rgba(14, 165, 233, ${0.2 + s2 * 0.55})`;
        ctx.fillRect(W / 2 + 6, 85, W / 2 - 12, 55 * s2);
        drawTree(ctx, W / 2 + 20, 82, 1.0, 0.9);
        for (let i = 0; i < 3; i++) {
          drawCrop(ctx, 32 + i * 42, 82, 0.3 - s3 * 0.1, 0.2);
          drawCrop(ctx, W / 2 + 55 + i * 36, 82, 0.4 + s2 * 0.6, 0.3 + s2 * 0.7);
        }
        ctx.fillStyle = "#fcd34d";
        ctx.font = "bold 9.5px sans-serif";
        ctx.fillText("Eketalpas szántó (-60% víz)", 10, 20);
        ctx.fillStyle = "#4ade80";
        ctx.fillText("Szivacstalaj (+200 m³/ha)", W / 2 + 12, 20);
        break;
      }
      case 3: {
        ctx.fillStyle = "#713f12";
        ctx.fillRect(0, 86, W, H - 86);
        ctx.fillStyle = "#0284c7";
        ctx.fillRect(14, 66 - Math.sin(p * Math.PI) * 12, 65, 55);
        const gateOpen = p > 0.2 && p < 0.75;
        ctx.fillStyle = gateOpen ? "#22c55e" : "#f59e0b";
        ctx.fillRect(84, gateOpen ? 46 : 66, 7, 20);
        const fpFill = Math.min(1, s2 * 1.15);
        if (fpFill > 0.05) {
          ctx.fillStyle = "rgba(56, 189, 248, 0.85)";
          ctx.beginPath();
          ctx.moveTo(105, 86);
          ctx.quadraticCurveTo(215, 86 + fpFill * 34, 320, 86);
          ctx.closePath();
          ctx.fill();
        }
        if (gateOpen) drawArrow(ctx, 80, 76, 130, 80, "#38bdf8");
        drawTree(ctx, 125, 85, 0.9, 0.4 + fpFill * 0.6);
        drawTree(ctx, 310, 85, 1.0, 0.4 + fpFill * 0.6);
        ctx.fillStyle = "#7dd3fc";
        ctx.font = "bold 10px sans-serif";
        ctx.fillText(gateOpen ? "Fok-zsilip NYITVA: ártér feltöltése" : "Fok-zsilip ZÁRVA: víz a tájban marad", 95, 22);
        break;
      }
      case 4: {
        ctx.fillStyle = "#78350f";
        ctx.fillRect(0, 78, W, H - 78);
        const canalY = 118 - s2 * 32;
        ctx.fillStyle = "#10b981";
        ctx.fillRect(145, canalY, 50, 128 - canalY);
        const spread = s2 * 125;
        ctx.fillStyle = "rgba(56, 189, 248, 0.55)";
        ctx.fillRect(145 - spread, canalY + 4, spread, H - canalY);
        ctx.fillRect(195, canalY + 4, spread, H - canalY);
        if (s2 > 0.2) {
          drawArrow(ctx, 142, 102, 142 - spread * 0.7, 102, "#38bdf8");
          drawArrow(ctx, 198, 102, 198 + spread * 0.7, 102, "#38bdf8");
        }
        for (let i = 0; i < 3; i++) {
          drawCrop(ctx, 30 + i * 38, 78, 0.35 + s3 * 0.6, 0.3 + s2 * 0.7);
          drawCrop(ctx, 225 + i * 38, 78, 0.35 + s3 * 0.6, 0.3 + s2 * 0.7);
        }
        ctx.fillStyle = "#6ee7b7";
        ctx.font = "bold 10px sans-serif";
        ctx.fillText("Okos-zsilip duzzasztás → Oldalirányú altalaj-nedvesítés", 35, 22);
        break;
      }
      case 5: {
        drawSun(ctx, 310, 22, 12, Math.sin(p * Math.PI * 4));
        ctx.fillStyle = "#5c2d0c";
        ctx.fillRect(0, 86, W, H - 86);
        ctx.fillStyle = "#334155";
        ctx.fillRect(12, 48, 46, 38);
        ctx.strokeStyle = "#0ea5e9";
        ctx.lineWidth = 2.5;
        ctx.beginPath();
        ctx.moveTo(58, 76);
        ctx.lineTo(80, 106);
        ctx.lineTo(325, 106);
        ctx.stroke();
        for (let i = 0; i < 4; i++) {
          const rx = 110 + i * 56;
          ctx.fillStyle = "rgba(56, 189, 248, 0.65)";
          ctx.beginPath();
          ctx.arc(rx, 106, 5 + s2 * 12, 0, Math.PI * 2);
          ctx.fill();
          ctx.strokeStyle = "#38bdf8";
          ctx.lineWidth = 3;
          ctx.beginPath();
          ctx.moveTo(rx - 20, 48);
          ctx.lineTo(rx + 6, 38);
          ctx.stroke();
          drawCrop(ctx, rx, 86, 0.35 + s2 * 0.6, 0.35 + s2 * 0.65);
        }
        ctx.fillStyle = "#fde047";
        ctx.font = "bold 10px sans-serif";
        ctx.fillText("Tisztított víz + Agro-PV árnyékolás + Föld alatti SDI", 42, 20);
        break;
      }
      case 6: {
        drawSun(ctx, 60, 22, 12, Math.sin(p * Math.PI * 4));
        ctx.fillStyle = "#78350f";
        ctx.beginPath();
        ctx.moveTo(0, 118);
        ctx.lineTo(70, 118);
        ctx.quadraticCurveTo(120, 68, 190, 68);
        ctx.quadraticCurveTo(260, 68, 300, 118);
        ctx.lineTo(W, 118);
        ctx.lineTo(W, H);
        ctx.lineTo(0, H);
        ctx.closePath();
        ctx.fill();
        ctx.fillStyle = "#0284c7";
        ctx.fillRect(6, 108, 52, 18);
        ctx.strokeStyle = "#10b981";
        ctx.lineWidth = 3;
        ctx.beginPath();
        ctx.moveTo(55, 114);
        ctx.quadraticCurveTo(115, 72, 185, 72);
        ctx.stroke();
        ctx.fillStyle = `rgba(56, 189, 248, ${0.25 + s2 * 0.65})`;
        ctx.fillRect(150, 66, 80, 10);
        drawCrop(ctx, 168, 68, 0.3 + s3 * 0.65, 0.3 + s2 * 0.7);
        drawCrop(ctx, 212, 68, 0.3 + s3 * 0.65, 0.3 + s2 * 0.7);
        ctx.fillStyle = "#6ee7b7";
        ctx.font = "bold 10px sans-serif";
        ctx.fillText("Napelemes átemelés (+35 m) a Homokhátság gerincére", 78, 22);
        break;
      }
      case 7: {
        ctx.fillStyle = "#713f12";
        ctx.beginPath();
        ctx.moveTo(0, 52);
        ctx.lineTo(W, 124);
        ctx.lineTo(W, H);
        ctx.lineTo(0, H);
        ctx.closePath();
        ctx.fill();
        const dams = [
          { x: 95, y: 72, fill: Math.min(1, s1 * 1.2) },
          { x: 185, y: 92, fill: Math.min(1, s2 * 1.2) },
          { x: 275, y: 112, fill: Math.min(1, s2 * 0.5 + s3 * 0.8) },
        ];
        dams.forEach((d) => {
          if (d.fill > 0.05) {
            ctx.fillStyle = "rgba(56, 189, 248, 0.85)";
            ctx.beginPath();
            ctx.moveTo(d.x, d.y - 12 * d.fill);
            ctx.lineTo(d.x, d.y + 4);
            ctx.lineTo(d.x - 55 * d.fill, d.y - 11 * d.fill);
            ctx.closePath();
            ctx.fill();
          }
          ctx.fillStyle = "#d97706";
          ctx.fillRect(d.x, d.y - 14, 6, 20);
        });
        ctx.fillStyle = "#7dd3fc";
        ctx.font = "bold 10px sans-serif";
        ctx.fillText("Völgyzárógátas kaszkád: Villámárvízből tartós vízkészlet", 22, 22);
        break;
      }
      case 8: {
        ctx.fillStyle = "#78350f";
        ctx.fillRect(0, 84, W, H - 84);
        ctx.fillStyle = "#0284c7";
        ctx.fillRect(12, 62 - s1 * 8, 72, 58);
        [150, 245].forEach((ox, i) => {
          const fill = i === 0 ? s2 : Math.min(1, s2 * 0.6 + s3 * 0.6);
          ctx.fillStyle = "rgba(16, 185, 129, 0.85)";
          ctx.beginPath();
          ctx.arc(ox, 84, 28 * fill, 0, Math.PI);
          ctx.fill();
          drawTree(ctx, ox + 34, 84, 0.85, 0.35 + fill * 0.65);
        });
        drawArrow(ctx, 88, 78, 122, 78, "#34d399");
        ctx.fillStyle = "#6ee7b7";
        ctx.font = "bold 10px sans-serif";
        ctx.fillText("Fenékküszöb → Ormánsági és Hansági holtágak feltöltése", 22, 22);
        break;
      }
      case 9: {
        ctx.fillStyle = "#14261c";
        ctx.fillRect(0, 0, W, H);
        ctx.strokeStyle = "#10b981";
        ctx.lineWidth = 4.5;
        ctx.beginPath();
        ctx.moveTo(95, 32);
        ctx.lineTo(95, 134);
        ctx.stroke();
        ctx.strokeStyle = "#38bdf8";
        ctx.lineWidth = 3.5;
        ctx.beginPath();
        ctx.moveTo(95, 68);
        ctx.lineTo(95 + s2 * 130, 68 - s2 * 10);
        ctx.stroke();
        const lakeScale = 0.35 + s2 * 0.85;
        ctx.fillStyle = "#0ea5e9";
        ctx.beginPath();
        ctx.arc(215, 58, 13 * lakeScale, 0, Math.PI * 2);
        ctx.arc(275, 84, 15 * lakeScale, 0, Math.PI * 2);
        ctx.fill();
        ctx.fillStyle = "#e0f2fe";
        ctx.font = "bold 10px sans-serif";
        ctx.fillText("Keleti-főcsatorna → Debrecen Nagyerdő & Erdőspuszták", 22, 22);
        break;
      }
      case 10: {
        ctx.fillStyle = "#091326";
        ctx.fillRect(0, 0, W, H);
        ctx.fillStyle = "#f59e0b";
        ctx.beginPath();
        ctx.arc(170, 54, 18, 0, Math.PI * 2);
        ctx.fill();
        ctx.fillStyle = "#0f172a";
        ctx.font = "bold 9px sans-serif";
        ctx.fillText("AI IKER", 152, 57);
        [60, 170, 280].forEach((nx) => {
          ctx.strokeStyle = "rgba(52, 211, 153, 0.5)";
          ctx.beginPath();
          ctx.moveTo(170, 72);
          ctx.lineTo(nx, 115);
          ctx.stroke();
          ctx.fillStyle = s2 > 0.6 ? "#10b981" : "#38bdf8";
          ctx.beginPath();
          ctx.arc(nx, 120, 8, 0, Math.PI * 2);
          ctx.fill();
        });
        ctx.fillStyle = "#7dd3fc";
        ctx.font = "bold 10px sans-serif";
        ctx.fillText("Műhold & Radar (T-48h) → AI Okos-zsilip hálózat vezérlés", 24, 22);
        break;
      }
    }
    return true;
  }

  function buildRetentionCardHTML(plan, canvasIdPrefix) {
    return `
      <div class="hover-header" style="margin-bottom: 6px;">
        <div>
          <span class="hover-river-badge" style="color: ${plan.color};">
            💧 #${plan.id} VÍZMEGTARTÁSI TERV • ${plan.region}
          </span>
          <h3 class="hover-station-title" style="font-size: 0.96rem; margin-top: 2px;">${plan.title}</h3>
        </div>
      </div>

      <div style="border-radius: 8px; overflow: hidden; border: 1px solid rgba(56,189,248,0.35); background: #091326; margin-bottom: 8px;">
        <div style="display:flex; align-items:center; justify-content:space-between; padding: 4px 8px; background: rgba(15,23,42,0.95); font-size: 10.5px; color: #7dd3fc; border-bottom: 1px solid rgba(255,255,255,0.08);">
          <span id="${canvasIdPrefix}-phase" style="font-weight:600; white-space:nowrap; overflow:hidden; text-overflow:ellipsis;">${plan.phases[0]}</span>
          <span id="${canvasIdPrefix}-timer" style="font-family:monospace; color:#cbd5e1; margin-left:6px;">0.0s / 5.0s</span>
        </div>
        <canvas id="${canvasIdPrefix}-canvas" width="340" height="145" style="width:100%; height:145px; display:block;"></canvas>
        <div style="height:3px; background:#1e293b; width:100%;">
          <div id="${canvasIdPrefix}-bar" style="height:100%; width:0%; background:linear-gradient(90deg,#38bdf8,#34d399,#fbbf24);"></div>
        </div>
      </div>

      <div class="hover-metrics-grid" style="margin-bottom: 6px;">
        <div class="metric-box">
          <span class="metric-box-label">Megtartott víz</span>
          <strong class="metric-box-val" style="color:#38bdf8; font-size:0.86rem;">${plan.volume}</strong>
        </div>
        <div class="metric-box">
          <span class="metric-box-label">Párolgás</span>
          <strong class="metric-box-val" style="color:#34d399; font-size:0.82rem;">${plan.evap}</strong>
        </div>
        <div class="metric-box">
          <span class="metric-box-label">Nemzetközi minta</span>
          <strong class="metric-box-val" style="color:#fbbf24; font-size:0.78rem;">${plan.precedent}</strong>
        </div>
      </div>

      <div style="font-size: 11.5px; line-height: 1.38; color: var(--text-primary); margin-bottom: 4px;">
        ${plan.desc}
      </div>
      <div style="font-size: 10.5px; color: #34d399; font-weight: 600;">
        ✓ Szomszéd országok: ${plan.neighborImpact}
      </div>
    `;
  }

  function startCardAnimation(plan, prefix) {
    if (animFrameId) cancelAnimationFrame(animFrameId);
    activeAnimStart = performance.now();

    function step(now) {
      const canvas = document.getElementById(`${prefix}-canvas`);
      const phaseEl = document.getElementById(`${prefix}-phase`);
      const timerEl = document.getElementById(`${prefix}-timer`);
      const barEl = document.getElementById(`${prefix}-bar`);
      const alive = drawPlanFrame(canvas, phaseEl, timerEl, barEl, plan, now);
      if (alive) {
        animFrameId = requestAnimationFrame(step);
      }
    }
    animFrameId = requestAnimationFrame(step);
  }

  function initRetentionLayer(map) {
    if (!map) return;
    if (!map.getPane("retentionPane")) {
      map.createPane("retentionPane").style.zIndex = 495;
    }

    const layerGroup = L.layerGroup().addTo(map);
    const hoverCardEl = document.getElementById("hydro-hover-card");
    const pinnedPanelEl = document.getElementById("pinned-station-panel");

    function positionCard(e) {
      if (!hoverCardEl || !e || !e.originalEvent) return;
      const ev = e.originalEvent;
      const cardW = 370;
      const cardH = 355;
      const offset = 18;
      let left = ev.clientX + offset;
      let top = ev.clientY + offset;
      if (left + cardW > window.innerWidth - 16) left = ev.clientX - cardW - offset;
      if (top + cardH > window.innerHeight - 16) top = ev.clientY - cardH - offset;
      hoverCardEl.style.left = `${Math.max(12, left)}px`;
      hoverCardEl.style.top = `${Math.max(12, top)}px`;
    }

    RETENTION_PLANS.forEach((plan) => {
      // Impact Zone Circle
      const zoneCircle = L.circle([plan.lat, plan.lon], {
        pane: "retentionPane",
        radius: plan.radiusMeters,
        color: plan.color,
        weight: 2,
        dashArray: "6 5",
        fillColor: plan.color,
        fillOpacity: 0.16,
      }).addTo(layerGroup);

      // Numbered Badge Marker (#1..#10)
      const icon = L.divIcon({
        className: "retention-plan-marker",
        html: `<div style="
          width: 28px; height: 28px; border-radius: 999px;
          background: ${plan.color}; color: #0f172a;
          font-weight: 800; font-size: 12px;
          display: flex; align-items: center; justify-content: center;
          border: 2.5px solid #ffffff;
          box-shadow: 0 0 0 4px ${plan.color}55, 0 4px 10px rgba(0,0,0,0.45);
          cursor: pointer;
        ">#${plan.id}</div>`,
        iconSize: [28, 28],
        iconAnchor: [14, 14],
      });

      const marker = L.marker([plan.lat, plan.lon], {
        pane: "retentionPane",
        icon,
      }).addTo(layerGroup);

      function onEnter(e) {
        if (!hoverCardEl) return;
        hoverCardEl.innerHTML = buildRetentionCardHTML(plan, "ret-hover");
        hoverCardEl.classList.remove("hidden");
        positionCard(e);
        startCardAnimation(plan, "ret-hover");
        zoneCircle.setStyle({ fillOpacity: 0.34, weight: 3 });
      }

      function onMove(e) {
        positionCard(e);
      }

      function onLeave() {
        if (hoverCardEl) hoverCardEl.classList.add("hidden");
        zoneCircle.setStyle({ fillOpacity: 0.16, weight: 2 });
      }

      function onClick() {
        if (pinnedPanelEl) {
          pinnedPanelEl.innerHTML = buildRetentionCardHTML(plan, "ret-pinned");
          startCardAnimation(plan, "ret-pinned");
        }
      }

      marker.on("mouseover", onEnter);
      marker.on("mousemove", onMove);
      marker.on("mouseout", onLeave);
      marker.on("click", onClick);

      zoneCircle.on("mouseover", onEnter);
      zoneCircle.on("mousemove", onMove);
      zoneCircle.on("mouseout", onLeave);
      zoneCircle.on("click", onClick);

      if (plan.secondaryZones) {
        plan.secondaryZones.forEach((sz) => {
          const subCircle = L.circle([sz.lat, sz.lon], {
            pane: "retentionPane",
            radius: sz.radiusMeters,
            color: plan.color,
            weight: 1.8,
            dashArray: "4 4",
            fillColor: plan.color,
            fillOpacity: 0.14,
          }).addTo(layerGroup);
          subCircle.on("mouseover", onEnter);
          subCircle.on("mousemove", onMove);
          subCircle.on("mouseout", onLeave);
          subCircle.on("click", onClick);
        });
      }
    });

    const toggleEl = document.getElementById("toggle-retention-plans");
    if (toggleEl) {
      toggleEl.addEventListener("change", (e) => {
        if (e.target.checked) {
          layerGroup.addTo(map);
        } else {
          map.removeLayer(layerGroup);
        }
      });
    }
  }

  // Hook into RiverRadar map instance once ready
  if (window.__RIVERRADAR_MAP__) {
    initRetentionLayer(window.__RIVERRADAR_MAP__);
  } else {
    window.addEventListener("riverradar:map-ready", (e) => {
      initRetentionLayer(e.detail.map);
    });
  }
})();
