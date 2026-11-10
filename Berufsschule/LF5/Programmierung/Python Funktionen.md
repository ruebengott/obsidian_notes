---
tags: [berufsschule, lf5, python, programmierung, funktion]
fach: LF5
typ: thema
quelle: "[[Funktionen.py]]"
datum: 2026-05-05
status: zu-lernen
---
# Python Funktionen

> [!summary] Kurz & knapp
> Eine **Funktion** ist ein benannter, wiederverwendbarer Codeblock. Sie wird mit `def` **definiert** und später **aufgerufen**. Werte werden über **Parameter** übergeben, das Ergebnis mit `return` **zurückgegeben**. Erst der Aufruf führt den Code aus.

## Aufbau
```python
def addieren(zahl1, zahl2):      # Definition mit zwei Parametern
    ergebnis = zahl1 + zahl2
    return ergebnis               # Rückgabewert

summe = addieren(5, 3)           # Aufruf mit Argumenten 5 und 3
print(summe)                     # 8
```

| Begriff | Bedeutung |
| --- | --- |
| **Parameter** | Platzhalter in der Definition (`zahl1`, `zahl2`) |
| **Argument** | konkreter Wert beim Aufruf (`5`, `3`) |
| **Rückgabewert** | was `return` liefert. Ohne `return` liefert die Funktion `None` |
| **Hauptprogramm** | Code außerhalb der Funktionen, der sie aufruft |

## Mit und ohne Rückgabe
```python
def begruessung():            # ohne Parameter, ohne return
    print("Hallo")

def ist_positiv(zahl):        # mit return: Ergebnis kann weiterverwendet werden
    return zahl > 0

begruessung()
if ist_positiv(5):
    print("positiv")
```
Faustregel: Funktionen sollten lieber ein Ergebnis **zurückgeben** als selbst `print` aufzurufen. Dann kann das Hauptprogramm entscheiden, was damit passiert.

## Rückgabewert verwenden
```python
addition(5, 3)            # Ergebnis wird berechnet und verworfen, keine Ausgabe!
print(addition(5, 3))     # 8
erg = addition(5, 3)      # 8 in Variable speichern
```

## Gültigkeitsbereich (Scope)
Variablen, die **in** einer Funktion angelegt werden, sind **lokal**. Sie existieren nur während des Funktionsaufrufs. Eine globale Variable gleichen Namens (z. B. `summe = 0` vor der Funktion) wird dadurch **nicht** verändert.

> [!tip] Merke
> - `def name(parameter):` + eingerückter Block.
> - Definition allein tut nichts, erst der **Aufruf** `name(...)` führt aus.
> - `return` beendet die Funktion und liefert den Wert an den Aufrufer.
> - Ein Rückgabewert, der weder gespeichert noch ausgegeben wird, geht verloren.

## Typische Fehler
> [!warning] Häufige Fehler
> - Rückgabewert ignoriert (`addition(5, 3)` ohne `print`).
> - Klammern beim Aufruf vergessen: `begruessung` statt `begruessung()`.
> - Funktion **nach** dem Aufruf definiert → `NameError`.
> - Ergebnisvariablen nur in einem `if`-Zweig angelegt und dann alle ausgegeben → `NameError`, siehe [[Übung Python Rechner mit Funktionen]].

## Lernfragen
> [!question]- Was ist der Unterschied zwischen Parameter und Argument?
> Der Parameter ist der Name in der Funktionsdefinition, das Argument der konkrete Wert beim Aufruf.

> [!question]- Was gibt eine Funktion ohne `return` zurück?
> `None`.

> [!question]- Warum erscheint bei `addition(5, 3)` keine Ausgabe?
> Die Funktion gibt 8 zurück, aber der Wert wird weder ausgegeben noch gespeichert. Richtig: `print(addition(5, 3))`.

> [!question]- Wird die globale Variable `summe` verändert, wenn in einer Funktion `summe = a + b` steht?
> Nein. In der Funktion entsteht eine neue lokale Variable `summe`.

## Siehe auch
- [[Übung Python Rechner mit Funktionen]]
- [[Übung Python Grundaufgaben 16 bis 33]]
- [[Python Verzweigungen]]
- [[LF5 - Übersicht]]
