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

// apertura a scorrimento
(function () {
  var box = document.querySelector(".slider");
  if (!box) return;
  var slides = box.querySelectorAll(".slide");
  var punti = box.querySelectorAll(".punti button");
  var i = 0, timer = null;
  var ridotto = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  function vai(n) {
    slides[i].classList.remove("attiva");
    slides[i].setAttribute("aria-hidden", "true");
    slides[i].querySelectorAll("a").forEach(function (a) { a.tabIndex = -1; });
    punti[i].removeAttribute("aria-current");
    i = (n + slides.length) % slides.length;
    var s = slides[i];
    // riavvia le animazioni (ricciolo che si disegna)
    s.classList.remove("attiva"); void s.offsetWidth; s.classList.add("attiva");
    s.removeAttribute("aria-hidden");
    s.querySelectorAll("a").forEach(function (a) { a.removeAttribute("tabindex"); });
    punti[i].setAttribute("aria-current", "true");
  }
  function avvia() { if (!ridotto) { ferma(); timer = setInterval(function () { vai(i + 1); }, 6500); } }
  function ferma() { if (timer) clearInterval(timer); timer = null; }
  box.querySelector(".freccia-sx").addEventListener("click", function () { vai(i - 1); avvia(); });
  box.querySelector(".freccia-dx").addEventListener("click", function () { vai(i + 1); avvia(); });
  punti.forEach(function (p, n) { p.addEventListener("click", function () { vai(n); avvia(); }); });
  box.addEventListener("mouseenter", ferma);
  box.addEventListener("mouseleave", avvia);
  box.addEventListener("focusin", ferma);
  // scorrimento col dito
  var x0 = null;
  box.addEventListener("touchstart", function (e) { x0 = e.touches[0].clientX; }, { passive: true });
  box.addEventListener("touchend", function (e) {
    if (x0 === null) return;
    var dx = e.changedTouches[0].clientX - x0;
    if (Math.abs(dx) > 40) { vai(dx < 0 ? i + 1 : i - 1); avvia(); }
    x0 = null;
  });
  avvia();
})();

// caroselli con frecce
document.querySelectorAll("[data-carosello]").forEach(function (box) {
  var pista = box.querySelector(".car-pista");
  var prec = box.querySelector(".car-prec");
  var succ = box.querySelector(".car-succ");
  if (!pista || !prec || !succ) return;
  function passo() {
    var li = pista.querySelector("li");
    if (!li) return pista.clientWidth;
    var gap = parseFloat(getComputedStyle(pista).columnGap) || 0;
    var n = Math.max(1, Math.floor((pista.clientWidth + gap) / (li.offsetWidth + gap)));
    return n * (li.offsetWidth + gap);
  }
  function aggiorna() {
    var max = pista.scrollWidth - pista.clientWidth - 2;
    prec.disabled = pista.scrollLeft <= 2;
    succ.disabled = pista.scrollLeft >= max;
    box.querySelector(".car-frecce").hidden = max <= 0;
  }
  prec.addEventListener("click", function () { pista.scrollBy({ left: -passo(), behavior: "smooth" }); });
  succ.addEventListener("click", function () { pista.scrollBy({ left: passo(), behavior: "smooth" }); });
  pista.addEventListener("scroll", function () { window.requestAnimationFrame(aggiorna); }, { passive: true });
  window.addEventListener("resize", aggiorna);
  aggiorna();
});
