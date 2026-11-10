---
tags: [berufsschule, lf5, python, programmierung, schleife]
fach: LF5
typ: thema
quelle: "[[for schleife summe.py]]"
datum: 2026-04-28
status: zu-lernen
---
# Python Schleifen for und while

> [!summary] Kurz & knapp
> Schleifen wiederholen Code. Die **`for`-Schleife** läuft über eine bekannte Folge (Zahlenbereich mit `range()`, Liste, String). Die **`while`-Schleife** läuft, **solange** eine Bedingung wahr ist. Man nimmt sie, wenn die Anzahl der Durchläufe vorher nicht feststeht.

## for-Schleife und range()
```python
for i in range(5):        # 0, 1, 2, 3, 4
    print(i + 1)          # gibt 1 bis 5 aus

for i in range(1, 11):    # 1 bis 10 (Ende ist exklusiv!)
    summe += i
```

| Aufruf | erzeugt |
| --- | --- |
| `range(5)` | 0, 1, 2, 3, 4 |
| `range(1, 6)` | 1, 2, 3, 4, 5 |
| `range(0, 10, 2)` | 0, 2, 4, 6, 8 |
| `range(5, 0, -1)` | 5, 4, 3, 2, 1 |

Über eine Liste direkt iterieren:
```python
ertraege = [340, 200, 500]
for tagertrag in ertraege:
    print(tagertrag)
```

## while-Schleife
```python
summe = 0
zahl = 0
while summe <= 100:       # Bedingung wird VOR jedem Durchlauf geprüft
    zahl = zahl + 1
    summe = summe + zahl
print(zahl)               # 14
```
Die Bedingung muss sich im Schleifenkörper irgendwann ändern, sonst entsteht eine **Endlosschleife**. Ist die Bedingung schon zu Beginn falsch (z. B. `while False:`), läuft die Schleife **kein einziges Mal** (kopfgesteuerte Schleife).

## Akkumulator-Muster (Summe, Produkt, Zähler)
Fast alle Übungen nutzen dasselbe Muster:
```python
summe = 0          # Startwert für Summe: 0
produkt = 1        # Startwert für Produkt: 1 (nicht 0!)
for zahl in range(1, ende + 1):
    summe += zahl
    produkt *= zahl
```

## Schreibtischtest (Trace-Tabelle)
Um `while`-Aufgaben ohne Computer zu lösen, schreibt man die Variablen nach jedem Durchlauf in eine Tabelle. Beispiel aus [[while b).py]] (`a = 10`, `b = 20`, `while b > 5: b -= 5; a += 2`):

| Durchlauf | b | a | Bedingung danach `b > 5` |
| --- | --- | --- | --- |
| Start | 20 | 10 | wahr |
| 1 | 15 | 12 | wahr |
| 2 | 10 | 14 | wahr |
| 3 | 5 | 16 | **falsch** → Ende |

Ausgabe: `16`.

## for oder while?

| Situation | Schleife |
| --- | --- |
| Anzahl der Durchläufe bekannt (1 bis n, jedes Listenelement) | `for` |
| Wiederholen, bis etwas eintritt (Summe > 100, Zahl = 0, richtige Eingabe) | `while` |

> [!tip] Merke
> - `range(a, b)` endet **vor** `b`.
> - Startwert für Summen `0`, für Produkte `1`.
> - In der `while`-Schleife muss sich die Bedingung ändern.
> - `break` beendet eine Schleife sofort, `continue` springt zum nächsten Durchlauf.

## Typische Fehler
> [!warning] Häufige Fehler
> - **Off-by-one:** `range(ende)` statt `range(1, ende + 1)`.
> - **Endlosschleife:** Zählvariable wird nicht verändert.
> - **Unnötiges `if` in der Schleife:** `for ele in range(ende+1): if ele > 0:` → besser gleich `range(1, ende + 1)`.
> - **Falsche Einrückung:** `print` innerhalb statt nach der Schleife gibt jeden Zwischenstand aus.

## Lernfragen
> [!question]- Welche Zahlen erzeugt `range(2, 8, 2)`?
> 2, 4, 6

> [!question]- Wie oft wird `print("Hello world")` in `while (False): ...` ausgeführt?
> Gar nicht. Die Bedingung ist von Anfang an falsch, der Schleifenkörper wird übersprungen.

> [!question]- Warum startet ein Produkt-Akkumulator mit 1?
> Weil jede Multiplikation mit 0 wieder 0 ergibt. 1 ist das neutrale Element der Multiplikation.

> [!question]- Wann ist `while` besser geeignet als `for`?
> Wenn vorher nicht feststeht, wie oft wiederholt wird, z. B. „addiere, bis die Summe über 100 liegt“ oder „teile, bis die Zahl 0 ist“.

## Siehe auch
- [[Übung Python Summe und Produkt mit for]]
- [[Übung Python while-Schleifen nachvollziehen]]
- [[Übung Python Quersumme]]
- [[Übung Python Solarertrag]]
- [[Python Listen und Strings]]
- [[Programmablaufplan und Flussdiagramm]]
- [[LF5 - Übersicht]]
