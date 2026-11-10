---
tags: [berufsschule, lf5, python, übung, verzweigung]
fach: LF5
typ: übung
quelle: "[[prämienberechnung.py]]"
datum: 2026-03-24
status: zu-lernen
---
# Übung Python Prämienberechnung

> [!summary] Kurz & knapp
> Übung zu [[Python Verzweigungen]]: Eine Prämie wird nach Beschäftigungsdauer gestaffelt. Das Programm hat einen **Laufzeitfehler** im letzten Zweig (`NameError`).

## Aufgabe (rekonstruiert aus dem Code)
Ein Mitarbeiter gibt seine Beschäftigungsdauer in Jahren ein. Die Prämie beträgt:

| Beschäftigungsdauer | Prämie |
| --- | --- |
| unter 1 Jahr | 0 € |
| 1 bis unter 2 Jahre | 50 € |
| 2 bis unter 4 Jahre | 100 € |
| ab 4 Jahren | 150 € + 10 € für jedes Jahr über 4 |

## Eigene Lösung
```python
duration= input("Gebe deine Beschäftigungsdauer ein: ")
int_duration = int(duration)

if int_duration < 1:
    prämie = 0
else:
    if int_duration < 2:
        prämie = 50
    else:
        if int_duration < 4:
            prämie = 100
        else:
            prämie = 150 + 10* (prämie-4)

print("Deine Prämie ist: ", prämie)
```

## Review
> [!warning] Korrektur
> In der Zeile `prämie = 150 + 10* (prämie-4)` wird `prämie` benutzt, **bevor** die Variable einen Wert hat. Bei einer Eingabe ab 4 bricht das Programm mit `NameError: name 'prämie' is not defined` ab. Gemeint ist die Beschäftigungsdauer:
> ```python
> prämie = 150 + 10 * (int_duration - 4)
> ```
> Die Fälle 0 bis 3 Jahre funktionieren, deshalb fällt der Fehler nur auf, wenn man die **höchste Stufe testet**.

> [!tip] Verbesserung
> ```python
> jahre = int(input("Beschäftigungsdauer in Jahren: "))
>
> if jahre < 1:
>     praemie = 0
> elif jahre < 2:
>     praemie = 50
> elif jahre < 4:
>     praemie = 100
> else:
>     praemie = 150 + 10 * (jahre - 4)
>
> print(f"Deine Prämie beträgt {praemie} €.")
> ```
> `elif` statt Verschachtelung, Einheit in der Ausgabe, keine Umlaute im Variablennamen.

## Zum Selbsttest
> [!question]- Welche Prämie ergibt sich (korrigiert) bei 4, 7 und 1 Jahr?
> 4 Jahre: 150 €. 7 Jahre: 150 + 10 · 3 = 180 €. 1 Jahr: 50 €.

> [!question]- Mit welchen Eingaben hättest du den Fehler gefunden?
> Mit Grenzwerten aller Stufen: 0, 1, 2, 3, 4, 5. Spätestens 4 löst den `NameError` aus.

## Siehe auch
- [[Python Verzweigungen]]
- [[Python Grundlagen - Variablen, Datentypen, Ein- und Ausgabe]]
- [[LF5 - Übersicht]]
