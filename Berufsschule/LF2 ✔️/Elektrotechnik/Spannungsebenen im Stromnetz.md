---
tags: [berufsschule, lf2, elektrotechnik]
fach: LF2
typ: thema
quelle: "[[LF2.pdf#page=55]]"
datum:
status: zu-lernen
---
# Spannungsebenen im Stromnetz

> [!summary] Kurz & knapp
> Strom wird über weite Strecken mit **Hoch- und Höchstspannung** transportiert und über Umspannwerke stufenweise auf **Mittelspannung** und schließlich **Niederspannung** (230/400 V) heruntertransformiert. Bei hoher Spannung braucht man für dieselbe Leistung weniger Strom, und die Leitungsverluste sinken.

## Die Spannungsebenen

| Ebene | Spannung (DE) | Einsatz |
| --- | --- | --- |
| Höchstspannung | 220 kV und 380 kV | überregionaler Transport (Übertragungsnetz) |
| Hochspannung | 110 kV | regionale Verteilung, Großindustrie |
| Mittelspannung | > 1 kV bis ca. 60 kV, typisch 10–30 kV | Versorgung von Ortsnetzen, Betriebsgeländen, Rechenzentren |
| Niederspannung | bis 1 kV, z. B. 230 V / 400 V | Haushalte, Büros, IT-Geräte |

> [!warning] Korrektur
> In der Mitschrift steht „Höchstspannung: 300 kV“. In Deutschland sind die üblichen Höchstspannungen **220 kV und 380 kV**. Die Mittelspannung reicht formal von über 1 kV bis ca. 60 kV. 10–30 kV sind die typischen Werte.

```mermaid
flowchart LR
    K["Kraftwerk"] --> H["Höchst-/Hochspannung 380/110 kV"]
    H --> U1["Umspannwerk"]
    U1 --> M["Mittelspannung 10 kV"]
    M --> T["Trafo im Betrieb"]
    T --> N["Niederspannung 400/230 V: Server, Netzwerk, Klima"]
```

## Warum hohe Spannung für den Transport?
- Leistung: $P = U \cdot I$ → bei **höherer Spannung** ist für dieselbe Leistung **weniger Strom** nötig.
- Leitungsverluste: $P_V = I^2 \cdot R$ → weniger Strom bedeutet **quadratisch weniger Verluste**.
- Dünnere Leiter sind möglich, was Material und Kosten spart.
- Mit 400 V wären die Ströme über weite Strecken riesig, die Verluste enorm und die Kabel unbezahlbar dick.

## Probleme für IT-Systeme bei Störungen
- **Stromausfall**: Absturz, Datenverlust, beschädigte Dateisysteme/Datenbanken
- **Spannungseinbrüche / -schwankungen**: Neustarts, instabiler Betrieb, Fehlfunktionen
- **Überspannung** (z. B. Blitz, Schaltvorgänge): Hardwareschäden an Netzteilen und Mainboards
- Gegenmaßnahmen: [[USV]], Notstromaggregat, Überspannungsschutz, redundante Einspeisung (A/B-Versorgung)

> [!tip] Merke
> - Nieder ≤ 1 kV, Mittel 10–30 kV, Hoch 110 kV, Höchst 220/380 kV.
> - Hohe Spannung → kleiner Strom → kleine Verluste ($I^2 R$).
> - Jede Trafostufe hat Verluste, die Wirkungsgrade werden multipliziert.

## Lernfragen
> [!question]- Warum wird Strom über weite Strecken mit 110 kV oder mehr übertragen?
> Für die gleiche Leistung fließt bei hoher Spannung ein kleinerer Strom. Die Verluste $P_V = I^2 R$ sinken quadratisch.

> [!question]- Welche Spannungsebene versorgt Haushalte und Büros?
> Die Niederspannung (230 V / 400 V).

> [!question]- Zwei Trafos mit je 98 % Wirkungsgrad: Wie viel Leistung muss oben eingespeist werden, wenn unten 41,975 kW gebraucht werden?
> $P = 41{,}975\,\text{kW} / (0{,}98 \cdot 0{,}98) \approx 43{,}71\,\text{kW}$

> [!question]- Welche Folgen können Spannungsschwankungen für Server haben?
> Abstürze, Datenverlust, beschädigte Dateisysteme und Hardwaredefekte. Schutz bieten USV und Überspannungsschutz.

## Siehe auch
- [[Wirkungsgrad]]
- [[Spannungsfall und Leitungsverluste]]
- [[USV]]
- [[Übung - Spannungsebenen Rechenzentrum]]
