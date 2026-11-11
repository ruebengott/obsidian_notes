---
tags: [berufsschule, lf5, html, css, web]
fach: LF5
typ: thema
quelle: "[[Ki_SVG.html]]"
datum: 2026-01-27
status: zu-lernen
---
# CSS Grundlagen

> [!summary] Kurz & knapp
> **CSS** (Cascading Style Sheets) legt das **Aussehen** einer HTML-Seite fest: Farben, Schriften, Abstände, Rahmen, Anordnung. Eine CSS-Regel besteht aus **Selektor** und **Deklarationen** (`eigenschaft: wert;`). CSS ersetzt veraltete HTML-Attribute wie `bgcolor` und `border`, die im Schnitzelhaus-Projekt noch verwendet wurden.

## Aufbau einer Regel
```css
body {                          /* Selektor */
  background-color: #f0f0f0;    /* Eigenschaft: Wert; */
  font-family: sans-serif;
  margin: 0;
}
```

## Wo steht CSS?

| Art | Beispiel | Einsatz |
| --- | --- | --- |
| **inline** | `<td style="background-color: #99FF00;">` | einzelnes Element, schnell, aber unübersichtlich |
| **intern** | `<style> … </style>` im `<head>` | eine Seite (so in [[Ki_SVG.html]]) |
| **extern** | `<link rel="stylesheet" href="style.css">` im `<head>` | mehrere Seiten teilen sich ein Design (best practice) |

## Selektoren

| Selektor | trifft | Beispiel |
| --- | --- | --- |
| Element | alle Elemente dieses Typs | `td { … }` |
| Klasse `.name` | alle mit `class="name"` | `.preis { … }` ↔ `<td class="preis">` |
| ID `#name` | genau ein Element mit `id="name"` | `#anschrift { … }` |

## Häufige Eigenschaften

| Eigenschaft | Beispiel |
| --- | --- |
| `color` | Textfarbe: `color: #333;` |
| `background-color` | Hintergrund: `background-color: #CC9900;` |
| `font-family`, `font-size`, `font-weight` | `font-family: sans-serif; font-size: 1.2em; font-weight: bold;` |
| `text-align` | `left`, `center`, `right` |
| `border` | `border: 1px solid black;` |
| `margin` / `padding` | Außen- / Innenabstand |
| `width`, `height` | `width: 200px;` oder `height: 100vh;` (100 % der Fensterhöhe) |
| `display: flex` | Flexbox-Layout, mit `justify-content` und `align-items` zentrieren |

## Farben
- Namen: `orange`, `green`, `yellow`
- Hex `#RRGGBB`: je zwei Stellen für Rot, Grün, Blau von `00` bis `FF`. `#FFFF00` = Rot + Grün voll = Gelb, `#99FF00` = Hellgrün, `#CC9900` = Braun/Ocker.
- `rgb(204, 153, 0)` ist dasselbe wie `#CC9900`.

## Beispiel: Speisekarte mit CSS statt bgcolor
```html
<head>
  <style>
    table, td { border: 1px solid #999; border-collapse: collapse; }
    .bild  { background-color: #CC9900; }
    .text  { background-color: #99FF00; }
    .preis { background-color: #FFFF00; font-size: 1.5em; font-weight: bold; }
  </style>
</head>
…
<td class="bild"><img src="xl.png" alt="XXL-Riesenschnitzel" width="200"></td>
<td class="text"><b>XXL-Riesenschnitzel</b> (ca. 1000 gr)<br>mit Beilage nach Wahl und Salat</td>
<td class="preis">€ 18,90</td>
```

## Beispiel: Inhalt zentrieren (aus Ki_SVG.html)
```css
body {
  display: flex;
  justify-content: center;   /* waagerecht mittig */
  align-items: center;       /* senkrecht mittig */
  height: 100vh;             /* volle Fensterhöhe */
  margin: 0;
}
```

> [!tip] Merke
> - HTML = **Struktur**, CSS = **Aussehen**.
> - `selektor { eigenschaft: wert; }`, Semikolon nach jeder Deklaration.
> - Klasse `.` für mehrere Elemente, ID `#` für ein einziges.
> - „Cascading“: Treffen mehrere Regeln zu, gewinnt die spezifischere (inline > ID > Klasse > Element) bzw. bei gleicher Spezifität die spätere.

## Lernfragen
> [!question]- Nenne die drei Möglichkeiten, CSS einzubinden.
> Inline mit dem `style`-Attribut, intern im `<style>`-Element im `head`, extern über `<link rel="stylesheet" href="…">`.

> [!question]- Was ist der Unterschied zwischen `.preis` und `#preis`?
> `.preis` wählt alle Elemente mit `class="preis"`, `#preis` genau das eine Element mit `id="preis"`.

> [!question]- Welche Farbe ist `#FF0000`?
> Rot (Rotanteil voll, Grün und Blau 0).

> [!question]- Was ist der Unterschied zwischen `margin` und `padding`?
> `padding` ist der Abstand **innerhalb** des Rahmens (zwischen Inhalt und Rand), `margin` der Abstand **außerhalb** zu anderen Elementen.

## Siehe auch
- [[HTML Grundgerüst]]
- [[HTML Tabellen]]
- [[SVG Grafiken in HTML]]
- [[Projekt Schnitzelhaus]]
- [[LF5 - Übersicht]]
