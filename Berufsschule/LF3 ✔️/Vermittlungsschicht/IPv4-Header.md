---
tags: [berufsschule, lf3, ipv4, ipv4-header, schicht-3]
fach: LF3
typ: thema
quelle: "[[LF3.pdf#page=38]]"
datum:
status: zu-lernen
---
# IPv4-Header

> [!summary] Kurz & knapp
> Der IPv4-Header steht vor den Nutzdaten jedes IP-Pakets. Er ist **mindestens 20 Byte** (5 Zeilen × 32 Bit) und **höchstens 60 Byte** groß. Er enthält u. a. Version, Headerlänge, Gesamtlänge, Fragmentierungs-Infos, TTL, Protokoll sowie Quell- und Ziel-IP-Adresse.

## Aufbau (je Zeile 32 Bit)

| Bit 0–3 | 4–7 | 8–15 | 16–18 | 19–31 |
|---|---|---|---|---|
| Version | IHL (Header Length) | Type of Service | Total Length (16 Bit) | ← |
| Identification (16 Bit) | ← | ← | Flags (3 Bit) | Fragment Offset (13 Bit) |
| Time to Live (8) | ← | Protocol (8) | Header Checksum (16 Bit) | ← |
| Source Address (32 Bit) | | | | |
| Destination Address (32 Bit) | | | | |
| Optionen + Padding (0–40 Byte) | | | | |

Original-Folie: ![[LF3.pdf#page=38]]

## Die Felder

| Feld | Bits | Inhalt |
|---|---|---|
| Version | 4 | IP-Version, bei IPv4 = 4 = `0100` |
| IHL (Internet Header Length) | 4 | Länge des Headers in **32-Bit-Worten**: 5 = `0101` → 5 × 32 Bit = 160 Bit = **20 Byte**. Max. 15 → 60 Byte |
| TOS (Type of Service) | 8 | Priorität und Eigenschaften des Pakets (QoS), siehe [[IPv4-Header - Type of Service]] |
| Total Length | 16 | Gesamtlänge des Pakets (Header + Daten) in Byte, max. 65.535 Byte (≈ 64 KByte) |
| Identification | 16 | laufende Nummer des Pakets. Alle Fragmente eines Pakets haben dieselbe ID, damit der Empfänger sie zusammensetzen kann |
| Flags | 3 | Bit 0: immer 0 (reserviert). Bit 1 **DF** (Don't Fragment): 0 = Fragmentierung erlaubt, 1 = verboten. Bit 2 **MF** (More Fragments): 0 = letztes Fragment, 1 = weitere folgen |
| Fragment Offset | 13 | Position des Fragments im Originalpaket (in 8-Byte-Einheiten), siehe [[IPv4-Fragmentierung]] |
| TTL (Time to Live) | 8 | Lebensdauer. Jeder Router zieht 1 ab, bei 0 wird das Paket verworfen. Siehe [[IPv4-Header - Time to Live]] |
| Protocol | 8 | Protokoll der nächsthöheren Schicht: **1 = ICMP, 6 = TCP, 17 = UDP** |
| Header Checksum | 16 | Prüfsumme **nur über den Header**, nicht über die Nutzdaten |
| Source Address | 32 | IP-Adresse des Absenders |
| Destination Address | 32 | IP-Adresse des Empfängers |
| Optionen | variabel | Angaben zu Routing und Diagnose (0–40 Byte) |
| Padding | variabel | Füllbits, damit der Header ein Vielfaches von 32 Bit lang ist |

> [!info] Fragmentierung und MTU
> Ist die Fragmentierung nicht erlaubt (DF = 1) und das Paket größer als die **MTU** (bei Ethernet 1500 Byte Nutzlast), verwirft der Router das Paket.

## Protokollnummern (Auszug)
| Dez | Hex | Protokoll |
|---|---|---|
| 1 | 0x01 | ICMP (z. B. ping) |
| 2 | 0x02 | IGMP |
| 6 | 0x06 | **TCP** |
| 17 | 0x11 | **UDP** |

## IPv4-Optionen
Der Header ist min. 20 und max. 60 Byte groß, also stehen **40 Byte für Optionen** zur Verfügung. Eine Option kann 1 Byte groß sein. Optionen werden ggf. durch **Padding** auf ein Vielfaches von 4 Byte aufgefüllt. Definiert sind 5 Optionen:

| Option | Bedeutung |
|---|---|
| Security | kennzeichnet die Geheimhaltung, z. B. könnten bestimmte Länder umroutet werden |
| Strict Source Routing | die Route wird strikt vorgegeben (max. 9 Hops). Sinnvoll z. B. bei Verlust von Routingtabellen oder für Zeitmessungen |
| Loose Source Routing | eine Reihe von Routern wird vorgegeben, dazwischen dürfen weitere liegen (politische/wirtschaftliche Gründe) |
| Record Route | zeichnet den Weg des Pakets auf, jeder Hop wird vermerkt (9 Hops, heute zu knapp) |
| Time Stamp | wie Record Route, zusätzlich mit Zeitstempel, nützlich zur Fehlersuche |

> [!warning] Korrektur
> - Die Folie gibt für „Optionen“ eine Länge von **2** Bit an. Das ist irreführend: Das Optionsfeld ist **variabel lang (0–40 Byte)**.
> - Handschriftliche Notiz zum DF-Bit: „bei Websites immer erlaubt / nur bei Paketen unter 1500 Byte, z. B. DHCP-Paket“. Das gilt so nicht allgemein. Viele Betriebssysteme setzen bei TCP das **DF-Bit = 1** (Path-MTU-Discovery), auch beim Surfen. Das DF-Bit sagt nur aus, ob ein Router das Paket teilen **darf**.

> [!tip] Merke
> - Header min. **20 Byte** (IHL = 5), max. **60 Byte** (IHL = 15)
> - Hex-Trace lesen: Byte 1 = Version/IHL (`45`), Byte 3–4 = Total Length, Byte 5–6 = ID, Byte 7–8 = Flags/Offset, Byte 9 = TTL, Byte 10 = Protokoll, Byte 13–16 = Quell-IP, Byte 17–20 = Ziel-IP
> - Protokoll: 01 = ICMP, 06 = TCP, 11 (hex) = 17 = UDP
> - Flags: `0 | DF | MF`

## Lernfragen
> [!question]- Wie groß ist der IPv4-Header mindestens und höchstens? Wie liest man das aus dem Header?
> 20 bis 60 Byte. Das IHL-Feld gibt die Länge in 32-Bit-Worten an: 5 × 4 Byte = 20 Byte, 15 × 4 Byte = 60 Byte.

> [!question]- Ein Trace beginnt mit `45`. Was bedeutet das?
> Version 4 (IPv4), IHL 5 → Header 20 Byte (keine Optionen).

> [!question]- Welche Bedeutung haben die drei Flag-Bits?
> Bit 0: reserviert (0). Bit 1 DF: 1 = nicht fragmentieren. Bit 2 MF: 1 = es folgen weitere Fragmente, 0 = letztes Fragment.

> [!question]- Wofür steht im Protokollfeld der Wert 6 bzw. 17?
> 6 = TCP, 17 (0x11) = UDP. 1 = ICMP.

> [!question]- Worüber wird die Header Checksum berechnet?
> Nur über den Header, nicht über die Nutzdaten.

> [!question]- Was passiert mit einem Paket mit DF = 1, das größer als die MTU ist?
> Der Router verwirft es (und meldet das per ICMP „Fragmentation needed“).

## Siehe auch
- [[IPv4-Header - Type of Service]]
- [[IPv4-Header - Time to Live]]
- [[IPv4-Fragmentierung]]
- [[Datenkapselung im TCP-IP-Modell]]
- [[Übung IPv4-Header Traceanalyse 1]] · [[Übung IPv4-Header Traceanalyse 2]]
