---
tags: [berufsschule, lf3, osi-modell]
fach: LF3
typ: thema
quelle: "[[LF3.pdf#page=13]]"
datum: 2025-09-29
status: zu-lernen
---
# OSI-Schichtenmodell

> [!summary] Kurz & knapp
> Das OSI-Modell (**Open Systems Interconnection**) teilt die Netzwerkkommunikation in 7 Schichten mit klar getrennten Aufgaben. Es ist ein herstellerunabhängiger internationaler Standard (ISO). Weil es modular ist, kann man eine Schicht austauschen, ohne dass die anderen Schichten nicht mehr funktionieren.

## Die Schichten

| Nr. | Schicht | Aufgabe | Beispiele (Adressen, Geräte, Protokolle) |
|---|---|---|---|
| 7 | Anwendungsschicht (Application) | Schnittstelle zur Anwendung | HTTP(S), DNS, DHCP, FTP |
| 6 | Darstellungsschicht (Presentation) | Kodierung, Verschlüsselung, Kompression | TLS, Zeichensätze |
| 5 | Sitzungsschicht (Session) | Auf- und Abbau von Sitzungen | – |
| 4 | Transportschicht (Transport) | Transport von Datenpaketen zwischen Anwendungen | **Ports**, TCP/UDP, Firewall |
| 3 | Vermittlungsschicht (Network) | Vermittlung zwischen Netzen (Routing) | **IP-Adressen**, Router, IP-Protokoll |
| 2 | Sicherungsschicht (Data Link) | Adressierung im lokalen Netz, Fehlererkennung | **MAC-Adressen**, Switch, Ethernet-Frame |
| 1 | Bitübertragungsschicht (Physical) | Technik für den Transport des Bitstroms (`01111011…`) | Kabel, Stecker, Funk, Hub |

Die Schichten 5–7 werden im Unterricht als „Software“ (anwendungsorientierte Schichten) zusammengefasst, die Schichten 1–4 als transportorientierte Schichten.

> [!info] Layer-3-Switch
> Ein Layer-3-Switch ist ein Kombigerät aus **Switch + Router**. Er arbeitet auf den OSI-Schichten 2 **und** 3.

> [!info] Eselsbrücke (Schicht 1 → 7)
> „**P**lease **D**o **N**ot **T**hrow **S**ausage **P**izza **A**way“: Physical, Data Link, Network, Transport, Session, Presentation, Application.

> [!warning] Korrektur
> In der Mitschrift stand „Open Systems Internet**connection**“. Richtig ist **Open Systems Interconnection**.

> [!tip] Merke
> - Schicht 2 = MAC-Adresse und Switch; Schicht 3 = IP-Adresse und Router; Schicht 4 = Ports, TCP/UDP.
> - Jede Schicht nutzt die Dienste der darunterliegenden Schicht ([[Datenkapselung im TCP-IP-Modell]]).
> - Vorteil: herstellerunabhängig und modular, Schichten sind austauschbar.

## Lernfragen
> [!question]- Wofür steht OSI und welchen Vorteil bietet das Modell?
> Open Systems Interconnection. Es ist ein herstellerunabhängiger Standard. Weil es modular ist, lassen sich einzelne Schichten (z. B. Kabel gegen WLAN) austauschen, ohne die anderen Schichten zu ändern.

> [!question]- Auf welcher Schicht arbeiten Switch, Router und Layer-3-Switch?
> Switch: Schicht 2. Router: Schicht 3. Layer-3-Switch: Schicht 2 und 3.

> [!question]- Welche Adressart gehört zu Schicht 2, welche zu Schicht 3, welche zu Schicht 4?
> Schicht 2: MAC-Adresse. Schicht 3: IP-Adresse. Schicht 4: Portnummer.

> [!question]- Nenne alle 7 Schichten in der richtigen Reihenfolge.
> 1 Bitübertragung, 2 Sicherung, 3 Vermittlung, 4 Transport, 5 Sitzung, 6 Darstellung, 7 Anwendung.

> [!question]- Auf welcher Schicht arbeiten TCP und UDP?
> Auf Schicht 4, der Transportschicht.

## Siehe auch
- [[MAC-Adresse]]
- [[IPv4-Adresse vs. MAC-Adresse]]
- [[Datenkapselung im TCP-IP-Modell]]
- [[UDP]] · [[TCP-Header]]
