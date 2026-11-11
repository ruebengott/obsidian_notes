---
tags: [berufsschule, lf2, elektrotechnik, usv, übung]
fach: LF2
typ: übung
quelle: "[[LF2.pdf#page=51]]"
datum:
status: zu-lernen
---
# Übung - USV-Dimensionierung

> [!summary] Kurz & knapp
> IT-Übungsaufgabe 2: Akkukapazität einer USV für einen Serverraum aus Leistung, Überbrückungszeit und Wirkungsgrad bestimmen. Auch in [[LF2 - Elektrotechnik.pdf#page=2]].

## Aufgabe
Ein Serverraum enthält:
- 2 Server à 450 W
- 1 Switch mit 150 W
- 1 Storage-System mit 300 W

Die USV soll die Systeme **20 Minuten** überbrücken. Wirkungsgrad der USV: **90 %**.

a) Berechne die Gesamtleistung.
b) Berechne die benötigte Energie in Wh.
c) Berücksichtige den Wirkungsgrad und bestimme die tatsächlich benötigte Energie.
d) Welche Akkukapazität (in Wh) ist mindestens erforderlich?

> [!success]- Lösung
> **a)** $P_{ges} = 2 \cdot 450\,\text{W} + 150\,\text{W} + 300\,\text{W} = \mathbf{1350\,W}$
>
> **b)** $20\,\text{min} = \tfrac{1}{3}\,\text{h}$
> $W = P \cdot t = 1350\,\text{W} \cdot \tfrac{1}{3}\,\text{h} = \mathbf{450\,Wh}$
>
> **c)** Der Akku muss wegen der Verluste mehr liefern:
> $W_{Akku} = \dfrac{W}{\eta} = \dfrac{450\,\text{Wh}}{0{,}9} = \mathbf{500\,Wh}$
> (Leistungsseitig: $P_{zu} = 1350\,\text{W} / 0{,}9 = 1500\,\text{W}$, $1500\,\text{W} \cdot \tfrac{1}{3}\,\text{h} = 500\,\text{Wh}$)
>
> **d)** Mindestens **500 Wh**. In der Praxis plant man zusätzlich Reserve ein (Akkualterung, keine Tiefentladung, Erweiterungen).

> [!warning] Korrektur
> In einer Mitschrift steht bei d) „405 Wh“. Da wurde mit dem Wirkungsgrad **multipliziert** ($450 \cdot 0{,}9$). Richtig ist **dividieren**, weil der Akku die Verluste zusätzlich decken muss: 500 Wh. In der Formel stand außerdem „/ 0,5“, gemeint ist **0,9**.

## Siehe auch
- [[USV]]
- [[Wirkungsgrad]]
- [[Übung - Akkulaufzeit mobiles Netzwerk]]
