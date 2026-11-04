---
tags: [berufsschule, lf3, übung, ipv4-header, fragmentierung]
fach: LF3
typ: übung
quelle: "[[LF3.pdf#page=49]]"
datum:
status: zu-lernen
---
# Übung: IPv4-Header – Traceanalyse 2 (TCP, Fragmentierung)

## Aufgaben
1. Wie viele Byte umfasst der IPv4-Header ohne Optionen/Padding?
2. Ein Protocol-Analyzer hat folgenden Trace aufgezeichnet:

```text
45 00 00 54 A1 1B 00 00 41 06 55 52 5D D6 C5 72
D9 A0 78 0F 00 00 9B E3 3F 1C 00 09 24 13 36 47
D5 98 0D 00 08 09 0A 0B 0C 0D 0E 0F 10 11 12 13
14 15 16 17 18 19 1A 1B 1C 1F 20 21 22 23 24 25 …
```

a) Bestimme die IPv4-Senderadresse hexadezimal und dezimal.
b) Bestimme die IPv4-Empfängeradresse hexadezimal und dezimal.
c) Welche Protokollart wird verwendet?
d) Wenn es sich **nicht** um das letzte Fragment eines Gesamtpakets handeln würde: Welches Bit müsste sich im Trace ändern, und welche Hexzahl ergäbe sich?

> [!success]- Lösung mit Rechenweg
> **1.** 5 Zeilen × 32 Bit = 160 Bit = **20 Byte** (IHL = 5)
>
> **a)** Bytes 13–16: `5D-D6-C5-72`
> 5D = 5·16 + 13 = 93 · D6 = 13·16 + 6 = 214 · C5 = 12·16 + 5 = 197 · 72 = 7·16 + 2 = 114 → **93.214.197.114**
>
> **b)** Bytes 17–20: `D9-A0-78-0F`
> D9 = 13·16 + 9 = 217 · A0 = 160 · 78 = 7·16 + 8 = 120 · 0F = 15 → **217.160.120.15**
>
> **c)** Byte 10: `06` = **TCP**
>
> **d)** Flags stehen in Byte 7 (= Bits 49–56 des Headers). Die ersten 3 Bit davon sind die Flags: Bit 49 = reserviert, Bit 50 = DF, **Bit 51 = MF**.
> Ist: Bits 49–52 = `0000` = 0x0 → MF = 0 → letztes Fragment.
> Soll: MF = 1 → Bits 49–52 = `0010` = **0x2**.
> Das **51. Bit** muss auf 1 gesetzt werden. Der Trace sähe dann so aus: `… A1 1B 20 00 …`

> [!note] Eigene Lösung im Original
> Handschriftlich notiert: Header 5 · 32 Bit, Protokoll TCP ✓. Bei der Senderadresse steht im Original eine schwer lesbare Rechnung (u. a. „216.197.116“). Richtig ist **93.214.197.114**, siehe Musterlösung (PDF-Seite 50).

> [!info] Zusatzbeobachtung
> Weitere Felder zum Üben: TTL `41` = **65**, Total Length `00 54` = 84 Byte, ID `A1 1B` = 41243, Flags `00` → DF = 0, die Fragmentierung ist also **erlaubt**. Die Header-Checksumme `55 52` wurde aus Trace 1 übernommen und passt hier nicht. Für die Aufgabe spielt das keine Rolle.

## Siehe auch
- [[IPv4-Header]]
- [[IPv4-Fragmentierung]]
- [[Übung IPv4-Header Traceanalyse 1]]
