---
tags: [berufsschule, lf2, elektrotechnik, usv, übung]
fach: LF2
typ: übung
quelle: "[[LF2.pdf#page=53]]"
datum:
status: zu-lernen
---
# Übung - Akkulaufzeit mobiles Netzwerk

> [!summary] Kurz & knapp
> IT-Übungsaufgabe 9: Nutzbare Akkuenergie und Laufzeit eines akkubetriebenen Netzwerks unter Berücksichtigung des Wirkungsgrads berechnen. Auch in [[LF2 - Elektrotechnik.pdf#page=3]] und [[LF2 - Elektrotechnik.pdf#page=4]].

## Aufgabe
Ein mobiler Router (**20 W**) und ein Switch (**30 W**) sollen über einen Akku betrieben werden. Der Akku hat **240 Wh**, Wirkungsgrad des Systems: **85 %**.

a) Berechne die Gesamtleistung.
b) Berechne die effektiv nutzbare Energie.
c) Berechne die Laufzeit.
d) Wie lange läuft das System, wenn nur der Router aktiv ist?

> [!success]- Lösung
> **a)** $P = 20\,\text{W} + 30\,\text{W} = \mathbf{50\,W}$
>
> **b)** $W_{nutz} = \eta \cdot W_{Akku} = 0{,}85 \cdot 240\,\text{Wh} = \mathbf{204\,Wh}$
>
> **c)** $t = \dfrac{W_{nutz}}{P} = \dfrac{204\,\text{Wh}}{50\,\text{W}} = \mathbf{4{,}08\,h} \approx 4\,\text{h}\ 5\,\text{min}$
>
> **d)** $t = \dfrac{204\,\text{Wh}}{20\,\text{W}} = \mathbf{10{,}2\,h} = 10\,\text{h}\ 12\,\text{min}$

> [!warning] Korrektur
> In der Mitschrift stehen drei Fehler:
> - b) „$240 \cdot 0{,}85 = 206\,\text{Wh}$“ ist ein Rechenfehler, richtig sind **204 Wh**.
> - c) „$240\,\text{Wh} / 50\,\text{W} = 4{,}8\,\text{h}$“ ignoriert den Wirkungsgrad. Richtig: 204 Wh / 50 W = **4,08 h**.
> - d) „$240\,\text{Wh} / 20\,\text{W} = 12\,\text{h}$“ ebenfalls ohne Wirkungsgrad. Richtig: **10,2 h**.

## Siehe auch
- [[USV]]
- [[Wirkungsgrad]]
- [[Übung - USV-Dimensionierung]]
