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
        "galleria": ["image00033.jpg", "bottoneria-7.jpg", "casa.jpg", "IMG_8683.jpg"],
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
        "galleria": ["bottoneria-6.jpg"],
        "intro": "Abitini, pigiamini e costumini con le nostre fantasie, anche coordinati mamma e bimba.",
        "sotto": ["Abitini", "Accessori", "Completi mare", "Costumini",
                  "Gonne mamma e bimba", "Pigiamini", "T-shirt ricamate"],
    },
    {
        "slug": "asilo", "nome": "Asilo",
        "foto": "image00025.jpg",
        "galleria": ["bottoneria-1.jpg", "image00042.jpg", "bottoneria-10.jpg"],
        "intro": "Grembiuli, sacchette e bavaglie per la scuola, con il nome ricamato perché nulla vada perso.",
        "sotto": ["Accessori", "Bavaglie", "Grembiuli", "Sacchette", "Salviette",
                  "Pettorine", "Tovagliette", "Tovaglioli", "Zainetti", "Portabavaglia"],
    },
    {
        "slug": "ricamo", "nome": "Ricamo",
        "foto": "image00005.jpg",
        "galleria": ["_1040309.jpg", "bottoneria-3.jpg", "bottoneria-10.jpg"],
        "intro": "Nomi, iniziali e disegni ricamati a macchina su capi, teli e accessori: scegli tu colore e scritta.",
        "sotto": ["Asilo", "Bagno", "Buste e sacche", "Cucina", "Neonato", "Arredo", "Su misura"],
    },
    {
        "slug": "merceria", "nome": "Merceria",
        "foto": "IMG_8658.jpg",
        "galleria": ["_1040357.jpg", "merceria.jpg", "image00015.jpg"],
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
        "slug": "buste-e-sacche", "nome": "Buste e sacche",
        "foto": "image00034.jpg",
        "galleria": ["idee_regalo.jpg", "bottoneria-3.jpg"],
        "intro": "Pochette, sacche e shopper in cotone e lino, ricamate e pronte da regalare.",
        "sotto": ["Buste", "Sacche", "Shopper"],
    },
    {
        "slug": "casa", "nome": "Casa e arredamento",
        "foto": "bottoneria-5.jpg",
        "galleria": ["image00009.jpg", "casa.jpg"],
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
        "foto": "bottoneria-9.jpg",
        "galleria": [],
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

# Pagina "Su misura"
SU_MISURA = {
    "grembiuli": {
        "titolo": "Grembiuli asilo e scuola su misura",
        "foto": "image00036.jpg",
        "testo": [
            "Realizziamo grembiuli in <strong>100% cotone su misura</strong> per scuola materna ed elementare, con le fantasie scelte da voi.",
            "Possibilità di personalizzazione con nome e ricamo a macchina (realizzato da noi), oppure con inserto in tela Aida per il ricamo fai da te.",
        ],
        "passi": [
            ("Scrivici", "Contattaci su WhatsApp o in negozio."),
            ("Prendi le misure", "Ti inviamo un semplice schema: ci bastano 3 misure."),
            ("Scegli la fantasia", "Tessuto, colletto e personalizzazione: decidi tu."),
        ],
    },
    "ricamo": {
        "titolo": "La personalizzazione è il nostro punto di forza",
        "foto": "_1040309.jpg",
        "testo": [
            "Realizziamo personalizzazioni su quasi tutti i tipi di capi e tessuti, scegliendo il colore e la scritta più adatti al tuo capo.",
            "Hai in mente una personalizzazione particolare? Chiedici informazioni, saremo liete di aiutarti a realizzarla.",
        ],
    },
    "set": [
        {"titolo": "Set nascita", "foto": "bottoneria-7.jpg",
         "testo": "Sacchetti, fiocchi nascita, bavaglini e lavette coordinati, con le iniziali del nuovo arrivato."},
        {"titolo": "Set asilo", "foto": "image00042.jpg",
         "testo": "Sacca, bavaglia, salvietta e tovaglietta abbinati e ricamati con il nome del bambino."},
    ],
}

CHI_SIAMO = {
    "foto": "_1040295.jpg",
    "testo": [
        "La Bottoneria è una merceria nel cuore di Brescia, in via Cremona: un negozio dove trovare bottoni, filati, tessuti e tutto il necessario per cucire, insieme a un laboratorio di sartoria dove nascono le nostre creazioni.",
        "Realizziamo <strong>pezzi unici</strong>, creati e confezionati artigianalmente, selezionando con cura i materiali e utilizzando tecniche di lavoro che rappresentano il cuore e l'impegno di chi li ha prodotti.",
        "Corredini per neonati, grembiuli su misura, sacche, accessori per la casa: tutto si può personalizzare con un ricamo, un nome, un colore scelto insieme a te.",
    ],
}
