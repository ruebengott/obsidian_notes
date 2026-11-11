---
tags: [berufsschule, lf2, kalkulation]
fach: LF2
typ: thema
quelle: "[[LF1-LF2-Rossian.pdf#page=81]]"
datum:
status: zu-lernen
---
# Zuschlagskalkulation

> [!summary] Kurz & knapp
> Die Zuschlagskalkulation (Vorwärtskalkulation im Handel) ermittelt ausgehend vom **Listeneinkaufspreis** schrittweise den **Listenverkaufspreis**: Einkaufskonditionen abziehen, Bezugskosten, Handlungskosten und Gewinn aufschlagen, dann Kundenskonto, Vertreterprovision, Kundenrabatt und Umsatzsteuer einrechnen.

## Wozu?
- **Orientierungshilfe** zur Findung eines Verkaufspreises für neue Produkte und Dienstleistungen.
- **Kostenorientierung:** Alle Kosten sollen gedeckt werden → Gefahr von Verlusten reduzieren.
- Nur *Orientierung*, weil letztlich der **Markt** entscheidet: zu hoher Preis → Ladenhüter, zu niedriger Preis → Verlustgefahr. Zu beachten sind Zahlungsbereitschaft der Zielgruppe, Attraktivität für Kunden und Preise der Konkurrenz.
- Preisstrategien: niedriger Preis → viele Aufträge; hoher Preis + Qualität → höherer Gewinn pro Auftrag.

## Kalkulationsschema (Handel)

| Schritt | Prozentsatz bezieht sich auf … | Beispiel |
|---|---|---|
| Listeneinkaufspreis (LEP) | | 100,00 € |
| − Liefererrabatt 20 % | LEP (vom Hundert) | 20,00 € |
| = Zieleinkaufspreis (ZEP) | | 80,00 € |
| − Liefererskonto 3 % | ZEP (vom Hundert) | 2,40 € |
| = Bareinkaufspreis (BEP) | | 77,60 € |
| + Bezugskosten | fester €-Betrag | 5,00 € |
| = Bezugspreis (Einstandspreis) | | 82,60 € |
| + Handlungskosten 40 % | Bezugspreis | 33,04 € |
| = Selbstkosten (SK) | | 115,64 € |
| + Gewinnzuschlag 10 % | Selbstkosten | 11,56 € |
| = Barverkaufspreis (BVP) | | 127,20 € |
| + Kundenskonto 3 % | **Zielverkaufspreis** (im Hundert) | 4,15 € |
| + Vertreterprovision 5 % | **Zielverkaufspreis** (im Hundert) | 6,91 € |
| = Zielverkaufspreis (ZVP) | | 138,27 € |
| + Kundenrabatt 10 % | **Listenverkaufspreis** (im Hundert) | 15,36 € |
| = Listenverkaufspreis (LVP, netto) | | 153,63 € |
| + Umsatzsteuer 19 % | LVP | 29,19 € |
| = Listenverkaufspreis inkl. USt (brutto) | | 182,82 € |

Original mit Excel-Formeln und Pfeilen: ![[LF1-LF2-Rossian.pdf#page=91]]

## Die runden Pfeile – worauf beziehen sich die Prozente?
Die Pfeile im Arbeitsblatt zeigen den **Grundwert**, von dem der Prozentsatz genommen wird:
- **Einkaufsseite und Kosten/Gewinn** (vom Hundert): Der Prozentsatz wird vom Wert **darüber** berechnet (Rabatt vom LEP, Skonto vom ZEP, HK vom Bezugspreis, Gewinn von den SK).
- **Verkaufsseite** (im Hundert): Kundenskonto und Provision werden vom **Zielverkaufspreis**, der Kundenrabatt vom **Listenverkaufspreis** berechnet – also vom Wert **darunter**, den man noch gar nicht kennt. Grund: Der Kunde zieht Rabatt und Skonto später von diesen Preisen ab; danach muss genau der Barverkaufspreis übrig bleiben.

Darum gilt für die Verkaufsseite (Rechnen mit vermindertem Grundwert):

$$
\text{ZVP} = \frac{\text{BVP}}{1 - \frac{s + p}{100}} \qquad \text{Skonto} = \text{BVP}\cdot\frac{s}{100-s-p} \qquad \text{Provision} = \text{BVP}\cdot\frac{p}{100-s-p}
$$

$$
\text{LVP} = \frac{\text{ZVP}}{1 - \frac{r}{100}} \qquad \text{Kundenrabatt} = \text{ZVP}\cdot\frac{r}{100-r}
$$

(In Excel z. B. `=D14*C15/(1-C15-C16)` für den Kundenskonto und `=D17*C18/(1-C18)` für den Kundenrabatt.)

## Zweites Beispiel (Folie Rossian)

| Schritt | % | € |
|---|---|---|
| Listeneinkaufspreis | | 100,00 |
| − Lieferrabatt | 30 % | 30,00 |
| = Zieleinkaufspreis | | 70,00 |
| − Lieferskonto | 3 % | 2,10 |
| = Bareinkaufspreis | | 67,90 |
| + Bezugskosten | | 3,00 |
| = Bezugspreis | | 70,90 |
| + Handlungskostenzuschlag | 26 % | 18,43 |
| = Selbstkosten | | 89,33 |
| + Gewinnzuschlag | 12 % | 10,72 |
| = Barverkaufspreis | | 100,05 |
| + Kundenskonto + Vertreterprovision | 2 % + 2 % = 4 % (vom ZVP) | 4,17 |
| = Zielverkaufspreis | | 104,22 |
| + Kundenrabatt | 30 % (vom Nettoverkaufspreis) | 44,67 |
| = Nettoverkaufspreis | | 148,89 |
| + Umsatzsteuer | 19 % | 28,29 |
| = Bruttoverkaufspreis | | 177,18 |

## Begriffe
- **Handlungskosten:** Gemeinkosten des Handelsbetriebs (z. B. Personal-, Raum-, Verwaltungskosten), als Prozentsatz auf den Bezugspreis (Handlungskostenzuschlagssatz).
- **Selbstkosten:** alle Kosten, die für Beschaffung und Vertrieb der Ware anfallen.
- **Vertreterprovision:** Vergütung eines Handelsvertreters für erzielte Umsätze.
- Die USt ist für das Unternehmen ein durchlaufender Posten und wird erst ganz am Ende aufgeschlagen.

> [!tip] Merke
> - Reihenfolge: **LEP → ZEP → BEP → Bezugspreis → SK → BVP → ZVP → LVP → Brutto**.
> - Einkauf: abziehen „vom Hundert“. Verkauf: Kundenskonto/Provision und Kundenrabatt „im Hundert“ (durch 1 − p teilen), **nicht** einfach mal p!
> - Kundenskonto und Provision gemeinsam vom ZVP, Kundenrabatt vom LVP.
> - Die Kalkulation liefert eine Preis-**Untergrenze/Orientierung**, der Markt bestimmt den tatsächlichen Preis.

## Lernfragen
> [!question]- Warum ist die Zuschlagskalkulation nur eine Orientierungshilfe?
> Weil der Markt (Konkurrenzpreise, Zahlungsbereitschaft der Kunden) entscheidet, ob der kalkulierte Preis durchsetzbar ist. Zu hoch → Ladenhüter, zu niedrig → Verluste.

> [!question]- Worauf werden die Handlungskosten aufgeschlagen?
> Auf den Bezugspreis (Einstandspreis).

> [!question]- Warum wird der Kundenskonto nicht vom Barverkaufspreis berechnet?
> Der Kunde zieht den Skonto vom Zielverkaufspreis ab. Damit nach dem Abzug genau der Barverkaufspreis übrig bleibt, muss man im Hundert rechnen: ZVP = BVP : (1 − s).

> [!question]- Berechnen Sie den Zielverkaufspreis bei BVP 100 €, 2 % Kundenskonto und 3 % Provision.
> ZVP = 100 : 0,95 = 105,26 € (Skonto 2,11 €, Provision 3,16 €).

> [!question]- Welche Rolle spielt die Umsatzsteuer in der Kalkulation?
> Sie ist kein Kostenbestandteil und wird erst am Ende auf den Listenverkaufspreis (netto) aufgeschlagen.

## Siehe auch
- [[Rückwärtskalkulation]]
- [[Stundensatzkalkulation]]
- [[Angebotsvergleich quantitativ]]
- [[Übung - Zuschlagskalkulation]]
- [[LF2 Wirtschaft - Übersicht]]
