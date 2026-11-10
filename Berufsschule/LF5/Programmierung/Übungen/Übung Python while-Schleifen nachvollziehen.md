---
tags: [berufsschule, lf5, python, übung, schleife]
fach: LF5
typ: übung
quelle: "[[while a).py]]"
datum: 2026-04-21
status: zu-lernen
---
# Übung Python while-Schleifen nachvollziehen

> [!summary] Kurz & knapp
> Drei kurze Programme zu [[Python Schleifen for und while]] aus den Dateien [[while.py]], [[while a).py]] und [[while b).py]]. Aufgabe war vermutlich jeweils: „Was gibt das Programm aus?“ Lösung per **Schreibtischtest**.

## while.py: Wie oft wird „Hello world“ ausgegeben?
```python
i = 0

while (False):
    print("Hello world")
    i = i+1
```
> [!success]- Lösung
> **Gar nicht.** Die Bedingung `False` ist schon vor dem ersten Durchlauf falsch. `while` ist kopfgesteuert und prüft die Bedingung **vor** dem Schleifenkörper. `i` bleibt 0. (Mit `while True:` ohne `break` gäbe es dagegen eine Endlosschleife.)

## a) Was wird ausgegeben?
```python
summe = 0
zahl = 0

while summe <=100:
    zahl = zahl + 1
    summe = summe + zahl

print(zahl)
```
> [!success]- Lösung
> Es werden 1 + 2 + 3 + … addiert, bis die Summe **über 100** liegt.
>
> | zahl | summe |
> | --- | --- |
> | 1 | 1 |
> | 2 | 3 |
> | … | … |
> | 12 | 78 |
> | 13 | 91 |
> | 14 | 105 → Bedingung `105 <= 100` falsch |
>
> Ausgabe: **14**. Gesucht ist also die kleinste Zahl n, bei der 1 + … + n größer als 100 ist.

## b) Was wird ausgegeben?
```python
a = 10
b = 20

while b > 5:
    b = b-5
    a=a+2
print(a)
```
> [!success]- Lösung
> | Durchlauf | b | a |
> | --- | --- | --- |
> | Start | 20 | 10 |
> | 1 | 15 | 12 |
> | 2 | 10 | 14 |
> | 3 | 5 | 16 |
>
> Danach ist `5 > 5` falsch. Ausgabe: **16**.

## Review
> [!tip] Verbesserung
> Die Programme sind korrekt. Stil: Klammern um die Bedingung (`while (False):`) sind unnötig, und um `=` gehören Leerzeichen (`a = a + 2` oder `a += 2`).

## Siehe auch
- [[Python Schleifen for und while]]
- [[LF5 - Übersicht]]
