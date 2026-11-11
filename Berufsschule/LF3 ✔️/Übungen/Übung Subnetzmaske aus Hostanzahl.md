---
tags: [berufsschule, lf3, übung, subnetting]
fach: LF3
typ: übung
quelle: "[[LF3.pdf#page=46]]"
datum:
status: zu-lernen
---
# Übung: Subnetzmaske ↔ CIDR ↔ Hostanzahl

Zusammengestellt aus den handschriftlichen Rechennotizen (PDF-Seite 36 und 46): ![[LF3.pdf#page=46]]

## Aufgaben
1. Wie lautet die Subnetzmaske zu **/18** in Dezimalschreibweise?
2. Wie viele Hosts passen in ein Netz mit der Maske **255.255.255.128**?
3. Der Hostanteil soll **8 Bit** groß sein (2⁸ = 256 Adressen). Präfix und Maske?
4. Der Hostanteil soll **4 Bit** groß sein (2⁴ = 16 Adressen). Präfix, Maske und Hostanzahl?
5. Der Hostanteil soll **2 Bit** groß sein. Präfix, Maske und Hostanzahl? Wofür nutzt man solche Netze?
6. Rechne `121 + 87` und gib das Ergebnis binär an.

> [!success]- Lösungen mit Rechenweg
> **1.** /18 = 8 + 8 + 2 Einsen → 3. Oktett `11000000` = 128 + 64 = 192 → **255.255.192.0**
>
> **2.** 128 = `10000000` → 25 Netzbits, 7 Hostbits → 2⁷ − 2 = **126 Hosts**
>
> **3.** 32 − 8 = **/24** → **255.255.255.0** (254 Hosts)
>
> **4.** 32 − 4 = **/28** → 4. Oktett `11110000` = 128+64+32+16 = **240** → 255.255.255.240, 2⁴ − 2 = **14 Hosts**
>
> **5.** 32 − 2 = **/30** → `11111100` = **252** → 255.255.255.252, 2² − 2 = **2 Hosts** → typisch für Punkt-zu-Punkt-Verbindungen zwischen zwei Routern (Transfernetze).
>
> **6.** 121 + 87 = **208** = `11010000` (128 + 64 + 16)

> [!warning] Korrektur
> In den Notizen standen „222.255.255.152“ und „225.255.255.128“. Gemeint ist jeweils **255**.255.255.…, denn ein Masken-Oktett vor dem „interessanten“ Oktett ist immer 255. Außerdem ist **152** (`10011000`) **keine gültige** Maskenzahl, weil die Einsen nicht zusammenhängen. Gültig sind nur 128, 192, 224, 240, 248, 252, 254, 255. Vermutlich war **192** gemeint (255.255.255.192 = /26, 62 Hosts).

## Siehe auch
- [[Subnetzmaske und CIDR-Notation]]
- [[Zahlensysteme Binär Dezimal Hexadezimal]]
