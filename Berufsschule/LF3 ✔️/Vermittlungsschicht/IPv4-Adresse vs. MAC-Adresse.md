---
tags: [berufsschule, lf3, ipv4, mac-adresse]
fach: LF3
typ: thema
quelle: "[[LF3.pdf#page=23]]"
datum: 2025-11-28
status: zu-lernen
---
# IPv4-Adresse vs. MAC-Adresse

> [!summary] Kurz & knapp
> Die **MAC-Adresse** (48 Bit, hex, Schicht 2) ist fest an die Hardware gebunden und adressiert Geräte **im lokalen Netz**. Die **IPv4-Adresse** (32 Bit, dezimal, Schicht 3) ist logisch, veränderbar und ermöglicht das **Routing zwischen Netzen**.

## Vergleichstabelle

| Merkmal | MAC-Adresse | IPv4-Adresse |
|---|---|---|
| ausgeschrieben | Media Access Control | Internet Protocol Version 4 |
| Bit | 48 | 32 |
| Bytes / Oktette | 6 | 4 |
| Zahlensystem | hexadezimal | dezimal |
| Schreibweise | 6 zweistellige Hex-Blöcke, getrennt durch Bindestrich (besser) oder Doppelpunkt | 4 durch Punkte getrennte Dezimalzahlen von 0–255 |
| Struktur | Herstellercode / lfd. Nr. (Geräte-ID): `XX-XX-XX-YY-YY-YY` | `XXX.XXX.XXX.XXX`: Netzanteil / Hostanteil (privat / öffentlich) |
| größte Zahl | FF-FF-FF-FF-FF-FF | 255.255.255.255 |
| OSI-Schicht | 2 | 3 |
| Adressierungsmöglichkeiten | 2⁴⁸ ≈ 281,5 Billionen | 2³² ≈ 4,3 Milliarden |
| Vergabe | durch den Hersteller der Netzwerkkarte | öffentlich: IANA (in Europa über RIPE und Provider); fest: durch Nutzer/Administrator; automatisch: per DHCP |
| Art und Veränderbarkeit | der Hardware physikalisch fest zugeordnet (in der Regel unveränderbar) | manuell in den Netzwerkeinstellungen oder automatisch (DHCP über Router, VPN-Dienst) veränderbar |
| Vorkommen | im Netzwerk und weltweit einmalig | in jedem Netzwerk einmalig (private Adressen wiederholen sich in anderen Netzen) |
| Aufgaben | Adressierung von Datenpaketen im lokalen Netz; Zugriffskontrolle von Hosts (z. B. MAC-Filter); Kennzeichnung von Netzwerkkarte und Hersteller | Adressierung und Kommunikation von Geräten; **Routing** von Datenpaketen zwischen Netzen; ermöglicht Subnetze |

> [!info] Zusammenspiel
> Für die Zustellung im LAN braucht ein Frame die MAC-Adresse des Ziels. Die passende MAC-Adresse zu einer IPv4-Adresse ermittelt **ARP** (Address Resolution Protocol, EtherType 0x0806). Liegt das Ziel in einem anderen Netz, wird der Frame an die MAC-Adresse des **Gateways** (Router) geschickt.

> [!tip] Merke
> - MAC: 48 Bit, hex, Schicht 2, fest, lokal
> - IPv4: 32 Bit, dezimal, Schicht 3, logisch, routbar
> - Beim Routing ändern sich die MAC-Adressen von Hop zu Hop, die IP-Adressen (Quelle/Ziel) bleiben gleich (ohne NAT).

## Lernfragen
> [!question]- Nenne vier Unterschiede zwischen MAC- und IPv4-Adresse.
> Länge (48 vs. 32 Bit), Darstellung (hex vs. dezimal), OSI-Schicht (2 vs. 3), Vergabe (Hersteller vs. IANA/Admin/DHCP), Veränderbarkeit (fest vs. veränderbar), Aufgabe (lokale Zustellung vs. Routing).

> [!question]- Wie viele Adressen sind mit IPv4 möglich?
> 2³² ≈ 4,3 Milliarden.

> [!question]- Welches Protokoll ermittelt zu einer IPv4-Adresse die MAC-Adresse?
> ARP (Address Resolution Protocol).

> [!question]- Welche Adresse ändert sich auf dem Weg eines Pakets durch mehrere Router?
> Die MAC-Adressen (Quelle/Ziel pro Teilstrecke). Die IP-Adressen bleiben gleich, sofern kein NAT eingesetzt wird.

## Siehe auch
- [[MAC-Adresse]]
- [[Subnetzmaske und CIDR-Notation]]
- [[Private und reservierte IPv4-Adressen]]
- [[OSI-Schichtenmodell]]
