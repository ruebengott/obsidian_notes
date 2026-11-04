---
tags: [berufsschule, lf3, mac-adresse, schicht-2, zahlensysteme]
fach: LF3
typ: thema
quelle: "[[LF3.pdf#page=7]]"
datum: 2025-09-29
status: zu-lernen
---
# MAC-Adresse: Darstellung und kanonische Form

> [!summary] Kurz & knapp
> Eine MAC-Adresse lässt sich als 48-Bit-Folge oder in **kanonischer Form** (6 Hex-Paare, z. B. `AC-DE-48-00-00-80`) darstellen. Ethernet überträgt jedes Oktett mit dem **niederwertigsten Bit zuerst**. Deshalb muss man ein Oktett aus der übertragenen Bitfolge vor der Umwandlung in Hex **spiegeln**.

## Kanonische Form
- Die 48 Bit werden in **6 Oktette** zu je 8 Bit geteilt.
- Jedes Oktett wird als **zweistellige Hexzahl** geschrieben.
- Die Paare werden durch **Bindestriche** getrennt. Doppelpunkte sind ebenfalls üblich (`AC:DE:48:00:00:80`), können aber mit IPv6-Adressen verwechselt werden.

## Bitfolge (Übertragungsreihenfolge) → kanonische Form
Auf der Leitung kommt pro Oktett zuerst das niederwertigste Bit (LSB first). Um von der übertragenen Bitfolge zur Hex-Schreibweise zu kommen:
1. Bitfolge in Oktette aufteilen
2. Jedes Oktett **umdrehen (spiegeln)**
3. Jede Hälfte (4 Bit) in eine Hex-Ziffer umwandeln

**Beispiel:** `00110101` → gespiegelt `10101100` → `[1010][1100]` → **AC**

| | Bitfolge (Übertragung) | Kanonische Form |
|---|---|---|
| Beispiel 1 | 00110101 01111011 00010010 00000000 00000000 00000001 | AC-DE-48-00-00-80 |
| Beispiel 2 | 01001000 00101100 01101010 00011110 01011001 00111101 | 12-34-56-78-9A-BC |

> [!example]- Rechenweg Beispiel 2 (zum Nachprüfen)
> | Oktett | gespiegelt | Hex |
> |---|---|---|
> | 01001000 | 00010010 | 12 |
> | 00101100 | 00110100 | 34 |
> | 01101010 | 01010110 | 56 |
> | 00011110 | 01111000 | 78 |
> | 01011001 | 10011010 | 9A |
> | 00111101 | 10111100 | BC |

## Folge für I/G- und U/L-Bit
Das „erste“ und „zweite“ Bit der MAC-Adresse sind die ersten beiden **übertragenen** Bits. In kanonischer Hex-Form sind das die **zwei niederwertigsten Bits des ersten Oktetts**:

| 2. Hex-Ziffer des 1. Oktetts | Bedeutung |
|---|---|
| 0, 4, 8, C | Unicast, universell (Herstelleradresse) |
| 2, 6, A, E | Unicast, lokal verwaltet (z. B. zufällige MAC) |
| 1, 5, 9, D | Multicast, universell |
| 3, 7, B, F | Multicast, lokal (z. B. Broadcast FF) |

Beispiel: `AC-DE-48-…`: AC = 1010 11**00** → I/G = 0, U/L = 0 → universelle Unicast-Adresse.

## Warum erscheint eine MAC-Adresse manchmal „rückwärts“?
In der Mitschrift wurde das mit der **Endianness** erklärt (Byte-Reihenfolge im Speicher):
- **Big Endian:** höchstwertiges Byte zuerst, wie man es liest
- **Little Endian:** niederwertigstes Byte zuerst, z. B. bei x86-Prozessoren. `00:1A:2B:3C:4D:5E` kann im Speicher als `5E:4D:3C:2B:1A:00` liegen, wenn ein Programm die Adresse als Integer speichert und ohne Umrechnung ausgibt.

Ob eine Adresse „rückwärts“ erscheint, hängt also davon ab, wie sie gespeichert, ausgelesen und dargestellt wird (Tool, Treiber, API).

> [!warning] Korrektur
> Die Endianness-Erklärung (sie stammt aus einer KI-Antwort) trifft nur auf die **Byte**-Reihenfolge in Programmen zu. Für Netzwerktechnik/Prüfung entscheidend ist die **Bit**-Reihenfolge: Ethernet überträgt jedes Oktett *LSB first*. Deshalb wird **jedes Oktett einzeln gespiegelt**, nicht die Reihenfolge der Bytes umgedreht. Das ist der Unterschied zwischen „physikalischer“ (übertragener) und „kanonischer“ Form.

> [!tip] Merke
> - Kanonische Form: 6 Hex-Paare, getrennt durch Bindestrich (oder Doppelpunkt).
> - Bitfolge → Hex: **jedes Oktett spiegeln**, dann in 4er-Gruppen in Hex umwandeln.
> - I/G und U/L stehen in kanonischer Form in den beiden **niederwertigsten** Bits des ersten Oktetts.

## Lernfragen
> [!question]- Wandle die übertragene Bitfolge `00110101` in die kanonische Hex-Form um.
> Spiegeln: 10101100 → 1010 = A, 1100 = C → **AC**.

> [!question]- Warum muss man das Oktett vor der Umrechnung spiegeln?
> Ethernet sendet jedes Byte mit dem niederwertigsten Bit zuerst. Die Bitfolge auf der Leitung ist pro Oktett also umgekehrt zur üblichen Schreibweise.

> [!question]- Ist `02-00-5E-12-34-56` eine universelle oder lokal verwaltete Adresse?
> 02 = 0000 00**10** → U/L-Bit = 1 → lokal verwaltet. Das I/G-Bit ist 0, es ist also eine Unicast-Adresse.

> [!question]- Warum sind Bindestriche als Trennzeichen besser als Doppelpunkte?
> Doppelpunkte werden auch bei IPv6-Adressen verwendet, man könnte beides verwechseln.

## Siehe auch
- [[MAC-Adresse]]
- [[Zahlensysteme Binär Dezimal Hexadezimal]]
- [[Ethernet-Frame]] (Präambel/SFD werden ebenfalls LSB-first übertragen)
