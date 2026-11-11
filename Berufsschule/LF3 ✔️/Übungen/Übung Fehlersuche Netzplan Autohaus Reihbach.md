---
tags: [berufsschule, lf3, übung, fehlersuche, subnetting]
fach: LF3
typ: übung
quelle: "[[LF3.pdf#page=34]]"
datum:
status: zu-lernen
---
# Übung: Fehlersuche im Netzplan des Autohauses „Reihbach und Sohn KG“

## Aufgabe 2
Das Autohaus „Reihbach und Sohn KG“ hat Probleme mit seinem Computernetz, einige Clients haben Verbindungsprobleme. Finde mithilfe des Netzwerkplans die Konfigurationsfehler und mache Korrekturvorschläge. Der erste Fehler ist bereits eingetragen. Finde die **weiteren sechs Fehler**.

![[LF3.pdf#page=34]]

### Netzplan (abgetippt)
**LAN 1 (Switch 1)**, Router1-Interface 192.168.1.33/27

| Gerät | IP-Adresse | Gateway | Maske |
|---|---|---|---|
| PC 1 | 192.168.1.56 | 192.168.1.33 | 255.255.255.224 |
| PC 2 | 192.168.1.68 | 192.168.1.33 | 255.255.255.224 |
| Server | 192.168.1.35 | 192.168.1.3 (o. ä., unleserlich) | 255.255.255.224 |

**LAN 2 (Switch1 + Access Point)**, Router1-Interface 192.168.1.65/**28**

| Gerät | IP-Adresse | Gateway | Maske |
|---|---|---|---|
| PC 31 | 192.168.1.66 | 192.168.1.65 | 255.255.255.224 |
| PC 32 | 192.168.1.62 | 192.168.1.65 | 255.255.255.224 |
| Laptop 1 (WLAN) | 172.16.1.72 | 192.168.1.65 | 255.255.255.224 |
| Laptop 2 (WLAN) | 192.168.1.95 | 192.168.1.65 | 255.255.255.224 |

**WAN**
| Verbindung | Adressen |
|---|---|
| Router1 ↔ Router2 (Verbindung zum ISP) | 79.207.157.101/30 ↔ 79.207.157.102/30 |
| Router2 ↔ Web-Server | 216.58.201.1/30 ↔ 216.58.201.10/30 |

Hilfstabelle /27-Subnetze von 192.168.1.0/24:

| Subnetz-ID | erster Host | letzter Host | Broadcast |
|---|---|---|---|
| 192.168.1.0 | .1 | .30 | .31 |
| 192.168.1.32 | .33 | .62 | .63 |
| 192.168.1.64 | .65 | .94 | .95 |
| 192.168.1.96 | .97 | .126 | .127 |
| … | | | |

> [!success]- Lösung (nachgerechnet)
> LAN 1 = 192.168.1.32/27 (Hosts .33–.62, BC .63). LAN 2 = 192.168.1.64/27 (Hosts .65–.94, BC .95).
>
> | Nr. | Gerät | Fehler | Korrekturvorschlag |
> |---|---|---|---|
> | 0 | PC 2 | IP .68 liegt außerhalb des eigenen Netzes (LAN 1: .33–.62) | gültige Host-IP, z. B. 192.168.1.50 |
> | 1 | Server | falsche Gateway-Adresse | Gateway auf **192.168.1.33** setzen |
> | 2 | Router1 (LAN-2-Interface) | falsche Subnetzmaske **/28** statt /27. Damit kennt der Router nur .64–.79, die Hosts .80–.94 (z. B. Laptop) wären nicht erreichbar | Interface auf **192.168.1.65/27** stellen (einheitlich /27) |
> | 3 | PC 32 | IP .62 gehört zu LAN 1 (.32/27), nicht zu LAN 2 | IP aus .65–.94, z. B. **192.168.1.67** |
> | 4 | Laptop 1 | IP 172.16.1.72 liegt in einem völlig anderen Netz | z. B. **192.168.1.72** |
> | 5 | Laptop 2 | IP .95 ist die **Broadcastadresse** von LAN 2 | z. B. **192.168.1.93** |
> | 6 | Web-Server | 216.58.201.10 liegt nicht im /30-Netz von Router2 (216.58.201.0/30 → nur .1 und .2 nutzbar) | Web-Server auf **216.58.201.2/30** setzen |
>
> **Kein Fehler:** Die Verbindung Router1 ↔ Router2 (79.207.157.101/30 und .102/30) ist korrekt. Das Netz 79.207.157.100/30 hat genau die Hosts .101 und .102.

## Eigene Lösung (Original, mit Lehrerbewertung)

| Gerät | Fehler (eigene Lösung) | Korrektur (eigene Lösung) | Bewertung | Kommentar |
|---|---|---|---|---|
| Server | falsche Gateway-Adresse | Gateway auf 192.168.1.33 setzen | ✓ | richtig |
| Router 1, 2 + Web-Server | falsche Subnetzmaske gewählt | Subnetzmaske muss überall auf /27 konfiguriert werden, um einheitlich zu sein | ✓ (Zeile später rot durchgestrichen) | Für Router1/LAN 2 richtig (/28 → /27). Für die WAN-Strecken bleibt /30 aber korrekt, dort ist /27 falsch |
| Web-Server, Router 2 | Web-Server kann nur mit Router 2 kommunizieren → unnötig, interne Netze können nicht mit dem Web-Server kommunizieren | Router 2 entfernen und Web-Server an Router 1 anbinden | ✗ | Router 2 ist die Verbindung zum ISP. Der echte Fehler ist die IP .10 außerhalb des /30-Netzes |
| Router 1 | Gateway-Adresse 79.207.157.101/30 → falsches Netz | Gateway-Adresse auf eine Adresse innerhalb des Subnetzes festlegen | (✓) | Die WAN-Adresse ist korrekt. Der Fehler am Router1 ist die Maske /28 am LAN-2-Interface |
| Laptop 2 | IP-Adresse ist die Broadcast-Adresse | IP-Adresse muss im Bereich liegen, z. B. 192.168.1.93 | ✓ | richtig |
| Laptop 1 | IP-Adresse falsch | IP auf 192.168.1.56 | – | ⚠️ .56 liegt in LAN 1 (und ist schon von PC 1 belegt). Richtig wäre eine Adresse aus .65–.94, z. B. 192.168.1.72 |

> [!warning] Korrektur
> - **Laptop 1:** Der Vorschlag 192.168.1.56 ist falsch. Diese Adresse gehört zum Subnetz von LAN 1 und ist bereits an PC 1 vergeben. Laptop 1 hängt am Access Point in LAN 2 und braucht eine Adresse aus 192.168.1.65–.94.
> - **Nicht gefunden:** PC 32 (.62 gehört zu LAN 1) und der Web-Server (.10 außerhalb von 216.58.201.0/30).

## Siehe auch
- [[Subnetting]]
- [[Netzbestimmung in 6 Schritten]]
- [[Übung Fehlersuche Netzplan Schulen N-Stadt]]
