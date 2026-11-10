---
tags: [berufsschule, lf5, python, programmierung, liste, string]
fach: LF5
typ: thema
quelle: "[[übungsaufgaben_strinngs_arrays.py]]"
datum: 2026-05-25
status: zu-lernen
---
# Python Listen und Strings

> [!summary] Kurz & knapp
> Eine **Liste** (`list`, in anderen Sprachen „Array“) speichert mehrere Werte in fester Reihenfolge und ist **veränderbar**. Ein **String** ist eine Zeichenkette und **nicht** veränderbar. Beide werden über einen **Index ab 0** angesprochen, negative Indizes zählen von hinten.

## Index
```python
text = "Hallo Welt"
liste = ["rot", "grün", "blau"]

text[0]      # 'H'      erstes Zeichen
text[-1]     # 't'      letztes Zeichen
liste[0]     # 'rot'
liste[-1]    # 'blau'
len(liste)   # 3        letzter gültiger Index ist len - 1 = 2
```

| Index | 0 | 1 | 2 |
| --- | --- | --- | --- |
| Wert | rot | grün | blau |
| negativ | -3 | -2 | -1 |

## Listen-Operationen

| Befehl | Wirkung |
| --- | --- |
| `liste.append("gelb")` | hängt am **Ende** an |
| `liste.insert(0, "Ananas")` | fügt an Position 0 ein |
| `liste.remove("gelb")` | entfernt das **erste** Vorkommen (Fehler, wenn nicht vorhanden) |
| `liste.pop()` | entfernt das letzte Element und gibt es zurück |
| `liste[1] = "türkis"` | Element überschreiben |
| `liste.sort()` | sortiert die Liste selbst (aufsteigend) |
| `len(liste)` | Anzahl der Elemente |
| `"rosa" in liste` | `True`/`False`: enthalten? |
| `sum(zahlen)`, `max(zahlen)` | Summe, Maximum einer Zahlenliste |

## Durchlaufen
```python
for farbe in liste:                 # direkt über die Elemente
    print(farbe)

for i in range(len(liste)):         # über den Index
    print(i, liste[i])
```

## String-Operationen

| Befehl | Ergebnis für `"Hallo Welt"` |
| --- | --- |
| `len(text)` | `10` |
| `text.upper()` | `'HALLO WELT'` |
| `text.lower()` | `'hallo welt'` |
| `text.find("Welt")` | `6` (Startindex) |
| `text.find("Python")` | `-1` (nicht gefunden) |
| `"Welt" in text` | `True` |
| `text.replace("Welt", "Python")` | `'Hallo Python'` (neuer String) |
| `text[0:5]` | `'Hallo'` (Slicing, Ende exklusiv) |

> [!tip] Merke
> - Index beginnt bei **0**, `[-1]` ist das letzte Element.
> - `sort()` sortiert **Groß- vor Kleinbuchstaben** (`"Test"` vor `"kiwi"`). Ohne Rücksicht auf Groß-/Kleinschreibung: `liste.sort(key=str.lower)`.
> - String-Methoden wie `upper()` ändern den String nicht, sie liefern einen **neuen** String.

## Typische Fehler
> [!warning] Häufige Fehler
> - `liste[len(liste)]` → `IndexError`, der letzte Index ist `len - 1`.
> - `liste.remove(x)`, obwohl `x` nicht enthalten ist → `ValueError`. Vorher mit `if x in liste:` prüfen.
> - `find()` liefert bei Misserfolg `-1` und keinen Fehler. `-1` ist aber auch ein gültiger Index, das führt leicht zu Folgefehlern.
> - `liste = liste.sort()` → `liste` ist danach `None`, weil `sort()` nichts zurückgibt.

## Lernfragen
> [!question]- Was liefert `"Pizza"[-2]`?
> `'z'`

> [!question]- Unterschied zwischen `append` und `insert`?
> `append(x)` hängt am Ende an, `insert(i, x)` fügt an Index `i` ein und verschiebt die folgenden Elemente.

> [!question]- Warum steht nach `sort()` „Test“ vor „kiwi“?
> Python sortiert nach Zeichencode. Großbuchstaben haben kleinere Codes als Kleinbuchstaben.

> [!question]- Wie prüfst du, ob „rosa“ in der Liste ist, und was wird ausgegeben, wenn nicht?
> `print("rosa" in liste)` gibt `False` aus.

## Siehe auch
- [[Übung Python Strings und Listen]]
- [[Übung Python Obstkorb-Liste]]
- [[Übung Python Solarertrag]]
- [[Python Schleifen for und while]]
- [[LF5 - Übersicht]]
