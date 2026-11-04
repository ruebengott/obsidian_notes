---
tags: [berufsschule, lf2, elektrotechnik, formelsammlung]
fach: LF2
typ: übersicht
quelle: "[[LF2.pdf#page=55]]"
datum: 2026-04-20
status: zu-lernen
---
# Formelsammlung Elektrotechnik

> [!summary] Kurz & knapp
> Alle Formeln, die du für die Rechenaufgaben in LF2 brauchst (Klausurthema „Rechenbeispiele“). Fast jede Aufgabe ist eine Kombination aus $U = R \cdot I$, $P = U \cdot I$, $W = P \cdot t$ und $\eta = P_{ab} / P_{zu}$.

## Größen und Einheiten

| Größe | Formelzeichen | Einheit | Hinweis |
| --- | --- | --- | --- |
| Spannung | $U$ | Volt (V) | „Druck“, der die Elektronen antreibt |
| Stromstärke | $I$ | Ampere (A) | fließende Ladung pro Zeit |
| Widerstand | $R$ | Ohm ($\Omega$) | hemmt den Stromfluss |
| Leistung | $P$ | Watt (W) = V·A | Energie pro Zeit |
| Arbeit / Energie | $W$ (oft auch $E$) | Wattstunde (Wh), kWh | $1\,\text{kWh} = 1000\,\text{Wh}$ |
| Wirkungsgrad | $\eta$ (eta) | ohne Einheit (oder %) | immer < 1 |
| Periodendauer | $T$ | Sekunde (s) | |
| Frequenz | $f$ | Hertz (Hz) = 1/s | |

## Grundformeln

| Thema | Formel | Umgestellt |
| --- | --- | --- |
| Ohmsches Gesetz | $U = R \cdot I$ | $R = \dfrac{U}{I}$, $I = \dfrac{U}{R}$ |
| Leistung | $P = U \cdot I$ | $I = \dfrac{P}{U}$, $U = \dfrac{P}{I}$ |
| Leistung (mit $R$) | $P = I^2 \cdot R = \dfrac{U^2}{R}$ | |
| Elektrische Arbeit | $W = P \cdot t$ | $t = \dfrac{W}{P}$, $P = \dfrac{W}{t}$ |
| Energiekosten | $K = W \cdot \text{Preis pro kWh}$ | $W$ immer in **kWh** einsetzen |
| Wirkungsgrad | $\eta = \dfrac{P_{ab}}{P_{zu}}$ | $P_{zu} = \dfrac{P_{ab}}{\eta}$, $P_{ab} = \eta \cdot P_{zu}$ |
| Verlustleistung | $P_V = P_{zu} - P_{ab}$ | $P_V = (1-\eta) \cdot P_{zu}$ |
| Mehrere Wirkungsgrade hintereinander | $\eta_{ges} = \eta_1 \cdot \eta_2 \cdot \ldots$ | |
| Frequenz / Periode | $f = \dfrac{1}{T}$ | $T = \dfrac{1}{f}$ |

## Schaltungen

| | Reihenschaltung | Parallelschaltung |
| --- | --- | --- |
| Strom | überall gleich: $I = I_1 = I_2$ | teilt sich auf: $I = I_1 + I_2$ |
| Spannung | teilt sich auf: $U = U_1 + U_2$ | überall gleich: $U = U_1 = U_2$ |
| Gesamtwiderstand | $R_{ges} = R_1 + R_2 + \ldots$ | $\dfrac{1}{R_{ges}} = \dfrac{1}{R_1} + \dfrac{1}{R_2} + \ldots$ |
| Zwei gleiche Widerstände | $R_{ges} = 2R$ | $R_{ges} = R/2$ |

## Leitungen, PoE und USV

| Thema | Formel |
| --- | --- |
| Spannungsfall auf der Leitung | $U_V = R_{Ltg} \cdot I$ |
| Leitungsverlust | $P_V = I^2 \cdot R_{Ltg}$ |
| Spannung an der Quelle (z. B. Switch) | $U_{Quelle} = U_{Gerät} + U_V$ |
| Übertragungswirkungsgrad | $\eta = \dfrac{P_{Gerät}}{P_{Gerät} + P_V}$ |
| PoE-Budget | $P_{ges} = \sum (\text{Anzahl} \cdot P_{Gerät}) \le P_{Budget}$ |
| USV-Energiebedarf | $W = P_{ges} \cdot t_{Überbrückung}$ |
| USV-Akkukapazität | $W_{Akku} = \dfrac{P_{ges} \cdot t}{\eta}$ |
| Akkulaufzeit | $t = \dfrac{W_{Akku} \cdot \eta}{P}$ |
| Belastbarkeit eines Stromkreises | $P_{max} = U \cdot I_{Sicherung}$ (z. B. $230\,\text{V} \cdot 16\,\text{A} = 3680\,\text{W}$) |
| Netzteil mit Puffer | $P_{NT} \ge P_{Summe} \cdot 1{,}1$ (10 % Puffer), dann nächstgrößeres Netzteil |

## Umrechnungen

- $1\,\text{kW} = 1000\,\text{W}$, $1\,\text{W} = 1000\,\text{mW}$
- $1\,\text{A} = 1000\,\text{mA}$
- $1\,\text{h} = 60\,\text{min}$, $20\,\text{min} = \tfrac{1}{3}\,\text{h}$
- $1\,\text{s} = 1000\,\text{ms}$
- $1\,\text{Jahr} = 365\,\text{Tage}$ (wenn nicht anders angegeben)
- Prozent → Dezimal: $90\,\% = 0{,}9$

> [!tip] Merke – Rechenweg in der Klausur
> 1. Gegebenes und Gesuchtes notieren (mit Einheiten).
> 2. Formel hinschreiben, dann umstellen.
> 3. Einsetzen **mit Einheiten**, Watt → Kilowatt umrechnen, bevor du mit dem kWh-Preis multiplizierst.
> 4. Beim Wirkungsgrad: Die **aufgenommene** Leistung ist immer **größer** als die abgegebene. Also $P_{zu} = P_{ab} / \eta$ (dividieren, nicht multiplizieren).
> 5. Ergebnis sinnvoll runden und einen Antwortsatz schreiben.

## Lernfragen
> [!question]- Ein Gerät nimmt 2 A bei 230 V auf. Wie groß ist die Leistung?
> $P = U \cdot I = 230\,\text{V} \cdot 2\,\text{A} = 460\,\text{W}$

> [!question]- Ein Netzteil soll 300 W abgeben und hat $\eta = 0{,}8$. Wie viel nimmt es auf?
> $P_{zu} = P_{ab} / \eta = 300\,\text{W} / 0{,}8 = 375\,\text{W}$ (75 W Verlust)

> [!question]- Wie viele Watt darf man an einen mit 16 A abgesicherten 230-V-Stromkreis anschließen?
> $P_{max} = 230\,\text{V} \cdot 16\,\text{A} = 3680\,\text{W}$

> [!question]- Warum steigen die Leitungsverluste bei doppeltem Strom auf das Vierfache?
> Weil $P_V = I^2 \cdot R$ gilt: Der Strom geht quadratisch ein, $2^2 = 4$.

## Siehe auch
- [[Ohmsches Gesetz]]
- [[Reihen- und Parallelschaltung]]
- [[Elektrische Leistung und Energie]]
- [[Wirkungsgrad]]
- [[Spannungsfall und Leitungsverluste]]
- [[Power over Ethernet]]
- [[USV]]
- [[Wechselspannung - Periode und Frequenz]]
- [[Spannungsebenen im Stromnetz]]
