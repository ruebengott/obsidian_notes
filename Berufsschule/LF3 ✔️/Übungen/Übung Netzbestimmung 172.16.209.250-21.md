---
tags: [berufsschule, lf3, übung, netzbestimmung, subnetting]
fach: LF3
typ: übung
quelle: "[[LF3.pdf#page=15]]"
datum: 2025-11-03
status: zu-lernen
---
# Übung: Netzbestimmung 172.16.209.250 / 255.255.248.0

## Aufgabe
„172.16.209.250 hat mein Laptop als IPv4-Adresse bekommen, dazu die Subnetzmaske 255.255.248.0.“
Bestimme für dieses Schulnetz:
1. die Subnetzmaske in CIDR-Notation
2. die Anzahl der möglichen Geräte (Hosts)
3. die Netzadresse (wird für das Routing zwischen Netzen benötigt)
4. die erste Hostadresse (wird meistens für das Gateway benutzt)
5. die Broadcastadresse (wird für die Anmeldung im Netz benötigt)
6. die letzte Hostadresse

> [!success]- Lösung mit Rechenweg
> **Zu 1: CIDR**
> 255.255.248.0 = `11111111.11111111.11111|000.00000000` (| = Grenze Netz-/Hostanteil)
> 21 Bits sind 1 → **/21**. Hostanteil: 32 − 21 = **11 Bit**.
> Schreibweise: 172.16.209.250/21
>
> **Zu 2: Hostanzahl**
> 2¹¹ − 2 = 2048 − 2 = **2046 Hosts** (minus Netz- und Broadcastadresse)
>
> **Zu 3: Netzadresse** (alle Hostbits = 0)
> | | 1. Oktett | 2. Oktett | 3. Oktett | 4. Oktett |
> |---|---|---|---|---|
> | IP | 10101100 | 00010000 | 11010\|001 | 11111010 |
> | Netzadresse | 10101100 | 00010000 | 11010\|000 | 00000000 |
> → **172.16.208.0**
>
> **Zu 4: erste Hostadresse** = Netzadresse + 1 → **172.16.208.1**
>
> **Zu 5: Broadcastadresse** (alle Hostbits = 1)
> | | 1. Oktett | 2. Oktett | 3. Oktett | 4. Oktett |
> |---|---|---|---|---|
> | Broadcast | 10101100 | 00010000 | 11010\|111 | 11111111 |
> 11010111 = 215 → **172.16.215.255**
>
> **Zu 6: letzte Hostadresse** = Broadcast − 1 → **172.16.215.254**
>
> **Probe über die Blockgröße:** 256 − 248 = 8 → Netze im 3. Oktett: …, 200, **208**, 216 … → 209 liegt in 208–215 ✓

> [!note] Hinweis zur Vorlage
> Im Original ist die binäre Broadcastadresse versehentlich mit „Netzadresse binär“ beschriftet. Die Werte selbst sind korrekt.

## Siehe auch
- [[Netzbestimmung in 6 Schritten]]
- [[Subnetzmaske und CIDR-Notation]]
- [[Übung Netzbestimmung 192.168.53.173-19]]
