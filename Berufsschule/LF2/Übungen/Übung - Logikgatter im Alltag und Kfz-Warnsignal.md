---
tags: [berufsschule, lf2, digitaltechnik, übung]
fach: LF2
typ: übung
quelle: "[[LF2.pdf#page=62]]"
datum:
status: zu-lernen
---
# Übung - Logikgatter im Alltag und Kfz-Warnsignal

> [!summary] Kurz & knapp
> Arbeitsblatt „Digitaltechnik – Logische Gatter“: Alltagsbeispiele für UND/ODER finden, eine Warnsignal-Schaltung entwerfen und Wahrheitstabellen sowie Zeitablaufdiagramme für AND, OR, NAND und NOR ausfüllen.

## Aufgabe 1/2 – Beispiele aus dem Alltag
Nenne Beispiele für UND- und ODER-Gatter aus den Bereichen a) zu Hause, b) Garagentor, c) Computer, d) Beleuchtung, e) Zugangskontrolle, und stelle Wahrheitstabellen auf (Eingänge definieren).

> [!success]- Lösung
> | Bereich | Beispiel | Verknüpfung |
> | --- | --- | --- |
> | a) zu Hause | Geschirrspüler startet: Tab eingelegt **UND** Startknopf gedrückt (Tür zu) | UND |
> | b) Garagentor | öffnet per Taster **ODER** Fernbedienung | ODER |
> | c) Computer | startet per Einschaltknopf **ODER** Wake-on-LAN | ODER |
> | d) Beleuchtung | Licht an über Schalter 1 **ODER** Schalter 2 | ODER |
> | e) Zugangskontrolle | Tür öffnet mit Karte **UND** PIN-Code | UND |
>
> Beispiel-Wahrheitstabelle (e): K = Karte gültig (1), C = Code richtig (1), T = Tür öffnet (1)
> | K | C | T |
> | --- | --- | --- |
> | 0 | 0 | 0 |
> | 0 | 1 | 0 |
> | 1 | 0 | 0 |
> | 1 | 1 | 1 |
>
> *Hinweis:* Eine echte Treppenhaus-Wechselschaltung (Licht mit zwei Schaltern an- **und** ausschalten) ist eigentlich ein **XOR** (exklusives ODER).

## Aufgabe 4 – Licht-Warnsignal im Auto
Das Warnsignal soll ertönen, wenn
- die **Scheinwerfer an** sind **und**
- der **Motor aus** ist **und**
- die **Fahrertür offen** ist.

Stelle Wahrheitstabelle (Eingänge definieren) und Funktionsgleichung auf.

> [!success]- Lösung
> **Eingänge**
> | Variable | 1 | 0 |
> | --- | --- | --- |
> | S | Scheinwerfer eingeschaltet | aus |
> | M | Motor läuft | Motor aus |
> | F | Fahrertür offen | geschlossen |
> | W (Ausgang) | Warnsignal ertönt | still |
>
> **Funktionsgleichung:** $W = S \land \overline{M} \land F$
>
> **Wahrheitstabelle**
> | S | M | F | W |
> | --- | --- | --- | --- |
> | 0 | 0 | 0 | 0 |
> | 0 | 0 | 1 | 0 |
> | 0 | 1 | 0 | 0 |
> | 0 | 1 | 1 | 0 |
> | 1 | 0 | 0 | 0 |
> | 1 | 0 | 1 | **1** |
> | 1 | 1 | 0 | 0 |
> | 1 | 1 | 1 | 0 |
>
> **Schaltung:** M über ein NICHT-Gatter negieren, dann S, $\overline{M}$ und F in ein UND-Gatter mit drei Eingängen → W.
>
> ```mermaid
> flowchart LR
>     S["S"] --> U["&"]
>     M["M"] --> N["NICHT"] --> U
>     F["F"] --> U
>     U --> W["W"]
> ```
>
> Die Lösung in der Mitschrift ist **richtig** (dort wurde die Tabelle nur angefangen).

## Aufgabe 5 – Wahrheitstabellen und Zeitablaufdiagramme
Fülle für AND, OR, NAND und NOR die Wahrheitstabelle und das Zeitablaufdiagramm aus.

> [!success]- Lösung
> | B | A | AND | OR | NAND | NOR |
> | --- | --- | --- | --- | --- | --- |
> | 0 | 0 | 0 | 0 | 1 | 1 |
> | 0 | 1 | 0 | 1 | 1 | 0 |
> | 1 | 0 | 0 | 1 | 1 | 0 |
> | 1 | 1 | 1 | 1 | 0 | 0 |
>
> Im Zeitablaufdiagramm ist Z bei AND nur dort 1, wo A **und** B gleichzeitig 1 sind. Bei OR ist Z überall dort 1, wo mindestens eins von beiden 1 ist. NAND und NOR sind jeweils genau umgekehrt. Die eingezeichneten Lösungen (rot) siehe Originalseite:
>
> ![[LF2.pdf#page=63]]

> [!note] Offen
> Aufgabe 3 (eigene Schaltung mit mindestens 3 Gattern) wurde in der Mitschrift nicht bearbeitet. Ein Beispiel ist die Zusatzaufgabe in [[Übung - Automatische Datensicherung mit Logikgattern]] (UND, ODER, UND).

## Siehe auch
- [[Logikgatter]]
- [[Schaltfunktionen aus Wertetabelle und Zeitablaufdiagramm]]
