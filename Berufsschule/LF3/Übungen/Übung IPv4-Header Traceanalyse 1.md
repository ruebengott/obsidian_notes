---
tags: [berufsschule, lf3, übung, ipv4-header, zahlensysteme]
fach: LF3
typ: übung
quelle: "[[LF3.pdf#page=47]]"
datum:
status: zu-lernen
---
# Übung: IPv4-Header – Traceanalyse 1 (ICMP)

## Aufgabe
Ein Protocol-Analyzer hat folgenden Trace aufgezeichnet:

```text
45 00 00 54 A1 1B 40 00 3F 01 55 52 C0 A8 01 02
C0 A8 01 E9 00 00 9B E3 3F 1C 00 09 24 13 36 47
D5 98 0D 00 08 09 0A 0B 0C 0D 0E 0F 10 11 12 13
14 15 16 17 18 19 1A 1B 1C 1F 20 21 22 23 24 25 …
```

a) Wie viele Byte umfasst der Header?
b) Bestimme die IPv4-Senderadresse.
c) Bestimme die IPv4-Empfängeradresse.
d) Wie lautet der Zahlenwert der TTL?
e) Ist bei diesem Datenpaket die Fragmentierung erlaubt?
f) Welche Protokollart wird verwendet?
g) Wie groß ist die Datenmenge des Gesamtpakets?
h) Welche Identifikationsnummer hat das Datenpaket?

> [!tip] Hilfe
> Ordne die Bytes zuerst den Header-Feldern zu, siehe [[IPv4-Header]]:
> `45` Version/IHL · `00` ToS · `00 54` Total Length · `A1 1B` ID · `40 00` Flags/Offset · `3F` TTL · `01` Protokoll · `55 52` Checksum · `C0 A8 01 02` Quelle · `C0 A8 01 E9` Ziel

> [!success]- Lösung mit Rechenweg
> **a)** Byte 1 = `45` → Version 4, IHL = **5** → 5 × 32 Bit = 160 Bit = **20 Byte**
>
> **b)** `C0 A8 01 02`: C0 = 12·16 = 192, A8 = 10·16 + 8 = 168, 01 = 1, 02 = 2 → **192.168.1.2**
>
> **c)** `C0 A8 01 E9`: E9 = 14·16 + 9 = 224 + 9 = 233 → **192.168.1.233**
>
> **d)** `3F` = 3·16 + 15 = **63**
>
> **e)** Flags-Byte `40` = `0100 0000` → die ersten 3 Bit sind `010`: Bit 0 = 0 (reserviert), **Bit 1 (DF) = 1**, Bit 2 (MF) = 0 → **Nein**, die Fragmentierung ist **verboten**.
>
> **f)** Protokoll `01` = **ICMP** (z. B. ein Ping)
>
> **g)** Total Length `00 54` = 5·16 + 4 = **84 Byte** (20 Byte Header + 64 Byte Daten)
>
> **h)** Identification `A1 1B` = 10·16³ + 1·16² + 1·16 + 11 = 40960 + 256 + 16 + 11 = **41243**

> [!note] Eigene Lösung im Original
> Alle Teilaufgaben b)–h) wurden handschriftlich richtig gelöst. a) war offen geblieben. Die Musterlösung des Lehrers (PDF-Seite 48) stimmt mit der obigen Lösung überein.

## Siehe auch
- [[IPv4-Header]]
- [[IPv4-Header - Time to Live]]
- [[Zahlensysteme Binär Dezimal Hexadezimal]]
- [[Übung IPv4-Header Traceanalyse 2]]
