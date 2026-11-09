// La Bottoneria — piccoli comportamenti del sito
(function () {
  // menu mobile
  var btn = document.querySelector(".menu-btn");
  var menu = document.getElementById("menu");
  if (btn && menu) {
    btn.addEventListener("click", function () {
      var aperto = menu.classList.toggle("aperto");
      btn.setAttribute("aria-expanded", aperto ? "true" : "false");
    });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && menu.classList.contains("aperto")) {
        menu.classList.remove("aperto");
        btn.setAttribute("aria-expanded", "false");
        btn.focus();
      }
    });
  }

  // anno nel piè di pagina
  document.querySelectorAll("[data-anno]").forEach(function (el) {
    el.textContent = new Date().getFullYear();
  });

  // "Aperto ora" / "Chiuso ora" (ora di Brescia)
  function oraItalia() {
    try {
      var parti = new Intl.DateTimeFormat("en-GB", {
        timeZone: "Europe/Rome", weekday: "short", hour: "2-digit", minute: "2-digit", hour12: false
      }).formatToParts(new Date());
      var m = {};
      parti.forEach(function (p) { m[p.type] = p.value; });
      var giorni = { Sun: 0, Mon: 1, Tue: 2, Wed: 3, Thu: 4, Fri: 5, Sat: 6 };
      return { giorno: giorni[m.weekday], minuti: (parseInt(m.hour, 10) % 24) * 60 + parseInt(m.minute, 10) };
    } catch (e) {
      var d = new Date();
      return { giorno: d.getDay(), minuti: d.getHours() * 60 + d.getMinutes() };
    }
  }
  function min(hhmm) { var p = hhmm.split(":"); return +p[0] * 60 + +p[1]; }
  var adesso = oraItalia();
  document.querySelectorAll(".stato-apertura").forEach(function (el) {
    var orari;
    try { orari = JSON.parse(el.getAttribute("data-orari")); } catch (e) { return; }
    var fasce = orari[String(adesso.giorno)] || [];
    var aperto = false, prossima = null;
    fasce.forEach(function (f) {
      var ab = f.split("-"), a = min(ab[0]), b = min(ab[1]);
      if (adesso.minuti >= a && adesso.minuti < b) { aperto = true; prossima = ab[1]; }
      else if (!aperto && prossima === null && adesso.minuti < a) { prossima = ab[0]; }
    });
    if (aperto) { el.textContent = "Aperto ora · chiude alle " + prossima.replace(/^0/, ""); el.classList.add("aperto"); }
    else if (prossima) { el.textContent = "Chiuso ora · apre alle " + prossima.replace(/^0/, ""); el.classList.add("chiuso"); }
    else { el.textContent = "Chiuso ora"; el.classList.add("chiuso"); }
    el.hidden = false;
    var tab = el.nextElementSibling;
    if (tab) {
      var riga = tab.querySelector('tr[data-giorno="' + adesso.giorno + '"]');
      if (riga) riga.classList.add("oggi");
    }
  });

  // mappa caricata solo su richiesta (niente cookie di Google prima del clic)
  document.querySelectorAll("[data-mappa]").forEach(function (box) {
    var b = box.querySelector("button");
    if (!b) return;
    b.addEventListener("click", function () {
      var f = document.createElement("iframe");
      f.src = box.getAttribute("data-mappa");
      f.title = "Mappa: La Bottoneria, via Cremona 76, Brescia";
      f.loading = "lazy";
      f.referrerPolicy = "no-referrer-when-downgrade";
      box.innerHTML = "";
      box.appendChild(f);
      box.classList.add("caricata");
    });
  });
})();
