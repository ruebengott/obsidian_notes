---
tags: [berufsschule, englisch, netzwerk, topologie]
fach: Englisch
typ: thema
quelle: "[[Technisches Englisch.pdf#page=19]]"
datum:
status: zu-lernen
---
# Networks – Types and Topologies

> [!summary] Kurz & knapp
> Ein Netzwerk verbindet Computer und Geräte, um **Ressourcen zu teilen** (Speicher, Internetzugang, Drucker, Dienste). Netzwerke werden eingeteilt nach **geografischer Ausdehnung** (PAN, LAN, MAN, WAN), **Architektur** (client-server, peer-to-peer), **Topologie** (bus, star, ring, tree, mesh) und **Protokoll** (z. B. TCP/IP).

## Purpose of a network
> *The purpose of a network is to share resources, e.g. data storage, Internet access, printers or services.*

## Classification (aus der Network FAQ)
| Kriterium | Typen |
|---|---|
| **Geographical area** | **PAN** (Personal Area Network – Laptop, Smartphone) · **LAN** (ein Gebäude) · **MAN** (Metropolitan – Campus/Stadt) · **WAN** (Land/Kontinent) |
| **Architecture** | **client-server**: ein Server speichert und verteilt Daten an die Clients · **peer-to-peer**: alle Rechner sind gleichberechtigt, teilen Dateien/Peripherie ohne eigenen Server |
| **Topology / layout** | bus, star, ring (+ tree, mesh) |
| **Network protocol** | *the language, or set of rules, that computers use to communicate* – z. B. TCP/IP im Internet |

## Topologies
| Topology | Description | Advantages | Disadvantages |
|---|---|---|---|
| **Bus** | All computers are connected to one main cable (the bus). | cheap, little cable, easy to set up | cable break = whole network down; collisions; hard to troubleshoot |
| **Star** | All data flows through a central hub/switch. | easy to add devices; one broken cable affects only one device; easy troubleshooting | central switch is a single point of failure; more cable |
| **Ring** | All devices are connected to one another in a continuous loop. | ordered data flow, no collisions | one failure can break the ring; adding devices interrupts the network |
| **Tree** | Several star networks connected hierarchically (star of stars). | scalable, easy to extend and structure (e.g. per floor) | if a higher-level switch fails, the whole branch is down; more planning |
| **Mesh** | Devices are connected to many/all other devices. | very reliable (redundant paths), no single point of failure | expensive, lots of cabling, complex configuration |
| **Point-to-Multipoint** | One central system (base station) connects multiple hosts that share one line/channel (typisch bei Funknetzen). | one distributor, many receivers; cost-efficient (one base, less hardware); central administration; scalable – easy to add users | shared bandwidth; more devices reduce performance; high latency; interference from other frequencies; more planning; single point of failure |

> [!note] Point-to-Multipoint (deine Notizen, sprachlich korrigiert)
> Original handschriftlich: „more devices can cause worse interconnection“, „disturbed by other frequencies“ → besser: *More devices **can reduce performance**.* / *It **can be disturbed by interference** from other frequencies.*
> ![[Technisches Englisch.pdf#page=20]]

## Wired vs. wireless
| | Wired LAN | Wireless LAN |
|---|---|---|
| Medium | Ethernet cables, phone lines, fibre optic cables | electromagnetic (radio) waves |
| Pro | cheaper, faster, more reliable | mobility – you can **roam** between access points |
| Contra | more difficult to install | less secure, subject to interference |

Wireless network types (laut FAQ): Satellite (long distances), WiMAX (connecting Wi-Fi hotspots), Wi-Fi (medium range), Bluetooth (short distances), GSM (mobile phones – heute 4G/5G).

> [!tip] Merke
> **Star** ist heute Standard im LAN (mit Switch). **Mesh** = maximale Ausfallsicherheit, aber teuer. **Single point of failure** ist das typische Gegenargument bei allem, was zentral ist.

## Lernfragen
> [!question]- What does PAN stand for?
> Personal Area Network.

> [!question]- What is a network protocol?
> The language, or set of rules, that computers use to communicate with each other (e.g. TCP/IP).

> [!question]- Describe a star topology in English.
> *All devices are connected to a central switch (or hub); all data flows through this central point.*

> [!question]- Name one advantage and one disadvantage of a mesh topology.
> Advantage: very reliable/redundant. Disadvantage: expensive and complex to cable.

> [!question]- What is the difference between client-server and peer-to-peer?
> Client-server: one computer acts as a server and distributes information to clients. Peer-to-peer: all computers have the same capabilities and share resources without a separate server.

## Siehe auch
- [[Vokabeln Networks]]
- [[Übung Networks IT023]]
- [[Englisch - Übersicht]]
