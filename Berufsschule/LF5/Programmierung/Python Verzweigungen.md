---
tags: [berufsschule, lf5, python, programmierung, verzweigung]
fach: LF5
typ: thema
quelle: "[[rabatt_verzweigt.py]]"
datum: 2026-04-14
status: zu-lernen
---
# Python Verzweigungen

> [!summary] Kurz & knapp
> Mit `if`, `elif` und `else` führt ein Programm je nach **Bedingung** unterschiedlichen Code aus. Bedingungen sind Ausdrücke, die `True` oder `False` ergeben. Der zugehörige Block wird durch **Einrückung** (4 Leerzeichen) und einen **Doppelpunkt** am Zeilenende gekennzeichnet.

## Aufbau
```python
alter = int(input("Alter: "))

if alter >= 18:
    print("volljährig")
elif alter >= 7:
    print("beschränkt geschäftsfähig")
else:
    print("geschäftsunfähig")
```
- `if` prüft die erste Bedingung.
- `elif` („else if“) wird nur geprüft, wenn alle vorherigen Bedingungen **falsch** waren.
- `else` greift, wenn **keine** Bedingung zutraf.
- Es wird immer **genau ein** Zweig ausgeführt (bei `if/elif/else`).

## Vergleichs- und logische Operatoren

| Operator | Bedeutung |
| --- | --- |
| `==`, `!=` | gleich, ungleich |
| `<`, `<=`, `>`, `>=` | kleiner, kleiner gleich, ... |
| `and` | beide Bedingungen wahr |
| `or` | mindestens eine wahr |
| `not` | kehrt um |
| `in` | Element in Liste/String enthalten, z. B. `"rosa" in liste` |

Python erlaubt **verkettete Vergleiche**: `10 < lizenzen <= 20` statt `lizenzen > 10 and lizenzen <= 20`.

## Verschachtelt oder `elif`?
In [[altersprüfung.py]], [[prämienberechnung.py]] und [[rabatt_verzweigt.py]] steht ein neues `if` **im** `else`-Block (verschachtelt). Das funktioniert, wird aber schnell unübersichtlich. Mit `elif` ist es gleichwertig und flacher:

```python
# verschachtelt
if lizenzen <= 10:
    rabatt = 0
else:
    if lizenzen <= 20:
        rabatt = 1
    else:
        rabatt = 2

# gleichwertig mit elif
if lizenzen <= 10:
    rabatt = 0
elif lizenzen <= 20:
    rabatt = 1
else:
    rabatt = 2
```

## Mehrere einzelne `if` vs. `if/elif`
In [[rabatt.py]] stehen mehrere **unabhängige** `if`-Anweisungen hintereinander. Dann werden **alle** geprüft, und bei überlappenden Bereichen gewinnt die letzte, die zutrifft. Lücken zwischen den Bereichen fallen nicht auf. Bei einer Staffel deshalb immer eine `if/elif/else`-Kette **in aufsteigender Reihenfolge** nur mit der oberen Grenze verwenden. Dann gibt es weder Lücken noch Überschneidungen (siehe [[Übung Python Rabattstaffel]]).

> [!tip] Merke
> - Doppelpunkt `:` nach jeder Bedingung und nach `else`.
> - Einrückung gehört zur Syntax, nicht zur Optik.
> - Bei Staffeln (Rabatt, Prämie, Alter) **Grenzwerte testen**: genau 10, 11, 20, 21, ...

## Typische Fehler
> [!warning] Häufige Fehler
> - Doppelpunkt vergessen: `if lizenzen > 51` → `SyntaxError`.
> - `=` statt `==` in der Bedingung → `SyntaxError`.
> - Operator oder Zeichen nicht in Anführungszeichen: `if operation == *:` → `SyntaxError`, richtig: `if operation == "*":`.
> - Lücken oder Überschneidungen bei Grenzen (`<= 10` und `>= 10` gleichzeitig).
> - Die Zahl 0 vergessen: `if zahl > 0 ... else: "negativ"` behandelt 0 als negativ.

## Lernfragen
> [!question]- Wann wird ein `elif`-Zweig überhaupt geprüft?
> Nur wenn alle Bedingungen davor (`if` und frühere `elif`) falsch waren.

> [!question]- Was passiert bei drei einzelnen `if`-Anweisungen, deren Bedingungen sich überschneiden?
> Alle drei werden geprüft. Treffen mehrere zu, werden alle ausgeführt, und die letzte Zuweisung überschreibt die vorherigen.

> [!question]- Schreibe `x >= 20 and x < 40` kürzer.
> `20 <= x < 40`

> [!question]- Welche Grenzwerte testest du bei der Staffel „bis 10: 0 %, bis 20: 1 %, darüber 2 %“?
> 0 bzw. 1, 10, 11, 20, 21 und einen großen Wert. Dazu ungültige Eingaben wie negative Zahlen.

## Siehe auch
- [[Übung Python Altersprüfung]]
- [[Übung Python Prämienberechnung]]
- [[Übung Python Rabattstaffel]]
- [[Programmablaufplan und Flussdiagramm]]
- [[Python Grundlagen - Variablen, Datentypen, Ein- und Ausgabe]]
- [[LF5 - Übersicht]]
