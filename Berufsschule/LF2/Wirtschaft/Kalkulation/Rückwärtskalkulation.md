---
tags: [berufsschule, lf2, kalkulation]
fach: LF2
typ: thema
quelle: "[[LF1-LF2-Rossian.pdf#page=100]]"
datum:
status: zu-lernen
---
# Rückwärtskalkulation

> [!summary] Kurz & knapp
> Die Rückwärtskalkulation geht vom **vorgegebenen (Markt-)Verkaufspreis** aus und rechnet das Kalkulationsschema von unten nach oben, um den **höchstens zulässigen Listeneinkaufspreis** (bzw. Bezugspreis) zu ermitteln, bei dem der geplante Gewinn noch erzielt wird.

## Wann?
- Der Listenverkaufspreis ist durch den **Markt** vorgegeben (Konkurrenz, Kundenwunsch, Marktanalyse). Weicht der eigene Preis stark davon ab, kann man sich nicht behaupten.
- Frage: *Wie viel darf ich im Einkauf höchstens bezahlen?*
- Hilft bei der Planung des Einkaufs und bei Preisverhandlungen mit Lieferern.

## Rechenweg
Jeder Schritt der [[Zuschlagskalkulation]] wird umgekehrt. Entscheidend ist, **welcher Wert 100 %** ist:

| Rückwärts-Schritt | Rechnung | Prozentrechnung |
|---|---|---|
| Brutto → Listenverkaufspreis | LVP = Brutto · 100 / 119 | auf Hundert (119 %) |
| − Kundenrabatt | Rabatt = LVP · r / 100 | vom Hundert |
| − Kundenskonto, − Provision | je ZVP · p / 100 | vom Hundert |
| − Gewinn | SK = BVP · 100 / (100 + g) | auf Hundert |
| − Handlungskosten | Bezugspreis = SK · 100 / (100 + hk) | auf Hundert |
| − Bezugskosten | BEP = Bezugspreis − Bezugskosten | € |
| + Liefererskonto | ZEP = BEP · 100 / (100 − s) | im Hundert |
| + Liefererrabatt | LEP = ZEP · 100 / (100 − r) | im Hundert |

Merkhilfe:
- **vom Hundert:** Grundwert (100 %) ist bekannt → mal p/100.
- **auf Hundert:** bekannt ist der vermehrte Grundwert (100 % + p) → durch (100 + p) teilen.
- **im Hundert:** bekannt ist der verminderte Grundwert (100 % − p) → durch (100 − p) teilen.

## Beispiel (Brutto-Listenverkaufspreis 182,82 €)

| Schritt | Satz | Betrag | Berechnung |
|---|---|---|---|
| Listen-VK inkl. USt | | 182,82 € | |
| − Umsatzsteuer | 19 % | 29,19 € | 182,82 · 19 / 119 |
| = Listenverkaufspreis | | 153,63 € | 182,82 − 29,19 |
| − Kundenrabatt | 10 % | 15,36 € | 153,63 · 10 / 100 |
| = Zielverkaufspreis | | 138,27 € | 153,63 − 15,36 |
| − Kundenskonto | 3 % | 4,15 € | 138,27 · 3 / 100 |
| − Vertreterprovision | 5 % | 6,91 € | 138,27 · 5 / 100 |
| = Barverkaufspreis | | 127,21 € | 138,27 − 4,15 − 6,91 |
| − Gewinnzuschlag | 10 % | 11,56 € | 127,21 · 10 / 110 |
| = Selbstkosten | | 115,64 € | 127,21 − 11,56 |
| − Handlungskosten | 40 % | 33,04 € | 115,64 · 40 / 140 |
| = Bezugspreis | | 82,60 € | 115,64 − 33,04 |
| − Bezugskosten | | 5,00 € | |
| = Bareinkaufspreis | | 77,60 € | 82,60 − 5,00 |
| + Lieferskonto | 3 % | 2,40 € | 77,60 · 3 / 97 |
| = Zieleinkaufspreis | | 80,00 € | 77,60 + 2,40 |
| + Lieferrabatt | 20 % | 20,00 € | 80,00 · 20 / 80 |
| = **Listeneinkaufspreis** | | **100,00 €** | 80,00 + 20,00 |

(Im Original steht in der Berechnungsspalte zweimal „138,37“ – gemeint ist 138,27. Der Barverkaufspreis weicht wegen Rundung um 1 Cent von der Vorwärtsrechnung ab: 127,21 statt 127,20.)

Original: ![[LF1-LF2-Rossian.pdf#page=100]]

> [!tip] Merke
> - Rückwärts = **von unten nach oben**, Ziel: maximaler Listeneinkaufspreis.
> - USt, Gewinn, Handlungskosten: **auf Hundert** (durch 119, 100+g, 100+hk teilen).
> - Kundenrabatt, Kundenskonto, Provision: rückwärts **vom Hundert** (sie wurden ja vom ZVP bzw. LVP berechnet).
> - Liefererskonto und -rabatt: **im Hundert** (durch 97, 80 … teilen).
> - Typischer Fehler: Gewinn als 10 % vom Barverkaufspreis abziehen – falsch, die 10 % beziehen sich auf die Selbstkosten!

## Lernfragen
> [!question]- Was ist das Ziel der Rückwärtskalkulation?
> Den Listeneinkaufspreis zu ermitteln, den man höchstens zahlen darf, wenn der Verkaufspreis vom Markt vorgegeben ist und der geplante Gewinn erzielt werden soll.

> [!question]- Wie berechnet man die Selbstkosten aus einem Barverkaufspreis von 112 € bei 12 % Gewinnzuschlag?
> SK = 112 · 100 / 112 = 100 € (auf Hundert).

> [!question]- Wie rechnet man aus einem Bareinkaufspreis von 97 € bei 3 % Liefererskonto den Zieleinkaufspreis?
> ZEP = 97 · 100 / 97 = 100 € (im Hundert), Skonto = 3 €.

> [!question]- Wie ermittelt man aus einem Bruttopreis von 238 € die enthaltene Umsatzsteuer?
> USt = 238 · 19 / 119 = 38 €; netto 200 €.

> [!question]- Warum kann man den Kundenrabatt rückwärts einfach „vom Hundert“ rechnen?
> Weil er in der Vorwärtskalkulation vom Listenverkaufspreis berechnet wurde – der LVP ist rückwärts bereits bekannt und damit der Grundwert.

## Siehe auch
- [[Zuschlagskalkulation]]
- [[Übung - Rückwärtskalkulation]]
- [[LF2 Wirtschaft - Übersicht]]
