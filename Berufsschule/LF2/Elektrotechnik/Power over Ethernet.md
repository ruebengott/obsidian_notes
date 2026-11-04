---
tags: [berufsschule, lf2, elektrotechnik, netzwerk, poe]
fach: LF2
typ: thema
quelle: "[[LF2.pdf#page=51]]"
datum:
status: zu-lernen
---
# Power over Ethernet

> [!summary] Kurz & knapp
> Bei **Power over Ethernet (PoE)** werden Daten **und** Strom über dasselbe Netzwerkkabel übertragen. Ein PoE-Switch versorgt so z. B. IP-Kameras, Access Points und VoIP-Telefone ohne eigenes Netzteil. Wichtig ist das **PoE-Leistungsbudget** des Switches: Die Summe aller Geräte darf es nicht überschreiten.

## Begriffe
- **PSE** (Power Sourcing Equipment): liefert den Strom, z. B. PoE-Switch oder PoE-Injektor
- **PD** (Powered Device): wird versorgt, z. B. Kamera, Access Point, Telefon
- **PoE-Budget**: maximale Gesamtleistung, die der Switch über **alle** Ports zusammen abgeben kann (z. B. 370 W). Das Budget ist meist kleiner als „Ports × Maximalleistung pro Port“.

## PoE-Standards (Überblick)

| Standard | Name | max. Leistung am Switch-Port (PSE) | ca. am Gerät (PD) |
| --- | --- | --- | --- |
| IEEE 802.3af | PoE | 15,4 W | 12,95 W |
| IEEE 802.3at | PoE+ | 30 W | 25,5 W |
| IEEE 802.3bt Typ 3 | PoE++ | 60 W | 51 W |
| IEEE 802.3bt Typ 4 | PoE++ | 90–100 W | 71 W |

Die Spannung liegt bei ca. **44–57 V Gleichspannung** (typisch 48 V). Die Differenz zwischen PSE- und PD-Leistung geht als Verlust auf dem Kabel verloren (max. 100 m Kabellänge).

## Leistungsbudget prüfen – Vorgehen
1. Leistung je Gerätetyp: Anzahl · Leistung pro Gerät
2. Alles addieren: $P_{ges}$
3. Vergleichen: $P_{ges} \le P_{Budget}$? Die Reserve ist $P_{Budget} - P_{ges}$.
4. Optional den Strom auf der Netzseite berechnen: $I = P / U$ (bei 230 V, ohne Eigenverbrauch und Netzteilverluste)

**Beispiel:** 8 × 12 W + 6 × 18 W + 4 × 7 W = 232 W ≤ 370 W → Reserve 138 W. Rechenweg in [[Übung - PoE-Leistungsbudget]].

## Vorteile
- kein separates Netzteil und keine Steckdose am Montageort nötig (Decke, Außenwand)
- zentrale Stromversorgung: Hängt der PoE-Switch an einer [[USV]], laufen auch Kameras und Telefone bei Stromausfall weiter.
- Geräte lassen sich per Switch aus der Ferne neu starten (Port aus/an).

> [!tip] Merke
> - PoE = Daten + Strom über Twisted-Pair-Kabel, ca. 48 V DC.
> - PoE (af) 15,4 W, PoE+ (at) 30 W, PoE++ (bt) bis 90 W.
> - Das **Gesamtbudget** des Switches begrenzt die Summe aller Ports.
> - Kabelverluste: $P_V = I^2 \cdot R$ → siehe [[Spannungsfall und Leitungsverluste]]

## Lernfragen
> [!question]- Was bedeutet PoE und welchen Vorteil bietet es?
> Power over Ethernet: Strom und Daten über ein Netzwerkkabel. Man braucht kein eigenes Netzteil und keine Steckdose am Gerät, und die Versorgung lässt sich zentral über eine USV absichern.

> [!question]- Was ist ein PoE-Leistungsbudget?
> Die maximale Gesamtleistung, die ein PoE-Switch über alle Ports zusammen bereitstellen kann.

> [!question]- Welche Leistung liefert ein Port nach IEEE 802.3at (PoE+)?
> Bis 30 W am Switch-Port (ca. 25,5 W am Gerät).

> [!question]- Was ist der Unterschied zwischen PSE und PD?
> Das PSE liefert die Energie (Switch/Injektor), das PD wird versorgt (z. B. Kamera, Access Point).

> [!question]- 10 Access Points à 25 W hängen an einem Switch mit 240 W Budget. Reicht das?
> Nein: $10 \cdot 25\,\text{W} = 250\,\text{W} > 240\,\text{W}$. Es fehlen 10 W.

## Siehe auch
- [[Spannungsfall und Leitungsverluste]]
- [[Netzwerkkabel - Twisted Pair und Kategorien]]
- [[USV]]
- [[Übung - PoE-Leistungsbudget]]
- [[Übung - Spannungsfall bei PoE und Netzwerkgeräten]]
