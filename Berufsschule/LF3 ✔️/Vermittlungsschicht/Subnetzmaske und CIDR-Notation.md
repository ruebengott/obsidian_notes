---
tags: [berufsschule, lf3, ipv4, subnetting]
fach: LF3
typ: thema
quelle: "[[LF3.pdf#page=15]]"
datum: 2025-11-03
status: zu-lernen
---
# Subnetzmaske und CIDR-Notation

> [!summary] Kurz & knapp
> Die **Subnetzmaske** kennzeichnet, welcher Teil einer IPv4-Adresse zum **Netz** gehört (Bits = 1) und welcher zum **Host** (Bits = 0). Die **CIDR-Notation** (Classless Inter-Domain Routing) ist die Kurzschreibweise: Man gibt die Anzahl der Netzbits an, z. B. `/21`.

## Prinzip
Die Einsen stehen immer zusammenhängend links, die Nullen rechts.

| Dezimal | Binär | CIDR |
|---|---|---|
| 255.255.248.0 | **11111111.11111111.11111**000.00000000 | /21 |
| 255.255.224.0 | **11111111.11111111.111**00000.00000000 | /19 |
| 255.255.255.0 | **11111111.11111111.11111111**.00000000 | /24 |
| 255.255.255.224 | **11111111.11111111.11111111.111**00000 | /27 |

- **Netzbits** (1en) = CIDR-Präfix, z. B. 21
- **Hostbits** (0en) = 32 − Präfix, z. B. 11
- Schreibweise: `172.16.209.250/21`

## Mögliche Werte eines Masken-Oktetts

| Binär | Dezimal | Bits im Oktett |
|---|---|---|
| 10000000 | 128 | 1 |
| 11000000 | 192 | 2 |
| 11100000 | 224 | 3 |
| 11110000 | 240 | 4 |
| 11111000 | 248 | 5 |
| 11111100 | 252 | 6 |
| 11111110 | 254 | 7 |
| 11111111 | 255 | 8 |

Stellenwerte zum Addieren: **128 64 32 16 8 4 2 1**

## Hostanzahl
**Hosts = 2^Hostbits − 2**
Abgezogen werden die **Netzadresse** (alle Hostbits 0) und die **Broadcastadresse** (alle Hostbits 1).

| CIDR | Maske | Hostbits | Hosts | Blockgröße |
|---|---|---|---|---|
| /30 | 255.255.255.252 | 2 | 2 | 4 |
| /29 | 255.255.255.248 | 3 | 6 | 8 |
| /28 | 255.255.255.240 | 4 | 14 | 16 |
| /27 | 255.255.255.224 | 5 | 30 | 32 |
| /26 | 255.255.255.192 | 6 | 62 | 64 |
| /25 | 255.255.255.128 | 7 | 126 | 128 |
| /24 | 255.255.255.0 | 8 | 254 | 256 |
| /22 | 255.255.252.0 | 10 | 1022 | 4 (im 3. Oktett) |
| /21 | 255.255.248.0 | 11 | 2046 | 8 (im 3. Oktett) |
| /19 | 255.255.224.0 | 13 | 8190 | 32 (im 3. Oktett) |

## Rückwärts: von der benötigten Größe zur Maske
1. Benötigte Hostbits bestimmen: kleinstes n mit 2ⁿ − 2 ≥ benötigte Hosts
2. Präfix = 32 − n
3. In Dezimal umwandeln

Beispiel (aus den Notizen): 2⁴ = 16 → 32 − 4 = **/28** → 255.255.255.**240** · 2² → 32 − 2 = **/30** → 255.255.255.**252** · 2⁸ = 256 → 32 − 8 = **/24** → 255.255.255.0

> [!tip] Merke
> - 1 = Netzanteil, 0 = Hostanteil
> - Hosts = 2^(32−Präfix) − 2
> - Blockgröße im „interessanten“ Oktett = 256 − Maskenwert (z. B. 256 − 224 = 32)
> - /30 (2 Hosts) wird typisch für Router-zu-Router-Verbindungen genutzt

## Lernfragen
> [!question]- Wandle 255.255.248.0 in die CIDR-Notation um.
> 11111111.11111111.11111000.00000000 → 21 Einsen → **/21**.

> [!question]- Wie viele Hosts passen in ein /27-Netz?
> 2⁵ − 2 = **30**.

> [!question]- Warum zieht man bei der Hostanzahl 2 ab?
> Die Netzadresse (alle Hostbits 0) und die Broadcastadresse (alle Hostbits 1) dürfen nicht an Hosts vergeben werden.

> [!question]- Welche Subnetzmaske braucht man für mindestens 100 Hosts?
> 2⁷ − 2 = 126 ≥ 100 → 7 Hostbits → /25 = **255.255.255.128**.

> [!question]- Wofür steht CIDR?
> Classless Inter-Domain Routing. Damit sind Netze ohne feste Klassengrenzen möglich, die Präfixlänge ist frei wählbar.

## Siehe auch
- [[Netzbestimmung in 6 Schritten]]
- [[Subnetting]]
- [[Übung Subnetzmaske aus Hostanzahl]]
- [[Zahlensysteme Binär Dezimal Hexadezimal]]
