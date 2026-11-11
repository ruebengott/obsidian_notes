---
tags: [berufsschule, lf3, übung, subnetting, netzbestimmung]
fach: LF3
typ: übung
quelle: "[[LF3.pdf#page=29]]"
datum: 2025-11-17
status: zu-lernen
---
# Übung: Subnetting Krankenhaus – Patiententrakt IV

## Ausgangslage
Netzplan eines Krankenhauses mit den Patiententrakten I–III. Jeder Trakt hat einen Switch mit Clients, einem Netzwerkdrucker und einem Server, die Trakte sind über einen gemeinsamen Router verbunden.

| Trakt | Subnetz | Gateway |
|---|---|---|
| Patiententrakt I | 192.168.1.32/27 | 192.168.1.33 |
| Patiententrakt II | 192.168.1.96/27 | 192.168.1.97 |
| Patiententrakt III | 192.168.1.160/27 | 192.168.1.161 |

![[LF3.pdf#page=29]]

## Aufgabe 1
Die Klinik wird um einen **Patiententrakt IV** erweitert (1 Server, 1 Netzwerkdrucker, 4 Clients). Plane die Netzanbindung und gib für das Subnetz an: dezimale Subnetzmaske, maximale Hostanzahl, Netzadresse, erste Hostadresse, Broadcastadresse und letzte Hostadresse.

> [!success]- Lösung Aufgabe 1
> Alle Trakte nutzen /27 → 192.168.1.0/24 in 8 Blöcke à 32. Belegt sind .32, .96 und .160. Frei sind .0, .64, .128, **.192** und .224.
> Gewählt: **192.168.1.192/27**
>
> | Angabe | Wert |
> |---|---|
> | Subnetzmaske | **255.255.255.224** (/27) |
> | max. Hostanzahl | 2⁵ − 2 = **30** (benötigt: 6 ✓) |
> | Netzadresse | **192.168.1.192** |
> | erste Hostadresse (Gateway) | **192.168.1.193** |
> | Broadcastadresse | **192.168.1.223** |
> | letzte Hostadresse | **192.168.1.222** |
>
> Auch .0/27, .64/27, .128/27 oder .224/27 wären richtig gewesen, solange sich das Subnetz nicht mit den anderen überschneidet.

## Aufgabe 2
Im Patiententrakt III hat der Administrator die Clients 1 und 2 erneuert:

| | Client 1 | Client 2 |
|---|---|---|
| IP-Adresse | 192.168.1.191/27 | 192.168.1.169 |
| Netzmaske | (/27) | 255.255.255.240 |
| Standardgateway | 192.168.1.161 | 192.168.1.161 |

Beide Clients können **nicht** auf den Netzwerkdrucker 192.168.1.190/27 zugreifen. Nenne jeweils die erforderliche Änderung.

> [!success]- Lösung Aufgabe 2
> Trakt III: 192.168.1.160/27 → Hosts .161–.190, Broadcast **.191**
>
> **Client 1:** 192.168.1.191 ist die **Broadcastadresse** des Subnetzes und darf nicht an einen Host vergeben werden. Ändern auf eine freie Hostadresse, z. B. **192.168.1.162**.
>
> **Client 2:** Die Maske 255.255.255.240 (/28) ist falsch. Damit liegt der Client im Netz 192.168.1.160/28 (Hosts .161–.174). Der Drucker .190 liegt aus seiner Sicht in einem fremden Netz. Die Maske muss **/27 = 255.255.255.224** sein.

## Aufgabe 3
Erstelle das Netz für alle vier Patiententrakte mit **Cisco Packet Tracer**.
*(Praktische Aufgabe, keine Lösung im Material.)*

## Siehe auch
- [[Subnetting]]
- [[Netzbestimmung in 6 Schritten]]
- [[Subnetzmaske und CIDR-Notation]]
