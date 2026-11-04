---
tags: [berufsschule, lf2, beschaffung, kalkulation]
fach: LF2
typ: thema
quelle: "[[LF1-LF2-Rossian.pdf#page=72]]"
datum:
status: zu-lernen
---
# Angebotsvergleich quantitativ

> [!summary] Kurz & knapp
> Beim quantitativen Angebotsvergleich wird für jedes Angebot der **Bezugspreis (Einstandspreis)** berechnet: Listeneinkaufspreis − Liefererrabatt − Liefererskonto + Bezugskosten. Das Angebot mit dem niedrigsten Bezugspreis ist preislich am günstigsten.

## Beschaffungskriterien
Bevor man rechnet, sollte man wissen, worauf es bei der Beschaffung überhaupt ankommt:
- Anschaffungspreis (Listenpreis)
- zusätzliche Kosten (Versand, Verpackung, Transportversicherung)
- Rabatte (z. B. Mengenrabatt) und Skonto
- Lieferzeit und Lieferkosten
- Zusammenarbeit/Vertrauen bzw. Image des Lieferers
- zusätzliche Leistungen, Support
- Herkunftsland (Zoll, Einfuhrbeschränkungen, Währungsunterschiede)
- Qualität

Nur die **in Euro messbaren** Kriterien fließen in den quantitativen Vergleich ein. Die übrigen (Qualität, Service, Image …) bewertet man mit der [[Nutzwertanalyse]].

## Kalkulationsschema (Bezugskalkulation)

| Schritt | Basis | Beispiel desktop.com | Beispiel it-market.de |
|---|---|---|---|
| Listeneinkaufspreis (LEP) | | 570,00 € | 540,00 € |
| − Liefererrabatt | % vom LEP | 10 % = 57,00 € | 15 % = 81,00 € |
| = Zieleinkaufspreis (ZEP) | | 513,00 € | 459,00 € |
| − Liefererskonto | % vom ZEP | 3 % = 15,39 € | 2 % = 9,18 € |
| = Bareinkaufspreis (BEP) | | 497,61 € | 449,82 € |
| + Bezugskosten | € (Fracht, Verpackung, Versicherung) | 8,00 € | 10,00 € |
| = **Bezugspreis (Einstandspreis)** | | **505,61 €** | **459,82 €** |

Differenz: 45,79 € → it-market.de ist günstiger (≈ 9,1 % bezogen auf it-market.de).

$$
\text{Bezugspreis} = \text{LEP}\cdot\left(1-\tfrac{r}{100}\right)\cdot\left(1-\tfrac{s}{100}\right) + \text{Bezugskosten}
$$

> [!info] Warum ohne Umsatzsteuer?
> Die Umsatzsteuer (Vorsteuer) bekommt ein Unternehmen vom Finanzamt zurück – sie ist **kein Kostenbestandteil** und wird daher im Angebotsvergleich nicht berücksichtigt.

## Typische Fallstricke
- **Reihenfolge einhalten:** erst Rabatt, dann Skonto, dann Bezugskosten. Skonto wird vom Zieleinkaufspreis (Warenwert) berechnet, **nicht** von den Bezugskosten.
- **Pauschale Bezugskosten** (z. B. „Versandkostenpauschale 50 € für die Lieferung“) gelten für die ganze Bestellung. Entweder mit der Gesamtmenge rechnen oder die Pauschale auf das Stück umlegen (50 € : 20 Stück = 2,50 €/Stück).
- Skonto gibt es nur bei Zahlung innerhalb der Skontofrist – beim Vergleich wird angenommen, dass man sie nutzt.

> [!tip] Merke
> - Schema: **LEP − Rabatt = ZEP − Skonto = BEP + Bezugskosten = Bezugspreis**
> - Rabatt vom LEP, Skonto vom ZEP.
> - USt bleibt außen vor.
> - Der Gesamtbetrag zählt: Ein höherer Listenpreis kann durch höheren Rabatt günstiger werden (Bauchgefühl ≠ Rechnung).

## Lernfragen
> [!question]- Was wird beim quantitativen Angebotsvergleich verglichen?
> Die Bezugspreise (Einstandspreise) der Anbieter, also Listeneinkaufspreis abzüglich Rabatt und Skonto zuzüglich Bezugskosten.

> [!question]- Von welchem Wert wird der Liefererskonto berechnet?
> Vom Zieleinkaufspreis (Listeneinkaufspreis nach Abzug des Rabatts) – nicht von den Bezugskosten.

> [!question]- Warum wird die Umsatzsteuer nicht einbezogen?
> Weil sie für das Unternehmen als Vorsteuer erstattet wird und damit kein Kostenbestandteil ist.

> [!question]- Was ist bei pauschalen Versandkosten für eine Sammelbestellung zu beachten?
> Die Pauschale fällt nur einmal pro Lieferung an. Man rechnet mit dem Gesamtwert der Bestellung oder legt die Pauschale auf die Stückzahl um – nicht die volle Pauschale auf jedes Stück aufschlagen.

> [!question]- Nennen Sie vier Kriterien, die neben dem Preis bei der Beschaffung eine Rolle spielen.
> z. B. Lieferzeit, Qualität, Service/Support, Zuverlässigkeit/Image des Lieferers, Herkunftsland (Zoll, Währung).

## Siehe auch
- [[Nutzwertanalyse]]
- [[Zuschlagskalkulation]]
- [[Übung - Quantitativer Angebotsvergleich]]
- [[LF2 Wirtschaft - Übersicht]]
