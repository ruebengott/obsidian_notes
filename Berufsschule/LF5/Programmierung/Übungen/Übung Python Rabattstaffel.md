---
tags: [berufsschule, lf5, python, übung, verzweigung]
fach: LF5
typ: übung
quelle: "[[rabatt.py]]"
datum: 2026-04-14
status: zu-lernen
---
# Übung Python Rabattstaffel

> [!summary] Kurz & knapp
> Übung zu [[Python Verzweigungen]]: Aus der Anzahl gekaufter Lizenzen wird ein Rabatt in Prozent ermittelt. Es gibt zwei Versionen: [[rabatt.py]] mit einzelnen `if`-Anweisungen (Syntaxfehler, Lücken und Überschneidungen) und [[rabatt_verzweigt.py]] mit verschachteltem `if/else` (funktioniert).

## Aufgabe (rekonstruiert)
Ein Softwarehändler gewährt Mengenrabatt auf Lizenzen. Lies die Anzahl der Lizenzen ein und gib den Rabatt aus. Die Staffel ergibt sich aus dem Code ungefähr so:

| Lizenzen | Rabatt |
| --- | --- |
| bis 10 | 0 % |
| 11 bis 20 | 1 % |
| 21 bis 40 | 2 % |
| 41 bis 50 (bzw. 51) | 3 % |
| darüber | 4 % |

## Version 1: einzelne if-Anweisungen
```python
#rabattstaffel
#E
lizenzen = int(input("Wieviele Lizenzen wollen Sie kaufen? (Bitte nur ganze Zahlen angeben): "))

#V
rabatt = 0
if lizenzen > 0 and lizenzen <= 10:
    rabatt = 0

if lizenzen >= 10 and lizenzen < 20:
    rabatt = 1

if lizenzen >= 20 and lizenzen < 40:
    rabatt = 2
    
if lizenzen > 41 and lizenzen < 51:
    rabatt = 3
    
if lizenzen > 51
    rabatt = 4
    
#A
print("Ihr Rabatt beträgt:", rabatt,"%")
```

> [!warning] Korrektur Version 1
> - **Syntaxfehler:** `if lizenzen > 51` ohne Doppelpunkt. Das Programm startet gar nicht.
> - **Überschneidungen:** 10 erfüllt die erste **und** die zweite Bedingung, 20 die zweite und dritte. Weil alle `if` geprüft werden, gewinnt die letzte: 10 Lizenzen ergeben 1 % statt 0 %.
> - **Lücken:** 40, 41 und 51 erfüllen **keine** Bedingung und bekommen 0 %.
> - Die Grenzen sind uneinheitlich: mal `<`, mal `<=`, mal `>`.

## Version 2: verschachtelt
```python
#V
rabatt = 0
if lizenzen <= 10:
    rabatt = 0
else:
    if lizenzen <= 20:
        rabatt = 1
    else:
        if lizenzen <= 40:
            rabatt = 2
        else:
            if lizenzen <= 51:
                rabatt = 3
            else:
                rabatt = 4
```
Hier gibt es keine Lücken und keine Überschneidungen: Jeder Zweig prüft nur die **obere** Grenze, die untere ist durch das vorherige `else` schon gesichert. Funktional richtig.

> [!tip] Verbesserung
> - Mit `elif` statt Verschachtelung.
> - Grenze 51 ist vermutlich ein Tippfehler für 50 (glatte Staffel, siehe offene Frage).
> - Ungültige Eingaben (0 oder negativ) abfangen.
> ```python
> lizenzen = int(input("Wie viele Lizenzen wollen Sie kaufen? "))
>
> if lizenzen <= 0:
>     print("Bitte eine positive Anzahl eingeben.")
> else:
>     if lizenzen <= 10:
>         rabatt = 0
>     elif lizenzen <= 20:
>         rabatt = 1
>     elif lizenzen <= 40:
>         rabatt = 2
>     elif lizenzen <= 50:
>         rabatt = 3
>     else:
>         rabatt = 4
>     print(f"Ihr Rabatt beträgt {rabatt} %.")
> ```

> [!question] Offene Frage
> Die genaue Staffel aus der Aufgabenstellung liegt nicht vor. Liegt die letzte Grenze bei 50 oder 51 Lizenzen?

## Zum Selbsttest
> [!question]- Welchen Rabatt liefert Version 1 (mit ergänztem Doppelpunkt) für 10, 40 und 51 Lizenzen?
> 10 → 1 % (Überschneidung), 40 → 0 % (Lücke), 51 → 0 % (Lücke).

> [!question]- Warum reicht bei einer `elif`-Kette die obere Grenze?
> Ein `elif` wird nur erreicht, wenn alle vorherigen Bedingungen falsch waren. Die untere Grenze ist damit automatisch erfüllt.

## Siehe auch
- [[Python Verzweigungen]]
- [[LF5 - Übersicht]]
