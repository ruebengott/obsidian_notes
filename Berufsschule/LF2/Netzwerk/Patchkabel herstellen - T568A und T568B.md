---
tags: [berufsschule, lf2, netzwerk, verkabelung]
fach: LF2
typ: thema
quelle: "[[LF2.pdf#page=69]]"
datum:
status: zu-lernen
---
# Patchkabel herstellen - T568A und T568B

> [!summary] Kurz & knapp
> Ein **Patchkabel** (1:1) hat an beiden Enden dieselbe Belegung, meist **T568B**. Ein **Crossover-Kabel** hat an einem Ende **T568A** und am anderen **T568B**. Dadurch werden die Sende- und Empfangspaare gekreuzt. Hergestellt wird es durch Abmanteln, Sortieren der Adern nach Farbcode und Crimpen des RJ45-Steckers.

## Farbcodes

| Pin | T568A | T568B |
| --- | --- | --- |
| 1 | grün-weiß | orange-weiß |
| 2 | grün | orange |
| 3 | orange-weiß | grün-weiß |
| 4 | blau | blau |
| 5 | blau-weiß | blau-weiß |
| 6 | orange | grün |
| 7 | braun-weiß | braun-weiß |
| 8 | braun | braun |

Merkhilfe: Bei T568A und T568B sind nur das **grüne und das orange Paar vertauscht**. Blau (4/5) und Braun (7/8) bleiben gleich.

## Patch- vs. Crossover-Kabel

| | Patchkabel (1:1, straight-through) | Crossover-Kabel |
| --- | --- | --- |
| Belegung | beide Enden gleich (B–B oder A–A) | ein Ende T568A, anderes T568B |
| Früher verwendet für | unterschiedliche Geräte (PC ↔ Switch) | gleiche Geräte (PC ↔ PC, Switch ↔ Switch) |
| Heute | Standard | kaum noch nötig, da fast alle Geräte **Auto-MDI-X** beherrschen (erkennen und tauschen die Paare automatisch) |

## Werkzeug
- Elektronik-Seitenschneider
- Koaxial-Abmantler (bzw. Abisolierwerkzeug)
- Seitenschneider
- Crimpzange für RJ45-Stecker
- Gliedermaßstab (Zollstock)
- Material: Patchleitung, Knickschutztüllen, RJ45-Stecker (ggf. mit Einführungshilfe)

## Arbeitsschritte

| Nr. | Arbeitsschritt | Werkzeug / Material |
| --- | --- | --- |
| 1 | Leitung auf die gewünschte Länge zuschneiden | Gliedermaßstab, Seitenschneider, Patchleitung |
| 2 | **Knickschutz** über die Leitung ziehen (wird gern vergessen!) | Knickschutz |
| 3 | Patchleitung ca. 2 cm abmanteln | Koaxial-Abmantler (kurze Klinge) |
| 4 | Schirmung (Folie/Geflecht, Beilauflitze) entfernen | Elektronik-Seitenschneider |
| 5 | Adern entdrillen und von links nach rechts nach **T568A oder T568B** sortieren | – |
| 6 | Einzeladern in die Einführungshilfe einführen | Einführungshilfe |
| 7 | Adern am oberen Ende der Einführungshilfe gerade einkürzen | Elektronik-Seitenschneider |
| 8 | Einführungshilfe in den RJ45-Stecker schieben (Adern bis ganz vorn) | RJ45-Stecker |
| 9 | Belegung durch das **Sichtfenster** kontrollieren | – |
| 10 | RJ45-Stecker crimpen | Crimpzange |
| 11 | Knickschutz über den Stecker ziehen | – |
| 12 | Schritte 2–10 am zweiten Ende wiederholen | – |

Danach das Kabel mit einem **Kabeltester** prüfen.

Originalanleitung mit Bildern: ![[LF2.pdf#page=69]] ![[LF2.pdf#page=70]]

> [!tip] Merke
> - T568B: **orange-weiß, orange, grün-weiß, blau, blau-weiß, grün, braun-weiß, braun**.
> - Patch = gleiche Norm an beiden Enden. Crossover = A auf der einen, B auf der anderen Seite.
> - Knickschutz **vor** dem Crimpen aufziehen!
> - Am Ende immer mit dem Kabeltester prüfen.

## Lernfragen
> [!question]- Wie lautet die Pinbelegung nach T568B?
> 1 orange-weiß, 2 orange, 3 grün-weiß, 4 blau, 5 blau-weiß, 6 grün, 7 braun-weiß, 8 braun.

> [!question]- Worin unterscheiden sich T568A und T568B?
> Das grüne und das orange Adernpaar sind vertauscht.

> [!question]- Wie ist ein Crossover-Kabel aufgebaut und warum braucht man es heute kaum noch?
> Ein Ende T568A, das andere T568B. Heutige Netzwerkkarten und Switches beherrschen Auto-MDI-X und tauschen Sende-/Empfangspaare automatisch.

> [!question]- Warum zieht man den Knickschutz vor dem Crimpen auf die Leitung?
> Nach dem Crimpen passt er nicht mehr über den Stecker auf das Kabel. Man müsste den Stecker abschneiden und neu crimpen.

## Siehe auch
- [[Netzwerkkabel - Twisted Pair und Kategorien]]
- [[Netzwerk-Grundbegriffe und Topologien]]
