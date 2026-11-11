---
tags: [berufsschule, lf5, html, web]
fach: LF5
typ: thema
quelle: "[[Schnitzelhaus.html]]"
datum: 2025-12-15
status: zu-lernen
---
# HTML Grundgerüst

> [!summary] Kurz & knapp
> **HTML** (Hypertext Markup Language) beschreibt die **Struktur** einer Webseite mit **Tags** wie `<h1>…</h1>`. Jede Seite hat dasselbe Grundgerüst: `<!DOCTYPE html>`, `<html>`, darin `<head>` (Infos über die Seite) und `<body>` (sichtbarer Inhalt). Das **Aussehen** regelt man mit [[CSS Grundlagen|CSS]].

## Grundgerüst
```html
<!DOCTYPE html>
<html lang="de">
  <head>
    <meta charset="UTF-8">
    <title>Schnitzelhaus</title>
  </head>
  <body>
    <h1>Willkommen im Schnitzelhaus!</h1>
  </body>
</html>
```

| Teil | Aufgabe |
| --- | --- |
| `<!DOCTYPE html>` | sagt dem Browser: HTML5. Steht ganz oben, ist kein Tag im eigentlichen Sinne |
| `<html lang="de">` | Wurzelelement, `lang` gibt die Sprache an (Vorlesefunktion, Silbentrennung) |
| `<head>` | Metadaten, nicht sichtbar: Zeichensatz, Titel, CSS |
| `<meta charset="UTF-8">` | Zeichenkodierung, damit Umlaute und € richtig angezeigt werden |
| `<title>` | Text im **Browser-Tab** („Schnitzelhaus“, „Riesen-Speisekarte“) |
| `<body>` | alles, was auf der Seite sichtbar ist |

## Tags, Elemente, Attribute
- **Tag:** `<p>` (Start-Tag) und `</p>` (End-Tag). Dazwischen steht der Inhalt. Zusammen bilden sie ein **Element**.
- **Leere Elemente** ohne End-Tag: `<br>`, `<img>`, `<meta>`. Die Schreibweise `<br />` ist ebenfalls erlaubt.
- **Attribute** stehen im Start-Tag als `name="wert"`: `<img src="bild.jpg" alt="...">`, `<a href="seite.html">`.
- Elemente werden **verschachtelt**, aber nicht überkreuzt: `<b><i>…</i></b>` richtig, `<b><i>…</b></i>` falsch.
- Einrückung und Zeilenumbrüche im Quelltext haben **keine** Wirkung auf die Darstellung. Mehrere Leerzeichen werden zu einem.

## Kommentare
```html
<!-- Das ist ein Kommentar, der Browser zeigt ihn nicht an -->
```

## Dateien und Pfade
- Dateiendung `.html`, Startseite heißt im Web meist `index.html`.
- Links und Bilder immer mit **relativen Pfaden** einbinden (`src="bilder/schnitzel.jpg"`), nicht mit `C:\Users\...`. Absolute lokale Pfade funktionieren nur auf dem eigenen PC (siehe [[Projekt Schnitzelhaus]]).
- Im Web wird `/` als Trennzeichen verwendet, nicht `\`.

> [!tip] Merke
> - `head` = Infos **über** die Seite, `body` = **sichtbarer** Inhalt.
> - `<title>` erscheint im Tab, `<h1>` auf der Seite.
> - `<meta charset="UTF-8">` nicht vergessen, sonst werden Umlaute falsch dargestellt.
> - HTML = Struktur, CSS = Aussehen.

## Lernfragen
> [!question]- Welche Teile gehören zum HTML-Grundgerüst?
> `<!DOCTYPE html>`, `<html>`, `<head>` mit `<meta charset>` und `<title>` sowie `<body>`.

> [!question]- Was ist der Unterschied zwischen `<title>` und `<h1>`?
> `<title>` steht im `head` und erscheint im Browser-Tab bzw. als Lesezeichen-Name. `<h1>` ist die sichtbare Hauptüberschrift auf der Seite.

> [!question]- Was ist ein Attribut? Nenne zwei Beispiele.
> Eine Zusatzangabe im Start-Tag in der Form `name="wert"`, z. B. `src` bei `<img>` und `href` bei `<a>`.

> [!question]- Warum sollte man keine Pfade wie `C:\Users\...` verwenden?
> Sie zeigen auf die Festplatte des eigenen Rechners. Auf einem Webserver oder anderen PC existiert der Pfad nicht, Bilder und Links funktionieren dann nicht.

## Siehe auch
- [[HTML Textgestaltung, Listen und Links]]
- [[HTML Bilder]]
- [[HTML Tabellen]]
- [[CSS Grundlagen]]
- [[Projekt Schnitzelhaus]]
- [[LF5 - Übersicht]]
