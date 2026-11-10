---
tags: [berufsschule, lf5, html, web]
fach: LF5
typ: thema
quelle: "[[Speisekarte.html]]"
datum: 2025-12-15
status: zu-lernen
---
# HTML Tabellen

> [!summary] Kurz & knapp
> Eine Tabelle besteht aus `<table>`, darin Zeilen `<tr>` (table row), darin Zellen `<td>` (table data) oder Kopfzellen `<th>` (table header). Zellen können mit `colspan`/`rowspan` verbunden werden. Im Schnitzelhaus-Projekt dienen Tabellen auch als **Layout-Raster**. Rahmen und Hintergrundfarben stellt man heute mit CSS ein.

## Aufbau
```html
<table>
  <tr>
    <th>Gericht</th>
    <th>Beschreibung</th>
    <th>Preis</th>
  </tr>
  <tr>
    <td><img src="xl.png" alt="XXL-Schnitzel" width="200"></td>
    <td><b>XXL-Riesenschnitzel</b> (ca. 1000 gr)<br>mit Beilage nach Wahl und Salat</td>
    <td><h2>€ 18,90</h2></td>
  </tr>
</table>
```
Die Tabelle wird **zeilenweise** aufgebaut: erst `<tr>`, darin die Zellen von links nach rechts. Jede Zeile sollte gleich viele Zellen haben.

| Element | Bedeutung |
| --- | --- |
| `<table>` | ganze Tabelle |
| `<tr>` | eine Zeile |
| `<td>` | normale Zelle |
| `<th>` | Kopfzelle (fett, zentriert) |
| `<caption>` | Tabellenüberschrift |
| `<thead>`, `<tbody>` | optionale Gruppierung von Kopf und Inhalt |

## Zellen verbinden
```html
<tr>
  <td colspan="2">geht über zwei Spalten</td>
</tr>
<tr>
  <td rowspan="2">geht über zwei Zeilen</td>
  <td>…</td>
</tr>
```

## Alte Attribute und CSS
Im Unterricht und im eigenen Code wurden Attribute verwendet, die in HTML5 **veraltet** sind, aber noch funktionieren:

| veraltet (HTML 4) | modern mit CSS |
| --- | --- |
| `<table border="1">` | `table, td { border: 1px solid black; }` |
| `<td bgcolor="#99FF00">` | `<td style="background-color: #99FF00;">` |
| `<td width="300">` | `td { width: 300px; }` |
| `cellpadding="5"` | `td { padding: 5px; }` |

Siehe [[CSS Grundlagen]].

> [!tip] Merke
> - Reihenfolge: `table` → `tr` → `td`/`th`. Es gibt **kein** Element für Spalten-Inhalte, Spalten entstehen aus den Zellen der Zeilen.
> - `colspan` = über Spalten verbinden, `rowspan` = über Zeilen.
> - Farben als Hex-Code `#RRGGBB`, z. B. braun `#CC9900`.

## Lernfragen
> [!question]- Wofür stehen `tr`, `td` und `th`?
> table row (Zeile), table data (Zelle), table header (Kopfzelle).

> [!question]- Wie verbindet man eine Zelle über drei Spalten?
> `<td colspan="3">…</td>`

> [!question]- Wie gibt man einer Zelle die Hintergrundfarbe `#FFFF00` in modernem HTML?
> Mit CSS: `<td style="background-color: #FFFF00;">` oder über eine Klasse im `<style>`-Bereich.

> [!question]- Eine Tabelle hat 4 Gerichte mit je Bild, Beschreibung, Preis. Wie viele `tr` und `td` braucht man?
> 4 `<tr>` mit je 3 `<td>`, insgesamt 12 Zellen.

## Siehe auch
- [[HTML Bilder]]
- [[CSS Grundlagen]]
- [[Projekt Schnitzelhaus]]
- [[LF5 - Übersicht]]
