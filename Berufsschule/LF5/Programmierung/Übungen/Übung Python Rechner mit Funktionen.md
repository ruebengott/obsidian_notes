---
tags: [berufsschule, lf5, python, übung, funktion]
fach: LF5
typ: übung
quelle: "[[Funktionen.py]]"
datum: 2026-05-05
status: zu-lernen
---
# Übung Python Rechner mit Funktionen

> [!summary] Kurz & knapp
> Übung zu [[Python Funktionen]]: Ein Taschenrechner mit je einer Funktion für die vier Grundrechenarten. Die Funktionen sind richtig, das **Hauptprogramm ist nicht lauffähig** (Syntaxfehler, fehlende Eingabe, `NameError` bei der Ausgabe).

## Aufgabe (rekonstruiert)
Schreibe ein Rechenprogramm mit den Funktionen `multiplizieren`, `dividieren`, `addieren` und `subtrahieren` (jeweils zwei Parameter, Rückgabe des Ergebnisses). Das Hauptprogramm liest zwei Zahlen und die gewünschte Rechenart ein und gibt das Ergebnis aus.

## Eigene Lösung
```python
#Rechenprogram mit Funktionen

#Funktion multiplizieren mit den Parametern zahl1 und zahl2
def multiplizieren(zahl1,zahl2):
    ergebnis = zahl1 * zahl2
    return ergebnis

def divideren(zahl1,zahl2):
    ergebnis = zahl1 / zahl2
    return ergebnis

def addieren(zahl1,zahl2):
    ergebnis = zahl1 + zahl2
    return ergebnis

def subtrahieren(zahl1,zahl2):
    ergebnis = zahl1 - zahl2
    return ergebnis


#Hauptprogramm
a = int(input("Zahl 1: "))
operation = "Welche Operation?"
b = int(input("Zahl 2: "))

if operation == *:
    funktionsergebnis1 = multiplizieren(a, b)
if operation == /:
    funktionsergebnis2 = divideren(a, b)

if operation == +:
    funktionsergebnis3 = addieren(a, b)
    
if operation == -:
    funktionsergebnis4 = subtrahieren(a, b)

#Ausgabe
print("Ergebnis der Multiplikation: ", funktionsergebnis1)
print("Ergebnis der Division: ", funktionsergebnis2)
print("Ergebnis der Addition: ", funktionsergebnis3)
print("Ergebnis der Subtraktion: ", funktionsergebnis4)
```

## Review
> [!warning] Korrektur
> 1. **Keine Eingabe der Operation:** `operation = "Welche Operation?"` weist nur den Fragetext zu. Richtig: `operation = input("Welche Operation (+ - * /)? ")`.
> 2. **Syntaxfehler:** `if operation == *:` – das Rechenzeichen ist ein String und muss in Anführungszeichen stehen: `"*"`. So startet das Programm gar nicht.
> 3. **`NameError` bei der Ausgabe:** Es wird nur **eine** der vier Variablen `funktionsergebnis1..4` angelegt, ausgegeben werden aber alle vier. Besser **eine** Variable `ergebnis` und **eine** Ausgabe.
> 4. **Division durch 0** führt zu `ZeroDivisionError`.
> 5. Tippfehler im Funktionsnamen: `divideren` → `dividieren`.
>
> ```python
> def multiplizieren(zahl1, zahl2):
>     return zahl1 * zahl2
>
> def dividieren(zahl1, zahl2):
>     return zahl1 / zahl2
>
> def addieren(zahl1, zahl2):
>     return zahl1 + zahl2
>
> def subtrahieren(zahl1, zahl2):
>     return zahl1 - zahl2
>
>
> # Hauptprogramm
> a = float(input("Zahl 1: "))
> operation = input("Welche Operation (+ - * /)? ")
> b = float(input("Zahl 2: "))
>
> if operation == "*":
>     print("Ergebnis:", multiplizieren(a, b))
> elif operation == "/":
>     if b == 0:
>         print("Division durch 0 ist nicht möglich.")
>     else:
>         print("Ergebnis:", dividieren(a, b))
> elif operation == "+":
>     print("Ergebnis:", addieren(a, b))
> elif operation == "-":
>     print("Ergebnis:", subtrahieren(a, b))
> else:
>     print("Unbekannte Operation:", operation)
> ```

> [!tip] Verbesserung
> - Die Hilfsvariable `ergebnis` in jeder Funktion ist erlaubt, `return zahl1 * zahl2` ist aber kürzer.
> - `float(input(...))` erlaubt auch Kommazahlen (Eingabe mit Punkt: `2.5`).

## Zum Selbsttest
> [!question]- Warum ist `if operation == *:` ein Syntaxfehler, `if operation == "*":` aber nicht?
> Ohne Anführungszeichen ist `*` der Multiplikationsoperator und braucht zwei Operanden. Mit Anführungszeichen ist es ein String, der mit dem Inhalt von `operation` verglichen wird.

> [!question]- Was passiert, wenn man `+` wählt und alle vier `print`-Zeilen stehen lässt?
> Bei `print(..., funktionsergebnis1)` bricht das Programm mit `NameError` ab, weil `funktionsergebnis1` nie angelegt wurde.

## Siehe auch
- [[Python Funktionen]]
- [[Python Verzweigungen]]
- [[LF5 - Übersicht]]
