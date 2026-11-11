---
tags: [berufsschule, lf5, python, übung, schleife]
fach: LF5
typ: übung
quelle: "[[quersumme.py]]"
datum: 2026-04-21
status: zu-lernen
---
# Übung Python Quersumme

> [!summary] Kurz & knapp
> Übung zu [[Python Schleifen for und while]]: Die Quersumme einer Zahl wird mit `while`, Modulo `%` und Division berechnet. Das Programm verwendet `/` statt `//` und liefert deshalb **falsche Ergebnisse**.

## Aufgabe (rekonstruiert)
Lies eine ganze Zahl ein und berechne ihre Quersumme (Summe aller Ziffern), z. B. 123 → 1 + 2 + 3 = 6.

## Eigene Lösung
```python
zahl = int(input("Gebe den Wert an: "))
quersumme = 0
letzte_ziffer = 0

while zahl > 0:
    letzte_ziffer = zahl % 10
    quersumme = quersumme + letzte_ziffer
    zahl = zahl / 10
    
print(int(quersumme))
```

## Idee
Die Idee ist richtig: `zahl % 10` holt die letzte Ziffer, danach wird die letzte Ziffer abgeschnitten, bis die Zahl 0 ist.

## Review
> [!warning] Korrektur
> `zahl = zahl / 10` ist eine **Kommadivision**: Aus 99 wird 9.9, dann 0.99, 0.099 und so weiter. Die Zahl wird nie genau 0, die Schleife läuft hunderte Male (bis die Kommazahl zu klein für den Rechner ist), und es werden Nachkommaanteile aufaddiert.
>
> | Eingabe | richtig | Programm gibt aus |
> | --- | --- | --- |
> | 123 | 6 | 6 (Zufallstreffer: 6,66… → `int` → 6) |
> | 19 | 10 | 11 |
> | 99 | 18 | 20 |
>
> Das `int()` am Ende versteckt den Fehler nur teilweise. Richtig ist die **ganzzahlige Division** `//`:
> ```python
> zahl = int(input("Zahl: "))
> quersumme = 0
>
> while zahl > 0:
>     quersumme += zahl % 10   # letzte Ziffer addieren
>     zahl = zahl // 10        # letzte Ziffer abschneiden
>
> print("Quersumme:", quersumme)
> ```
> `letzte_ziffer = 0` vor der Schleife ist nicht nötig, `int()` bei der Ausgabe dann auch nicht.

## Schreibtischtest (korrigiert, Eingabe 472)

| Durchlauf | `zahl % 10` | quersumme | zahl danach |
| --- | --- | --- | --- |
| 1 | 2 | 2 | 47 |
| 2 | 7 | 9 | 4 |
| 3 | 4 | 13 | 0 → Ende |

> [!tip] Merke
> Eine Prüfung mit nur einem Testwert reicht nicht. 123 liefert hier zufällig das richtige Ergebnis.

## Zum Selbsttest
> [!question]- Alternative Lösung ohne Rechnen, nur mit Strings?
> > [!success]- Lösung
> > ```python
> > text = input("Zahl: ")
> > quersumme = 0
> > for ziffer in text:
> >     quersumme += int(ziffer)
> > print(quersumme)
> > ```

## Siehe auch
- [[Python Schleifen for und while]]
- [[Python Grundlagen - Variablen, Datentypen, Ein- und Ausgabe]]
- [[Programmablaufplan und Flussdiagramm]]
- [[LF5 - Übersicht]]
