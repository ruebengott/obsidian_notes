---
tags: [berufsschule, lf5, python, übung]
fach: LF5
typ: übung
quelle: "[[übungsaufgaben_python.py]]"
datum: 2026-05-25
status: zu-lernen
---
# Übung Python Grundaufgaben 16 bis 33

> [!summary] Kurz & knapp
> Sammlung kurzer Wiederholungsaufgaben (Nr. 16 bis 33) zu Verzweigungen, Schleifen, Listen und Funktionen aus [[übungsaufgaben_python.py]]. Die Aufgabentexte sind aus dem Code rekonstruiert. Nr. 24, 25 und 32 fehlen in der Datei.

## Verzweigungen
**16.** Prüfe, ob `zahl` größer als 10 ist.
**17.** Prüfe, ob `zahl` durch 2 teilbar ist.
```python
zahl = 30
if zahl > 10:
    print("Zahl ist größer als 10.")

if zahl % 2 == 0:
    print("Zahl ist durch 2 teilbar.")
else:
    print("Nicht durch 2 teilbar.")
```

**18.** Alter einlesen, volljährig ja/nein. **19.** Passwortabfrage (`python123`). Beide sind in der Datei auskommentiert, damit beim Ausführen keine Eingabe nötig ist:
```python
alter = int(input("Wie ist dein Alter?"))
if alter >= 18:
    print("Du bist volljährig")
else:
    print("Du bist leider noch minderjährig")

eingabe = str(input("Wie lautet das Passwort?: "))
if eingabe == "python123":
    print("Zugriff erlaubt.")
else:
    print("Zugriff verweigert.")
```
> [!tip] Verbesserung
> `str(input(...))` ist doppelt gemoppelt, `input()` liefert bereits einen String.

## Schleifen
**20.** Zahlen 1 bis 5 ausgeben. **21.** Fünfmal „Hallo“. **22.** Summe 1 bis 10. **23.** Countdown mit `while`.
```python
for i in range(5):
    print(i+1)

for i in range(5):
    print("Hallo")

summe = 0
for i in range(1,11):
    summe += i
print(summe)          # 55

zahl = 4
while zahl > 1:
    zahl = zahl - 1
    print(zahl)       # 3, 2, 1
```
> [!tip] Verbesserung
> Bei 20 ist `for i in range(1, 6): print(i)` direkter. Bei 21 wird `i` nicht gebraucht, dafür schreibt man üblicherweise `_`: `for _ in range(5):`.

## Listen
**26.** Liste anlegen. **27.** Erstes Element. **28.** Element anhängen. **29.** Alle Elemente ausgeben.
```python
liste = ["rot", "blau", "lila"]
print(liste[0])         # rot
liste.append("rosa")
print(liste)            # ['rot', 'blau', 'lila', 'rosa']
for i in liste:
    print(i)
```

## Funktionen
**30.** Funktion ohne Parameter. **31.** Funktion `addition(a, b)`. **33.** Funktion, die prüft, ob eine Zahl positiv ist.
```python
def begruessung():
    print("Hallo")

begruessung()

summe = 0
def addition(a,b):
    summe = a+b
    return summe

addition(5,3)

def positiv(zahl):
    if zahl > 0:
        print("Die Zahl:", zahl ,"ist positiv.")
    else:
        print("Zahl ist negativ")

positiv(int(input("Welche Zahl möchtest du prüfen?")))
```

> [!warning] Korrektur
> - **Nr. 31:** `addition(5,3)` berechnet 8, aber das Ergebnis wird **verworfen**, es erscheint keine Ausgabe. Richtig: `print(addition(5, 3))`. Das globale `summe = 0` ist überflüssig, die `summe` in der Funktion ist eine **eigene lokale** Variable.
> - **Nr. 33:** Die Zahl **0** wird als „negativ“ gemeldet. 0 ist weder positiv noch negativ:
> ```python
> def positiv(zahl):
>     if zahl > 0:
>         print("Die Zahl", zahl, "ist positiv.")
>     elif zahl < 0:
>         print("Die Zahl", zahl, "ist negativ.")
>     else:
>         print("Die Zahl ist 0.")
> ```

## Zum Selbsttest
> [!question]- Was gibt Nr. 23 aus, wenn `zahl = 1` ist?
> Nichts. `1 > 1` ist falsch, die Schleife läuft nicht.

> [!question]- Schreibe Nr. 22 mit `while`.
> > [!success]- Lösung
> > ```python
> > summe = 0
> > i = 1
> > while i <= 10:
> >     summe += i
> >     i += 1
> > print(summe)
> > ```

## Siehe auch
- [[Python Verzweigungen]]
- [[Python Schleifen for und while]]
- [[Python Funktionen]]
- [[Übung Python Strings und Listen]]
- [[LF5 - Übersicht]]
