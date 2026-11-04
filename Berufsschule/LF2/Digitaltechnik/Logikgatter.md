---
tags: [berufsschule, lf2, digitaltechnik, logik]
fach: LF2
typ: thema
quelle: "[[LF2.pdf#page=57]]"
datum:
status: zu-lernen
---
# Logikgatter

> [!summary] Kurz & knapp
> Digitale Schaltungen arbeiten mit zwei Zuständen, **0 und 1**. Die Grundverknüpfungen sind **UND** (&), **ODER** (≥1) und **NICHT** (Negation). Daraus entstehen **NAND** und **NOR**. Mit den **De-Morganschen Regeln** kann man zwischen ihnen umformen.

## Grundverknüpfungen

| Gatter | Schaltzeichen (DIN) | Funktionsgleichung | Ausgang ist 1, wenn … |
| --- | --- | --- | --- |
| **UND** (AND) | Kasten mit **&** | $X = A \land B$ | **alle** Eingänge 1 sind |
| **ODER** (OR) | Kasten mit **≥1** | $X = A \lor B$ | **mindestens ein** Eingang 1 ist |
| **NICHT** (NOT) | Kasten mit **1** und Kreis am Ausgang | $X = \overline{A}$ | der Eingang 0 ist |
| **NAND** | & mit Kreis am Ausgang | $X = \overline{A \land B}$ | **nicht alle** Eingänge 1 sind |
| **NOR** | ≥1 mit Kreis am Ausgang | $X = \overline{A \lor B}$ | **alle** Eingänge 0 sind |

Der **Kreis** am Ein- oder Ausgang bedeutet immer **Negation**.

## Wertetabellen

| B | A | UND | ODER | NAND | NOR |
| --- | --- | --- | --- | --- | --- |
| 0 | 0 | 0 | 0 | 1 | 1 |
| 0 | 1 | 0 | 1 | 1 | 0 |
| 1 | 0 | 0 | 1 | 1 | 0 |
| 1 | 1 | 1 | 1 | 0 | 0 |

| A | NICHT $\overline{A}$ |
| --- | --- |
| 0 | 1 |
| 1 | 0 |

Bei $n$ Eingängen hat die Wertetabelle $2^n$ Zeilen (2 Eingänge → 4 Zeilen, 3 → 8, 4 → 16).

## De-Morgansche Regeln (Tafelbild)

$$\overline{A \land B} = \overline{A} \lor \overline{B} \qquad \text{(NAND)}$$
$$\overline{A \lor B} = \overline{A} \land \overline{B} \qquad \text{(NOR)}$$

Merksatz: **„Strich trennen, Zeichen tauschen.“** Den langen Negationsstrich auf die einzelnen Variablen aufteilen und dabei ∧ ↔ ∨ tauschen.

> [!warning] Korrektur
> In der Mitschrift zu „Beispiel 2“ (NOR-Gatter) steht $X = \overline{A} \lor \overline{B}$. Die notierte Wertetabelle (nur bei 0/0 ist X = 1) ist aber die eines **NOR**, und nach De Morgan gilt dafür $X = \overline{A \lor B} = \overline{A} \land \overline{B}$. $\overline{A} \lor \overline{B}$ wäre ein **NAND**.

## Kontaktlogik ↔ Gatter
Schalter (Kontakte) in einem Stromkreis lassen sich direkt in Gatter übersetzen:
- **Reihenschaltung** von Kontakten = **UND** (Lampe leuchtet nur, wenn alle geschlossen sind)
- **Parallelschaltung** von Kontakten = **ODER** (einer reicht)
- **Öffner** (im Ruhezustand geschlossener Kontakt) = **negierter** Eingang ($\overline{a}$)
- **Schließer** (im Ruhezustand offen) = normaler Eingang ($a$)

Beispiel: [[Übung - Kontaktlogik in Gatter umsetzen]]

## Beispiele aus dem Alltag
- **UND:** Geschirrspüler startet nur, wenn Tab eingelegt **und** Startknopf gedrückt; Zugangskontrolle mit Karte **und** PIN-Code
- **ODER:** Garagentor öffnet per Taster **oder** Fernbedienung; PC startet per Einschaltknopf **oder** Wake-on-LAN; Licht über Schalter 1 **oder** Schalter 2

> [!tip] Merke
> - & = UND (alle), ≥1 = ODER (mindestens einer), Kreis = Negation.
> - NAND = $\overline{A} \lor \overline{B}$, NOR = $\overline{A} \land \overline{B}$ (De Morgan).
> - Reihe = UND, parallel = ODER, Öffner = negiert.

## Lernfragen
> [!question]- Wann liefert ein ODER-Gatter eine 1?
> Wenn mindestens ein Eingang 1 ist.

> [!question]- Wie lautet die Wertetabelle eines NAND-Gatters mit zwei Eingängen?
> 00 → 1, 01 → 1, 10 → 1, 11 → 0.

> [!question]- Forme $\overline{A \lor B}$ mit De Morgan um.
> $\overline{A} \land \overline{B}$

> [!question]- Welcher Verknüpfung entspricht eine Reihenschaltung von zwei Schaltern?
> Einer UND-Verknüpfung.

> [!question]- Wie viele Zeilen hat die Wertetabelle einer Schaltung mit 3 Eingängen?
> $2^3 = 8$ Zeilen.

## Siehe auch
- [[Schaltfunktionen aus Wertetabelle und Zeitablaufdiagramm]]
- [[Übung - Logikgatter im Alltag und Kfz-Warnsignal]]
- [[Übung - Automatische Datensicherung mit Logikgattern]]
- [[Übung - Kontaktlogik in Gatter umsetzen]]
- [[CPU - Aufbau und Kenngrößen]]
