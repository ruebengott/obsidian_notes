---
tags: [berufsschule, lf2, elektrotechnik, übung]
fach: LF2
typ: übung
quelle: "[[LF2.pdf#page=52]]"
datum:
status: zu-lernen
---
# Übung - Stromkreisplanung im Rechenzentrum

> [!summary] Kurz & knapp
> IT-Übungsaufgabe 5: Prüfen, ob ein mit 16 A abgesicherter Stromkreis die geplanten Geräte tragen kann.

## Aufgabe
Ein Stromkreis ist mit **16 A bei 230 V** abgesichert. Angeschlossen werden sollen:
- 5 Server à 350 W
- 2 Switches à 120 W
- 1 USV mit Eigenverbrauch 100 W

a) Berechne die Gesamtleistung.
b) Berechne den Gesamtstrom.
c) Prüfe, ob der Stromkreis überlastet ist.
d) Plane, wie viele Stromkreise mindestens benötigt werden.

> [!success]- Lösung
> **a)** $P_{ges} = 5 \cdot 350\,\text{W} + 2 \cdot 120\,\text{W} + 100\,\text{W} = 1750 + 240 + 100 = \mathbf{2090\,W}$
>
> **b)** $I = \dfrac{P}{U} = \dfrac{2090\,\text{W}}{230\,\text{V}} \approx \mathbf{9{,}09\,A}$
>
> **c)** Maximale Leistung: $P_{max} = 230\,\text{V} \cdot 16\,\text{A} = 3680\,\text{W}$
> $2090\,\text{W} < 3680\,\text{W}$ bzw. $9{,}09\,\text{A} < 16\,\text{A}$ → **nicht überlastet** (Auslastung ca. 57 %).
>
> **d)** Rechnerisch reicht **ein** Stromkreis. Für Ausfallsicherheit plant man im Rechenzentrum aber **mindestens zwei** Stromkreise (A- und B-Schiene): Die Server mit redundanten Netzteilen hängen an beiden, sodass beim Ausfall eines Kreises alles weiterläuft. Dann muss **jeder** Kreis allein die Gesamtlast tragen können, und das schafft er hier mit 2090 W < 3680 W.

> [!warning] Korrektur
> In der Mitschrift steht $P_{ges} = 2050\,\text{W}$. Richtig ist $1750 + 240 + 100 = $ **2090 W**. Der notierte Strom von 9,1 A passt zu 2090 W. Außerdem wurde „3680 W < 2050 W“ geschrieben. Das Zeichen ist falsch herum: **3680 W > 2090 W**.

> [!tip] Praxis
> Stromkreise sollten nicht dauerhaft bis zum Limit belastet werden. Üblich ist max. ca. 80 % Dauerlast (hier ca. 2950 W). Auch das wird eingehalten.

## Siehe auch
- [[Elektrische Leistung und Energie]]
- [[USV]]
- [[Übung - Netzteile und Wirkungsgrad]]
