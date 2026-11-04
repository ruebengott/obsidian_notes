---
tags: [berufsschule, wipo, lohnabrechnung, sozialversicherung, steuern]
fach: WiPo
typ: thema
quelle: "[[WIPO.pdf#page=49]]"
status: zu-lernen
---
# Gehaltsabrechnung

> [!summary] Kurz & knapp
> Vom **Bruttogehalt** (plus vermögenswirksamer Leistung des Arbeitgebers) werden **Steuern** (Lohnsteuer, Kirchensteuer, ggf. Soli) und die **Arbeitnehmeranteile zur Sozialversicherung** abgezogen. Das ergibt das **Nettogehalt**. Davon gehen noch persönliche Abzüge wie das **vermögenswirksame Sparen** oder ein **Vorschuss** ab; übrig bleibt der **Überweisungsbetrag**.

## Schema

| Schritt | Position |
|---|---|
| | **Bruttogehalt** |
| + | vermögenswirksame Leistung des Arbeitgebers (**vL-AG**) |
| = | **steuer- und sozialversicherungspflichtiges Gehalt** (st + sv Gehalt) |
| − | Lohnsteuer (laut Lohnsteuertabelle, abhängig von der [[Lohnsteuerklassen\|Steuerklasse]]) |
| − | Kirchensteuer (8 % bzw. 9 % **der Lohnsteuer**) |
| − | KV-Anteil AN (7,3 % + ½ Zusatzbeitrag) – max. bis BBG KV |
| − | RV-Anteil AN (9,3 %) – max. bis BBG RV |
| − | AV-Anteil AN (1,3 %) – max. bis BBG RV |
| − | PV-Anteil AN (1,8 %, kinderlos ab 23: 2,4 %) – max. bis BBG KV |
| = | **Nettogehalt** |
| − | vermögenswirksames Sparen (**vS**), Vorschuss usw. |
| = | **Überweisungsbetrag** |

```mermaid
flowchart LR
    B[Brutto + vL-AG] -->|"− Steuern<br/>− SV-Anteile AN"| N[Netto]
    N -->|"− vS<br/>− Vorschuss"| U[Überweisung]
```

## Typische Fehlerquellen

- **Kirchensteuer** wird von der **Lohnsteuer** berechnet, nicht vom Brutto.
- Die **vermögenswirksame Leistung des AG** erhöht das steuer- und sv-pflichtige Gehalt. Das **vermögenswirksame Sparen** (vS) wird erst **nach** dem Netto abgezogen – es wird ja vom Arbeitnehmer angespart.
- **Beitragsbemessungsgrenzen** beachten: Liegt das Gehalt darüber, wird nur von der Grenze gerechnet (2026: KV/PV 5.812,50 €, RV/AV 8.450 € monatlich).
- Der **Kinderlosenzuschlag** in der PV geht nur zulasten des Arbeitnehmers.

## Rechenbeispiel (Fall 1 aus dem Unterricht)

Annahmen: KV inkl. Zusatzbeitrag 15,6 % (AN 7,8 %), kinderlos (PV 2,4 %), vL-AG 20 €, vS 40 €, Lohnsteuer 250 €, Kirchensteuer 9 %.

| Position | Betrag |
|---|---|
| Bruttogehalt | 2.500,00 € |
| + vL-AG | 20,00 € |
| = st + sv Gehalt | **2.520,00 €** |
| − Lohnsteuer | 250,00 € |
| − KiSt (9 % von 250 €) | 22,50 € |
| − KV 7,8 % | 196,56 € |
| − RV 9,3 % | 234,36 € |
| − AV 1,3 % | 32,76 € |
| − PV 2,4 % | 60,48 € |
| = Nettogehalt | **1.723,34 €** |
| − vS | 40,00 € |
| = Überweisungsbetrag | **1.683,34 €** |

Alle Fälle mit Lösung: [[Übung Gehaltsabrechnung 2026]].

> [!tip] Merke
> - **Brutto + vL-AG → − Steuern − SV-AN → Netto → − vS/Vorschuss → Überweisung.**
> - KiSt = % **der Lohnsteuer**.
> - Oberhalb der **BBG** bleiben die SV-Beiträge konstant.

## Lernfragen
> [!question]- Wovon wird die Kirchensteuer berechnet?
> Von der Lohnsteuer (8 % in BW/BY, sonst 9 %).

> [!question]- Was ist der Unterschied zwischen vL-AG und vS?
> vL-AG ist ein Zuschuss des Arbeitgebers. Er wird zum Brutto addiert und ist steuer- und sv-pflichtig. vS ist der Sparbetrag, der vom Netto abgezogen und z. B. auf einen Bausparvertrag überwiesen wird.

> [!question]- Ein AN verdient 7.000 € brutto. Von welchem Betrag wird sein KV-Beitrag berechnet?
> Von der Beitragsbemessungsgrenze der KV, 5.812,50 € (2026).

> [!question]- Wie berechnet man den RV-Anteil des Arbeitnehmers bei 3.020 € st+sv-Gehalt?
> 3.020 € × 9,3 % = 280,86 €.

## Siehe auch
- [[Gesetzliche Sozialversicherung]]
- [[Lohnsteuerklassen]]
- [[Übung Gehaltsabrechnung 2026]]
