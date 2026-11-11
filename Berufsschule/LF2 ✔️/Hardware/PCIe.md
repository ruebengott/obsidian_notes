---
tags: [berufsschule, lf2, hardware, bus, pcie]
fach: LF2
typ: thema
quelle: "[[LF2.pdf#page=7]]"
datum: 2025-12-01
status: zu-lernen
---
# PCIe

> [!summary] Kurz & knapp
> **PCIe (Peripheral Component Interconnect Express)** ist der serielle Hochgeschwindigkeitsbus für Grafikkarten, NVMe-SSDs und Netzwerkkarten. Er arbeitet mit **Lanes** (x1, x4, x8, x16). Jede neue Version **verdoppelt** etwa die Bandbreite pro Lane, und alle Versionen sind **abwärtskompatibel**.

## Grundprinzip
- **seriell** und **Point-to-Point**: Jedes Gerät hat eine eigene Verbindung, keinen geteilten Bus wie beim alten PCI.
- Eine **Lane** = je ein Leitungspaar zum Senden und Empfangen (Vollduplex).
- Mehrere Lanes werden gebündelt: **x1, x4, x8, x16**. Grafikkarten nutzen meist x16, NVMe-SSDs x4.
- Wichtig für alles mit hoher Bandbreite: Gaming, KI, Server, schnelle SSDs.

## PCIe-Versionen (Aufgaben 6–9)

| Version | Jahr | Transferrate pro Lane | Kodierung | ca. Bandbreite pro Lane (je Richtung) | ca. x16 (je Richtung) |
| --- | --- | --- | --- | --- | --- |
| 1.0 | 2003 | 2,5 GT/s | 8b/10b | 0,25 GB/s | 4 GB/s |
| 2.0 | 2007 | 5 GT/s | 8b/10b | 0,5 GB/s | 8 GB/s |
| 3.0 | 2010 | 8 GT/s | 128b/130b | ~1 GB/s | ~16 GB/s |
| 4.0 | 2017 | 16 GT/s | 128b/130b | ~2 GB/s | ~32 GB/s |
| 5.0 | 2019 | **32 GT/s** | 128b/130b | ~4 GB/s | ~64 GB/s |
| 6.0 | 2022 | 64 GT/s | PAM4 + FLIT, FEC | ~8 GB/s | ~128 GB/s |

*GT/s = Gigatransfers pro Sekunde. Bidirektional (beide Richtungen zusammen) ist der Wert doppelt so hoch.*

> [!warning] Korrektur
> - In der Mitschrift steht „PCIe 5.0: 64 GT/s“. Richtig sind **32 GT/s** pro Lane. 64 GT/s hat erst **PCIe 6.0**.
> - „PCIe 5.0 … 256 GB/s x16“ ist zu hoch. PCIe 5.0 x16 schafft ca. **64 GB/s je Richtung** (ca. 128 GB/s bidirektional). Die ca. 256 GB/s (bidirektional) gelten für **PCIe 6.0 x16**.

### Antworten zum Aufgabenblatt
- **Unterschiede der Versionen (6):** höhere Transferrate pro Lane (Verdopplung je Generation), effizientere Kodierung (8b/10b → 128b/130b → PAM4), bessere Fehlerkorrektur.
- **PCIe 4.0 vs. 3.0 (7):** 16 GT/s (~2 GB/s pro Lane) statt 8 GT/s (~1 GB/s), also doppelt so schnell.
- **PCIe 5.0 (8):** 32 GT/s (~4 GB/s pro Lane), wichtig für sehr schnelle NVMe-SSDs, High-End-Grafik, KI-Beschleuniger und Server-Netzwerkkarten (100/400 GbE).
- **PCIe 6.0 – Neuheiten (9):** **PAM4**-Signalisierung (4 Spannungsstufen = 2 Bit pro Symbol) → 64 GT/s, **FLIT**-Modus, **FEC** (Forward Error Correction), Grundlage für **CXL** (Compute Express Link, z. B. Speicher-Pooling in Rechenzentren).

## Abwärtskompatibilität (Aufgabe 10)
- Neue Karten passen in alte Slots und umgekehrt. Ein x4-Gerät funktioniert auch im x16-Slot.
- Die Verbindung läuft mit der **höchsten Version, die beide Seiten beherrschen**, und mit der kleineren Lane-Anzahl (**Link-Training / Negotiated Link Speed**).
- Beispiel: PCIe-4.0-SSD in einem PCIe-3.0-Slot → läuft, aber nur mit PCIe-3.0-Geschwindigkeit.

> [!tip] Merke
> - PCIe = seriell, Point-to-Point, Lanes x1/x4/x8/x16.
> - Faustregel: Jede Generation **verdoppelt** die Bandbreite. 3.0 ≈ 1 GB/s, 4.0 ≈ 2 GB/s, 5.0 ≈ 4 GB/s, 6.0 ≈ 8 GB/s pro Lane.
> - Abwärtskompatibel: Es gilt immer der **langsamste** gemeinsame Standard.

## Lernfragen
> [!question]- Was ist eine PCIe-Lane?
> Eine serielle Vollduplex-Verbindung aus je einem Leitungspaar für Senden und Empfangen. Mehrere Lanes werden zu x4, x8 oder x16 gebündelt.

> [!question]- Welche Bandbreite hat PCIe 4.0 x4 ungefähr?
> ca. 2 GB/s pro Lane · 4 = ca. **8 GB/s** je Richtung (typisch für schnelle NVMe-SSDs).

> [!question]- Was passiert, wenn eine PCIe-5.0-Grafikkarte in einen PCIe-4.0-Slot gesteckt wird?
> Sie funktioniert (abwärtskompatibel), läuft aber nur mit PCIe-4.0-Geschwindigkeit.

> [!question]- Welche Neuerung brachte PCIe 6.0?
> PAM4-Signalisierung (64 GT/s), FLIT-Modus und Fehlerkorrektur (FEC). Außerdem ist es Grundlage für CXL.

> [!question]- Warum ist PCIe für moderne Systeme so wichtig?
> Grafikkarten, NVMe-SSDs, KI-Beschleuniger und schnelle Netzwerkkarten brauchen sehr hohe Bandbreiten, die nur PCIe bietet.

## Siehe auch
- [[Bussysteme]]
- [[Bridge- und Hub-Architektur]]
- [[HDD und SSD]]
- [[Mainboard-Bestandteile]]
