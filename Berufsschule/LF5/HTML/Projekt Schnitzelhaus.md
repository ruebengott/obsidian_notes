---
tags: [berufsschule, lf5, html, übung, web]
fach: LF5
typ: übung
quelle: "[[Aufgabe_Schnitzel.pdf]]"
datum: 2025-12-15
status: zu-lernen
---
# Projekt Schnitzelhaus

> [!summary] Kurz & knapp
> Praxisprojekt zu HTML: eine Webpräsenz für ein Restaurant aus zwei verlinkten Seiten (Startseite und Speisekarte), aufgebaut mit Überschriften, Absätzen, Bildern, Links und Tabellen. Die eigene Lösung hat die Grundstruktur richtig. Die Speisekarte ist aber erst zu einem Viertel fertig, außerdem stimmen Dateinamen und Farbcodes nicht, und alle Pfade sind absolut. Das entspricht dem Klausurniveau „Restaurantwebsite“.

## Aufgabe
Quelle: [[Aufgabe_Schnitzel.pdf]]

> **Erstellen Sie eine Web-Präsenz (Homepage) für ein Lokal!**
> 1. Bilder: currywurst.jpeg, Monsterschnitzel.jpg, schnitzelhausc.jpg, sitzen.png, xl.png, xxl.png, xxxl.png.
> 2. Farbcodes für die Speisekarte: braun `#CC9900`, grün `#99FF00`, gelb `#FFFF00`.
> 3. Zwei HTML-Dateien: **0_start.html** und **1_speisekarte.html**. Aussehen und Inhalte möglichst ähnlich zu den Abbildungen. „Speisekarte“ verlinkt auf 1_speisekarte.html, „zurück zur Startseite...“ auf 0_start.html.

### Vorlage Startseite
![[Aufgabe_Schnitzel.pdf#page=2]]

### Vorlage Speisekarte
![[Aufgabe_Schnitzel.pdf#page=3]]

Aufbau der Speisekarte laut Vorlage (Tabelle mit Rahmen, 4 Zeilen × 3 Spalten, Spalten braun/grün/gelb):

| Bild | Beschreibung | Preis |
| --- | --- | --- |
| XXL-Schnitzel | **XXL-Riesenschnitzel** (ca. 1000gr), mit Beilage nach Wahl und Salat | € 18,90 |
| XXXL-Schnitzel | **XXXL-Riesenschnitzel** (ca. 1500gr), mit Beilage nach Wahl und Salat | € 23,90 |
| Currywurst | **1 Meter Currywurst**, mit Pommes Frites | € 13,20 |
| Monsterschnitzel | **Monsterschnitzel** | € 31,20 |

## Bilder
| | |
| --- | --- |
| ![[schnitzelhausc.jpg\|250]] | ![[sitzen.png\|250]] |
| schnitzelhausc.jpg (Startseite oben) | sitzen.png (Gastraum) |
| ![[xl.png\|200]] | ![[xxl.png\|200]] |
| xl.png (vermutlich XXL-Schnitzel) | xxl.png (vermutlich XXXL-Schnitzel) |
| ![[currywurst.jpeg\|120]] | ![[Monsterschnitzel.jpg\|200]] |
| currywurst.jpeg | Monsterschnitzel.jpg |

`xxxl.png` liegt nicht im Quellordner.

## Eigene Lösung
Dateien: [[Schnitzelhaus.html]] (Startseite), [[Speisekarte.html]], [[Schnitzelhaus.txt]] (früher Entwurf der Startseite mit leerem `src`).

### Startseite (Auszug)
```html
<!DOCTYPE html>
<html>
	<head>
		<title>Schnitzelhaus</title>
	</head>
	<body>
		<h1>Willkommen im Schnitzelhaus!</h1>
		<img src="C:\Users\moehr\OneDrive\...\LF5\HTML\schnitzelhausc.jpg">
	<table border="0">
		<tr>
			<td>
				<h2>Reservierung</h2>
				<p>Rufen Sie uns einfach an:</p>
				<br />
				<p>04331/895242</p>
			</td>
			<td>
				<a href="file:///C:/Users/moehr/OneDrive/.../Speisekarte.html"><h2>Speisekarte</h2></a>
			</td>
		</tr>
		<tr>
			<td>
				<h2>Anschrift:</h2>
				<p>Schnitzel & Steakhaus</p>
				<p>Vorstrasse 1</p>
				<p>24768 Rendsburg</p>
			</td>
			<td>
				<p>Unser gemütliches Restaurant</p>
				<img src="C:\Users\moehr\OneDrive\...\LF5\HTML\sitzen.png">
			</td>
		</tr>
	</table>
	</body>
</html>
```
(Pfade hier mit `...` gekürzt.)

### Speisekarte (Auszug)
```html
<h1>Riesen-Speisekarte</h1>
<h2>XXL-Riesenschnitzel und Currywurst</h2>
<table border="1">
	<tr>
		<td bgcolor ="orange"> <img width="200px" src="C:\...\Monsterschnitzel.jpg"></td>
		<td bgcolor="green">
			<b>XXL-Riesenschnitzel</b> (ca. 1000gr)
			<p>mit Beilage nach Wahl und Salat</p>
		</td>
		<td bgcolor="yellow">
			<h2>€ 18,90</h2>
		</td>
	</tr>
</table>
<a href="C:\...\Schnitzelhaus.html">zurück zur Startseite </a>
```

### Was gut ist
- Grundgerüst, Überschriften-Hierarchie (`h1` → `h2`) und `<title>` passen zur Vorlage.
- Die Startseite nutzt eine **unsichtbare Tabelle** (`border="0"`) als 2×2-Layout, genau wie in der Vorlage: Reservierung | Speisekarte, Anschrift | Gastraum-Bild.
- Die Speisekarte ist korrekt als Tabelle mit Bild, Beschreibung und Preis aufgebaut. Links in beide Richtungen sind vorhanden.

## Review
> [!warning] Korrektur
> 1. **Absolute lokale Pfade:** `C:\Users\moehr\...` und `file:///C:/...` funktionieren nur auf dem eigenen PC und nur, solange der Ordner nicht verschoben wird. Seit die Dateien in einem anderen Ordner liegen, sind **alle Bilder und Links kaputt**. Richtig: `src="schnitzelhausc.jpg"`, `href="1_speisekarte.html"`.
> 2. **Dateinamen:** Gefordert sind `0_start.html` und `1_speisekarte.html`, nicht `Schnitzelhaus.html`/`Speisekarte.html`.
> 3. **Farben:** `orange`, `green`, `yellow` statt der vorgegebenen Codes `#CC9900`, `#99FF00`, `#FFFF00`. Besonders `green` (#008000, dunkelgrün) weicht stark ab.
> 4. **Speisekarte unvollständig:** Nur 1 von 4 Gerichten. Es fehlen XXXL-Schnitzel, Currywurst und Monsterschnitzel.
> 5. **Falsches Bild:** In der XXL-Zeile steht `Monsterschnitzel.jpg`. Laut Vorlage gehört dort das freigestellte Schnitzel (`xl.png`) hin, das Monsterschnitzel in die letzte Zeile.
> 6. `width="200px"`: Das HTML-Attribut erwartet eine Zahl **ohne** Einheit, also `width="200"`. Die meisten Browser verzeihen es.
> 7. Kleinigkeiten: kein `alt` bei den Bildern, `&` sollte `&amp;` sein, „Reservierung:“ in der Vorlage mit Doppelpunkt, `<meta charset="UTF-8">` und `lang="de"` fehlen (Umlaute, €-Zeichen).

> [!tip] Verbesserung
> - Die Adresse ist **ein** Absatz mit Zeilenumbrüchen: `<p>Schnitzel &amp; Steakhaus<br>Vorstrasse 1<br>24768 Rendsburg</p>`. Drei `<p>` erzeugen zu viel Abstand.
> - `<br />` zwischen zwei `<p>` ist überflüssig, `<p>` macht schon einen Abstand.
> - `bgcolor` und `border` sind veraltet. Für die Klausur reichen sie meist, sauberer ist [[CSS Grundlagen|CSS]].

## Musterlösung
> [!success]- 0_start.html
> ```html
> <!DOCTYPE html>
> <html lang="de">
> <head>
>   <meta charset="UTF-8">
>   <title>Schnitzelhaus</title>
> </head>
> <body>
>   <h1>Willkommen im Schnitzelhaus!</h1>
>   <img src="schnitzelhausc.jpg" alt="Eingang des Schnitzelhauses">
>
>   <table>
>     <tr>
>       <td>
>         <h2>Reservierung:</h2>
>         <p>Rufen Sie uns einfach an:<br>04331 / 895242</p>
>       </td>
>       <td>
>         <h2><a href="1_speisekarte.html">Speisekarte</a></h2>
>       </td>
>     </tr>
>     <tr>
>       <td>
>         <h2>Anschrift:</h2>
>         <p>Schnitzel &amp; Steakhaus<br>Vorstrasse 1<br>24768 Rendsburg</p>
>       </td>
>       <td>
>         <p>Unser gemütliches Restaurant</p>
>         <img src="sitzen.png" alt="Gastraum">
>       </td>
>     </tr>
>   </table>
> </body>
> </html>
> ```

> [!success]- 1_speisekarte.html
> ```html
> <!DOCTYPE html>
> <html lang="de">
> <head>
>   <meta charset="UTF-8">
>   <title>Riesen-Speisekarte</title>
> </head>
> <body>
>   <h1>Riesen-Speisekarte</h1>
>   <h3>XXL-Riesenschnitzel und Currywurst</h3>
>
>   <table border="1" width="100%">
>     <tr>
>       <td bgcolor="#CC9900"><img src="xl.png" alt="XXL-Riesenschnitzel" width="200"></td>
>       <td bgcolor="#99FF00"><b>XXL-Riesenschnitzel</b> (ca. 1000gr)<br>mit Beilage nach Wahl und Salat</td>
>       <td bgcolor="#FFFF00"><h2>€ 18,90</h2></td>
>     </tr>
>     <tr>
>       <td bgcolor="#CC9900"><img src="xxl.png" alt="XXXL-Riesenschnitzel" width="200"></td>
>       <td bgcolor="#99FF00"><b>XXXL-Riesenschnitzel</b> (ca. 1500gr)<br>mit Beilage nach Wahl und Salat</td>
>       <td bgcolor="#FFFF00"><h2>€ 23,90</h2></td>
>     </tr>
>     <tr>
>       <td bgcolor="#CC9900"><img src="currywurst.jpeg" alt="1 Meter Currywurst" width="130"></td>
>       <td bgcolor="#99FF00"><b>1 Meter Currywurst</b><br>mit Pommes Frites</td>
>       <td bgcolor="#FFFF00"><h2>€ 13,20</h2></td>
>     </tr>
>     <tr>
>       <td bgcolor="#CC9900"><img src="Monsterschnitzel.jpg" alt="Monsterschnitzel" width="250"></td>
>       <td bgcolor="#99FF00"><b>Monsterschnitzel</b></td>
>       <td bgcolor="#FFFF00"><h2>€ 31,20</h2></td>
>     </tr>
>   </table>
>
>   <p><a href="0_start.html">zurück zur Startseite...</a></p>
> </body>
> </html>
> ```
> Mit CSS statt `bgcolor`: siehe Beispiel in [[CSS Grundlagen]].

> [!question] Offene Frage
> Welches Bild gehört zu welchem Schnitzel? Die Zuordnung `xl.png` → XXL und `xxl.png` → XXXL ist angenommen. `xxxl.png` aus der Bilderliste liegt nicht im Quellordner.

## Zum Selbsttest
> [!question]- Warum werden die Bilder auf einem anderen Rechner nicht angezeigt?
> Weil die `src`-Pfade absolut auf `C:\Users\moehr\...` zeigen. Mit relativen Pfaden und den Bildern im selben Ordner funktioniert es überall.

> [!question]- Wie viele `<tr>` und `<td>` hat die fertige Speisekarten-Tabelle?
> 4 Zeilen mit je 3 Zellen, also 4 `<tr>` und 12 `<td>`.

> [!question]- Mit welchem Tag-Attribut macht man die Tabelle der Startseite unsichtbar, mit welchem die Rahmen der Speisekarte sichtbar?
> `border="0"` bzw. `border="1"` (modern: CSS `border`).

## Siehe auch
- [[HTML Grundgerüst]]
- [[HTML Textgestaltung, Listen und Links]]
- [[HTML Bilder]]
- [[HTML Tabellen]]
- [[CSS Grundlagen]]
- [[LF5 - Übersicht]]
