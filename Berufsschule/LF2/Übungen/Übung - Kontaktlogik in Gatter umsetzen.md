---
tags: [berufsschule, lf2, digitaltechnik, übung]
fach: LF2
typ: übung
quelle: "[[LF2.pdf#page=65]]"
datum:
status: zu-lernen
---
# Übung - Kontaktlogik in Gatter umsetzen

> [!summary] Kurz & knapp
> Eine Schalter-/Kontaktschaltung mit Lampe (Ausgang y) in eine Schaltung aus digitalen Gattern übersetzen. Reihe = UND, parallel = ODER, Öffner = negiert.

## Aufgabe
Verwirkliche die dargestellte Kontaktlogik mit digitalen Gattern (Eingänge d, c, b, a / Ausgang y).

![[LF2.pdf#page=65]]

Aufbau der Kontaktschaltung:
- Kontakte **a** und **b** liegen **parallel** zueinander,
- dazu **in Reihe** Kontakt **c**,
- und dieser ganze Zweig liegt **parallel** zu Kontakt **d**.

> [!success]- Lösung
> **Funktionsgleichung**
> $y = \big((\overline{a} \lor \overline{b}) \land c\big) \lor d$
>
> (Falls a und b als normale Schließer gemeint sind: $y = \big((a \lor b) \land c\big) \lor d$)
>
> **Gatterschaltung**
> ```mermaid
> flowchart LR
>     a["a"] --> Na["NICHT"] --> O1["≥1"]
>     b["b"] --> Nb["NICHT"] --> O1
>     O1 --> U["&"]
>     c["c"] --> U
>     U --> O2["≥1"]
>     d["d"] --> O2
>     O2 --> y["y"]
> ```

> [!warning] Korrektur
> 1. In der Mitschrift ist das ODER-Gatter mit „**≤1**“ beschriftet. Richtig ist **≥1** (mindestens ein Eingang = 1).
> 2. Die Kontakte **a** und **b** sind im Schaltbild mit dem Haken-Symbol gezeichnet. Das ist das Symbol für **Öffner** (im Ruhezustand geschlossen). Dann müssen a und b am Gatter **negiert** werden. In der Mitschrift fehlt die Negation. Bitte mit der Lehrkraft klären, ob Öffner gemeint waren. Sonst ist die Mitschrift-Lösung $((a \lor b) \land c) \lor d$ richtig.

## Siehe auch
- [[Logikgatter]]
- [[Reihen- und Parallelschaltung]]
