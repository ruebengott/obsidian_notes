---
tags: [berufsschule, lf2, kalkulation, übung]
fach: LF2
typ: übung
quelle: "[[LF1-LF2-Rossian.pdf#page=94]]"
datum:
status: zu-lernen
---
# Übung - Zuschlagskalkulation

> [!summary] Kurz & knapp
> Arbeitsaufträge zur Zuschlagskalkulation im Handel (S. 94–97): Bedeutung der Pfeile im Kalkulationsschema, Barverkaufspreis (a) und Listenverkaufspreis (b). Die Excel-Lösungen der Mitschrift (S. 92–93) enthalten Fehler und sind unten korrigiert.

## Aufgabe 1: Bedeutung der runden Pfeile
Erläutern Sie im Beispiel ([[Zuschlagskalkulation]], Excel-Schema S. 91), welche Bedeutung die runden Pfeile links haben.

> [!success]- Lösung
> Die Pfeile zeigen, **von welchem Grundwert** der jeweilige Prozentsatz genommen wird (Musterlösung: „von welchem Grundwert die Prozentwerte genommen werden müssen“). Beim Liefererrabatt ist es der Listeneinkaufspreis, beim Lieferskonto der Zieleinkaufspreis, bei den Handlungskosten der Bezugspreis, beim Gewinn die Selbstkosten. Auf der Verkaufsseite zeigen die Pfeile **nach unten**: Kundenskonto und Provision beziehen sich auf den Zielverkaufspreis, der Kundenrabatt auf den Listenverkaufspreis (Rechnen im Hundert).

## Aufgabe 2a: Barverkaufspreis
Listeneinkaufspreis 30,00 €, Lieferrabatt 20 %, Lieferskonto 3 %, Frachtkosten 3,00 €, Handlungskostenzuschlagssatz 70 %, Gewinnaufschlag 8 %.

> [!success]- Lösung
> | Schritt | Satz | Betrag |
> |---|---|---|
> | Listeneinkaufspreis | | 30,00 € |
> | − Liefererrabatt | 20 % | 6,00 € |
> | = Zieleinkaufspreis | | 24,00 € |
> | − Liefererskonto | 3 % | 0,72 € |
> | = Bareinkaufspreis | | 23,28 € |
> | + Bezugskosten (Fracht) | | 3,00 € |
> | = Bezugspreis | | 26,28 € |
> | + Handlungskosten | 70 % | 18,40 € |
> | = Selbstkosten | | 44,68 € |
> | + Gewinnzuschlag | 8 % | 3,57 € |
> | = **Barverkaufspreis** | | **48,25 €** |
>
> > [!warning] Korrektur
> > In der Excel-Lösung der Mitschrift fehlen die **Frachtkosten von 3,00 €** (Bezugskosten = 0). Dadurch ergab sich ein Barverkaufspreis von 42,74 €; die Notiz „Lösung für a = 20,28“ ist nicht nachvollziehbar. Richtig: **48,25 €**.

## Aufgabe 2b: Listenverkaufspreis
Listeneinkaufspreis 40,00 €, Lieferrabatt 20 %, Lieferskonto 2 %, Frachtkosten 7,00 €, Handlungskostenzuschlagssatz 75 %, Gewinnaufschlag 10 %, Kundenskonto 3 %, Kundenrabatt 20 %.

> [!success]- Lösung
> | Schritt | Satz | Betrag | Rechenweg |
> |---|---|---|---|
> | Listeneinkaufspreis | | 40,00 € | |
> | − Liefererrabatt | 20 % | 8,00 € | 40 · 0,20 |
> | = Zieleinkaufspreis | | 32,00 € | |
> | − Liefererskonto | 2 % | 0,64 € | 32 · 0,02 |
> | = Bareinkaufspreis | | 31,36 € | |
> | + Bezugskosten | | 7,00 € | |
> | = Bezugspreis | | 38,36 € | |
> | + Handlungskosten | 75 % | 28,77 € | 38,36 · 0,75 |
> | = Selbstkosten | | 67,13 € | |
> | + Gewinnzuschlag | 10 % | 6,71 € | 67,13 · 0,10 |
> | = Barverkaufspreis | | 73,84 € | |
> | + Kundenskonto | 3 % (im Hundert) | 2,28 € | 73,84 · 3 / 97 |
> | = Zielverkaufspreis | | 76,12 € | |
> | + Kundenrabatt | 20 % (im Hundert) | 19,03 € | 76,12 · 20 / 80 |
> | = **Listenverkaufspreis** | | **95,15 €** | |
>
> Probe: 95,15 − 20 % = 76,12; 76,12 − 3 % = 73,84 ✓
>
> > [!warning] Korrektur
> > Die Mitschrift kommt auf **77 €**. Drei Fehler: (1) Lieferskonto mit **3 %** statt 2 %, (2) **Frachtkosten 7,00 € fehlen**, (3) Kundenskonto als 3 % *vom Barverkaufspreis* (1,85 €) statt im Hundert vom Zielverkaufspreis gerechnet. Der Kundenrabatt (25 % auf den ZVP = 20 % vom LVP) war dagegen richtig im Hundert gerechnet. Richtig: **95,15 €**.

## Siehe auch
- [[Zuschlagskalkulation]]
- [[Übung - Rückwärtskalkulation]]
- [[LF2 Wirtschaft - Übersicht]]
