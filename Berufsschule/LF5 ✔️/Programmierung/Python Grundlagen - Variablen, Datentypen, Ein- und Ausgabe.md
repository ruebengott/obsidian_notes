---
tags: [berufsschule, lf5, python, programmierung]
fach: LF5
typ: thema
quelle: "[[altersprüfung.py]]"
datum: 2026-03-24
status: zu-lernen
---
# Python Grundlagen - Variablen, Datentypen, Ein- und Ausgabe

> [!summary] Kurz & knapp
> Ein Python-Programm folgt dem **EVA-Prinzip**: **E**ingabe mit `input()`, **V**erarbeitung mit Variablen und Operatoren, **A**usgabe mit `print()`. `input()` liefert immer einen **String**. Zum Rechnen muss er mit `int()` oder `float()` umgewandelt werden.

## EVA-Prinzip im Programm
In den eigenen Skripten (z. B. [[rabatt.py]]) sind die Abschnitte mit Kommentaren `#E`, `#V`, `#A` markiert:

```python
# E – Eingabe
lizenzen = int(input("Wie viele Lizenzen? "))

# V – Verarbeitung
preis = lizenzen * 49.90

# A – Ausgabe
print("Gesamtpreis:", preis, "€")
```

## Variablen
- Eine Variable ist ein **Name für einen Wert**: `zahl = 30`. Das `=` ist eine **Zuweisung**, kein Vergleich.
- Python ist **dynamisch typisiert**: Man schreibt keinen Datentyp hin, der Typ ergibt sich aus dem Wert.
- Namen: Kleinbuchstaben, Wörter mit `_` trennen (`ertrag_gesamt`). Keine Leerzeichen, nicht mit Ziffer beginnen. Umlaute (`prämie`) sind erlaubt, aber besser vermeiden.
- `zahlensumme = zahlensumme + ele` kann man kürzer als `zahlensumme += ele` schreiben.

## Datentypen

| Typ | Bedeutung | Beispiel |
| --- | --- | --- |
| `int` | ganze Zahl | `18`, `-3` |
| `float` | Kommazahl (mit **Punkt**) | `18.90`, `2.163` |
| `str` | Zeichenkette (String) | `"Hallo Welt"` |
| `bool` | Wahrheitswert | `True`, `False` |
| `list` | Liste, siehe [[Python Listen und Strings]] | `["rot", "blau"]` |

Mit `type(x)` kann man den Typ prüfen. Umwandeln (**Typkonvertierung, Casting**): `int("18")` → `18`, `float("2.5")` → `2.5`, `str(18)` → `"18"`.

## Operatoren

| Operator | Bedeutung | Beispiel | Ergebnis |
| --- | --- | --- | --- |
| `+ - *` | Grundrechenarten | `3 * 4` | `12` |
| `/` | Division, **immer float** | `123 / 10` | `12.3` |
| `//` | ganzzahlige Division | `123 // 10` | `12` |
| `%` | Modulo (Rest) | `123 % 10` | `3` |
| `**` | Potenz | `2 ** 3` | `8` |

> [!tip] Merke
> `zahl % 10` liefert die **letzte Ziffer**, `zahl // 10` **entfernt** die letzte Ziffer. `zahl % 2 == 0` prüft, ob eine Zahl **gerade** ist.

## Eingabe und Ausgabe
```python
alter = int(input("Bitte Alter eingeben: "))   # Eingabe -> String -> int
print("Du bist", alter, "Jahre alt.")          # Komma setzt ein Leerzeichen
print(f"Du bist {alter} Jahre alt.")           # f-String, übersichtlicher
print("=" * 22)                                # String wiederholen: 22 Gleichheitszeichen
```

## Kommentare
`# ...` ist ein Kommentar und wird nicht ausgeführt. Man kann damit auch Code vorübergehend „auskommentieren“ (so in [[übungsaufgaben_python.py]] bei den Aufgaben mit `input`).

## Typische Fehler
> [!warning] Häufige Fehler
> - **`input` nicht umgewandelt:** `alter = input(...)` und dann `alter >= 18` → `TypeError`, weil String mit Zahl verglichen wird.
> - **`/` statt `//`:** `zahl / 10` liefert eine Kommazahl, siehe [[Übung Python Quersumme]].
> - **Variable vor der Zuweisung benutzt** → `NameError`, siehe [[Übung Python Prämienberechnung]].
> - **Ungültige Eingabe:** `int("abc")` → `ValueError`. Abfangen mit `try/except` (fortgeschritten).
> - **Komma statt Punkt** bei Kommazahlen: `18,90` ist in Python ein Tupel, nicht 18.9.

## Lernfragen
> [!question]- Welchen Datentyp liefert `input()` immer?
> Einen String (`str`). Zum Rechnen muss man ihn mit `int()` oder `float()` umwandeln.

> [!question]- Was ergeben `17 / 5`, `17 // 5` und `17 % 5`?
> `3.4`, `3` und `2`.

> [!question]- Wofür steht EVA?
> Eingabe, Verarbeitung, Ausgabe. Das ist die Grundstruktur fast jedes einfachen Programms.

> [!question]- Was ist der Unterschied zwischen `=` und `==`?
> `=` weist einer Variablen einen Wert zu. `==` vergleicht zwei Werte und liefert `True` oder `False`.

## Siehe auch
- [[Python Verzweigungen]]
- [[Python Schleifen for und while]]
- [[Programmablaufplan und Flussdiagramm]]
- [[LF5 - Übersicht]]
