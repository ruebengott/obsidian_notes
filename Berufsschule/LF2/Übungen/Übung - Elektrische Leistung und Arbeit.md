---
tags: [berufsschule, lf2, elektrotechnik, übung]
fach: LF2
typ: übung
quelle: "[[LF2.pdf#page=48]]"
datum:
status: zu-lernen
---
# Übung - Elektrische Leistung und Arbeit

> [!summary] Kurz & knapp
> Arbeitsblatt „Elektrische Leistung & Arbeit“: Energie und Stromkosten berechnen, Netzteil mit Puffer auswählen, Wirkungsgrad berücksichtigen. Lösungen und Mitschrift: [[LF2.pdf#page=49]] und [[LF2 - Elektrotechnik.pdf#page=1]].

## Aufgabe 1 – Treppenbeleuchtung
Die Treppenbeleuchtung eines Hauses (60-W-Leuchtmittel) ist jede Nacht von 21:00 bis 08:00 Uhr eingeschaltet. Berechnen Sie die elektrische Arbeit für ein Jahr sowie die Kosten (1 Jahr = 365 Tage, Strom 41 ct/kWh).

> [!success]- Lösung
> - Einschaltdauer pro Nacht: 21:00 → 08:00 = **11 h**
> - Pro Jahr: $t = 11\,\text{h} \cdot 365 = 4015\,\text{h}$
> - $W = P \cdot t = 60\,\text{W} \cdot 4015\,\text{h} = 240\,900\,\text{Wh} = 240{,}9\,\text{kWh}$
> - $K = 240{,}9\,\text{kWh} \cdot 0{,}41\,\text{€/kWh} \approx \mathbf{98{,}77\,€}$
>
> *Alternativer Weg (Mitschrift):* pro Tag $0{,}66\,\text{kWh} \cdot 0{,}41\,\text{€} = 0{,}2706\,\text{€}$, mal 365 = 98,77 €. In der Mitschrift wurden 98,80 € bzw. 98,55 € notiert. Die Abweichung kommt vom zu frühen Runden (0,27 € · 365 = 98,55 €). Erst am Ende runden!

## Aufgabe 2 – Bühnenstrahler
Während einer Fernsehshow sind 150 Bühnenstrahler (je 1 kW) für 5,5 Stunden eingeschaltet. Wie hoch sind die Kosten pro Show bei 41 ct pro kWh?

> [!success]- Lösung
> - Ein Strahler: $W = 1\,\text{kW} \cdot 5{,}5\,\text{h} = 5{,}5\,\text{kWh}$
> - 150 Strahler: $W_{ges} = 5{,}5\,\text{kWh} \cdot 150 = 825\,\text{kWh}$
> - $K = 825\,\text{kWh} \cdot 0{,}41\,\text{€/kWh} = \mathbf{338{,}25\,€}$ pro Show
>
> (Im Aufgabentext steht „eine kW kostet 41 ct“. Gemeint ist eine **kWh**.)

## Aufgabe 3 – PC mit 350-W-Netzteil
Ein PC ist täglich 10 Stunden eingeschaltet, das Netzteil nimmt 350 W auf. Wie hoch sind elektrische Arbeit und Kosten (41 ct/kWh) a) am Tag, b) im Jahr? c) Wie hoch ist die Leistungsabgabe bei einem Wirkungsgrad von 0,8?

> [!success]- Lösung
> **a) Pro Tag**
> - $W = 350\,\text{W} \cdot 10\,\text{h} = 3500\,\text{Wh} = 3{,}5\,\text{kWh}$
> - $K = 3{,}5\,\text{kWh} \cdot 0{,}41\,\text{€} = 1{,}435\,\text{€} \approx \mathbf{1{,}44\,€}$
>
> **b) Pro Jahr**
> - $W = 3{,}5\,\text{kWh} \cdot 365 = \mathbf{1277{,}5\,kWh}$
> - $K = 1277{,}5\,\text{kWh} \cdot 0{,}41\,\text{€} \approx \mathbf{523{,}78\,€}$
>
> **c) Leistungsabgabe**
> - $P_{ab} = \eta \cdot P_{zu} = 0{,}8 \cdot 350\,\text{W} = \mathbf{280\,W}$ (70 W Verlust)

> [!warning] Korrektur
> Im ersten Lösungsversuch zu b) wurde mit **24 h × 365** gerechnet (3066 kWh / 1257,06 €). Der PC läuft aber nur **10 h pro Tag**. Richtig ist 1277,5 kWh. Das war in der Mitschrift bereits rot korrigiert, dort aber mit 523,70 € statt **523,78 €**.

## Aufgabe 4 – Netzteil für einen CAD-Rechner
Netzteile gibt es von 400 W bis 1200 W in 50-W-Schritten. Zur ermittelten Leistungsaufnahme ist ein Puffer von 10 % hinzuzurechnen.

| Komponente | max. Leistungsaufnahme je Stück | Anzahl |
| --- | --- | --- |
| Mainboard | 20 W | 1 |
| Prozessor | 172 W | 1 |
| Prozessor-Lüfter | 12 W | 1 |
| Arbeitsspeicher | 5 W | 4 |
| Grafikkarte | 310 W | 1 |
| M.2-SSD | 5 W | 2 |
| Gehäuselüfter | 8 W | 2 |

> [!success]- Lösung
> - Summe: $20 + 172 + 12 + 4 \cdot 5 + 310 + 2 \cdot 5 + 2 \cdot 8 = 20 + 172 + 12 + 20 + 310 + 10 + 16 = 560\,\text{W}$
> - Mit Puffer: $560\,\text{W} \cdot 1{,}1 = 616\,\text{W}$
> - Nächstgrößeres Netzteil: **650 W**

## Aufgabe 5 – Jährliche Stromkosten des CAD-PCs
Der PC läuft an 200 Arbeitstagen je 9 Stunden. Das Netzteil (aus Aufgabe 4) hat einen Wirkungsgrad von 90 % und ist im Schnitt zu 50 % ausgelastet. Strompreis 0,40 €/kWh. (Hinweis: Ohne Ergebnis aus Aufgabe 4 mit 750 W rechnen.)

> [!success]- Lösung
> - Laufzeit: $t = 200 \cdot 9\,\text{h} = 1800\,\text{h}$
> - Abgegebene Leistung (50 % von 650 W): $P_{ab} = 0{,}5 \cdot 650\,\text{W} = 325\,\text{W}$
> - Aufgenommene Leistung: $P_{zu} = \dfrac{P_{ab}}{\eta} = \dfrac{325\,\text{W}}{0{,}9} \approx 361{,}1\,\text{W}$
> - Energie: $W = 361{,}1\,\text{W} \cdot 1800\,\text{h} \approx 650\,000\,\text{Wh} = 650\,\text{kWh}$
> - Kosten: $K = 650\,\text{kWh} \cdot 0{,}40\,\text{€/kWh} = \mathbf{260\,€}$
>
> *Mit 750 W (Hinweis):* $P_{ab} = 375\,\text{W}$, $P_{zu} = 416{,}7\,\text{W}$, $W = 750\,\text{kWh}$, $K = 300\,€$

> [!note] Hinweis zur Mitschrift
> In der Mitschrift steht zwischendurch „$0{,}5 = 0{,}5 \cdot 650\,\text{W} / P_{zu}$“, also wurde $\eta$ mit der Auslastung verwechselt. Am Ende wurde aber richtig durch 0,9 geteilt ($325 / 0{,}9 = 361{,}1\,\text{W}$). Die Einheit ist **W**, nicht kWh. Das Ergebnis von 260 € stimmt.

## Siehe auch
- [[Elektrische Leistung und Energie]]
- [[Wirkungsgrad]]
- [[Formelsammlung Elektrotechnik]]
