---
tags: [berufsschule, lf2, elektrotechnik]
fach: LF2
typ: thema
quelle: "[[LF2.pdf#page=45]]"
datum: 2026-04-20
status: zu-lernen
---
# Elektrische Leistung und Energie

> [!summary] Kurz & knapp
> Die **Leistung** $P = U \cdot I$ (in Watt) sagt, wie viel Energie ein Gerät pro Zeit umsetzt. Die **elektrische Arbeit/Energie** $W = P \cdot t$ (in kWh) ist das, was der Stromzähler misst und was man bezahlt: Kosten = kWh · Preis.

## Leistung

$$P = U \cdot I \qquad [P] = \text{V} \cdot \text{A} = \text{W (Watt)}$$

Mit dem ohmschen Gesetz ergeben sich außerdem $P = I^2 \cdot R$ und $P = U^2 / R$.

**Beispiel:** Laptop-Netzteil, Ausgang 20 V / 3,25 A → $P = 20\,\text{V} \cdot 3{,}25\,\text{A} = 65\,\text{W}$

## Elektrische Arbeit (Energie)

$$W = P \cdot t \qquad [W] = \text{W} \cdot \text{h} = \text{Wh}, \quad 1\,\text{kWh} = 1000\,\text{Wh}$$

Im Unterricht wurde dafür auch $E = P \cdot t$ geschrieben. Gemeint ist dasselbe.

## Stromkosten berechnen

$$K = W\,[\text{kWh}] \cdot \text{Preis}\,[\text{€/kWh}]$$

**Vorgehen:**
1. Laufzeit $t$ bestimmen (Stunden pro Tag · Tage).
2. $W = P \cdot t$ berechnen und in **kWh** umrechnen.
3. Mit dem Preis pro kWh multiplizieren.

**Beispiel:** Ein PC mit 350 W läuft täglich 10 h bei 0,41 €/kWh.
$W = 350\,\text{W} \cdot 10\,\text{h} = 3500\,\text{Wh} = 3{,}5\,\text{kWh}$ → $K = 3{,}5\,\text{kWh} \cdot 0{,}41\,\text{€/kWh} \approx 1{,}44\,\text{€}$ pro Tag.

## Netzteil dimensionieren
1. Maximale Leistungsaufnahme aller Komponenten addieren (Anzahl beachten!).
2. Puffer aufschlagen (z. B. 10 %): $P \cdot 1{,}1$.
3. Das **nächstgrößere** verfügbare Netzteil wählen.

Beispiel siehe [[Übung - Elektrische Leistung und Arbeit]] (Aufgabe 4: 560 W + 10 % = 616 W → 650-W-Netzteil).

> [!tip] Merke
> - Leistung = „wie stark“ (W), Arbeit = „wie viel insgesamt“ (kWh).
> - Vor dem Multiplizieren mit dem Strompreis **immer in kWh umrechnen**.
> - Strompreisangabe „pro kW“ ist umgangssprachlich und meint **pro kWh**.

## Lernfragen
> [!question]- Was ist der Unterschied zwischen Leistung und Arbeit?
> Leistung $P$ (W) ist die Energie pro Zeit. Arbeit $W = P \cdot t$ (kWh) ist die insgesamt umgesetzte Energie über eine Zeitspanne.

> [!question]- Ein 60-W-Leuchtmittel brennt 11 h. Wie viel Energie wird verbraucht?
> $W = 60\,\text{W} \cdot 11\,\text{h} = 660\,\text{Wh} = 0{,}66\,\text{kWh}$

> [!question]- Wie berechnet man die Stromkosten?
> Energie in kWh mal Preis pro kWh: $K = W \cdot \text{Preis}$.

> [!question]- Warum schlägt man bei der Netzteilauswahl einen Puffer auf?
> Lastspitzen, spätere Aufrüstung und Alterung. Außerdem arbeiten Netzteile im mittleren Lastbereich am effizientesten und werden nicht dauerhaft am Limit betrieben.

> [!question]- Ein Gerät nimmt bei 230 V 1,5 A auf. Welche Leistung hat es?
> $P = 230\,\text{V} \cdot 1{,}5\,\text{A} = 345\,\text{W}$

## Siehe auch
- [[Formelsammlung Elektrotechnik]]
- [[Wirkungsgrad]]
- [[Ohmsches Gesetz]]
- [[Übung - Elektrische Leistung und Arbeit]]
- [[Übung - Energiekosten Klimaanlage und Server]]
- [[Green IT]]
