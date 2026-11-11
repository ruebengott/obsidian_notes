---
tags: [berufsschule, lf5, python, übung, schleife]
fach: LF5
typ: übung
quelle: "[[for schleife summe.py]]"
datum: 2026-04-28
status: zu-lernen
---
# Übung Python Summe und Produkt mit for

> [!summary] Kurz & knapp
> Übung zu [[Python Schleifen for und while]]: Für die Zahlen 1 bis n werden Summe und Produkt (Fakultät n!) berechnet. Das Programm ist korrekt. Der Umweg über `if ele > 0` lässt sich mit dem passenden `range` vermeiden.

## Aufgabe (rekonstruiert)
Lies eine Endzahl `ende` ein. Gib alle Zahlen von 1 bis `ende` aus und berechne ihre Summe und ihr Produkt.

## Eigene Lösung
```python
#Programm zur Berechnung einer Zahlenfolge von 1 bis ende
ende = int(input("Bitte Reihenfolge eingeben: "))
zahlensumme = 0
zahlenprodukt = 1
for ele in range(ende+1):
    if (ele>0):
        print(ele)
        zahlensumme = zahlensumme + ele
        zahlenprodukt = zahlenprodukt * ele
        
print("Zahlensumme:", zahlensumme)
print("Zahlenprodukt:", zahlenprodukt)
```

## Erklärung
- `range(ende+1)` erzeugt 0 bis `ende`. Die 0 wird mit `if ele > 0` übersprungen, sonst wäre das Produkt 0.
- Startwerte richtig gewählt: Summe 0, Produkt 1.
- Beispiel `ende = 5`: Summe 15, Produkt 120.

## Review
> [!tip] Verbesserung
> - `range(1, ende + 1)` startet direkt bei 1, das `if` entfällt.
> - Klammern um die Bedingung `(ele>0)` sind in Python unnötig.
> - Der Eingabetext „Reihenfolge“ ist irreführend, gemeint ist die Endzahl.
> ```python
> ende = int(input("Bis zu welcher Zahl? "))
> summe = 0
> produkt = 1
> for zahl in range(1, ende + 1):
>     print(zahl)
>     summe += zahl
>     produkt *= zahl
>
> print("Summe:", summe)
> print("Produkt:", produkt)
> ```
> Kontrolle der Summe mit der Gauß-Formel: `ende * (ende + 1) // 2`.

## Zum Selbsttest
> [!question]- Was wäre das Produkt, wenn man das `if ele > 0` weglässt?
> 0, weil die erste Multiplikation `1 * 0` ergibt.

> [!question]- Ergebnis für `ende = 4`?
> Summe 10, Produkt 24.

## Siehe auch
- [[Python Schleifen for und while]]
- [[LF5 - Übersicht]]
