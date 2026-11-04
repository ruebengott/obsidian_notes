---
tags: [berufsschule, lf3, ipv4-header, fragmentierung]
fach: LF3
typ: thema
quelle: "[[LF3.pdf#page=45]]"
datum:
status: zu-lernen
---
# IPv4-Fragmentierung

> [!summary] Kurz & knapp
> Ist ein IP-Paket größer als die **MTU** (Ethernet: 1500 Byte), wird es in **Fragmente** zerlegt. Jedes Fragment bekommt einen eigenen 20-Byte-Header mit **derselben Identification**, dem **MF-Flag** (weitere Fragmente folgen) und dem **Fragment Offset** (Position der Daten in 8-Byte-Einheiten).

## Beteiligte Header-Felder
| Feld | Funktion |
|---|---|
| Identification | gleiche Nummer in allen Fragmenten, damit der Empfänger sie zusammensetzen kann |
| Flags: DF (May Fragment) | 0 = Fragmentierung erlaubt, 1 = verboten |
| Flags: MF (More Fragments) | 1 = es folgen weitere Fragmente, 0 = **letztes** Fragment |
| Fragment Offset | Position der Nutzdaten im Originalpaket = Byte-Position **÷ 8** |
| Total Length | Länge des jeweiligen Fragments (Header + Daten) |

## Beispiel: Paket mit 4464 Byte über Ethernet
Originalpaket: 20 Byte Header + **4444 Byte** Daten = 4464 Byte. MTU = 1500 → pro Fragment max. 1500 − 20 = **1480 Byte** Daten (1480 ist durch 8 teilbar ✓).

4444 = 3 × 1480 + **4** → 4 Fragmente

| Fragment | Identifier | Reserved | DF (May Fragment) | MF (More Fragments) | Fragment Offset | Nutzdaten | Total Length |
|---|---|---|---|---|---|---|---|
| 1 | 321 | 0 | 0 | 1 | **0** | 1480 | 1500 |
| 2 | 321 | 0 | 0 | 1 | **185** | 1480 | 1500 |
| 3 | 321 | 0 | 0 | 1 | **370** | 1480 | 1500 |
| 4 | 321 | 0 | 0 | **0** (letztes) | **555** | 4 | 24 |

**Rechenweg Offset:** Nutzdaten ohne Header werden durch 8 geteilt.
- Fragment 1: beginnt immer bei 0
- Fragment 2: 1480 / 8 = **185**
- Fragment 3: 2960 / 8 = **370**
- Fragment 4: 4440 / 8 = **555**

Original mit Notizen: ![[LF3.pdf#page=45]]

> [!warning] Korrektur
> In der Mitschrift wurde in der Spalte „Paket Length“ 1500 zu 1480 korrigiert. Beides stimmt, gemeint ist aber Verschiedenes: Das Header-Feld **Total Length** enthält **1500** (20 Header + 1480 Daten). **1480** sind die **Nutzdaten** pro Fragment. Beim letzten Fragment ist Total Length = **24** (20 + 4 Daten).

> [!tip] Merke
> - Nutzdaten pro Fragment = MTU − IP-Header = 1500 − 20 = 1480 Byte
> - Offset = bisherige Datenbytes ÷ 8
> - Alle Fragmente: gleiche ID, MF = 1, nur das letzte hat MF = 0
> - Zusammengesetzt wird erst beim Empfänger

## Lernfragen
> [!question]- Ein Paket hat 3000 Byte Nutzdaten. In wie viele Fragmente wird es bei MTU 1500 geteilt und welche Offsets haben sie?
> 3000 = 1480 + 1480 + 40 → 3 Fragmente. Offsets: 0, 185, 370. MF: 1, 1, 0.

> [!question]- Warum steht im Fragment Offset 185 und nicht 1480?
> Der Offset wird in Einheiten von 8 Byte angegeben (13-Bit-Feld): 1480 / 8 = 185.

> [!question]- Woran erkennt der Empfänger, welche Fragmente zusammengehören?
> An der gleichen Identification-Nummer (sowie gleicher Quell-/Ziel-IP und gleichem Protokoll).

> [!question]- Woran erkennt man das letzte Fragment?
> Am MF-Flag = 0 bei einem Offset > 0.

## Siehe auch
- [[IPv4-Header]]
- [[Ethernet-Frame]] (MTU 1500 Byte)
- [[Übung IPv4-Header Traceanalyse 2]]
