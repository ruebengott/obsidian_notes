---
tags: [berufsschule, lf5, html, svg, web]
fach: LF5
typ: thema
quelle: "[[Ki_SVG.html]]"
datum: 2026-01-27
status: zu-lernen
---
# SVG Grafiken in HTML

> [!summary] Kurz & knapp
> **SVG** (Scalable Vector Graphics) beschreibt Grafiken als **Vektoren** in XML-Schreibweise: Rechtecke, Kreise, Linien und Polygone mit Koordinaten. SVG lässt sich direkt in HTML schreiben und ohne Qualitätsverlust skalieren. Die Datei [[Ki_SVG.html]] zeigt ein Haus mit Auto. Der Name deutet darauf hin, dass sie mit einer KI erzeugt und dann untersucht wurde.

## Koordinatensystem
- Der Ursprung (0,0) liegt **oben links**. x wächst nach rechts, y wächst **nach unten**.
- `<svg width="350" height="300" viewBox="0 0 350 300">` legt die Anzeigegröße und den sichtbaren Koordinatenbereich fest.
- Was später im Code steht, wird **darüber** gezeichnet. Deshalb kommt der Boden zuerst und die Türklinke nach der Tür.

## Grundformen (aus Ki_SVG.html)
```html
<!-- Rechteck: linke obere Ecke x/y, Breite, Höhe -->
<rect x="80" y="130" width="140" height="100" fill="#ffcc80" stroke="#795548" stroke-width="3" />

<!-- Polygon: Eckpunkte "x,y x,y x,y" (hier das Dach als Dreieck) -->
<polygon points="70,130 150,70 230,130" fill="#e57373" stroke="#b71c1c" stroke-width="3" />

<!-- Kreis: Mittelpunkt cx/cy, Radius r (Türklinke, Räder) -->
<circle cx="45" cy="215" r="12" fill="#424242" />

<!-- Linie: von x1/y1 nach x2/y2 (Fensterkreuz) -->
<line x1="110" y1="145" x2="110" y2="170" stroke="#1e88e5" stroke-width="2" />
```

| Attribut | Bedeutung |
| --- | --- |
| `fill` | Füllfarbe |
| `stroke` | Linien-/Randfarbe |
| `stroke-width` | Liniendicke |

Weitere Formen: `<ellipse>`, `<polyline>`, `<path>` (beliebige Kurven), `<text>`.

## Rastergrafik vs. Vektorgrafik

| | Raster (JPEG, PNG) | Vektor (SVG) |
| --- | --- | --- |
| Inhalt | einzelne Pixel | geometrische Formen |
| Vergrößern | wird pixelig | bleibt scharf |
| geeignet für | Fotos | Logos, Icons, Diagramme |
| bearbeitbar mit | Bildbearbeitung | Texteditor, CSS, JavaScript |

> [!tip] Merke
> - y-Achse zeigt **nach unten**.
> - `rect` = x, y, width, height · `circle` = cx, cy, r · `line` = x1, y1, x2, y2 · `polygon` = points.
> - Reihenfolge im Code = Zeichenreihenfolge (später = weiter vorne).

## Lernfragen
> [!question]- Warum wird ein SVG-Logo beim Vergrößern nicht unscharf?
> Weil es aus mathematisch beschriebenen Formen besteht, die bei jeder Größe neu berechnet werden, und nicht aus festen Pixeln.

> [!question]- Ein Rechteck hat `y="220"` und `height="80"`, das SVG ist 300 hoch. Wo liegt es?
> Am unteren Rand: von y = 220 bis y = 300. Das ist der grüne Boden in Ki_SVG.html.

> [!question]- Wie zeichnet man ein Dreieck in SVG?
> Mit `<polygon points="x1,y1 x2,y2 x3,y3" />`.

> [!question]- Ergänze eine gelbe Sonne oben rechts.
> > [!success]- Lösung
> > `<circle cx="310" cy="40" r="25" fill="#ffeb3b" />` vor dem Haus einfügen (z. B. direkt nach dem Boden).

## Siehe auch
- [[HTML Bilder]]
- [[CSS Grundlagen]]
- [[HTML Grundgerüst]]
- [[LF5 - Übersicht]]
