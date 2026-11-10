---
tags: [berufsschule, lf5, python, übung, string, liste]
fach: LF5
typ: übung
quelle: "[[übungsaufgaben_strinngs_arrays.py]]"
datum: 2026-05-25
status: zu-lernen
---
# Übung Python Strings und Listen

> [!summary] Kurz & knapp
> Kurze Aufgaben zu [[Python Listen und Strings]] aus [[übungsaufgaben_strinngs_arrays.py]]: Zugriff per Index, String-Methoden, Listenoperationen und `in`. Nummern 1 bis 7 und 16 bis 25. Nr. 8 bis 15 fehlen in der Datei.

## Strings (Nr. 1 bis 7)
Decke die Kommentare ab und überlege die Ausgabe.
```python
name = "Moritz"
print(name)               # 1: Moritz

text = "Hallo Welt"
print(text[0])            # 2: H
print(text[-1])           # 3: t

l_essen = "Pizza"
print(len(l_essen))       # 4: 5

print(text.upper())       # 5: HALLO WELT
print(text.lower())       # 6: hallo welt
print(text.find("Python"))  # 7: -1
```
> [!info] Nr. 7
> `find()` liefert den Startindex des Suchtexts. „Python“ kommt in „Hallo Welt“ nicht vor, daher **-1**. Vermutlich sollte man genau das herausfinden. `text.find("Welt")` ergäbe 6.

## Listen (Nr. 16 bis 25)
```python
liste = ["rot", "grün", "blau"]   # 16
print(liste[0])                   # 17: rot
print(liste[-1])                  # 18: blau
liste.append("gelb")
print(liste)                      # 19: ['rot', 'grün', 'blau', 'gelb']
liste.remove("gelb")
print(liste)                      # 20: ['rot', 'grün', 'blau']
liste[1] = "türkis"
print(liste)                      # 21: ['rot', 'türkis', 'blau']
print(len(liste))                 # 22: 3
for i in liste:                   # 23: rot / türkis / blau
    print(i)

summe = 0                         # 24
zahlen = [3,3,4,3]
for i in zahlen:
    summe = summe+i
print(summe)                      # 13

if "rosa" in liste:               # 25
    print("true")
else:
    print("false")                # false
```

## Review
> [!tip] Verbesserung
> - **Nr. 24:** Kürzer mit `print(sum(zahlen))`.
> - **Nr. 25:** `"rosa" in liste` ist bereits ein Wahrheitswert: `print("rosa" in liste)` gibt `False` aus. Die Strings `"true"`/`"false"` sind nicht dasselbe wie die Python-Werte `True`/`False`.
> - Variablennamen: `i` ist üblich für Indizes. Für Elemente ist ein sprechender Name besser: `for farbe in liste:`.
> - Dateiname mit Tippfehler: „strinngs“.

## Zum Selbsttest
> [!question]- Was gibt `print(text[6:])` aus?
> `Welt`

> [!question]- Was passiert bei `liste.remove("gelb")`, wenn „gelb“ nicht enthalten ist?
> `ValueError: list.remove(x): x not in list`.

## Siehe auch
- [[Python Listen und Strings]]
- [[Übung Python Grundaufgaben 16 bis 33]]
- [[LF5 - Übersicht]]
