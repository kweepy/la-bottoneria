# La Bottoneria — sito web

Sito vetrina della merceria **La Bottoneria** (via Cremona 76, Brescia).
Gli ordini e le richieste arrivano via **WhatsApp**: ogni categoria e ogni tipologia di prodotto ha un pulsante "Chiedi" che apre WhatsApp con il messaggio già scritto.

## Struttura

| Cartella / file      | Cosa contiene |
|----------------------|---------------|
| `docs/`              | **Il sito pronto** (generato automaticamente, non modificarlo a mano) |
| `src/contenuti.py`   | **Testi, orari, contatti, categorie e foto**: è l'unico file da modificare |
| `src/build.py`       | Lo script che genera il sito |
| `src/style.css`, `src/main.js` | Grafica e piccole funzioni (menu, "aperto ora", mappa) |
| `immagini/`, `logo/`, `icone/` | Materiale originale. Le foto vengono ridotte e convertite in WebP in automatico |

## Modificare il sito

1. Cambia testi o foto in `src/contenuti.py` (le foto si indicano con il nome del file in `immagini/`).
2. Rigenera il sito:
   ```bash
   pip install Pillow   # solo la prima volta
   python3 src/build.py
   ```
3. Salva le modifiche su GitHub (commit + push).

## Pubblicare con GitHub Pages (gratis)

Su GitHub: **Settings → Pages → Build and deployment → Source: "Deploy from a branch"**,
scegli il branch `main` e la cartella **`/docs`**, poi **Save**.
Dopo un paio di minuti il sito è online su `https://kweepy.github.io/la-bottoneria/`.
Per usare un dominio proprio (es. `labottoneria.it`) si imposta in **Custom domain** nella stessa pagina,
e va scritto anche in `NEGOZIO["sito"]` dentro `src/contenuti.py`.

## Note

- La mappa di Google viene caricata solo quando il visitatore clicca "Mostra la mappa", così il sito non usa cookie di terze parti all'apertura.
- L'indicatore "Aperto ora / Chiuso ora" usa l'ora italiana e gli orari scritti in `contenuti.py`.
