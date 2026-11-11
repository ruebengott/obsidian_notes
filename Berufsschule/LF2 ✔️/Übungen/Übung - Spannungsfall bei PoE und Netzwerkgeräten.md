---
tags: [berufsschule, lf2, elektrotechnik, poe, übung]
fach: LF2
typ: übung
quelle: "[[LF2.pdf#page=51]]"
datum:
status: zu-lernen
---
# Übung - Spannungsfall bei PoE und Netzwerkgeräten

> [!summary] Kurz & knapp
> IT-Übungsaufgaben 3, 6 und 10: Spannungsfall, Leitungsverluste und Übertragungswirkungsgrad berechnen sowie einen Fehlerfall mit erhöhtem Strom bewerten. Quellen: [[LF2.pdf#page=51]], [[LF2.pdf#page=52]], [[LF2.pdf#page=53]], [[LF2 - Elektrotechnik.pdf#page=3]].

## Aufgabe 3 – Spannungsabfall bei Netzwerkverkabelung
Ein PoE-Gerät wird über ein Kabel mit einem Gesamtwiderstand von **8 Ω** betrieben. Das Gerät benötigt **48 V und 0,5 A**.

a) Berechne den Spannungsabfall auf der Leitung.
b) Welche Spannung muss am Switch anliegen?
c) Berechne die Verlustleistung in der Leitung.
d) Beurteile, ob das System effizient ist.

> [!success]- Lösung
> **a)** $U_V = R \cdot I = 8\,\Omega \cdot 0{,}5\,\text{A} = \mathbf{4\,V}$
>
> **b)** $U_{Switch} = 48\,\text{V} + 4\,\text{V} = \mathbf{52\,V}$
>
> **c)** $P_V = I^2 \cdot R = (0{,}5\,\text{A})^2 \cdot 8\,\Omega = \mathbf{2\,W}$ (oder $U_V \cdot I = 4\,\text{V} \cdot 0{,}5\,\text{A}$)
>
> **d)** Gerät: $P = 48\,\text{V} \cdot 0{,}5\,\text{A} = 24\,\text{W}$. Switch liefert $52\,\text{V} \cdot 0{,}5\,\text{A} = 26\,\text{W}$.
> $\eta = 24 / 26 \approx \mathbf{92{,}3\,\%}$ → **effizient**, nur ca. 7,7 % gehen auf der Leitung verloren.

> [!warning] Korrektur
> In der Mitschrift steht „24 W − 2 W = 22 W“. Die 2 W Verlust werden aber **zusätzlich** vom Switch geliefert und nicht vom Gerätebedarf abgezogen. Das Gerät bekommt seine 24 W, der Switch muss 26 W liefern. Die Bewertung „effizient“ stimmt.

## Aufgabe 6 – WLAN-Access-Point und PoE
Ein Access Point benötigt **15 W bei 48 V** (PoE). Das Kabel hat einen Widerstand von **5 Ω**.

a) Berechne den Strom.
b) Berechne den Spannungsabfall im Kabel.
c) Welche Leistung kommt tatsächlich am Gerät an?
d) Berechne den Wirkungsgrad der Übertragung.

> [!success]- Lösung
> **a)** $I = \dfrac{P}{U} = \dfrac{15\,\text{W}}{48\,\text{V}} = \mathbf{0{,}3125\,A}$
>
> **b)** $U_V = R \cdot I = 5\,\Omega \cdot 0{,}3125\,\text{A} \approx \mathbf{1{,}56\,V}$
>
> **c)** Verlust im Kabel: $P_V = I^2 \cdot R = (0{,}3125\,\text{A})^2 \cdot 5\,\Omega \approx 0{,}49\,\text{W}$
> Wenn der Switch 48 V und 15 W einspeist, kommen am Gerät an: $15\,\text{W} - 0{,}49\,\text{W} \approx \mathbf{14{,}51\,W}$ (bei $48 - 1{,}56 = 46{,}44\,\text{V}$)
>
> **d)** $\eta = \dfrac{14{,}51\,\text{W}}{15\,\text{W}} \approx \mathbf{96{,}7\,\%}$

> [!note] Hinweis
> In c) hat die Mitschrift „$P = 1{,}6\,\text{V} \cdot 0{,}3125\,\text{A} = 0{,}5\,\text{W}$“. Das ist die **Verlustleistung** im Kabel, nicht die Leistung am Gerät. Danach wurde aber richtig mit 14,51 W weitergerechnet. Die Aufgabe ist nicht ganz eindeutig: Versteht man „15 W bei 48 V“ als Bedarf **am Gerät**, muss der Switch $15 + 0{,}49 = 15{,}49\,\text{W}$ liefern und $\eta = 15 / 15{,}49 \approx 96{,}8\,\%$. Das Ergebnis ist praktisch gleich.

## Aufgabe 10 – Fehleranalyse in einer Installation
Ein Netzwerkgerät soll mit **12 V** betrieben werden, zieht aber statt **2 A** plötzlich **3 A**. Der Widerstand der Leitung beträgt **2 Ω**.

a) Berechne den Spannungsabfall vorher und nachher.
b) Berechne die Verlustleistung in beiden Fällen.
c) Erkläre mögliche Ursachen für den erhöhten Strom.
d) Bewerte die Gefahr für die Installation.

> [!success]- Lösung
> **a)**
> - vorher: $U_V = 2\,\Omega \cdot 2\,\text{A} = \mathbf{4\,V}$
> - nachher: $U_V = 2\,\Omega \cdot 3\,\text{A} = \mathbf{6\,V}$ (also 2 V mehr)
>
> **b)**
> - vorher: $P_V = U_V \cdot I = 4\,\text{V} \cdot 2\,\text{A} = \mathbf{8\,W}$ (= $I^2 R = 4 \cdot 2$)
> - nachher: $P_V = 6\,\text{V} \cdot 3\,\text{A} = \mathbf{18\,W}$ (= $9 \cdot 2$) → das 2,25-Fache
>
> **c)** Mögliche Ursachen:
> - **defektes Gerät** (z. B. defektes Netzteil/Bauteil im Gerät)
> - **Kurzschluss** oder Teilkurzschluss, beschädigte Isolierung
> - zusätzliche Verbraucher, Überlast
> - Feuchtigkeit/Korrosion
>
> **d)** Gefahr:
> - Leitungsverluste steigen quadratisch → **Erwärmung** von Kabel und Klemmen → **Brandgefahr**
> - Am Gerät kommt deutlich weniger Spannung an (bei 12 V Quelle nur noch $12 - 6 = 6\,\text{V}$) → Fehlfunktion
> - Die Sicherung kann auslösen und es kommt zum Ausfall. Ursache sofort prüfen und das Gerät ggf. vom Netz trennen.

## Siehe auch
- [[Spannungsfall und Leitungsverluste]]
- [[Power over Ethernet]]
- [[Ohmsches Gesetz]]
- [[Übung - PoE-Leistungsbudget]]
