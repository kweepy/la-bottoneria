#!/usr/bin/env python3
"""
Genera il sito statico de La Bottoneria nella cartella docs/.

    python3 src/build.py

Richiede Python 3 e Pillow (pip install Pillow).
I contenuti si modificano in src/contenuti.py.
"""
import html
import json
import re
import shutil
import sys
import zipfile
from pathlib import Path
from urllib.parse import quote

from PIL import Image, ImageOps

sys.path.insert(0, str(Path(__file__).parent))
from contenuti import (CARTELLINO, CATEGORIE, CATEGORIE_HOME, CHI_SIAMO,  # noqa: E402
                       HERO, NEGOZIO, ORARI, PERSONALIZZAZIONI, SCEGLI_TU)

import math  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "src"
OUT = ROOT / "docs"
FOTO_DIR = ROOT / "immagini"
LARGHEZZE = (800, 1600)

esc = html.escape


# ---------------------------------------------------------------- immagini
_cache = {}


def prepara_foto(nome):
    """Converte una foto di immagini/ in WebP a 800 e 1600 px. Ritorna info."""
    if nome in _cache:
        return _cache[nome]
    src = FOTO_DIR / nome
    if not src.exists():
        sys.exit(f"Foto non trovata: immagini/{nome}")
    stem = re.sub(r"[^a-z0-9]+", "-", Path(nome).stem.lower()).strip("-")[:40]
    im = ImageOps.exif_transpose(Image.open(src)).convert("RGB")
    w, h = im.size
    varianti = []
    for lw in LARGHEZZE:
        tw = min(lw, w)
        if varianti and tw == varianti[-1][1]:
            break
        dest = OUT / "img" / f"{stem}-{tw}.webp"
        if not dest.exists():
            r = im.resize((tw, round(h * tw / w)), Image.LANCZOS) if tw < w else im
            r.save(dest, "WEBP", quality=78, method=6)
        varianti.append((f"img/{dest.name}", tw))
    info = {"varianti": varianti, "w": w, "h": h}
    _cache[nome] = info
    return info


def img(nome, alt, sizes="100vw", cls="", eager=False):
    info = prepara_foto(nome)
    srcset = ", ".join(f"{p} {w}w" for p, w in info["varianti"])
    small = info["varianti"][0][0]
    load = 'fetchpriority="high"' if eager else 'loading="lazy" decoding="async"'
    c = f' class="{cls}"' if cls else ""
    return (f'<img src="{small}" srcset="{srcset}" sizes="{sizes}" '
            f'width="{info["w"]}" height="{info["h"]}" alt="{esc(alt)}" {load}{c}>')


# ---------------------------------------------------------------- utilità
def wa(testo="Ciao! Vorrei qualche informazione."):
    return f"https://wa.me/{NEGOZIO['whatsapp']}?text={quote(testo)}"


ICONA_WA = ('<svg class="ico" viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M12.04 2a9.9 9.9 0 0 0-8.5 15l-1.4 5 5.1-1.3A9.9 9.9 0 1 0 12.04 2Zm0 18.1a8.2 8.2 0 0 1-4.2-1.2l-.3-.2-3 .8.8-2.9-.2-.3a8.2 8.2 0 1 1 6.9 3.8Zm4.5-6.1c-.2-.1-1.5-.7-1.7-.8-.2-.1-.4-.1-.6.1l-.8 1c-.1.2-.3.2-.5.1a6.7 6.7 0 0 1-3.3-2.9c-.2-.4.2-.4.7-1.3.1-.2 0-.3 0-.4l-.8-1.8c-.2-.5-.4-.4-.6-.4h-.5a1 1 0 0 0-.7.3 3 3 0 0 0-.9 2.2 5.2 5.2 0 0 0 1.1 2.7 11.8 11.8 0 0 0 4.5 4c1.7.7 2.3.8 3.2.6.5-.1 1.5-.6 1.7-1.2.2-.6.2-1.1.1-1.2l-.4-.2Z"/></svg>')

ICONA_TEL = ('<svg class="ico" viewBox="0 0 24 24" aria-hidden="true"><path fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" d="M6.6 3.5h-2A1.6 1.6 0 0 0 3 5.2 15.8 15.8 0 0 0 18.8 21a1.6 1.6 0 0 0 1.7-1.6v-2a1.2 1.2 0 0 0-.9-1.2l-3.2-.9a1.2 1.2 0 0 0-1.2.3l-1.4 1.4a12 12 0 0 1-5-5l1.4-1.4a1.2 1.2 0 0 0 .3-1.2l-.9-3.2a1.2 1.2 0 0 0-1.2-.9Z"/></svg>')
ICONA_MAIL = ('<svg class="ico" viewBox="0 0 24 24" aria-hidden="true"><g fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3.5 6.5 8.5 6.5 8.5-6.5"/></g></svg>')
ICONA_POS = ('<svg class="ico" viewBox="0 0 24 24" aria-hidden="true"><g fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M12 21s-7-6.2-7-11.5a7 7 0 0 1 14 0C19 14.8 12 21 12 21Z"/><circle cx="12" cy="9.5" r="2.5"/></g></svg>')


def indirizzo_link(sep="<br>"):
    return (f'<a class="link-mappa" href="{NEGOZIO["mappa"]}" target="_blank" rel="noopener">'
            f'{ICONA_POS}<span>{NEGOZIO["indirizzo"]}{sep}{NEGOZIO["cap_citta"]}</span></a>')


def contatti_icone(cls="contatti-icone"):
    return f"""<ul class="{cls}">
  <li><a href="{wa()}" target="_blank" rel="noopener" aria-label="WhatsApp">{ICONA_WA}<span>{NEGOZIO['whatsapp_visibile']}</span></a></li>
  <li><a href="tel:+{NEGOZIO['whatsapp']}" aria-label="Telefono">{ICONA_TEL}<span>{NEGOZIO['whatsapp_visibile']}</span></a></li>
  <li><a href="mailto:{NEGOZIO['email']}" aria-label="Email">{ICONA_MAIL}<span>{NEGOZIO['email']}</span></a></li>
</ul>"""


DIVISORE = '<div class="divisore" aria-hidden="true"><span></span><i></i><i></i><span></span></div>'


def fmt_fascia(f):
    a, b = f.split("-")
    t = lambda x: x[1:] if x.startswith("0") else x  # noqa: E731
    return f"{t(a).replace(':00', '')}–{t(b).replace(':00', '')}"


def orari_html(cls="orari"):
    righe = []
    for i, (giorno, fasce) in enumerate(ORARI):
        val = " e ".join(fmt_fascia(f) for f in fasce) if fasce else "Chiuso"
        righe.append(f'<tr data-giorno="{(i + 1) % 7}"><th scope="row">{giorno}</th><td>{val}</td></tr>')
    dati = json.dumps({str((i + 1) % 7): f for i, (_, f) in enumerate(ORARI)})
    return (f'<p class="stato-apertura" data-orari=\'{dati}\' hidden></p>'
            f'<table class="{cls}"><tbody>{"".join(righe)}</tbody></table>')


def jsonld():
    giorni_en = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    spec = []
    for (g, fasce), en in zip(ORARI, giorni_en):
        for f in fasce:
            a, b = f.split("-")
            spec.append({"@type": "OpeningHoursSpecification", "dayOfWeek": en, "opens": a, "closes": b})
    d = {
        "@context": "https://schema.org", "@type": "Store",
        "name": f"{NEGOZIO['nome']} Merceria",
        "telephone": NEGOZIO["whatsapp_visibile"], "email": NEGOZIO["email"],
        "address": {"@type": "PostalAddress", "streetAddress": NEGOZIO["indirizzo"],
                    "postalCode": "25124", "addressLocality": "Brescia", "addressCountry": "IT"},
        "openingHoursSpecification": spec,
    }
    if NEGOZIO["sito"]:
        d["url"] = NEGOZIO["sito"]
    return f'<script type="application/ld+json">{json.dumps(d, ensure_ascii=False)}</script>'


# ---------------------------------------------------------------- layout
NAV = [("personalizzazioni.html", "Personalizzazioni"), ("prodotti.html", "Prodotti"),
       ("chi-siamo.html", "Chi siamo"), ("contatti.html", "Contatti")]


def pagina(file, titolo, descrizione, corpo, attivo=None, extra_head=""):
    nav = "".join(
        f'<li><a href="{h}"{" aria-current=page" if h == attivo else ""}>{t}</a></li>' for h, t in NAV)
    titolo_completo = f"{titolo} · {NEGOZIO['nome']}" if titolo else f"{NEGOZIO['nome']} · Merceria e sartoria a Brescia"
    social = "".join(
        f'<a href="{esc(NEGOZIO[k])}" rel="noopener">{n}</a>'
        for k, n in (("instagram", "Instagram"), ("facebook", "Facebook")) if NEGOZIO[k])
    cat_links = "".join(f'<li><a href="{c["slug"]}.html">{c["nome"]}</a></li>' for c in CATEGORIE[:8])
    canon = f'<link rel="canonical" href="{NEGOZIO["sito"].rstrip("/")}/{"" if file == "index.html" else file}">' if NEGOZIO["sito"] else ""
    doc = f"""<!doctype html>
<html lang="it">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(titolo_completo)}</title>
<meta name="description" content="{esc(descrizione)}">
<meta property="og:title" content="{esc(titolo_completo)}">
<meta property="og:description" content="{esc(descrizione)}">
<meta property="og:type" content="website">
<meta property="og:locale" content="it_IT">
{canon}
<meta name="theme-color" content="#355743">
<link rel="icon" href="favicon.png" type="image/png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Caveat:wght@500;600&family=Fraunces:opsz,wght@9..144,400;9..144,600&family=Nunito+Sans:opsz,wght@6..12,400;6..12,600;6..12,700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="style.css">
{extra_head}
</head>
<body>
<a class="salta" href="#contenuto">Vai al contenuto</a>
<header class="testata">
  <div class="testata-in">
    <a class="marchio" href="index.html" aria-label="{NEGOZIO['nome']} – home">
      <img src="logo.png" width="300" height="300" alt="">
      <span><b>La Bottoneria</b><small>merceria · Brescia</small></span>
    </a>
    <button class="menu-btn" aria-expanded="false" aria-controls="menu">
      <span class="hamb" aria-hidden="true"></span><span class="vh">Menu</span>
    </button>
    <nav id="menu" class="menu" aria-label="Principale">
      <ul>{nav}</ul>
      <a class="btn btn-wa btn-small" href="{wa()}" target="_blank" rel="noopener">{ICONA_WA}Scrivici</a>
    </nav>
  </div>
</header>
<main id="contenuto">
{corpo}
</main>
<footer class="piede">
  <div class="piede-in wrap">
    <div class="piede-col piede-marchio">
      <img src="logo.png" width="300" height="300" alt="{NEGOZIO['nome']} merceria" loading="lazy">
      <p class="script">{CARTELLINO['titolo']}</p>
      <p>Creati e confezionati artigianalmente nella nostra sartoria.</p>
    </div>
    <div class="piede-col">
      <h2>Prodotti</h2>
      <ul>{cat_links}<li><a href="prodotti.html">Tutte le categorie →</a></li></ul>
    </div>
    <div class="piede-col">
      <h2>Vieni a trovarci</h2>
      <address>{indirizzo_link()}</address>
      {contatti_icone("contatti-icone contatti-piede")}
      <p class="social">{social}</p>
    </div>
    <div class="piede-col">
      <h2>Orari</h2>
      {orari_html("orari orari-mini")}
    </div>
  </div>
  <div class="legale wrap">
    <span>© <span data-anno>2026</span> {NEGOZIO['nome']}</span>
    <span>P.IVA {NEGOZIO['piva']} · REA {NEGOZIO['rea']}</span>
  </div>
</footer>
<a class="wa-float" href="{wa()}" target="_blank" rel="noopener" aria-label="Scrivici su WhatsApp">{ICONA_WA}</a>
<script src="main.js" defer></script>
</body>
</html>
"""
    (OUT / file).write_text(doc, encoding="utf-8")
    print("  ✓", file)


# ---------------------------------------------------------------- blocchi
VALORI = [
    ("sew", "Fatto a mano", "Cuciamo e confezioniamo nella nostra sartoria."),
    ("abc", "Ricamo personalizzato", "Nomi e iniziali ricamati da noi."),
    ("uniform", "Su misura", "Grembiuli e capi fatti sulle tue misure."),
    ("gift", "Buoni regalo", "Per regalare la libertà di scelta."),
]
def _carica_icone():
    """Le icone Fontello sono salvate come tracciati SVG in config.json."""
    with zipfile.ZipFile(ROOT / "icone" / "fontello-e358c347.zip") as z:
        cfg = json.loads(z.read("fontello-e358c347/config.json"))
    return {g["css"]: g["svg"] for g in cfg["glyphs"]}


ICONE = _carica_icone()


def icona(nome):
    g = ICONE[nome]
    return (f'<span class="icona" aria-hidden="true"><svg viewBox="0 0 {g["width"]} 1000">'
            f'<path fill="currentColor" d="{g["path"]}"/></svg></span>')


def valori_html():
    items = "".join(f'<li>{icona(i)}<div><h3>{t}</h3><p>{d}</p></div></li>' for i, t, d in VALORI)
    return f'<section class="valori wrap" aria-label="Perché sceglierci"><ul>{items}</ul></section>'


def card_categoria(c, sizes="(min-width: 1000px) 25vw, (min-width: 600px) 33vw, 50vw"):
    n = len(c["sotto"])
    meta = f"{n} tipologie" if n else "Chiedi in negozio"
    return (f'<li><a class="card-cat" href="{c["slug"]}.html">'
            f'<span class="card-foto">{img(c["foto"], "", sizes)}</span>'
            f'<span class="card-testo"><b>{c["nome"]}</b><small>{meta}</small></span></a></li>')


def griglia_categorie(cats):
    return f'<ul class="griglia-cat">{"".join(card_categoria(c) for c in cats)}</ul>'


def cartellino_html():
    return f"""<figure class="cartellino">
  <span class="spago" aria-hidden="true"></span>
  <p class="script">{CARTELLINO['titolo']}</p>
  <blockquote><p>{CARTELLINO['testo']}</p><p class="motto">{CARTELLINO['motto']}</p></blockquote>
  <figcaption>{CARTELLINO['nota']}</figcaption>
</figure>"""


def visita_html():
    return f"""<section class="visita">
  <div class="wrap visita-in">
    <div class="visita-foto">{img("bottoneria-2.jpg", "La vetrina della Bottoneria in via Cremona a Brescia", "(min-width: 900px) 55vw, 100vw")}</div>
    <div class="visita-testo">
      <p class="occhiello">Vieni a trovarci</p>
      <h2>In via Cremona, a Brescia</h2>
      <address>{indirizzo_link(" · ")}</address>
      {orari_html()}
      <div class="azioni">
        <a class="btn" href="contatti.html">Come arrivare</a>
        <a class="btn btn-ghost" href="{wa()}" target="_blank" rel="noopener">{ICONA_WA}WhatsApp</a>
      </div>
    </div>
  </div>
</section>"""


def come_ordinare_html():
    return f"""<aside class="come-ordinare">
  <h2>Come si ordina?</h2>
  <ol>
    <li><b>Scrivici su WhatsApp</b> cosa ti interessa: ti mandiamo foto, fantasie disponibili e prezzi.</li>
    <li><b>Scegli insieme a noi</b> tessuto, colore e personalizzazione.</li>
    <li><b>Ritira in negozio</b> o chiedici della spedizione.</li>
  </ol>
  <a class="btn btn-wa" href="{wa()}" target="_blank" rel="noopener">{ICONA_WA}Scrivici su WhatsApp</a>
</aside>"""


# ---------------------------------------------------------------- pagine
def ricciolo_path(a=4.0, b0=16.0, b1=7.0, giri=3, spire=1.6, rs=9.0):
    """Un filo che si arrotola: anelli che si stringono e finiscono in una spirale."""
    pts = []
    n = 300
    tot = giri * 2 * math.pi
    for i in range(n + 1):
        t = i / n * tot
        r = b0 + (b1 - b0) * i / n
        pts.append((a * t + r * math.sin(t), 30 - r * math.cos(t)))
    cx, cy = pts[-1][0], pts[-1][1] - rs
    m = 120
    for j in range(1, m + 1):
        th = j / m * spire * 2 * math.pi
        r = rs * (1 - 0.75 * j / m)
        pts.append((cx + r * math.sin(th), cy + r * math.cos(th)))
    mx = min(x for x, _ in pts) - 3
    my = min(y for _, y in pts) - 3
    d = "M" + " L".join(f"{x - mx:.1f},{y - my:.1f}" for x, y in pts)
    w = max(x for x, _ in pts) - mx + 3
    h = max(y for _, y in pts) - my + 3
    return d, w, h


RICCIOLO_D, RICCIOLO_W, RICCIOLO_H = ricciolo_path()


def ricciolo(lato):
    return (f'<svg class="ricciolo ricciolo-{lato}" viewBox="0 0 {RICCIOLO_W:.0f} {RICCIOLO_H:.0f}" aria-hidden="true">'
            f'<path d="{RICCIOLO_D}" pathLength="1"/></svg>')


def hero_html():
    slides = []
    for i, h in enumerate(HERO):
        testo, href = h["bottone"]
        slides.append(f"""<div class="slide{' attiva' if i == 0 else ''}" role="group" aria-roledescription="slide" aria-label="{i + 1} di {len(HERO)}"{'' if i == 0 else ' aria-hidden="true"'}>
    {img(h["foto"], "", "100vw", cls="slide-foto", eager=(i == 0)).replace('loading="lazy"', 'loading="eager"')}
    <div class="slide-testo">
      <p class="slide-riga">{ricciolo("sx")}<span>{h['riga']}</span>{ricciolo("dx")}</p>
      <{'h1' if i == 0 else 'p'} class="slide-titolo">{h['titolo']}</{'h1' if i == 0 else 'p'}>
      <p class="slide-sotto">{h['sotto']}</p>
      <a class="btn btn-chiaro" href="{href}"{'' if i == 0 else ' tabindex="-1"'}>{testo}</a>
    </div>
  </div>""")
    punti = "".join(f'<button type="button" aria-label="Vai alla slide {i + 1}"{" aria-current=true" if i == 0 else ""}></button>' for i in range(len(HERO)))
    return f"""<section class="slider" aria-roledescription="carousel" aria-label="In evidenza">
  {"".join(slides)}
  <button class="freccia freccia-sx" type="button" aria-label="Slide precedente"><svg viewBox="0 0 24 24"><path d="M15 5l-7 7 7 7"/></svg></button>
  <button class="freccia freccia-dx" type="button" aria-label="Slide successiva"><svg viewBox="0 0 24 24"><path d="M9 5l7 7-7 7"/></svg></button>
  <div class="punti">{punti}</div>
</section>"""


def scegli_tu_html():
    st = SCEGLI_TU
    scelte = "".join(f'<li>{icona(i)}<h3>{t}</h3><p>{d}</p></li>' for i, t, d in st["scelte"])
    return f"""<section class="scegli wrap">
  <header class="sez-testa">
    <p class="occhiello">{st['occhiello']}</p>
    <h2>{st['titolo']}</h2>
    {DIVISORE}
    <p class="lead">{st['testo']}</p>
  </header>
  <ol class="scelte">{scelte}</ol>
</section>"""


def card_pers(p):
    return f"""<li><a class="card-pers" href="{p['slug']}.html">
  <span class="card-pers-foto"><span class="card-pers-img">{img(p["foto"], "", "(min-width: 1000px) 33vw, (min-width: 640px) 50vw, 100vw")}</span>{icona(p["icona"])}</span>
  <span class="card-pers-testo"><b>{p['nome']}</b><span>{p['breve']}</span><span class="btn btn-small">Scopri e personalizza →</span></span>
</a></li>"""


def personalizzazioni_griglia():
    return f'<ul class="griglia-pers">{"".join(card_pers(p) for p in PERSONALIZZAZIONI)}</ul>'


def quattro_categorie():
    cats = [next(c for c in CATEGORIE if c["slug"] == s) for s in CATEGORIE_HOME]
    voci = "".join(f'<li><a href="{c["slug"]}.html">{img(c["foto"], "", "(min-width: 900px) 25vw, 50vw")}<span>{c["nome"]}</span></a></li>' for c in cats)
    return f'<ul class="quattro">{voci}</ul>'


def home():
    corpo = f"""
{hero_html()}
{scegli_tu_html()}
<section class="sezione-pers">
  <div class="wrap">
    <header class="sez-testa">
      <p class="occhiello">Le nostre personalizzazioni</p>
      <h2>Fatto a mano, con il tuo nome</h2>
      {DIVISORE}
    </header>
    {personalizzazioni_griglia()}
    <div class="azioni centro-flex"><a class="btn btn-wa" href="{wa("Ciao! Vorrei personalizzare un capo.")}" target="_blank" rel="noopener">{ICONA_WA}Raccontaci la tua idea</a></div>
  </div>
</section>
<section class="sezione wrap">
  <header class="sez-testa">
    <p class="occhiello">In negozio</p>
    <h2>La merceria</h2>
    {DIVISORE}
  </header>
  {quattro_categorie()}
  <p class="centro"><a class="link-freccia" href="prodotti.html">Tutti i prodotti: neonato, asilo, casa, buoni regalo e altro →</a></p>
</section>
"""
    pagina("index.html", "", "La Bottoneria, merceria a Brescia da 50 anni: nomi ricamati, grembiulini su misura, set asilo, set nascita e regali per le maestre. Scegli tutto tu.", corpo, extra_head=jsonld())


def prodotti():
    corpo = f"""
<section class="testa-pagina wrap">
  <p class="occhiello">Prodotti</p>
  <h1>Tutte le categorie</h1>
  <p class="lead">Molti articoli sono pezzi unici o si realizzano su richiesta: scrivici per sapere cosa c'è disponibile, ti mandiamo le foto.</p>
  {DIVISORE}
</section>
<section class="wrap sezione-stretta">
  {griglia_categorie(CATEGORIE)}
</section>
<section class="wrap sezione">{come_ordinare_html()}</section>
"""
    pagina("prodotti.html", "Prodotti", "Neonato, bimbo e bimba, asilo, ricamo, merceria, tessuti, buste e sacche, casa: tutte le categorie della Bottoneria di Brescia.", corpo, attivo="prodotti.html")


def categoria(c):
    if c["sotto"]:
        voci = "".join(
            f'<li><span>{esc(s)}</span><a href="{wa(f"Ciao! Vorrei informazioni su: {c["nome"]} – {s}")}" target="_blank" rel="noopener" aria-label="Chiedi informazioni su {esc(s)} via WhatsApp">Chiedi {ICONA_WA}</a></li>'
            for s in c["sotto"])
        elenco = f"""<section class="wrap sezione-stretta">
  <h2 class="titolo-sez">Cosa realizziamo</h2>
  <ul class="sottocat">{voci}</ul>
</section>"""
    else:
        elenco = ""
    gal = ""
    if c["galleria"]:
        gal = ('<section class="wrap sezione-stretta"><h2 class="titolo-sez">Dal nostro laboratorio</h2><ul class="galleria">'
               + "".join(f'<li>{img(g, "", "(min-width: 900px) 25vw, 50vw")}</li>' for g in c["galleria"])
               + "</ul></section>")
    altre = [x for x in CATEGORIE if x["slug"] != c["slug"]][:4]
    corpo = f"""
<nav class="briciole wrap" aria-label="Percorso"><a href="index.html">Home</a> / <a href="prodotti.html">Prodotti</a> / <span>{c['nome']}</span></nav>
<section class="cat-testa wrap">
  <div class="cat-testo">
    <h1>{c['nome']}</h1>
    <p class="lead">{c['intro']}</p>
    <a class="btn btn-wa" href="{wa(f"Ciao! Vorrei informazioni sulla categoria {c['nome']}.")}" target="_blank" rel="noopener">{ICONA_WA}Chiedi disponibilità e prezzi</a>
  </div>
  <div class="cat-foto cucito">{img(c["foto"], c["nome"], "(min-width: 900px) 45vw, 100vw", eager=True)}</div>
</section>
{elenco}
{gal}
<section class="wrap sezione">{come_ordinare_html()}</section>
<section class="wrap sezione">
  <h2 class="titolo-sez">Altre categorie</h2>
  {griglia_categorie(altre)}
</section>
"""
    pagina(f"{c['slug']}.html", c["nome"], f"{c['nome']} alla Bottoneria di Brescia: {c['intro']}", corpo, attivo="prodotti.html")


def personalizzazioni():
    corpo = f"""
<section class="testa-pagina wrap">
  <p class="occhiello">Personalizzazioni</p>
  <h1>{SCEGLI_TU['titolo']}</h1>
  <p class="lead">{SCEGLI_TU['testo']}</p>
  {DIVISORE}
</section>
<section class="wrap sezione-stretta">{personalizzazioni_griglia()}</section>
{scegli_tu_html().replace('<h2>' + SCEGLI_TU['titolo'] + '</h2>', '<h2>Cosa puoi scegliere</h2>').replace('<p class="lead">' + SCEGLI_TU['testo'] + '</p>', '')}
<section class="wrap sezione">{come_ordinare_html()}</section>
"""
    pagina("personalizzazioni.html", "Personalizzazioni", "Nomi ricamati, grembiulini su misura, set asilo, set nascita e regali per le maestre: alla Bottoneria di Brescia scegli tutto tu.", corpo, attivo="personalizzazioni.html")


def pagina_pers(p):
    scegli = "".join(f"<li>{s}</li>" for s in p["scegli"])
    contiene = ""
    if p["contiene"]:
        voci = "".join(
            f'<li><span>{esc(c)}</span><a href="{wa(f"Ciao! Per il {p["nome"].lower()} vorrei informazioni su: {c}")}" target="_blank" rel="noopener" aria-label="Chiedi informazioni su {esc(c)} via WhatsApp">Chiedi {ICONA_WA}</a></li>'
            for c in p["contiene"])
        contiene = f'<section class="wrap sezione-stretta"><h2 class="titolo-sez">{p["contiene_titolo"]}</h2><ul class="sottocat">{voci}</ul></section>'
    gal = ""
    if p["galleria"]:
        gal = ('<section class="wrap sezione-stretta"><h2 class="titolo-sez">Dal nostro laboratorio</h2><ul class="galleria">'
               + "".join(f'<li>{img(g, "", "(min-width: 900px) 25vw, 50vw")}</li>' for g in p["galleria"])
               + "</ul></section>")
    altre = "".join(card_pers(x) for x in PERSONALIZZAZIONI if x["slug"] != p["slug"])
    passi = ""
    if p["slug"] == "grembiulini":
        passi = """<ol class="passi"><li><b>Scrivici</b><span>Contattaci su WhatsApp o vieni in negozio.</span></li>
<li><b>Prendi le misure</b><span>Ti inviamo un semplice schema: ci bastano 3 misure.</span></li>
<li><b>Scegli la fantasia</b><span>Tessuto, colletto e personalizzazione: decidi tu.</span></li></ol>"""
    corpo = f"""
<nav class="briciole wrap" aria-label="Percorso"><a href="index.html">Home</a> / <a href="personalizzazioni.html">Personalizzazioni</a> / <span>{p['nome']}</span></nav>
<section class="cat-testa wrap">
  <div class="cat-testo">
    <p class="occhiello">Su misura per te</p>
    <h1>{p['nome']}</h1>
    <p class="lead">{p['intro']}</p>
    {passi}
    <a class="btn btn-wa" href="{wa(f"Ciao! Vorrei informazioni su: {p['nome']}.")}" target="_blank" rel="noopener">{ICONA_WA}Chiedi informazioni</a>
  </div>
  <div class="cat-foto cucito">{img(p["foto"], p["nome"], "(min-width: 900px) 45vw, 100vw", eager=True)}</div>
</section>
<section class="wrap sezione-stretta">
  <div class="scegli-box">
    <h2>Scegli tu</h2>
    <ul class="spunte">{scegli}</ul>
  </div>
</section>
{contiene}
{gal}
<section class="wrap sezione">{come_ordinare_html()}</section>
<section class="wrap sezione">
  <h2 class="titolo-sez">Altre personalizzazioni</h2>
  <ul class="griglia-pers griglia-pers-4">{altre}</ul>
</section>
"""
    pagina(f"{p['slug']}.html", p["nome"], f"{p['nome']} alla Bottoneria di Brescia: {p['breve']}", corpo, attivo="personalizzazioni.html")


def chi_siamo():
    corpo = f"""
<section class="testa-pagina wrap">
  <p class="occhiello">Chi siamo</p>
  <h1>La Bottoneria, merceria di Brescia</h1>
  {DIVISORE}
</section>
<section class="feature">
  <div class="wrap feature-in">
    <div class="feature-foto cucito">{img(CHI_SIAMO["foto"], "Il tavolo da lavoro della sartoria con tessuti patchwork, forbici e taglierina", "(min-width: 900px) 45vw, 100vw", eager=True)}</div>
    <div class="feature-testo prosa">{"".join(f"<p>{t}</p>" for t in CHI_SIAMO["testo"])}</div>
  </div>
</section>
<section class="wrap sezione-stretta">
  <ul class="galleria">
    <li>{img("_1040357.jpg", "Parete di bottoni colorati", "(min-width: 900px) 25vw, 50vw")}</li>
    <li>{img("image00015.jpg", "Nastri con il marchio La Bottoneria Merceria Brescia", "(min-width: 900px) 25vw, 50vw")}</li>
    <li>{img("merceria.jpg", "Scaffale di gomitoli", "(min-width: 900px) 25vw, 50vw")}</li>
    <li>{img("bottoneria-9.jpg", "L'interno del negozio", "(min-width: 900px) 25vw, 50vw")}</li>
  </ul>
</section>
<section class="motto-banda"><div class="wrap">{cartellino_html()}</div></section>
{visita_html()}
"""
    pagina("chi-siamo.html", "Chi siamo", "La storia della Bottoneria, merceria e laboratorio di sartoria in via Cremona a Brescia.", corpo, attivo="chi-siamo.html")


def contatti():
    q = quote(f"{NEGOZIO['indirizzo']}, {NEGOZIO['cap_citta']}")
    corpo = f"""
<section class="testa-pagina wrap">
  <p class="occhiello">Contatti</p>
  <h1>Dove trovarci</h1>
  {DIVISORE}
</section>
<section class="wrap contatti-griglia">
  <div class="contatti-box">
    <h2>La Bottoneria Merceria</h2>
    <address>{indirizzo_link()}</address>
    {contatti_icone()}
    <h2>Orari di apertura</h2>
    {orari_html()}
    <div class="azioni">
      <a class="btn btn-wa" href="{wa()}" target="_blank" rel="noopener">{ICONA_WA}Scrivici su WhatsApp</a>
      <a class="btn btn-ghost" href="{NEGOZIO['mappa']}" target="_blank" rel="noopener">Apri in Google Maps</a>
    </div>
  </div>
  <div class="mappa cucito" data-mappa="https://www.google.com/maps?q={q}&amp;output=embed">
    {img("bottoneria-2.jpg", "La vetrina della Bottoneria", "(min-width: 900px) 50vw, 100vw")}
    <div class="mappa-velo">
      <p>La mappa è fornita da Google Maps, che potrebbe usare cookie.</p>
      <button class="btn" type="button">Mostra la mappa</button>
    </div>
  </div>
</section>
"""
    pagina("contatti.html", "Contatti", f"Indirizzo, orari e contatti della Bottoneria: {NEGOZIO['indirizzo']}, {NEGOZIO['cap_citta']}. Scrivici su WhatsApp.", corpo, attivo="contatti.html", extra_head=jsonld())


def pagina_404():
    corpo = f"""<section class="testa-pagina wrap">
  <p class="script hero-script">ops, un filo si è perso…</p>
  <h1>Pagina non trovata</h1>
  <p class="lead">La pagina che cerchi non esiste o è stata spostata.</p>
  <div class="azioni centro-flex"><a class="btn" href="index.html">Torna alla home</a></div>
</section>"""
    pagina("404.html", "Pagina non trovata", "Pagina non trovata.", corpo)


# ---------------------------------------------------------------- main
def main():
    OUT.mkdir(exist_ok=True)
    (OUT / "img").mkdir(exist_ok=True)
    shutil.copy(SRC / "style.css", OUT / "style.css")
    shutil.copy(SRC / "main.js", OUT / "main.js")
    shutil.copy(ROOT / "logo" / "logo-300.png", OUT / "logo.png")
    shutil.copy(ROOT / "logo" / "favicon.png", OUT / "favicon.png")
    (OUT / ".nojekyll").write_text("")

    print("Genero le pagine…")
    home()
    prodotti()
    for c in CATEGORIE:
        categoria(c)
    personalizzazioni()
    for p in PERSONALIZZAZIONI:
        pagina_pers(p)
    chi_siamo()
    contatti()
    pagina_404()

    # rimuove le immagini non più usate
    usate = {p.split("/")[-1] for i in _cache.values() for p, _ in i["varianti"]}
    for f in (OUT / "img").glob("*.webp"):
        if f.name not in usate:
            f.unlink()
    peso = sum(f.stat().st_size for f in OUT.rglob("*") if f.is_file()) / 1e6
    print(f"Fatto: {len(_cache)} foto, sito in docs/ ({peso:.1f} MB)")


if __name__ == "__main__":
    main()
