---
tags: [berufsschule, lf2, elektrotechnik, green-it, übung]
fach: LF2
typ: übung
quelle: "[[LF2.pdf#page=53]]"
datum:
status: zu-lernen
---
# Übung - Energiekosten Klimaanlage und Server

> [!summary] Kurz & knapp
> IT-Übungsaufgabe 7: Energieverbrauch und Kosten einer Serverraum-Klimaanlage berechnen und mit einem Server im Dauerbetrieb vergleichen. Auch in [[LF2 - Elektrotechnik.pdf#page=3]] und [[LF2 - Elektrotechnik.pdf#page=4]].

## Aufgabe
Eine Klimaanlage hat eine Leistung von **2,5 kW** und läuft täglich **10 Stunden**.

a) Berechne den täglichen Energieverbrauch.
b) Berechne den monatlichen Verbrauch (30 Tage).
c) Berechne die Kosten bei 0,40 €/kWh.
d) Vergleiche den Verbrauch mit einem Server (500 W, 24 h Betrieb).

> [!success]- Lösung
> **a)** $W = P \cdot t = 2{,}5\,\text{kW} \cdot 10\,\text{h} = \mathbf{25\,kWh}$ pro Tag
>
> **b)** $W = 25\,\text{kWh} \cdot 30 = \mathbf{750\,kWh}$ pro Monat
>
> **c)** $K = 750\,\text{kWh} \cdot 0{,}40\,\text{€/kWh} = \mathbf{300\,€}$ pro Monat (pro Tag: $25 \cdot 0{,}40 = 10\,€$)
>
> **d)** Server:
> - pro Tag: $0{,}5\,\text{kW} \cdot 24\,\text{h} = 12\,\text{kWh}$
> - pro Monat: $12\,\text{kWh} \cdot 30 = 360\,\text{kWh}$ → $360 \cdot 0{,}40\,€ = 144\,€$
>
> Vergleich: Die Klimaanlage verbraucht $750 - 360 = 390\,\text{kWh}$ mehr (etwa das **2,1-Fache**) und kostet **156 € mehr pro Monat**, obwohl sie nur 10 h statt 24 h läuft.

> [!tip] Green-IT-Bezug
> Kühlung ist in Rechenzentren einer der größten Stromverbraucher. Maßnahmen: Kalt-/Warmgang-Einhausung, höhere Raumtemperatur zulassen, freie Kühlung mit Außenluft, Abwärme nutzen, effizientere Server (weniger Abwärme). → [[Green IT]]

## Siehe auch
- [[Elektrische Leistung und Energie]]
- [[Green IT]]
