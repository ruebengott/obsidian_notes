---
tags: [berufsschule, lf5, html, web]
fach: LF5
typ: thema
quelle: "[[Speisekarte.html]]"
datum: 2025-12-15
status: zu-lernen
---
# HTML Textgestaltung, Listen und Links

> [!summary] Kurz & knapp
> Texte werden mit **Überschriften** `<h1>`–`<h6>`, **Absätzen** `<p>` und **Zeilenumbrüchen** `<br>` gegliedert und mit `<b>`/`<strong>` oder `<i>`/`<em>` hervorgehoben. **Listen** gibt es ungeordnet `<ul>` und nummeriert `<ol>`. **Links** setzt man mit `<a href="...">`. Laut Klausurhinweis gehören Listen und Textgestaltung zum Prüfungsstoff („Restaurantwebsite“).

## Überschriften und Absätze
```html
<h1>Riesen-Speisekarte</h1>
<h2>XXL-Riesenschnitzel und Currywurst</h2>
<p>mit Beilage nach Wahl und Salat</p>
<p>Schnitzel &amp; Steakhaus<br>Vorstrasse 1<br>24768 Rendsburg</p>
```
- `<h1>` ist die wichtigste Überschrift (pro Seite nur einmal), `<h6>` die kleinste.
- `<p>` ist ein **Absatz** mit Abstand davor und danach. `<br>` macht einen **Zeilenumbruch** ohne neuen Absatz, passend z. B. für Adressen.

## Textauszeichnung

| Tag | Wirkung | Hinweis |
| --- | --- | --- |
| `<b>` / `<strong>` | **fett** | `strong` = inhaltlich wichtig |
| `<i>` / `<em>` | *kursiv* | `em` = betont |
| `<u>` | unterstrichen | leicht mit Links zu verwechseln |
| `<small>` | kleiner Text | z. B. „(ca. 1000 gr)“ |
| `<hr>` | waagerechte Linie | |

**Sonderzeichen** (Entities): `&amp;` für &, `&lt;` für <, `&gt;` für >, `&euro;` für €, `&nbsp;` für ein geschütztes Leerzeichen. Mit `<meta charset="UTF-8">` kann man € und Umlaute meist direkt schreiben, `&` sollte aber als `&amp;` stehen.

## Listen
```html
<ul>                         <!-- ungeordnet: Aufzählungspunkte -->
  <li>Pommes Frites</li>
  <li>Bratkartoffeln</li>
</ul>

<ol>                         <!-- geordnet: 1., 2., 3. -->
  <li>Schnitzel klopfen</li>
  <li>panieren</li>
  <li>braten</li>
</ol>
```
Jeder Listenpunkt steht in `<li>`. Listen können verschachtelt werden (`<ul>` innerhalb eines `<li>`). Im Schnitzelhaus-Projekt kommen keine Listen vor, für die Klausur sollte man sie trotzdem können.

## Links
```html
<a href="1_speisekarte.html">Speisekarte</a>                 <!-- relative Datei im selben Ordner -->
<a href="0_start.html">zurück zur Startseite...</a>
<a href="https://www.rendsburg.de" target="_blank">Rendsburg</a>  <!-- extern, neuer Tab -->
<a href="tel:+494331895242">04331 / 895242</a>                 <!-- Telefonnummer antippbar -->
<a href="mailto:info@schnitzelhaus.de">E-Mail</a>
<a href="#anschrift">zur Anschrift</a>                         <!-- Sprung zu id="anschrift" -->
```
- `href` = Ziel des Links. Relativ (`seite.html`, `bilder/x.jpg`, `../index.html`) oder absolut (`https://…`).
- Auch ein Bild oder eine Überschrift kann ein Link sein: `<a href="..."><h2>Speisekarte</h2></a>`.

> [!tip] Merke
> - `<p>` = Absatz, `<br>` = Zeilenumbruch.
> - `ul` = Punkte, `ol` = Nummern, `li` = einzelner Eintrag.
> - Links zwischen eigenen Seiten **relativ** angeben: `href="0_start.html"`.

## Lernfragen
> [!question]- Unterschied zwischen `<ul>` und `<ol>`?
> `<ul>` ist eine ungeordnete Liste mit Aufzählungszeichen, `<ol>` eine nummerierte Liste.

> [!question]- Wie schreibt man einen Link auf die Datei `1_speisekarte.html` im selben Ordner?
> `<a href="1_speisekarte.html">Speisekarte</a>`

> [!question]- Wann verwendet man `<br>` statt eines neuen `<p>`?
> Wenn eine neue Zeile ohne neuen Absatz gewünscht ist, z. B. in einer Adresse.

> [!question]- Wie öffnet man einen Link in einem neuen Tab?
> Mit dem Attribut `target="_blank"`.

## Siehe auch
- [[HTML Grundgerüst]]
- [[HTML Bilder]]
- [[HTML Tabellen]]
- [[Projekt Schnitzelhaus]]
- [[LF5 - Übersicht]]
