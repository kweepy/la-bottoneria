"""
CONTENUTI DEL SITO — LA BOTTONERIA
==================================
Questo è l'unico file da modificare per cambiare testi, orari, contatti,
categorie e foto. Dopo una modifica, rigenera il sito con:

    python3 src/build.py

Le foto si prendono dalla cartella "immagini/" (basta scrivere il nome del file).
"""

NEGOZIO = {
    "nome": "La Bottoneria",
    "sottotitolo": "Merceria a Brescia",
    "indirizzo": "Via Cremona, 76",
    "cap_citta": "25124 Brescia",
    "mappa": "https://maps.app.goo.gl/boP4J8TNVsKsBB378",   # link Google Maps dell'indirizzo
    "whatsapp": "393476002282",          # solo cifre, con prefisso 39
    "whatsapp_visibile": "+39 347 600 2282",
    "email": "info@labottoneria.it",
    "piva": "03212540177",
    "rea": "BS-343978",
    "instagram": "",   # es. "https://www.instagram.com/labottoneria" (vuoto = non mostrato)
    "facebook": "",
    "sito": "",        # es. "https://www.labottoneria.it" (serve per i link condivisi)
}

# Orari: giorno -> lista di fasce "HH:MM-HH:MM" (lista vuota = chiuso)
ORARI = [
    ("Lunedì",    ["15:00-19:00"]),
    ("Martedì",   ["09:00-12:00", "15:00-18:00"]),
    ("Mercoledì", ["10:00-18:00"]),
    ("Giovedì",   ["10:00-18:00"]),
    ("Venerdì",   ["10:00-18:00"]),
    ("Sabato",    ["09:00-12:00"]),
    ("Domenica",  []),
]

# Testi ricorrenti
CARTELLINO = {
    "titolo": "pezzi unici in puro cotone",
    "testo": ("Creati e confezionati artigianalmente nella nostra sartoria, "
              "selezionando con cura i materiali e utilizzando tecniche di lavoro "
              "che rappresentano il cuore e l'impegno di chi li ha prodotti."),
    "motto": ("Ogni dettaglio, ogni imperfezione è la conferma dell'opera "
              "artigianale e dell'unicità di ogni prodotto."),
    "nota": "Si confezionano articoli su misura",
}

# Categorie di prodotti (ordine = ordine nel sito)
CATEGORIE = [
    {
        "slug": "neonato", "nome": "Neonato",
        "foto": "IMG_8666.jpg",
        "galleria": ["nascita-1.jpeg", "nascita-8.jpeg", "nascita-2.jpeg", "nascita-10g.jpeg", "nascita-7.jpeg", "nascita-3.jpeg", "nascita-9g.jpg", "nascita-4.jpeg", "nascita-5.jpeg", "nascita-6.jpeg", "borsa-cambio-3.jpeg", "borsa-cambio-2.jpeg", "borsa-cambio-1.jpeg", "image00033.jpg", "bottoneria-7.jpg", "casa.jpg", "IMG_8683.jpg"],
        "intro": "Il corredo per i primi mesi, cucito da noi in puro cotone e personalizzabile con il nome del bimbo.",
        "sotto": ["Accappatoi", "Asciugamani", "Bavagli", "Beauty case", "Borse",
                  "Buste e sacche", "Copertine", "Fasciatoio da passeggio",
                  "Fiocchi nascita", "Sacchetti nascita", "Set lavette",
                  "Set lenzuolini culla", "Set lenzuolini lettino",
                  "Accessori doudou", "Accessori calzine", "Cappellini"],
    },
    {
        "slug": "bambino", "nome": "Bimbo e bimba",
        "foto": "b05d42bb-13e7-4b55-81e9-1b95c1cc162b.jpg",
        "galleria": ["zainetto-10g.jpeg", "zainetto-7.jpeg", "zainetto-8.jpeg", "bottoneria-6.jpg"],
        "intro": "Abitini, pigiamini e costumini con le nostre fantasie, anche coordinati mamma e bimba.",
        "sotto": ["Abitini", "Accessori", "Completi mare", "Costumini",
                  "Gonne mamma e bimba", "Pigiamini", "T-shirt ricamate"],
    },
    {
        "slug": "asilo", "nome": "Asilo",
        "foto": "image00025.jpg",
        "galleria": ["grembiulino-5.jpeg", "grembiulino-1.jpeg", "grembiulino-2.jpeg", "grembiulino-8.jpeg", "grembiulino-9.jpeg", "grembiulino-11.jpeg", "zainetto-1.jpeg", "zainetto-7.jpeg", "zainetto-8.jpeg", "zainetto-3.jpeg", "zainetto-6.jpeg", "grembiulino-4.jpeg", "grembiulino-3.jpeg", "grembiulino-6.jpeg", "grembiulino-10.jpeg", "grembiulino-12g.jpeg", "grembiulino-7.jpeg", "zainetto-9.jpeg", "zainetto3.jpeg", "zainnetto-5.jpeg", "zainetto-10g.jpeg", "grembiule.jpg", "set_asilo_zainetto_personalizzato.jpg", "zainetto_personalizzato.jpg", "pochette.jpg", "bottoneria-1.jpg", "image00042.jpg", "bottoneria-10.jpg"],
        "intro": "Grembiuli, sacchette e bavaglie per la scuola, con il nome ricamato perché nulla vada perso.",
        "sotto": ["Accessori", "Bavaglie", "Grembiuli", "Sacchette", "Salviette",
                  "Pettorine", "Tovagliette", "Tovaglioli", "Zainetti", "Portabavaglia"],
    },
    {
        "slug": "ricamo", "nome": "Ricamo",
        "foto": "image00005.jpg",
        "galleria": ["grembiulino-4.jpeg", "zainetto-1.jpeg", "nascita-2.jpeg", "pochette-1g.jpeg", "tote-bag-1.jpeg", "borsa-cambio-3.jpeg", "grembiulino-10.jpeg", "nascita-4.jpeg", "porta-fedi.jpeg", "zainetto3.jpeg", "grembiulino-12g.jpeg", "nascita-8.jpeg", "_1040309.jpg", "pochette.jpg", "zainetto_personalizzato.jpg", "regalo-maestra-best-teacher.jpg", "bottoneria-3.jpg", "bottoneria-10.jpg"],
        "intro": "Nomi, iniziali e disegni ricamati a macchina su capi, teli e accessori: scegli tu colore e scritta.",
        "sotto": ["Asilo", "Bagno", "Buste e sacche", "Cucina", "Neonato", "Arredo", "Su misura"],
    },
    {
        "slug": "merceria", "nome": "Merceria",
        "foto": "IMG_8658.jpg",
        "galleria": ["_1040357.jpg", "merceria.jpg", "image00015.jpg", "image00009.jpg"],
        "intro": "Bottoni, pizzi, elastici, passamanerie e tutta la minuteria per cucire, rammendare e creare.",
        "sotto": ["Accessori", "Bottoni", "Bordi elastici", "Bordi e passamanerie",
                  "Minuteria", "Pizzi"],
    },
    {
        "slug": "tessuti", "nome": "Tessuti",
        "foto": "image00040.jpg",
        "galleria": ["image00012.jpg", "image00004.jpg"],
        "intro": "Cotonine americane, cotoni italiani, lino e tele da ricamo: vieni a toccarli in negozio.",
        "sotto": ["Cotonine americane", "Cotoni italiani", "Piquet",
                  "Tele da ricamo", "Tinti in filo", "Lino"],
    },
    {
        "slug": "buste-e-sacche", "nome": "Pochette e sacche",
        "foto": "image00034.jpg",
        "galleria": ["pochette-1g.jpeg", "tote-bag-2.jpeg", "tote-bag-1.jpeg", "tote-bag-3.jpeg", "tasca-interna.jpeg", "borsa-cambio-3.jpeg", "borsa-cambio-2.jpeg", "borsa-cambio-1.jpeg", "pochette.jpg", "regalo-maestra-best-teacher.jpg", "idee_regalo.jpg", "bottoneria-3.jpg"],
        "intro": "Pochette, sacche e shopper in cotone e lino, ricamate e pronte da regalare.",
        "sotto": ["Buste", "Sacche", "Shopper"],
    },
    {
        "slug": "casa", "nome": "Casa e arredamento",
        "foto": "bottoneria-5.jpg",
        "galleria": ["porta-fedi.jpeg", "image00009.jpg", "casa.jpg"],
        "intro": "Cuscini, tessili per bagno e cucina, cesti e nappe per dare un tocco artigianale alla casa.",
        "sotto": ["Bagno", "Casa", "Cesterie", "Cucina"],
    },
    {
        "slug": "libri-e-schemi", "nome": "Libri e schemi",
        "foto": "image00004.jpg",
        "galleria": [],
        "intro": "Libri di cucito e ricamo e schemi per i tuoi progetti di punto croce.",
        "sotto": [],
    },
    {
        "slug": "novita", "nome": "Novità",
        "foto": "novita-zainetto-adele.jpg",
        "galleria": ["zainetto-1.jpeg", "tote-bag-2.jpeg", "grembiulino-5.jpeg", "nascita-8.jpeg", "pochette-1g.jpeg", "borsa-cambio-3.jpeg"],
        "intro": "Gli ultimi arrivi in negozio e le nuove creazioni della nostra sartoria.",
        "sotto": [],
    },
    {
        "slug": "buono-regalo", "nome": "Buono regalo",
        "foto": "buono-regalo.jpg",
        "galleria": [],
        "intro": "Per regalare la libertà di scelta: il buono spesa vale in negozio su tutti gli articoli.",
        "sotto": [],
    },
    {
        "slug": "outlet", "nome": "Outlet",
        "foto": "bottoneria-8.jpg",
        "galleria": [],
        "intro": "Fine serie, scampoli e ultimi pezzi a prezzo ridotto.",
        "sotto": [],
    },
]

# ---------------------------------------------------------------------------
# APERTURA DELLA HOME (foto che scorrono)
# "riga" = frase piccola sopra, "titolo" = scritta grande, "sotto" = frase sotto
HERO = [
    {"foto": "_1040357.jpg", "riga": "Benvenuti alla", "titolo": "La Bottoneria",
     "sotto": "Merceria a Brescia da 35 anni",
     "bottone": ("Scopri la nostra storia", "chi-siamo.html")},
    {"foto": "bottoneria-1.jpg", "riga": "Su misura per te", "titolo": "Set asilo",
     "sotto": "Sacca, bavaglia e grembiulino con il nome del tuo bambino",
     "bottone": ("Scopri il set asilo", "set-asilo.html")},
    {"foto": "la-bottoneria-brescia-7.jpg", "riga": "Su misura per te", "titolo": "Set nascita",
     "sotto": "Il corredo per il nuovo arrivato, scelto e ricamato con te",
     "bottone": ("Scopri il set nascita", "set-nascita.html")},
]

# Il "punto focale": la personalizzazione, scegli tutto tu
SCEGLI_TU = {
    "occhiello": "Personalizzazione",
    "titolo": "Fai la tua scelta",
    "testo": ("Ogni capo nasce su misura nel nostro laboratorio: tu scegli, noi cuciamo e ricamiamo. "
              "Nomi, grembiulini, set per l'asilo e per la nascita, regali per le maestre: "
              "nulla è uguale a un altro, perché è fatto per te."),
    "scelte": [
        ("uniform", "Il capo", "Grembiule, sacca, bavaglia, asciugamano, pochette…"),
        ("tailor", "La fantasia", "Tessuti in puro cotone tra cui scegliere in negozio."),
        ("abc", "Nome e colore", "Il nome, lo stile della scritta e il colore del filo."),
        ("meter-2", "Le misure", "Su misura per il tuo bambino, con 3 semplici misure."),
    ],
}

# Le personalizzazioni: ognuna ha una sua pagina (slug.html)
PERSONALIZZAZIONI = [
    {
        "slug": "nomi-ricamati", "nome": "Nomi ricamati", "icona": "abc",
        "foto": "_1040309.jpg", "galleria": ["grembiulino-4.jpeg", "zainetto-1.jpeg", "nascita-2.jpeg", "pochette-1g.jpeg", "tote-bag-1.jpeg", "borsa-cambio-3.jpeg", "grembiulino-10.jpeg", "nascita-4.jpeg", "porta-fedi.jpeg", "zainetto3.jpeg", "grembiulino-12g.jpeg", "nascita-8.jpeg", "image00005.jpg", "pochette.jpg", "zainetto_personalizzato.jpg", "regalo-maestra-best-teacher.jpg", "bottoneria-10.jpg", "bottoneria-3.jpg", "image00033.jpg", "grembiule.jpg"],
        "breve": "Il nome, le iniziali o un disegno ricamati a macchina su quasi ogni capo e tessuto.",
        "intro": ("Realizziamo personalizzazioni su quasi tutti i tipi di capi e tessuti: asciugamani, "
                  "bavaglie, sacche, accappatoi, tovagliette. Scegli il colore e la scritta più adatti al tuo capo."),
        "scegli": ["Il nome, le iniziali o una breve frase", "Lo stile della scritta",
                   "Il colore del filo", "La posizione del ricamo", "Un piccolo disegno da abbinare"],
        "contiene_titolo": "Cosa possiamo ricamare",
        "contiene": ["Asilo", "Bagno", "Buste e sacche", "Cucina", "Neonato", "Arredo"],
    },
    {
        "slug": "grembiulini", "nome": "Grembiulini su misura", "icona": "uniform",
        "foto": "image00025.jpg", "galleria": ["grembiulino-5.jpeg", "grembiulino-1.jpeg", "grembiulino-2.jpeg", "grembiulino-8.jpeg", "grembiulino-9.jpeg", "grembiulino-11.jpeg", "grembiulino-4.jpeg", "grembiulino-3.jpeg", "grembiulino-6.jpeg", "grembiulino-10.jpeg", "grembiulino-12g.jpeg", "grembiulino-7.jpeg", "grembiule.jpg", "image00036.jpg", "bottoneria-1.jpg"],
        "breve": "Grembiuli in 100% cotone per scuola materna ed elementare, cuciti sulle misure del bambino.",
        "intro": ("Realizziamo grembiuli in <strong>100% cotone su misura</strong> per scuola materna ed elementare, "
                  "con le fantasie scelte da voi. Possibilità di personalizzazione con nome e ricamo a macchina "
                  "(realizzato da noi), oppure con inserto in tela Aida per il ricamo fai da te."),
        "scegli": ["La fantasia del tessuto", "Il colletto e le finiture", "Il nome ricamato o l'inserto in tela Aida",
                   "Il colore del ricamo", "Le misure del bambino"],
        "contiene_titolo": None, "contiene": [],
    },
    {
        "slug": "set-asilo", "nome": "Set asilo", "icona": "rucksack",
        "foto": "image00042.jpg", "galleria": ["zainetto-1.jpeg", "zainetto-7.jpeg", "zainetto-8.jpeg", "zainetto-3.jpeg", "zainetto-6.jpeg", "zainetto-9.jpeg", "zainetto3.jpeg", "zainnetto-5.jpeg", "zainetto-10g.jpeg", "grembiulino-5.jpeg", "grembiulino-1.jpeg", "grembiulino-2.jpeg", "grembiulino-8.jpeg", "set_asilo_zainetto_personalizzato.jpg", "zainetto_personalizzato.jpg", "pochette.jpg", "grembiule.jpg", "bottoneria-1.jpg", "image00025.jpg", "bottoneria-10.jpg"],
        "breve": "Sacca, bavaglia, salvietta e tovaglietta coordinati, con il nome del bambino.",
        "intro": ("Il set per l'asilo lo componi tu: scegli i pezzi che servono, la fantasia e il nome da ricamare. "
                  "Tutto coordinato, tutto riconoscibile, così nulla va perso."),
        "scegli": ["I pezzi del set", "La fantasia coordinata", "Il nome da ricamare", "Il colore del filo"],
        "contiene_titolo": "Puoi comporre il set con",
        "contiene": ["Sacchetta", "Bavaglia", "Portabavaglia", "Salvietta", "Tovaglietta",
                     "Tovagliolo", "Pettorina", "Zainetto", "Grembiule"],
    },
    {
        "slug": "set-nascita", "nome": "Set nascita", "icona": "gift-2",
        "foto": "la-bottoneria-brescia-10.jpg", "galleria": ["nascita-1.jpeg", "nascita-8.jpeg", "nascita-2.jpeg", "nascita-10g.jpeg", "nascita-7.jpeg", "nascita-3.jpeg", "nascita-9g.jpg", "nascita-4.jpeg", "nascita-5.jpeg", "nascita-6.jpeg", "borsa-cambio-3.jpeg", "borsa-cambio-2.jpeg", "borsa-cambio-1.jpeg", "bottoneria-7.jpg", "IMG_8666.jpg", "casa.jpg", "IMG_8683.jpg"],
        "breve": "Il corredo per il nuovo arrivato in 100% cotone: lavette, bavagli, lenzuolini e fiocco nascita.",
        "intro": ("Per accogliere il nuovo arrivato prepariamo un corredo coordinato, cucito in puro cotone e "
                  "personalizzato con il nome o le iniziali. Un regalo unico anche per chi diventa nonno, zia o amica."),
        "scegli": ["I pezzi del corredo", "Tessuti e colori", "Il nome o le iniziali", "La confezione regalo"],
        "contiene_titolo": "Puoi comporre il set con",
        "contiene": ["Fiocco nascita", "Sacchetti nascita", "Set lavette", "Bavagli", "Copertine",
                     "Set lenzuolini culla", "Set lenzuolini lettino", "Asciugamani", "Accappatoi",
                     "Fasciatoio da passeggio", "Cappellini", "Accessori doudou"],
    },
    {
        "slug": "regali-maestre", "nome": "Regali per le maestre", "icona": "gift",
        "foto": "regalo-maestra-best-teacher.jpg", "galleria": ["pochette-1g.jpeg", "tote-bag-2.jpeg", "tote-bag-1.jpeg", "tote-bag-3.jpeg", "tasca-interna.jpeg", "bottoneria-3.jpg", "idee_regalo.jpg", "image00034.jpg", "pochette.jpg"],
        "breve": "Grembiule personalizzato, pochette, shopper e sacche ricamate per dire grazie alle maestre a fine anno.",
        "intro": ("Per la fine dell'anno o per Natale, un pensiero fatto a mano per le maestre: grembiule personalizzato, pochette, "
                  "shopper e sacche con l'iniziale, il nome della classe o una dedica ricamata."),
        "scegli": ["Il tipo di regalo", "Il tessuto", "Iniziale, nome o dedica da ricamare", "Il colore del filo"],
        "contiene_titolo": "Idee regalo",
        "contiene": ["Grembiule personalizzato", "Pochette", "Shopper", "Sacche", "Beauty case"],
    },
]

# Ordine in cui compaiono le personalizzazioni (in home e nelle altre pagine)
ORDINE_PERSONALIZZAZIONI = ["set-nascita", "set-asilo", "grembiulini", "regali-maestre", "nomi-ricamati"]
PERSONALIZZAZIONI.sort(key=lambda p: ORDINE_PERSONALIZZAZIONI.index(p["slug"]))

# Testo sopra le quattro categorie della merceria in home
MERCERIA_INTRO = ("Alla Bottoneria Merceria di Brescia trovi tutto quello che puoi desiderare da una merceria: "
                  "bottoni, nastri, pizzi, elastici, aghi, fili, cotonine americane di qualità, filati DMC "
                  "e tutto quello che serve per il cucito creativo.")

# Le quattro categorie in fondo alla home (slug delle CATEGORIE qui sopra)
CATEGORIE_HOME = ["buste-e-sacche", "tessuti", "novita", "merceria"]

CHI_SIAMO = {
    "foto": "_1040295.jpg",
    "testo": [
        "La Bottoneria è una merceria nel cuore di Brescia, in via Cremona: un negozio dove trovare bottoni, filati, tessuti e tutto il necessario per cucire, insieme a un laboratorio di sartoria dove nascono le nostre creazioni.",
        "Realizziamo <strong>pezzi unici</strong>, creati e confezionati artigianalmente, selezionando con cura i materiali e utilizzando tecniche di lavoro che rappresentano il cuore e l'impegno di chi li ha prodotti.",
        "Corredini per neonati, grembiuli su misura, sacche, accessori per la casa: tutto si può personalizzare con un ricamo, un nome, un colore scelto insieme a te.",
    ],
}
