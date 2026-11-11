---
tags: [berufsschule, lf3, zahlensysteme]
fach: LF3
typ: thema
quelle: "[[LF3.pdf#page=9]]"
datum: 2025-09-22
status: zu-lernen
---
# Zahlensysteme: Binär, Dezimal, Hexadezimal

> [!summary] Kurz & knapp
> Netzwerkadressen (MAC, IPv4, Header-Traces) werden binär gespeichert, aber meist hexadezimal oder dezimal dargestellt. Ein Hex-Zeichen entspricht genau 4 Bit (1 Nibble), zwei Hex-Zeichen entsprechen 1 Byte (Oktett).

## Die drei Systeme

| System | Basis | Ziffern | Schreibweise |
|---|---|---|---|
| Dezimal | 10 | 0–9 | 5₁₀, 5DEZ |
| Hexadezimal | 16 | 0–9, A–F | 5₁₆, 5HEX, 0x5 |
| Binär (dual) | 2 | 0, 1 | 1₂, 1dual |

Das Hexadezimalsystem hat **16 Ziffern** (0–F):

| Hex | Dez | Binär | | Hex | Dez | Binär |
|---|---|---|---|---|---|---|
| 0 | 0 | 0000 | | 8 | 8 | 1000 |
| 1 | 1 | 0001 | | 9 | 9 | 1001 |
| 2 | 2 | 0010 | | A | 10 | 1010 |
| 3 | 3 | 0011 | | B | 11 | 1011 |
| 4 | 4 | 0100 | | C | 12 | 1100 |
| 5 | 5 | 0101 | | D | 13 | 1101 |
| 6 | 6 | 0110 | | E | 14 | 1110 |
| 7 | 7 | 0111 | | F | 15 | 1111 |

**1 Oktett = 8 Bit = 1 Byte = 2 Hex-Zeichen**

## Binär ↔ Hex (8-4-2-1-Methode)
Jede 4er-Gruppe wird mit den Stellenwerten **8 4 2 1** addiert:
- `1111` = 8+4+2+1 = 15 = **F**
- DE₁₆ in Bitfolge: D = 13 = `1101`, E = 14 = `1110` → **`1101 1110`**

## Hex → Dezimal
Jede Stelle mit ihrer Potenz von 16 multiplizieren und addieren:
- 55₁₆ = 5·16¹ + 5·16⁰ = 80 + 5 = **85₁₀**
- A3₁₆ = 10·16¹ + 3·16⁰ = 160 + 3 = **163₁₀**

## Dezimal → Hex (Restwertverfahren)
Die Dezimalzahl immer wieder durch 16 teilen und den Rest notieren. Die Reste **von unten nach oben** gelesen ergeben die Hexzahl.

Beispiel 50.370₁₀:

| Rechnung | Ergebnis | Rest |
|---|---|---|
| 50370 : 16 | 3148 | 2 |
| 3148 : 16 | 196 | 12 = C |
| 196 : 16 | 12 | 4 |
| 12 : 16 | 0 | 12 = C |

→ **C4C2₁₆** (Probe: 12·4096 + 4·256 + 12·16 + 2 = 50370 ✓)

> [!tip] Rest mit dem Taschenrechner
> Die Nachkommastellen mal 16 nehmen. Beispiel: 50370 / 16 = 3148,125 → 0,125 · 16 = **2**.

> [!tip] Merke
> - Hex hat 16 Ziffern: 0–9 und A (10) bis F (15).
> - 4 Bit = 1 Hex-Zeichen, 8 Bit = 2 Hex-Zeichen = 1 Byte.
> - Dez → Hex: durch 16 teilen, Reste von unten nach oben lesen.
> - Ein Oktett geht von 0 bis 255 (dezimal) bzw. von 00 bis FF (hex).

## Lernfragen
> [!question]- Wie viele Ziffern hat das Hexadezimalsystem und welche?
> 16 Ziffern: 0–9 und A–F (A=10 … F=15).

> [!question]- Wandle C0₁₆ in Dezimal und Binär um.
> C0 = 12·16 + 0 = 192₁₀ = 1100 0000₂.

> [!question]- Wandle 233₁₀ in Hex um.
> 233 : 16 = 14 Rest 9; 14 : 16 = 0 Rest 14 (E) → **E9₁₆**.

> [!question]- Wie viele Bit stellt ein Hex-Zeichen dar?
> 4 Bit (ein Nibble). Zwei Hex-Zeichen ergeben ein Byte.

> [!question]- Was ist der größte Wert eines Oktetts in dezimal, hex und binär?
> 255 = FF = 1111 1111.

## Siehe auch
- [[MAC-Adresse - Darstellung und kanonische Form]]
- [[Subnetzmaske und CIDR-Notation]]
- [[Übung IPv4-Header Traceanalyse 1]]
