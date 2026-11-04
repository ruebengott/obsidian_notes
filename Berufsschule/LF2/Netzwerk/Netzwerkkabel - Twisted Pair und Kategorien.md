---
tags: [berufsschule, lf2, netzwerk, verkabelung]
fach: LF2
typ: thema
quelle: "[[LF2.pdf#page=66]]"
datum:
status: zu-lernen
---
# Netzwerkkabel - Twisted Pair und Kategorien

> [!summary] Kurz & knapp
> Im LAN werden meist **Twisted-Pair-Kabel** (verdrillte Kupferadernpaare) mit RJ45-Steckern verwendet. Die Bezeichnung **X/YTP** beschreibt die **Schirmung**, die **Kategorie (Cat)** die maximale Frequenz und Datenrate. Die maximale Länge einer Ethernet-Strecke beträgt **100 m** (90 m fest verlegt + 10 m Patchkabel).

## Kabelarten (Aufgabe 1)

| Kabelart | Medium | Einsatz |
| --- | --- | --- |
| **Twisted Pair** (Cat 5e–8) | Kupfer, 4 verdrillte Adernpaare | LAN, Ethernet, PoE |
| **Koaxialkabel** | Kupfer-Innenleiter + Schirm | Kabelfernsehen/-internet, früher Ethernet |
| **Lichtwellenleiter (LWL, Glasfaser)** | Licht in Glasfasern (Multimode/Singlemode) | Backbone, lange Strecken, Rechenzentrum, FTTH |
| Geräte-/Peripheriekabel | USB, HDMI, DisplayPort | Anschluss von Peripherie und Monitoren |

> [!warning] Korrektur
> In der Mitschrift stehen bei Aufgabe 1 „USB-C/HDMI, Bluetooth, WLAN“. **Bluetooth und WLAN sind Funktechniken, keine Kabel.** Gefragt sind Datenkabel: v. a. Twisted Pair, Koaxialkabel und Glasfaser (LWL), dazu Gerätekabel wie USB oder HDMI.

## Schirmungsbezeichnung X/YTP (Aufgabe 2)
Schema: **Gesamtschirm / Paarschirm + TP** (Twisted Pair)

| Kürzel | Bedeutung |
| --- | --- |
| U | unshielded = ungeschirmt |
| F | foiled = Folienschirm |
| S | screened = Geflechtschirm |
| SF | Geflecht + Folie |

| Kabel | Erklärung |
| --- | --- |
| **U/UTP Cat.5** | komplett ungeschirmt, Kategorie 5 |
| **F/UTP Cat.5e** | Gesamtschirm aus Folie, Paare ungeschirmt. Cat 5e ist die verbesserte Version von Cat 5. |
| **U/FTP Cat.6** | kein Gesamtschirm, aber jedes Adernpaar einzeln mit Folie geschirmt |
| **S/FTP Cat.7A** | Gesamtschirm aus Geflecht **und** jedes Paar einzeln foliengeschirmt, sehr störsicher |
| **S/FTP Cat.8** | wie S/FTP, für sehr hohe Frequenzen/Datenraten, vor allem im Rechenzentrum (kurze Strecken) |

## Vergleich der Kategorien (Aufgabe 3)

| Kategorie | Frequenz | typische Datenrate | Schirmung (Beispiel) | Kurzbeschreibung |
| --- | --- | --- | --- | --- |
| Cat 5 | 100 MHz | 100 Mbit/s | U/UTP – keine | günstig, aber störanfällig, veraltet |
| Cat 5e | 100 MHz | 1 Gbit/s | F/UTP – Folie außen | Mindeststandard für Gigabit, besser gegen Störungen |
| Cat 6 | 250 MHz | 1 Gbit/s (10 Gbit/s bis ca. 55 m) | U/FTP – Paare einzeln | gute Signalqualität |
| Cat 6A | 500 MHz | 10 Gbit/s (100 m) | meist geschirmt | heutiger Standard für Neuverkabelung |
| Cat 7 / 7A | 600 / 1000 MHz | 10 Gbit/s | S/FTP – Geflecht + Paare | sehr hohe Störsicherheit, Verlegekabel |
| Cat 8 | 2000 MHz | 25/40 Gbit/s (bis 30 m) | S/FTP – starke Schirmung | Rechenzentrum, sehr hohe Datenraten |

## Kurzantworten zu den weiteren Fragen
- **Maximale Länge (4):** 100 m pro Strecke (Permanent Link 90 m + 10 m Patchkabel). Danach wird das Signal zu schwach (Dämpfung).
- **Farbcodierung (5):** 4 Paare mit festen Farben (orange, grün, blau, braun, jeweils mit weißem Partner). Belegung nach **T568A oder T568B**, damit Stecker und Dosen überall gleich aufgelegt werden → [[Patchkabel herstellen - T568A und T568B]]
- **Defektes Kabel (6):** Symptome sind Verbindungsabbrüche, geringe Geschwindigkeit (z. B. nur 100 statt 1000 Mbit/s) oder gar keine Verbindung. Prüfen per Sichtkontrolle und **Kabeltester**. Reparatur: Stecker neu crimpen bzw. Dose neu auflegen oder Kabel ersetzen.
- **Biegen > 90° (7):** nicht sinnvoll. Zu enge Biegeradien (Faustregel: mind. 4–8 × Kabeldurchmesser) beschädigen Adern, Verdrillung und Schirmung, und die Übertragung wird schlechter.
- **Vorteile geschirmter Kabel (8):** besserer Schutz vor elektromagnetischen Störungen (EMV) und weniger **Übersprechen** (Crosstalk) → stabilere, schnellere Verbindung. Die Schirmung muss aber korrekt geerdet sein.
- **Rolle der Geschwindigkeit (9):** Die benötigte Datenrate bestimmt die Kategorie. Höhere Kategorien bieten mehr Bandbreite und sind zukunftssicher.
- **Testen (10):** Kabeltester bzw. Zertifizierungsgeräte prüfen Durchgang, Aderbelegung (Wiremap), Länge, Dämpfung und Übersprechen (NEXT).
- **Weitere Einflussfaktoren (11):** Switch, Router, Netzwerkkarte, Treiber, Auslastung, Duplex-Einstellungen, Störquellen, Konfiguration.
- **Verlegen (12):** Biegeradius, maximale Zugbelastung, **Abstand zu Stromleitungen**, Brandschutz (z. B. halogenfreie LSOH-Kabel), Normen wie **DIN EN 50173** (strukturierte Verkabelung) und DIN EN 50174 (Installation).
- **Entsorgung (13):** über **Elektroschrott- bzw. Wertstoffsammlung**, damit Kupfer und Kunststoff recycelt werden können (→ [[Green IT]]).
- **Datenblatt (14):** Kategorie, Schirmung, Frequenzbereich, Leiteraufbau (AWG, massiv/Litze), Mantelmaterial (z. B. LSOH), Brandklasse, Normen, Einsatzbereich, Biegeradius.

> [!tip] Merke
> - X/YTP: erst **Gesamtschirm**, dann **Paarschirm**. U = ungeschirmt, F = Folie, S = Geflecht.
> - Cat 5e → 1 Gbit/s, Cat 6A → 10 Gbit/s, Cat 8 → 25/40 Gbit/s auf 30 m.
> - Max. **100 m** (90 + 10).
> - Bluetooth/WLAN sind keine Kabel!

## Lernfragen
> [!question]- Was bedeutet die Bezeichnung S/FTP?
> Gesamtschirm aus Geflecht (S), jedes Adernpaar zusätzlich mit Folie geschirmt (F), Twisted Pair (TP).

> [!question]- Wie lang darf eine Twisted-Pair-Ethernet-Strecke maximal sein?
> 100 m, üblich aufgeteilt in 90 m feste Verkabelung und 10 m Patchkabel.

> [!question]- Welche Kabelkategorie braucht man mindestens für 10 Gbit/s über 100 m?
> Cat 6A (oder höher).

> [!question]- Welche Vorteile haben geschirmte Netzwerkkabel?
> Besserer Schutz gegen elektromagnetische Störungen und weniger Übersprechen, dadurch stabilere Übertragung.

> [!question]- Womit prüft man ein Netzwerkkabel?
> Mit einem Kabeltester (Durchgang, Aderbelegung) bzw. einem Zertifizierungsgerät (zusätzlich Länge, Dämpfung, Übersprechen).

## Siehe auch
- [[Patchkabel herstellen - T568A und T568B]]
- [[Netzwerk-Grundbegriffe und Topologien]]
- [[Power over Ethernet]]
- [[Green IT]]
