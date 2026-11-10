---
tags: [berufsschule, lf3, übung, dhcp]
fach: LF3
typ: übung
quelle: "[[DHCP-Aufgaben.docx]]"
datum: 2026-01-12
status: zu-lernen
---
# Übung: DHCP-Aufgaben (Fragebogen)

> [!summary] Kurz & knapp
> Rechercheauftrag zu DHCP mit 14 Fragen. Die Antworten wurden in Word mit Quellen-URLs festgehalten (bearbeitet vom 12.01. bis 26.01.2026). Der Fragebogen selbst lag auf CryptPad (Link in [[LF3.pdf#page=31]]). Theorie dazu in [[DHCP]] und [[DHCP-Starvation-Angriff]].

> [!info] Fragen rekonstruiert
> Das Word-Dokument enthält **nur die nummerierten Antworten**, nicht die Fragen. Die Fragen unten wurden aus den Antworten abgeleitet. Ihr Wortlaut kann vom Original-Fragebogen abweichen.

## Fragen
1. Wofür steht die Abkürzung DHCP?
2. Um welche Protokollart handelt es sich bei einer DHCP-Anfrage und auf welcher OSI-Schicht arbeitet DHCP?
3. Welche Ports nutzt DHCP?
4. Welche vier Informationen benötigt ein Client von einem DHCP-Server?
5. Warum kommt man heute ohne DHCP nicht mehr aus?
6. Wie groß kann ein DHCP-Paket sein?
7. Was ist ein DHCP-Relay-Agent?
8. Welche Arten der IP-Adresszuweisung gibt es?
9. Welche Antworten kann ein DHCP-Server senden (OFFER, ACK, NAK)?
10. Was ist eine DHCP-DECLINE-Nachricht und wann wird sie ausgelöst?
11. Was ist ein DHCP-Refresh und warum wird er durchgeführt?
12. Nenne drei mögliche Ursachen, warum ein Client keine IP-Adresse vom DHCP-Server erhält.
13. Ein Client hat eine Adresse aus 169.254.0.0/16. Was bedeutet das?
14. Wie läuft eine DHCP-Starvation-Attacke ab?

## Eigene Antworten mit Prüfung

### 1. Abkürzung
> [!success]- Lösung
> **D**ynamic **H**ost **C**onfiguration **P**rotocol. ✓

### 2. Protokollart und OSI-Schicht
> [!example]- Eigene Antwort
> „Die Protokollart einer DHCP-Anfrage ist ein eigenes Netzwerkprotokoll. (Layer 1-4 werden bedient + Layer 7 (Kommunikation zwischen Mensch & Maschine). Quelle: Cisco Packet Tracer)“

> [!success]- Lösung
> DHCP ist ein **Client-Server-Protokoll der Anwendungsschicht (OSI-Schicht 7)**. Es wird **verbindungslos über UDP** (Schicht 4) und IP (Schicht 3) transportiert. Die DISCOVER-Nachricht ist ein **Broadcast**. In Packet Tracer sieht man deshalb im PDU die Schichten 1 bis 4 plus Schicht 7.

> [!warning] Korrektur
> - „Eigenes Netzwerkprotokoll“ ist zu ungenau. Die Antwort sollte lauten: **Anwendungsprotokoll (Schicht 7), transportiert per UDP**.
> - Schicht 7 bedeutet nicht „Kommunikation zwischen Mensch und Maschine“. Die Anwendungsschicht ist die **Schnittstelle zu den Anwendungen bzw. Netzwerkdiensten**. DHCP läuft ganz ohne Benutzer im Hintergrund.

### 3. Ports
> [!example]- Eigene Antwort
> IPv4: Port **67** für Nachrichten an DHCP-Server oder Relay-Agenten, Port **68** für Nachrichten an DHCP-Clients. IPv6 (DHCPv6): Port **547** an Server/Relay-Agenten, Port **546** an Clients.

> [!success]- Lösung
> Richtig. ✓ Ergänzung: Alle Ports sind **UDP**-Ports.

### 4. Die vier Informationen
> [!example]- Eigene Antwort
> IP-Adresse des Clients, Subnetzmaske, Adresse des Routers (Gateway) und DNS-Serveradresse(n).

> [!success]- Lösung
> Richtig. ✓ Dazu kommt die **Lease-Dauer** (wie lange die Adresse gilt). Weitere Optionen sind möglich, z. B. NTP-Server oder Domänenname.
>
> Kleiner Tippfehler im Original: „Grateway“ → **Gateway**.

### 5. Warum DHCP unverzichtbar ist
> [!example]- Eigene Antwort
> Jedes internetfähige Gerät braucht eine IPv4-Adresse. Die Geräte sind mobil und wechseln oft den Standort, deshalb wäre die manuelle Eingabe viel zu zeitaufwendig. Außerdem können Admins mit DHCP die Netzwerkkonfiguration zentral und einfacher verwalten.

> [!success]- Lösung
> Richtig. ✓ Weitere Argumente: **keine Tippfehler und doppelt vergebenen Adressen**, Änderungen (z. B. neuer DNS-Server) wirken sofort für alle Clients, und freie Adressen fallen nach Ablauf der Lease automatisch zurück in den Pool. Das gilt auch für IPv6, nicht nur für IPv4.

### 6. Größe eines DHCP-Pakets
> [!example]- Eigene Antwort
> „Ein DHCP-Paket kann maximal 576 Bytes groß sein. Die Größe setzt sich aus Headern (Grundaufbau) und Optionen (flexible Zusatzfelder) zusammen.“

> [!success]- Lösung
> Ein DHCP-Paket besteht aus einem **festen Teil von 236 Byte** (u. a. Client-MAC, angebotene IP, Server-IP) plus dem **Optionsfeld** variabler Länge. Jeder Client muss Nachrichten von mindestens **576 Byte** (IP-Paket inkl. 312 Byte Optionen) annehmen können.

> [!warning] Korrektur
> 576 Byte sind die **Mindestgröße, die jeder Client verarbeiten können muss** (RFC 2131), keine feste Obergrenze. Mit der Option „Maximum DHCP Message Size“ (Option 57) kann ein Client größere Pakete erlauben. Richtig ist die Aufteilung in festen Kopfteil und Optionen.

### 7. DHCP-Relay-Agent
> [!example]- Eigene Antwort
> Ein DHCP-Relay-Agent ist ein Host oder Router, der DHCP-Pakete zwischen Clients und Server weiterleitet.

> [!success]- Lösung
> Richtig. ✓ Begründung, warum man ihn braucht: Router leiten **Broadcasts nicht weiter**. Steht der DHCP-Server in einem anderen Subnetz, nimmt der Relay-Agent (meist der Router) den DISCOVER-Broadcast an und schickt ihn per **Unicast** an den Server. So reicht **ein zentraler DHCP-Server für mehrere Subnetze**. Bei Cisco wird das mit `ip helper-address <Server-IP>` auf dem Router-Interface eingerichtet.

### 8. Arten der Adresszuweisung
> [!example]- Eigene Antwort
> - Manuelle Zuweisung: Jedes Gerät erhält eine eigene IP-Adresse vom Administrator (praktisch für kleine Netze).
> - Dynamische Zuweisung: DHCP vergibt automatisch IP-Adressen (Regelfall).
> - Statische Zuweisung: Die IP-Adresse bleibt unverändert und wird einmalig gesetzt (praktisch für Server).

> [!success]- Lösung
> Im Zusammenhang mit **DHCP** gibt es drei Zuordnungsarten:
>
> | Art | Ablauf | Einsatz |
> |---|---|---|
> | **Manuell (statisch, Reservierung)** | Der Admin hinterlegt im DHCP-Server eine feste Zuordnung **MAC-Adresse → IP-Adresse**. Das Gerät bekommt immer dieselbe IP, aber trotzdem per DHCP. | Drucker, Server, Access Points |
> | **Automatisch** | Der Server vergibt eine freie Adresse aus dem Pool **dauerhaft** (unbegrenzte Lease). | selten |
> | **Dynamisch** | Der Server vergibt eine Adresse aus dem Pool **zeitlich begrenzt** (Lease), danach kann sie neu vergeben werden. | Regelfall (PCs, Smartphones) |

> [!warning] Korrektur
> Die eigene Antwort trennt „manuell“ und „statisch“, beschreibt aber zweimal dasselbe: eine Adresse, die direkt am Gerät eingetragen wird (das ist **gar kein DHCP**). Bei DHCP heißt „manuell/statisch“: Die feste Adresse wird **im DHCP-Server per MAC-Reservierung** hinterlegt. Es fehlt die **automatische** (dauerhafte) Zuordnung.

### 9. Antworten des DHCP-Servers
> [!example]- Eigene Antwort
> 1. DHCPOFFER (Angebot): Server bietet dem Client eine IP-Adresse an.
> 2. DHCPPACK (Bestätigung): Server bestätigt die Vergabe.
> 3. DHCPNAK (Ablehnung): Server lehnt die Anfrage ab, weil die angefragte IP-Adresse nicht mehr verfügbar ist oder im falschen Netz liegt.

> [!success]- Lösung
> Inhaltlich richtig. ✓ Ein NAK kommt z. B., wenn ein Laptop aus einem anderen Netz seine alte Adresse wieder anfordert (REQUEST) und diese im neuen Netz nicht passt. Der Client startet dann neu mit DISCOVER.

> [!warning] Korrektur
> Tippfehler: Die Nachricht heißt **DHCPACK** (Acknowledge), nicht „DHCPPACK“.

### 10. DHCP-DECLINE
> [!example]- Eigene Antwort
> „Eine DECLINE-Nachricht kann ausgelöst werden, wenn ein Gerät beispielsweise eine statische IP-Adresse erhält, wenn der DHCP-Server ausfällt oder wenn alle verfügbaren IP-Adressen im Bereich belegt sind. Auch falsche DHCP-Einstellungen können diese Meldung auslösen. Dazu wird das Address Resolution Protocol nach der DHCP-Vergabe eingesetzt.“

> [!success]- Lösung
> **DHCPDECLINE** schickt der **Client an den Server**. Er lehnt damit eine bereits zugewiesene Adresse ab, weil er festgestellt hat, dass sie **schon von einem anderen Gerät benutzt wird**. Dazu prüft der Client die Adresse nach dem ACK per **ARP** („Hat jemand diese IP?“). Antwortet ein anderes Gerät, gibt es einen Adresskonflikt. Der Client sendet DECLINE und startet neu mit DISCOVER, der Server markiert die Adresse als belegt.
>
> Typische Ursache: Jemand hat an einem Gerät eine **statische IP aus dem DHCP-Pool** eingetragen.

> [!warning] Korrektur
> Die Antwort vermischt verschiedene Fehlerfälle. Ein ausgefallener DHCP-Server oder ein voller Pool lösen **kein** DECLINE aus, denn dann gibt es gar kein Angebot, das man ablehnen könnte (Folge: APIPA, siehe Frage 13). Richtig ist der Hinweis auf **ARP**: DECLINE bedeutet immer „**Adresse ist bereits belegt (Konflikt)**“. Absender ist der **Client**, nicht der Server.

### 11. DHCP-Refresh (Lease-Erneuerung)
> [!example]- Eigene Antwort
> Ein DHCP-Refresh ist der Prozess, bei dem ein Client seine IP-Adresse und Netzwerkkonfiguration beim DHCP-Server erneuert. Das vermeidet IP-Konflikte, hält die Konfiguration aktuell und sorgt für eine stabile Netzwerkverbindung.

> [!success]- Lösung
> Richtig. ✓ Ergänzung zum Ablauf:
> - Nach **50 %** der Lease-Dauer (T1) schickt der Client ein **REQUEST per Unicast** an seinen Server, der mit ACK die Lease verlängert.
> - Antwortet der Server nicht, versucht der Client es nach **87,5 %** (T2) per **Broadcast** bei irgendeinem DHCP-Server (Rebinding).
> - Läuft die Lease ab, muss der Client die Adresse abgeben und neu mit DISCOVER beginnen.
> - Manuell unter Windows: `ipconfig /release` und `ipconfig /renew`.

### 12. Ursachen für fehlende IP-Adresse
> [!example]- Eigene Antwort
> 1. DHCP-Server wegen falscher Einstellungen nicht erreichbar
> 2. Adresspool erschöpft, keine freien Adressen mehr
> 3. DHCP-Server antwortet nicht, z. B. wegen Firewall oder weil der Dienst gestoppt wurde

> [!success]- Lösung
> Richtig. ✓ Weitere typische Ursachen: Kabel/WLAN getrennt, Client im **falschen VLAN**, fehlender **Relay-Agent** (Server in einem anderen Subnetz), DHCP-Snooping blockiert, Netzwerkkarte am Client auf statische IP eingestellt.

### 13. Adresse 169.254.x.x
> [!example]- Eigene Antwort
> „Diese Adresse ist eine sogenannte APIPA-Adresse und wird immer dann erzeugt, wenn der DHCP-Server nicht erreichbar ist, nicht richtig läuft oder alle verfügbaren Adressen vergeben wurden. Diese APIPA-Adresse (Automatic Private IP Editing) vergibt sich der Client selbst, sodass eine minimale lokale Kommunikation möglich ist.“

> [!success]- Lösung
> Inhaltlich richtig. ✓ Der Client wählt zufällig eine Adresse aus **169.254.0.0/16** (Link-Local), prüft per ARP, ob sie frei ist, und fragt im Hintergrund weiter nach einem DHCP-Server. Mit APIPA gibt es **kein Gateway**, also keinen Internetzugang.

> [!warning] Korrektur
> APIPA steht für **Automatic Private IP Addressing**, nicht „Editing“.

### 14. DHCP-Starvation-Attacke
> [!example]- Eigene Antwort
> „Der Angreifer sendet massenhaft gefälschte DHCP-DISCOVER-Pakete zu einem Client. Jedes Paket enthält eine neue, zufällige MAC-Adresse, die gleichzeitig eine neue IP-Adresse zugewiesen bekommt. Dadurch leert sich der Adresspool sehr schnell und echte Clients erhalten keine IP-Adresse mehr. Der Angreifer kann dadurch das Netzwerk lahmlegen oder weitere Angriffe durchführen.“

> [!success]- Lösung
> Im Kern richtig. ✓ Typische Folgeangriffe: Der Angreifer stellt einen eigenen **Rogue-DHCP-Server** auf und verteilt sich selbst als Gateway oder DNS-Server (Man in the Middle). Schutz: **DHCP-Snooping** und **Port-Security** auf dem Switch. Details in [[DHCP-Starvation-Angriff]].

> [!warning] Korrektur
> Die gefälschten DISCOVER-Pakete gehen **nicht an einen Client**, sondern als Broadcast an den **DHCP-Server**. Nur der Server hat einen Adresspool, den man leeren kann.

## Quellen im Original
Wikipedia (DHCP, IP-Adresse), technik-kiste.de, Citrix-Doku (DHCP-Relay), elektronik-kompendium.de, Cisco-Dokument 27470 (DHCP), linuxvox.com (Linux DHCP Refresh), prosec-networks.com (DHCP Starvation), IT-Lexikon (APIPA), Cisco Packet Tracer.

## Siehe auch
- [[DHCP]]
- [[DHCP-Starvation-Angriff]]
- [[Private und reservierte IPv4-Adressen]]
- [[UDP]]
- [[Übung Fragebogen UDP]]
