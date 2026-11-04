---
tags: [berufsschule, lf2, elektrotechnik, übung]
fach: LF2
typ: übung
quelle: "[[LF2.pdf#page=52]]"
datum:
status: zu-lernen
---
# Übung - Netzteile und Wirkungsgrad

> [!summary] Kurz & knapp
> IT-Übungsaufgaben 4 und 8: Leistungsaufnahme, Verlustleistung und Strom eines Servernetzteils berechnen, außerdem redundante Netzteile. Quellen: [[LF2.pdf#page=52]], [[LF2.pdf#page=53]], [[LF2 - Elektrotechnik.pdf#page=4]].

## Aufgabe 4 – Netzteilwirkungsgrad eines Servers
Ein Server benötigt intern **300 W**. Das Netzteil hat einen Wirkungsgrad von **82 %**.

a) Berechne die aufgenommene Leistung aus dem Stromnetz.
b) Berechne die Verlustleistung.
c) Wie groß ist der Strom bei 230 V?
d) Wie viel Energie wird in 10 Stunden verbraucht (kWh)?

> [!success]- Lösung
> **a)** $P_{zu} = \dfrac{P_{ab}}{\eta} = \dfrac{300\,\text{W}}{0{,}82} \approx \mathbf{365{,}9\,W}$
>
> **b)** $P_V = P_{zu} - P_{ab} = 365{,}9\,\text{W} - 300\,\text{W} \approx \mathbf{65{,}9\,W}$
> (oder $0{,}18 \cdot 365{,}9\,\text{W}$)
>
> **c)** $I = \dfrac{P}{U} = \dfrac{365{,}9\,\text{W}}{230\,\text{V}} \approx \mathbf{1{,}59\,A}$
>
> **d)** $W = 365{,}9\,\text{W} \cdot 10\,\text{h} \approx 3659\,\text{Wh} \approx \mathbf{3{,}66\,kWh}$

## Aufgabe 8 – Redundante Stromversorgung
Ein Server hat **zwei Netzteile mit jeweils 400 W** (Redundanz, die Last verteilt sich gleichmäßig). Wirkungsgrad pro Netzteil: **88 %**.

a) Wie viel Leistung liefert jedes Netzteil?
b) Wie viel Leistung wird jeweils aufgenommen?
c) Berechne die Gesamtverlustleistung.
d) Warum ist Redundanz trotz höherer Verluste sinnvoll?

> [!success]- Lösung
> *Annahme:* Der Server braucht insgesamt 400 W, also so viel, wie **ein** Netzteil allein schaffen muss, damit echte Redundanz besteht.
>
> **a)** $P_{ab} = 400\,\text{W} / 2 = \mathbf{200\,W}$ je Netzteil
>
> **b)** $P_{zu} = \dfrac{200\,\text{W}}{0{,}88} \approx \mathbf{227{,}3\,W}$ je Netzteil
>
> **c)** Verlust je Netzteil: $227{,}3\,\text{W} - 200\,\text{W} \approx 27{,}3\,\text{W}$
> Gesamt: $2 \cdot 27{,}3\,\text{W} \approx \mathbf{54{,}5\,W}$ (Gesamtaufnahme ca. 454,5 W)
>
> **d)** Fällt ein Netzteil aus, übernimmt das andere sofort die volle Last und der Server läuft **ohne Unterbrechung** weiter. Mit Hot-Swap kann das defekte Netzteil im laufenden Betrieb getauscht werden. Wenn die Netzteile an zwei getrennten Stromkreisen hängen (A/B-Einspeisung), schützt das auch gegen den Ausfall eines Stromkreises. Ein Serverausfall kostet meist viel mehr als die paar Watt Mehrverlust (Netzteile im Teillastbereich sind etwas ineffizienter).

> [!warning] Korrektur
> In den Mitschriften wurden verschiedene Werte gemischt:
> - b) „$400\,\text{W} / 0{,}88 = 454{,}55\,\text{W}$“ ist die Aufnahme **beider** Netzteile zusammen, nicht „jeweils“.
> - Eine andere Version rechnet a) „$0{,}88 \cdot 400\,\text{W} = 352\,\text{W}$“. Die 400 W sind aber die Nennleistung (Abgabe), auf die man den Wirkungsgrad nicht nochmal anwendet.
> - c) „$0{,}12 \cdot 400\,\text{W} = 48\,\text{W}$“: Der Verlustanteil 12 % bezieht sich auf die **aufgenommene** Leistung, also $0{,}12 \cdot 454{,}5\,\text{W} \approx 54{,}5\,\text{W}$. Das „205 W“ am Ende ist kein sinnvolles Ergebnis.
>
> *Falls* jedes Netzteil tatsächlich 400 W abgibt (Serverlast 800 W): Aufnahme je 454,5 W, Verlust je 54,5 W, gesamt ca. 109 W.

## Siehe auch
- [[Wirkungsgrad]]
- [[Elektrische Leistung und Energie]]
- [[USV]]
