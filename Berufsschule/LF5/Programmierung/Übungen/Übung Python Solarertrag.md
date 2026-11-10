---
tags: [berufsschule, lf5, python, übung, schleife, liste]
fach: LF5
typ: übung
quelle: "[[solarertrag.py]]"
datum: 2026-04-28
status: zu-lernen
---
# Übung Python Solarertrag

> [!summary] Kurz & knapp
> Übung zu Listen und `for`-Schleifen: Die Tageserträge einer Solaranlage (in Wh) für eine Woche stehen in einer Liste. Das Programm summiert sie und gibt den Wochenertrag aus, ab 1000 Wh in kWh. Es funktioniert, bei der Ausgabe fehlen aber Einheiten.

## Aufgabe (rekonstruiert)
Gegeben sind die Tageserträge einer Woche in Wh. Berechne den Gesamtertrag. Ist er größer als 1000 Wh, gib ihn in kWh aus.

## Eigene Lösung
```python
#Tagesertrag in Wh
ertraege = [340, 200, 500, 80, 566, 242, 235]

ertrag_gesamt = 0
ertrag_gesamt_k = 0
for tagertrag in ertraege:
    ertrag_gesamt = ertrag_gesamt + tagertrag

if ertrag_gesamt > 1000:
    ertrag_gesamt_k = ertrag_gesamt / 1000
    print("Gesamtertrag in der Woche: ", ertrag_gesamt_k, "KWh")
else:
    print("Gesamtertrag in der Woche: ", ertrag_gesamt)
```

## Erklärung
- Akkumulator `ertrag_gesamt` startet bei 0, die `for`-Schleife addiert jeden Tageswert.
- Summe: 340 + 200 + 500 + 80 + 566 + 242 + 235 = **2163 Wh** → Ausgabe `2.163 KWh`.

## Review
> [!tip] Verbesserung
> - Im `else`-Zweig fehlt die Einheit **Wh**.
> - Die Einheit heißt **kWh** (kleines k für Kilo).
> - `ertrag_gesamt_k = 0` vorab ist überflüssig.
> - Python kann Listen direkt summieren: `sum(ertraege)`.
> ```python
> ertraege = [340, 200, 500, 80, 566, 242, 235]   # Wh pro Tag
> gesamt = sum(ertraege)
>
> if gesamt > 1000:
>     print(f"Gesamtertrag in der Woche: {gesamt / 1000:.2f} kWh")
> else:
>     print(f"Gesamtertrag in der Woche: {gesamt} Wh")
> ```
> `:.2f` rundet die Ausgabe auf zwei Nachkommastellen (2.16 kWh).

## Zum Selbsttest
> [!question]- Erweitere das Programm um den besten Tag und den Durchschnitt.
> > [!success]- Lösung
> > ```python
> > print("Bester Tag:", max(ertraege), "Wh")
> > print("Durchschnitt:", round(sum(ertraege) / len(ertraege), 1), "Wh")
> > ```
> > Ergebnis: 566 Wh und 309.0 Wh.

## Siehe auch
- [[Python Listen und Strings]]
- [[Python Schleifen for und while]]
- [[LF5 - Übersicht]]
