---
tags: [berufsschule, lf3, übung, fehlersuche, subnetting]
fach: LF3
typ: übung
quelle: "[[LF3.pdf#page=33]]"
datum:
status: zu-lernen
---
# Übung: Fehlersuche im Netzplan der Beruflichen Schulen N-Stadt

## Aufgabe
Finde die Konfigurationsfehler im Netzplan und nenne Korrekturvorschläge.

![[LF3.pdf#page=33]]

### Netzplan (abgetippt)
**LAN N-Stadt** (Router ETH0 192.168.1.254/24)

| Gerät | IP | Subnetzmaske | Gateway |
|---|---|---|---|
| Client N1 | 192.168.1.0 | 255.255.255.0 | 192.168.1.254 |
| Client N2 | 192.168.1.2 | 255.255.255.0 | 192.168.1.240 |
| Client N199 | 192.168.1.199 | 255.255.0.0 | 192.168.1.254 |
| Verzeichnisserver mit DNS | 192.168.1.200 | 255.255.255.0 | 192.168.1.254 |

**LAN Außenstelle A-Hausen** (Router ETH0 192.168.2.254/24)

| Gerät | IP | Subnetzmaske | Gateway |
|---|---|---|---|
| Client A1 | 192.168.2.11 | 255.255.255.0 | 192.168.2.254 |
| Client A2 | 192.168.2.11 | 255.255.255.0 | 192.168.2.254 |

**LAN Außenstelle B-Heim** (Router ETH0 192.168.3.254/24)

| Gerät | IP | Subnetzmaske | Gateway |
|---|---|---|---|
| Client B1 | 192.168.3.11 | 255.255.255.0 | 192.168.3.254 |
| Client B2 | 192.168.3.12 | 255.255.255.0 | 192.168.3.254 |

**Router-Verbindungen (Transfernetze /30)**
- Zentrale ETH1 10.10.10.9/30 ↔ A-Hausen ETH1 10.10.10.10/30
- Zentrale ETH2 10.10.10.13/30 ↔ B-Heim ETH1 10.10.10.14/30
- Zentrale ETH4 210.10.10.2/30 → Internet

> [!success]- Lösung (geprüft)
> | Gerät | Fehler | Korrektur |
> |---|---|---|
> | Client N1 | 192.168.1.0 ist die **Netzadresse** von 192.168.1.0/24 | gültige Hostadresse, z. B. 192.168.1.1 |
> | Client N2 | Gateway 192.168.1.240 ist falsch. Das Router-Interface hat .254. Ohne korrektes Gateway kann der Client **nur mit Clients innerhalb des Subnetzes kommunizieren** | Gateway auf **192.168.1.254** |
> | Client N199 | Subnetzmaske 255.255.0.0 (/16) statt /24. Der Client hält z. B. 192.168.2.x und 192.168.3.x für lokal und schickt sie nicht ans Gateway | Maske **255.255.255.0** |
> | Client A1 / A2 | **gleiche IP-Adresse** 192.168.2.11 → Adresskonflikt | einem Client eine andere Adresse geben, z. B. A2 = 192.168.2.12 |
>
> **Korrekt sind:** Verzeichnisserver, B1, B2 und die Transfernetze:
> - 10.10.10.8/30 → Hosts .9 und .10 ✓
> - 10.10.10.12/30 → Hosts .13 und .14 ✓
> - 210.10.10.0/30 → .2 ist ein gültiger Host ✓

> [!note] Eigene Notizen im Original
> Handschriftlich markiert waren: Client N2 Gateway „240 → 254“ mit dem Hinweis „(nur mit den Clients innerhalb des Subnetzes kommunizieren)“ sowie bei A1/A2 „gleiche IP“. Die vollständige Lösungstabelle lag auf CryptPad (Link im Original), sie ist nicht im PDF.

## Siehe auch
- [[Übung Fehlersuche Netzplan Autohaus Reihbach]]
- [[Netzbestimmung in 6 Schritten]]
- [[Routing und Default Route]]
