---
tags: [berufsschule, lf5, python, übung, liste]
fach: LF5
typ: übung
quelle: "[[liste.py]]"
datum: 2026-04-28
status: zu-lernen
---
# Übung Python Obstkorb-Liste

> [!summary] Kurz & knapp
> Übung zu [[Python Listen und Strings]]: Eine Obstliste wird verändert (`insert`, `sort`) und zweimal ausgegeben, einmal direkt und einmal über den Index, vorwärts und rückwärts nebeneinander.

## Aufgabe (rekonstruiert)
Lege eine Liste mit Obstsorten an. Füge Elemente hinzu bzw. entferne welche (per Eingabe), sortiere die Liste und gib sie als „Obstkorb“ aus. Gib die Liste zusätzlich über den Index aus.

## Eigene Lösung
```python
l = ["Apfel","Test","kiwi","orangen","papaya"]
#a = input("Was möchtest du hinzufügen? ")
#l.append(a)
l.insert(0, "Ananas")
#b = input("Was möchtest du entfernen? ")
#l.remove(b)
l.sort()
anzahl = len(l)

print("Obstkorb")
print("="*22)

for element in l:
    print(element)

print("="*22)
print("Liste über Index: ")

for i in range(anzahl):
    print(i, l[i], "\t\t", anzahl-i-1, l[anzahl-i-1])
```

## Ausgabe
```text
Obstkorb
======================
Ananas
Apfel
Test
kiwi
orangen
papaya
======================
Liste über Index: 
0 Ananas 		 5 papaya
1 Apfel 		 4 orangen
...
```
`anzahl - i - 1` läuft von 5 bis 0 und liefert damit die Liste **rückwärts**.

## Review
> [!tip] Verbesserung
> - **Sortierung:** „Test“ steht vor „kiwi“, weil Großbuchstaben vor Kleinbuchstaben sortiert werden. Einheitlich schreiben oder `l.sort(key=str.lower)` verwenden.
> - Der Variablenname `l` ist schlecht lesbar (leicht mit `1` zu verwechseln). Besser: `obstkorb`.
> - `l.remove(b)` (auskommentiert) bricht mit `ValueError` ab, wenn die Sorte nicht in der Liste ist. Vorher prüfen:
> ```python
> sorte = input("Was möchtest du entfernen? ")
> if sorte in obstkorb:
>     obstkorb.remove(sorte)
> else:
>     print(sorte, "ist nicht im Korb.")
> ```
> - Rückwärts geht auch mit `obstkorb[-1 - i]` oder `for obst in reversed(obstkorb):`.

## Zum Selbsttest
> [!question]- Was ist `l[anzahl-i-1]` für `i = 0`?
> Das letzte Element, gleichbedeutend mit `l[-1]`.

> [!question]- Was macht `"="*22`?
> Es wiederholt den String 22-mal und erzeugt so eine Trennlinie.

## Siehe auch
- [[Python Listen und Strings]]
- [[Python Schleifen for und while]]
- [[LF5 - Übersicht]]
