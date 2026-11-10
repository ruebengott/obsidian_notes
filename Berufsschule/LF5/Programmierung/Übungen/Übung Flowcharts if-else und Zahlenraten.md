---
tags: [berufsschule, lf5, englisch, flowchart, programmierung]
fach: LF5
typ: übung
quelle: "[[Technisches Englisch.pdf#page=23]]"
datum:
status: zu-lernen
---
# Übung Flowcharts if-else und Zahlenraten

> [!summary] Kurz & knapp
> Zwei handschriftliche Flussdiagramme am Ende des Englisch-Notizbuchs: ein einfaches **if-else** (Rauchmelder → Sirene) und ein **Zahlenraten-Spiel** mit Schleife. Daneben war „for“ als nächste Struktur angefangen.

## 1. if-else – Rauchmelder
![[Technisches Englisch.pdf#page=23]]

```text
Start
if smoke == true        (Mitschrift: "if Rauch == true")
    siren := 1
else
    do nothing
```

## 2. Zahlenraten (number guessing game)
![[Technisches Englisch.pdf#page=24]]

```text
input "Wie lautet die Zahl?"   -> set var number
input "Tell me the range"      -> set var range
loop:
    guess a (random) number in range
    if guess == number:
        print "right"
        end
    else:
        print "wrong"
        input "higher or lower?"
        adjust var range
        repeat loop
```

## Beschreibung auf Englisch (Beispiel)
> *First, the user enters the secret number and the range. Then the program guesses a random number within the range. If the guess is correct, it prints "right" and the program ends. Otherwise, it prints "wrong" and asks whether the number is higher or lower. After that, the range is adjusted and the program guesses again.*

## Hinweise zur Darstellung
| In der Skizze | Üblich (Flowchart-Symbole) |
|---|---|
| *Start* in einer Raute | **Start/End** = abgerundetes Rechteck/Oval (*terminator*) |
| *input* in einer Raute | **Input/Output** = Parallelogramm |
| *if …* als Parallelogramm | **Decision** = Raute (*diamond*) mit Ausgängen *yes/no* |
| *set var …* | **Process** = Rechteck |
| „set var span“ / „edit var range“ | einheitlich benennen: *range* |

> [!tip] Merke
> Flowchart-Symbole: **oval** = start/end · **rectangle** = process · **diamond** = decision · **parallelogram** = input/output.

## Lernfragen
> [!question]- Welches Symbol steht in einem Flowchart für eine Entscheidung?
> Die Raute (*diamond*).

> [!question]- What's the English word for „Schleife“?
> *loop*

> [!question]- Beschreibe den else-Zweig des Zahlenratens auf Englisch.
> *If the guess is wrong, the program prints "wrong", asks "higher or lower?", adjusts the range and guesses again.*

## Siehe auch
- [[Programmablaufplan und Flussdiagramm]]
- [[Python Verzweigungen]]
- [[Python Schleifen for und while]]
- [[Writing Instructions]]
- [[Englisch - Übersicht]]
- [[LF5 - Übersicht]]
