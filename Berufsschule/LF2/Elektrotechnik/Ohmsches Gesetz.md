---
tags: [berufsschule, lf2, elektrotechnik]
fach: LF2
typ: thema
quelle: "[[LF2.pdf#page=42]]"
datum: 2026-04-20
status: zu-lernen
---
# Ohmsches Gesetz

> [!summary] Kurz & knapp
> Spannung $U$, Strom $I$ und Widerstand $R$ hängen über das ohmsche Gesetz zusammen: $U = R \cdot I$. Kennt man zwei Größen, kann man die dritte berechnen.

## Die drei Grundgrößen

| Größe | Zeichen | Einheit | Vorstellung (Wasser-Modell) |
| --- | --- | --- | --- |
| Spannung | $U$ | Volt, $[U] = \text{V}$ | Wasserdruck |
| Strom | $I$ | Ampere, $[I] = \text{A}$ | durchfließende Wassermenge |
| Widerstand | $R$ | Ohm, $[R] = \Omega$ | Engstelle im Rohr |

Ein **Stromkreis** braucht eine Spannungsquelle (z. B. Netzteil, Akku), Leitungen und einen Verbraucher (z. B. PC, Monitor). Der Verbraucher wirkt dabei wie ein Widerstand $R$.

```mermaid
flowchart LR
    Q["Spannungsquelle U"] -- "Strom I" --> V["Verbraucher (Widerstand R)"]
    V --> Q
```

## Formel und Umstellungen

$$U = R \cdot I \qquad R = \frac{U}{I} \qquad I = \frac{U}{R}$$

## Beispiel aus dem Unterricht (Tafel, 20.04.2026)

Ein Laptop-Netzteil liefert $20\,\text{V}$ Gleichspannung bei $3{,}25\,\text{A}$. Welchen Widerstand hat der Laptop als Verbraucher?

$$R = \frac{U}{I} = \frac{20\,\text{V}}{3{,}25\,\text{A}} \approx 6{,}15\,\Omega$$

## Gleichstrom und Wechselstrom

| | Gleichstrom (DC, Symbol „⎓“) | Wechselstrom (AC, Symbol „~“) |
| --- | --- | --- |
| Verhalten | Strom fließt immer in dieselbe Richtung | Richtung wechselt periodisch (in DE 50-mal pro Sekunde) |
| Beispiele | Akku, Laptop-Netzteil-Ausgang (20 V), USB, PoE | Steckdose (230 V, 50 Hz) |

Ein PC-Netzteil wandelt die Wechselspannung aus der Steckdose in Gleichspannungen (12 V, 5 V, 3,3 V) um. Mehr dazu: [[Wechselspannung - Periode und Frequenz]].

> [!tip] Merke
> - $U = R \cdot I$ – das „URI“-Dreieck: Die gesuchte Größe zuhalten, der Rest zeigt die Formel.
> - Mehr Widerstand bei gleicher Spannung → weniger Strom.
> - Einheiten immer mitschreiben: V, A, Ω.

## Lernfragen
> [!question]- Wie lautet das ohmsche Gesetz und wie stellt man es nach $I$ um?
> $U = R \cdot I$, umgestellt $I = U / R$.

> [!question]- An einem Widerstand von 8 Ω fließen 0,5 A. Wie groß ist die Spannung?
> $U = 8\,\Omega \cdot 0{,}5\,\text{A} = 4\,\text{V}$

> [!question]- In welcher Einheit wird der Widerstand angegeben?
> In Ohm (Ω). $1\,\Omega = 1\,\text{V} / 1\,\text{A}$.

> [!question]- Was ist der Unterschied zwischen Gleich- und Wechselstrom?
> Gleichstrom fließt immer in eine Richtung (z. B. Akku). Bei Wechselstrom wechselt die Richtung periodisch (Steckdose: 50 Hz).

## Siehe auch
- [[Formelsammlung Elektrotechnik]]
- [[Reihen- und Parallelschaltung]]
- [[Elektrische Leistung und Energie]]
- [[Spannungsfall und Leitungsverluste]]
