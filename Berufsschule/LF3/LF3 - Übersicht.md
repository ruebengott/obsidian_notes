---
tags: [berufsschule, lf3]
fach: LF3
typ: übersicht
quelle: "[[LF3.pdf]]"
---
# LF3 – Clients in Netzwerke einbinden

← [[Berufsschule]]

> [!info] Lernfeld-Infos
> - **Lehrer:** Helge Repenning – h.repenning@bbz-nok.de (Duzen ist okay)
> - **Schule:** BBZ am Nord-Ostsee-Kanal, Schuljahr 2025/26
> - **Quelle:** OneNote-Export [[LF3.pdf]] (61 Seiten inkl. Arbeitsblätter, Folien, Tafelbilder)

## 1. Grundlagen
- [[Zahlensysteme Binär Dezimal Hexadezimal]]: Binär, Dezimal, Hex sowie Umrechnung per 8-4-2-1 und Restwertverfahren
- [[OSI-Schichtenmodell]]: 7 Schichten, welche Adressen, Geräte und Protokolle wohin gehören
- [[Datenkapselung im TCP-IP-Modell]]: IP-Paket als Nutzlast des Ethernet-Frames

## 2. Sicherungsschicht (Schicht 2)
- [[MAC-Adresse]]: 48-Bit-Hardwareadresse, Aufbau aus I/G, U/L, OUI und OUA
- [[MAC-Adresse - Darstellung und kanonische Form]]: Hex-Schreibweise, Oktette spiegeln, LSB first
- [[MAC-Broadcast und Multicast]]: FF-FF-FF-FF-FF-FF, Rundruf bei der Anmeldung, Broadcast-Sturm
- [[MAC-Randomisierung]]: zufällige MAC-Adressen gegen WLAN-Tracking
- [[Ethernet-Frame]]: Präambel, SFD, MACs, VLAN-Tag, Typ, Daten, PAD, FCS
- [[VLAN]]: ein physischer Switch, mehrere logische Netze; Access- vs. Trunk-Line

## 3. Vermittlungsschicht (Schicht 3)
- [[IPv4-Adresse vs. MAC-Adresse]]: Vergleichstabelle der beiden Adressarten
- [[Subnetzmaske und CIDR-Notation]]: Netz- und Hostanteil, /-Schreibweise, Hostanzahl
- [[Netzbestimmung in 6 Schritten]]: CIDR, Hosts, Netzadresse, erste Host, Broadcast, letzte Host
- [[Private und reservierte IPv4-Adressen]]: RFC 1918, Loopback, APIPA, Multicast
- [[Subnetting]]: Netze aufteilen, Vorteile, Beispiel 192.168.1.0/24 → 8 × /27
- [[Routing und Default Route]]: Routingtabelle, Next Hop, 0.0.0.0/0, `route print`
- [[IPv4-Header]]: alle Felder, Flags, Protokollnummern, Optionen
- [[IPv4-Header - Type of Service]]: Priorisierung, DSCP/QoS
- [[IPv4-Header - Time to Live]]: Hop-Zähler, Start-TTL der Betriebssysteme
- [[IPv4-Fragmentierung]]: MF/DF, Fragment Offset, Rechenbeispiel

## 4. Transportschicht (Schicht 4)
- [[UDP]]: verbindungslos, 8-Byte-Header, Ports, Einsatzgebiete
- [[TCP-Header]]: Sequence/Ack Number, Flags, Window, 3-Way-Handshake

## 5. Anwendungsschicht (Schicht 7)
- [[DHCP]]: automatische IP-Konfiguration, DORA
- [[DHCP-Starvation-Angriff]]: Rogue DHCP, Fake-DNS, Phishing
- [[DNS]]: Namensauflösung, Ablauf einer Abfrage, Vorteile
- [[URL, Domain und Hostname]]: Bestandteile einer URL

## Übungen
| Übung | Thema |
|---|---|
| [[Übung Netzbestimmung 172.16.209.250-21]] | Netzbestimmung /21 |
| [[Übung Netzbestimmung 192.168.53.173-19]] | Netzbestimmung /19 |
| [[Übung Subnetzmaske aus Hostanzahl]] | Maske ↔ CIDR ↔ Hosts |
| [[Übung Subnetting Patiententrakt]] | Subnetz planen und Fehler finden (Krankenhaus) |
| [[Übung Fehlersuche Netzplan Autohaus Reihbach]] | 7 Konfigurationsfehler finden |
| [[Übung Fehlersuche Netzplan Schulen N-Stadt]] | Konfigurationsfehler finden |
| [[Übung IPv4-Header Traceanalyse 1]] | Hex-Trace auswerten (ICMP) |
| [[Übung IPv4-Header Traceanalyse 2]] | Hex-Trace auswerten (TCP, MF-Bit) |
| [[Übung Fragebogen UDP]] | 7 Fragen zu UDP |
| [[Übung DHCP-Aufgaben]] | 14 Fragen zu DHCP (Ports, Relay, DECLINE, APIPA, Starvation) |

