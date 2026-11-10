---
tags: [berufsschule, lf5, programmierung, pap, flowchart]
fach: LF5
typ: thema
quelle: "[[Übung Flowcharts if-else und Zahlenraten]]"
datum:
status: zu-lernen
---
# Programmablaufplan und Flussdiagramm

> [!summary] Kurz & knapp
> Ein **Programmablaufplan (PAP)**, englisch **flowchart**, zeigt den Ablauf eines Programms grafisch **vor** dem Programmieren. Die Symbole sind in **DIN 66001** genormt. Jede Grundstruktur hat ein Gegenstück im Code: **Folge** (Anweisungen nacheinander), **Verzweigung** (`if`) und **Schleife** (`while`/`for`).

## Symbole

| Symbol | Bedeutung | englisch | Python |
| --- | --- | --- | --- |
| Oval / abgerundetes Rechteck | Start, Ende | terminator | Programmanfang/-ende |
| Rechteck | Verarbeitung | process | `summe = summe + zahl` |
| Parallelogramm | Ein-/Ausgabe | input/output | `input()`, `print()` |
| Raute | Verzweigung (ja/nein) | decision | `if`, Bedingung einer `while` |
| Pfeil | Ablaufrichtung | flow line | |
| Rechteck mit doppelten Seitenlinien | Unterprogramm | predefined process | Funktionsaufruf |

## Beispiel: Quersumme
PAP zu [[Übung Python Quersumme]]. Die Schleife erkennt man am Pfeil, der **zurück** vor die Raute führt.

```mermaid
flowchart TD
    S([Start]) --> E[/Eingabe zahl/]
    E --> I[quersumme = 0]
    I --> D{zahl > 0?}
    D -->|ja| V1["quersumme = quersumme + zahl % 10"]
    V1 --> V2["zahl = zahl // 10"]
    V2 --> D
    D -->|nein| A[/Ausgabe quersumme/]
    A --> X([Ende])
```

## Beispiel: Verzweigung (Altersprüfung)
```mermaid
flowchart TD
    S([Start]) --> E[/Eingabe alter/]
    E --> D1{alter >= 18?}
    D1 -->|ja| A1[/volljährig/]
    D1 -->|nein| D2{alter >= 16?}
    D2 -->|ja| A2[/beschränkt geschäftsfähig/]
    D2 -->|nein| A3[/bedingt geschäftsfähig/]
    A1 --> X([Ende])
    A2 --> X
    A3 --> X
```

> [!tip] Merke
> - **oval** = Start/Ende, **Rechteck** = Verarbeitung, **Raute** = Entscheidung, **Parallelogramm** = Ein-/Ausgabe.
> - Eine Raute hat **genau zwei** beschriftete Ausgänge (ja/nein).
> - Eine Schleife ist im PAP eine Raute mit Rücksprung. Ein eigenes Schleifensymbol braucht man nicht.
> - Ähnliche Diagrammart in UML: [[UML-Aktivitätsdiagramm]].

## Lernfragen
> [!question]- Welches Symbol steht für `input()`?
> Das Parallelogramm (Ein-/Ausgabe).

> [!question]- Woran erkennt man im PAP eine Schleife?
> An einem Pfeil, der zu einer früheren Raute zurückführt.

> [!question]- Welche drei Grundstrukturen kennt die strukturierte Programmierung?
> Folge (Sequenz), Verzweigung (Auswahl) und Wiederholung (Schleife).

## Siehe auch
- [[Übung Flowcharts if-else und Zahlenraten]]
- [[Python Verzweigungen]]
- [[Python Schleifen for und while]]
- [[UML-Aktivitätsdiagramm]]
- [[LF5 - Übersicht]]
