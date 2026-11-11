---
tags: [berufsschule, lf2, digitaltechnik, übung]
fach: LF2
typ: übung
quelle: "[[LF2.pdf#page=59]]"
datum:
status: zu-lernen
---
# Übung - Schaltfunktionen bestimmen

> [!summary] Kurz & knapp
> Arbeitsblatt Digitaltechnik: Funktionsgleichungen aus einer Wertetabelle (Aufgabe 1), aus einer Schaltung (Aufgabe 2) und aus einem Zeitablaufdiagramm (Aufgabe 3) bestimmen.

![[LF2.pdf#page=59]]

## Aufgabe 1 – Wertetabelle
Bestimmen Sie aus Tabelle 1 a) die Teilfunktionen für X = 1, b) die Funktionsgleichung, c) den Funktionsplan.

| D | C | B | A | X |
| --- | --- | --- | --- | --- |
| 0 | 1 | 0 | 1 | 1 |
| 1 | 0 | 1 | 0 | 1 |
| 1 | 1 | 0 | 1 | 1 |
| alle anderen | | | | 0 |

> [!success]- Lösung
> **a) Teilfunktionen**
> 1. $\overline{D} \land C \land \overline{B} \land A$
> 2. $D \land \overline{C} \land B \land \overline{A}$
> 3. $D \land C \land \overline{B} \land A$
>
> **b) Funktionsgleichung**
> $X = (\overline{D} \land C \land \overline{B} \land A) \lor (D \land \overline{C} \land B \land \overline{A}) \lor (D \land C \land \overline{B} \land A)$
>
> Vereinfachung: Teilfunktionen 1 und 3 unterscheiden sich nur in D → D fällt weg:
> $X = (C \land \overline{B} \land A) \lor (D \land \overline{C} \land B \land \overline{A})$
>
> **c) Funktionsplan:** drei UND-Gatter mit je vier Eingängen (negiert: 1. B und D, 2. A und C, 3. B), deren Ausgänge in ein ODER-Gatter → X.

> [!warning] Korrektur
> In der Mitschrift wurde die dritte Teilfunktion in der Gesamtgleichung **durchgestrichen**. Ohne sie fehlt die Zeile 1-1-0-1. Entweder alle drei Teilfunktionen mit ODER verknüpfen oder die vereinfachte Form oben verwenden.

## Aufgabe 2 – Schaltung (Bild 2)
Die Schaltung: $U = A \lor B$ (≥1), $V = U \land C$ (&), $W = A \lor B$ (≥1), $X = V \land W$ (&).
Ermitteln Sie a) die Teilfunktionen für U, V, W, b) die Wertetabelle, c) alle Teilfunktionen für X = 1, d) die Funktionsgleichung für X.

> [!success]- Lösung
> **a)** $U = A \lor B$, $V = U \land C$, $W = A \lor B$, $X = V \land W$
>
> **b) Wertetabelle**
> | A | B | C | U | V | W | X |
> | --- | --- | --- | --- | --- | --- | --- |
> | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
> | 0 | 0 | 1 | 0 | 0 | 0 | 0 |
> | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
> | 0 | 1 | 1 | 1 | 1 | 1 | **1** |
> | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
> | 1 | 0 | 1 | 1 | 1 | 1 | **1** |
> | 1 | 1 | 0 | 1 | 0 | 1 | 0 |
> | 1 | 1 | 1 | 1 | 1 | 1 | **1** |
>
> **c) Teilfunktionen für X = 1**
> $\overline{A} \land B \land C$, $A \land \overline{B} \land C$, $A \land B \land C$
>
> **d) Funktionsgleichung**
> $X = (\overline{A} \land B \land C) \lor (A \land \overline{B} \land C) \lor (A \land B \land C)$
> vereinfacht: $X = (A \lor B) \land C$, weil W dasselbe wie U ist und $(A \lor B) \land C \land (A \lor B) = (A \lor B) \land C$

> [!warning] Korrektur
> In der Mitschrift fehlt bei c)/d) die Teilfunktion $A \land \overline{B} \land C$ (A = 1, B = 0, C = 1 → X = 1). Auch die notierte Wertetabelle ist in einigen Zeilen inkonsistent. Oben steht die vollständig neu berechnete Tabelle.

## Aufgabe 3 – Zeitablaufdiagramm (Bild 3)
Geben Sie a) alle Teilfunktionen für X = 1, b) die Funktionsgleichung und c) den Funktionsplan an.

![[LF2.pdf#page=60]]

> [!success]- Lösung
> **Abgelesene Abschnitte**
> | A | B | C | X |
> | --- | --- | --- | --- |
> | 0 | 0 | 0 | 1 |
> | 0 | 1 | 0 | 1 |
> | 1 | 1 | 0 | 0 |
> | 0 | 0 | 1 | 1 |
> | 1 | 1 | 1 | 0 |
> | 0 | 1 | 1 | 0 |
> | 1 | 0 | 1 | 0 |
> | 1 | 0 | 0 | 0 |
>
> **a) Teilfunktionen für X = 1**
> $\overline{A} \land \overline{B} \land \overline{C}$, $\overline{A} \land B \land \overline{C}$, $\overline{A} \land \overline{B} \land C$
>
> **b) Funktionsgleichung**
> $X = (\overline{A} \land \overline{B} \land \overline{C}) \lor (\overline{A} \land B \land \overline{C}) \lor (\overline{A} \land \overline{B} \land C)$
> vereinfacht: $X = \overline{A} \land (\overline{B} \lor \overline{C}) = \overline{A} \land \overline{B \land C}$
>
> **c) Funktionsplan:** drei UND-Gatter (mit entsprechend negierten Eingängen) → ODER-Gatter → X. Für die vereinfachte Form genügt ein NAND aus B und C, dessen Ausgang mit $\overline{A}$ UND-verknüpft wird.
>
> Die Lösung in der Mitschrift (a, b) ist **richtig**.

> [!note] Hinweis
> Im allerletzten Stück des Diagramms (nach dem Abfallen von A) sind alle Eingänge 0, X ist aber ebenfalls 0. Das widerspricht dem ersten Abschnitt (000 → 1). Vermutlich ist das nur das Diagrammende und gehört nicht zur Auswertung. Die Mitschrift hat es ebenfalls ignoriert.

## Siehe auch
- [[Schaltfunktionen aus Wertetabelle und Zeitablaufdiagramm]]
- [[Logikgatter]]
