---
tags: [berufsschule, lf2, digitaltechnik, übung]
fach: LF2
typ: übung
quelle: "[[LF2.pdf#page=61]]"
datum:
status: zu-lernen
---
# Übung - Automatische Datensicherung mit Logikgattern

> [!summary] Kurz & knapp
> Textaufgabe: Eine Startbedingung für ein Backup in eine Funktionsgleichung und eine Gatterschaltung übersetzen.

## Aufgabe
Ein Unternehmen möchte die tägliche Datensicherung automatisieren. Die Sicherung (**S**) soll gestartet werden, wenn
- ein **Backup-Laufwerk angeschlossen** ist (**B**) **UND**
- **genügend Speicherplatz** vorhanden ist (**P**)

**ODER**
- der **Systemadministrator die Sicherung manuell startet** (**M**).

1. Definiere die Variablen B, P und M.
2. Stelle die Funktionsgleichung für S auf.
3. Zeichne die Schaltung mit UND- und ODER-Gattern.
4. Berechne S für die Eingaben 110, 100, 001, 010 (B P M).

**Zusatz:** Erweitere die Schaltung so, dass die Sicherung nur startet, wenn zusätzlich der **Virenscanner aktiv** ist (**V**).

> [!success]- Lösung
> **1. Variablen**
> | Variable | 1 bedeutet | 0 bedeutet |
> | --- | --- | --- |
> | B | Backup-Laufwerk angeschlossen | nicht angeschlossen |
> | P | genügend Speicherplatz | zu wenig Speicherplatz |
> | M | Admin startet manuell | kein manueller Start |
> | S (Ausgang) | Sicherung startet | Sicherung startet nicht |
>
> **2. Funktionsgleichung**
> $S = (B \land P) \lor M$
>
> **3. Schaltung**
> ```mermaid
> flowchart LR
>     B["B"] --> U["&"]
>     P["P"] --> U
>     U --> O["≥1"]
>     M["M"] --> O
>     O --> S["S"]
> ```
>
> **4. Wertetabelle**
> | B | P | M | S |
> | --- | --- | --- | --- |
> | 1 | 1 | 0 | 1 |
> | 1 | 0 | 0 | 0 |
> | 0 | 0 | 1 | 1 |
> | 0 | 1 | 0 | 0 |
> | 1 | 1 | 1 | 1 |
> | 0 | 0 | 0 | 0 |
> | 0 | 1 | 1 | 1 |
>
> **Zusatz**
> $S = \big((B \land P) \lor M\big) \land V$. Der Ausgang des ODER-Gatters geht zusammen mit V in ein weiteres UND-Gatter.
>
> Die Lösung in der Mitschrift ist **richtig**.

## Siehe auch
- [[Logikgatter]]
- [[Schaltfunktionen aus Wertetabelle und Zeitablaufdiagramm]]
