---
tags: [berufsschule, lf3, übung, netzbestimmung, subnetting]
fach: LF3
typ: übung
quelle: "[[LF3.pdf#page=17]]"
datum: 2025-11-03
status: zu-lernen
---
# Übung: Netzbestimmung 192.168.53.173 / 255.255.224.0

## Aufgabe
IPv4-Adresse: **192.168.53.173**, Subnetzmaske: **255.255.224.0**
Bestimme CIDR, Hostanzahl, Netzadresse, erste Hostadresse, Broadcastadresse und letzte Hostadresse.

> [!success]- Lösung mit Rechenweg
> **Subnetzmaske binär:** `11111111.11111111.111|00000.00000000`
> Netzbits: **19**, Hostbits: **13** → **CIDR: 192.168.53.173/19**
>
> **Hostanzahl:** 2¹³ − 2 = 8192 − 2 = **8190**
>
> **Netzadresse** (alle Hostbits = 0):
> 192.168.53.173 = `11000000.10101000.001|10101.10101101`. Im 3. Oktett trennen sich Netz- und Hostanteil.
> Netzadresse = `11000000.10101000.001|00000.00000000` = **192.168.32.0**
>
> **Erste Hostadresse:** Netzadresse + 1 = **192.168.32.1**
>
> **Broadcastadresse** (alle Hostbits = 1):
> `11000000.10101000.001|11111.11111111` → 3. Oktett 00111111 = 63 → **192.168.63.255**
>
> **Letzte Hostadresse:** **192.168.63.254**
>
> **Probe:** Blockgröße 256 − 224 = 32 → Netze 0, **32**, 64 … → 53 liegt in 32–63 ✓

## Siehe auch
- [[Netzbestimmung in 6 Schritten]]
- [[Übung Netzbestimmung 172.16.209.250-21]]
