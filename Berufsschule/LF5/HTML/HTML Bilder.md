---
tags: [berufsschule, lf5, html, web]
fach: LF5
typ: thema
quelle: "[[Speisekarte.html]]"
datum: 2025-12-15
status: zu-lernen
---
# HTML Bilder

> [!summary] Kurz & knapp
> Bilder bindet man mit dem leeren Element `<img>` ein. Pflicht sind `src` (Pfad zur Bilddatei) und `alt` (Ersatztext). Die Größe stellt man mit `width`/`height` (in Pixel, **ohne** „px“) oder besser mit CSS ein. Pfade immer **relativ** angeben.

## Syntax
```html
<img src="schnitzelhausc.jpg" alt="Eingang des Schnitzelhauses">
<img src="xl.png" alt="XXL-Riesenschnitzel" width="200">
<img src="bilder/sitzen.png" alt="Gastraum" style="width: 300px;">
```

| Attribut | Bedeutung |
| --- | --- |
| `src` | Pfad oder URL der Bilddatei |
| `alt` | Ersatztext, wenn das Bild fehlt, und für Screenreader (Barrierefreiheit) |
| `width`, `height` | Breite/Höhe in Pixeln, z. B. `width="200"`. Gibt man nur eins an, bleibt das Seitenverhältnis erhalten |
| `title` | Tooltip beim Überfahren mit der Maus |

## Pfade

| Pfad | bedeutet |
| --- | --- |
| `bild.jpg` | gleicher Ordner wie die HTML-Datei |
| `bilder/bild.jpg` | Unterordner `bilder` |
| `../bild.jpg` | ein Ordner höher |
| `https://…/bild.jpg` | Bild von einem Webserver |
| `C:\Users\…\bild.jpg` | **falsch**: funktioniert nur auf dem eigenen PC |

## Bildformate

| Format | geeignet für |
| --- | --- |
| **JPEG** (`.jpg`, `.jpeg`) | Fotos, verlustbehaftet komprimiert, keine Transparenz |
| **PNG** (`.png`) | Grafiken, Screenshots, verlustfrei, **Transparenz** möglich (z. B. freigestellte Schnitzel `xl.png`) |
| **GIF** | einfache Animationen, nur 256 Farben |
| **SVG** | Vektorgrafik, beliebig skalierbar, siehe [[SVG Grafiken in HTML]] |
| **WebP** | modernes Format, kleiner als JPEG/PNG |

## Bild als Link
```html
<a href="1_speisekarte.html"><img src="xl.png" alt="Zur Speisekarte"></a>
```

> [!tip] Merke
> - `<img>` hat **kein** End-Tag.
> - `alt` immer angeben.
> - `width="200"` (HTML-Attribut, Zahl ohne Einheit) oder `style="width: 200px"` (CSS, mit Einheit).
> - Bilder in den Projektordner legen und relativ verlinken.

## Lernfragen
> [!question]- Welche zwei Attribute braucht ein `<img>` mindestens?
> `src` für die Bildquelle und `alt` für den Ersatztext.

> [!question]- Wann wählt man PNG statt JPEG?
> Für Grafiken mit scharfen Kanten oder wenn **Transparenz** nötig ist, z. B. ein freigestelltes Schnitzel auf farbigem Hintergrund. JPEG eignet sich für Fotos.

> [!question]- Die Bilder einer Seite werden auf dem Schulrechner nicht angezeigt, zu Hause schon. Woran liegt das wahrscheinlich?
> An absoluten lokalen Pfaden wie `C:\Users\…`. Die Bilder in den Projektordner kopieren und relativ einbinden: `src="sitzen.png"`.

## Siehe auch
- [[HTML Grundgerüst]]
- [[HTML Tabellen]]
- [[SVG Grafiken in HTML]]
- [[Projekt Schnitzelhaus]]
- [[LF5 - Übersicht]]
