---
tags: [berufsschule, lf3, mac-adresse, datenschutz]
fach: LF3
typ: thema
quelle: "[[LF3.pdf#page=8]]"
datum: 2025-09-15
status: zu-lernen
---
# MAC-Randomisierung (zufällige / dynamische MAC-Adressen)

> [!summary] Kurz & knapp
> Weil die feste MAC-Adresse ein Gerät eindeutig identifiziert, kann man Geräte über WLAN-Access-Points verfolgen (**WLAN-Tracking**). Bei der MAC-Randomisierung verwendet ein Mobilgerät daher bei der Suche nach WLANs zufällig erzeugte, **lokal verwaltete** MAC-Adressen.

## Problem: MAC-Adressen und Privatsphäre
- Die MAC-Adresse ist einem Hardware-Interface fest zugeordnet und damit ein eindeutiges Identifikationsmerkmal.
- Aus Hersteller- und Gerätekennung kann man auf das Gerät schließen.
- Wer mehrere WLAN-Access-Points betreibt und die MAC-Adressen sammelt, kann **Bewegungsprofile** von Smartphones erstellen. Dafür reichen die **Probe Requests** beim Scannen nach Netzen, eine Verbindung ist nicht nötig.

## Lösung: MAC Randomization
- Beim **Scannen** nach WLANs nutzt das Gerät eine **zufällig generierte** MAC-Adresse.
- Erst wenn es sich **tatsächlich verbindet**, nutzt es die echte (bzw. eine pro Netz feste) MAC-Adresse.
- So hinterlässt man beim Vorbeigehen an fremden Access Points kein Identifikationsmerkmal.
- Verfügbar ab Windows 10, iOS 8, Android 6. IEEE 802 erlaubt zufällige Adressen, die für die Dauer einer Sitzung konstant bleiben.
- Zufällige Adressen stammen aus dem **lokal verwalteten Adressraum** (U/L-Bit = 1, siehe [[MAC-Adresse]]).

## Nachteile
- **Adress-Kollisionen:** In großen Netzen steigt die Wahrscheinlichkeit, dass zwei Geräte zufällig dieselbe MAC-Adresse haben. Ein LAN funktioniert aber nur mit eindeutigen MAC-Adressen.
- **Middle-Boxen** (Switches, Firewalls, Router, Deep-Packet-Inspection-Systeme) sind teilweise auf feste MAC-Zuordnungen angewiesen, z. B. bei MAC-Filtern oder festen DHCP-Reservierungen.
- Deshalb sind zufällige MAC-Adressen für **stationäre Geräte** wenig sinnvoll und nicht nötig. Für **mobile Geräte**, die sich in wechselnden Netzen anmelden, sind sie sinnvoll.
- Ein „Locally Administered Address Space“ kann auch **virtuelle Maschinen** ohne eigenes Hardware-Interface mit MAC-Adressen versorgen.

> [!info] Ergänzung
> Aktuelle Betriebssysteme nutzen oft auch **nach** dem Verbinden eine eigene, zufällige MAC-Adresse pro WLAN („private WLAN-Adresse“). Sie bleibt für dieses Netz gleich, unterscheidet sich aber von Netz zu Netz.

> [!tip] Merke
> - Zweck: Schutz vor WLAN-Tracking (Bewegungsprofile)
> - Zufällige MAC beim Scannen, echte MAC beim Verbinden
> - Nachteil: mögliche Kollisionen, Probleme mit Geräten, die feste MACs erwarten
> - Sinnvoll für mobile Geräte, nicht für stationäre Systeme

## Lernfragen
> [!question]- Welches Datenschutzproblem entsteht durch feste MAC-Adressen?
> Geräte und damit Nutzer lassen sich eindeutig identifizieren. Mit mehreren Access Points kann man Bewegungsprofile erstellen (WLAN-Tracking).

> [!question]- Wann verwendet ein Smartphone mit MAC-Randomisierung die zufällige und wann die echte Adresse?
> Die zufällige beim Scannen nach Netzen (Probe Requests), die echte (bzw. eine feste pro Netz) beim tatsächlichen Verbinden.

> [!question]- Warum sind zufällige MAC-Adressen für stationäre Systeme ungeeignet?
> Middle-Boxen wie Switches, Firewalls oder DHCP-Reservierungen sind auf feste MAC-Adressen angewiesen. Außerdem besteht ein Kollisionsrisiko, und stationäre Geräte brauchen keinen Tracking-Schutz.

> [!question]- Welches Bit ist bei einer zufällig erzeugten MAC-Adresse gesetzt?
> Das U/L-Bit (= 1, lokal verwaltet).

## Siehe auch
- [[MAC-Adresse]]
- [[MAC-Adresse - Darstellung und kanonische Form]]
