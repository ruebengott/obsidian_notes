---
tags: [berufsschule, lf5, hardware, server]
fach: LF5
typ: thema
quelle: "[[LF5.pdf#page=10]]"
datum: 2025-10-07
status: zu-lernen
---
# Server-Hardware

> [!summary] Kurz & knapp
> Server laufen rund um die Uhr und stellen Dienste für viele Nutzer bereit. Ihre Hardware ist deshalb auf **Ausfallsicherheit** ausgelegt: ECC-RAM, redundante Netzteile, Hot-Swap, RAID und eine USV. Je nach Einsatz baut man sie als Tower-, Rack- oder Blade-Server.

## Typische Server-Komponenten

| Begriff | Bedeutung |
| --- | --- |
| **ECC-RAM** | fehlerkorrigierender Arbeitsspeicher (Error Correcting Code), erkennt und korrigiert Bitfehler. Server-CPUs unterstützen ECC |
| **Redundante PSU** | zwei oder mehr Netzteile; fällt eins aus, übernimmt das andere |
| **Hot-Swap** | Austausch von Komponenten (Festplatten, Netzteile, Lüfter) im laufenden Betrieb |
| **RAID-Controller** | verwaltet mehrere Festplatten in einem RAID-Verbund, siehe [[RAID-Level]] |
| **USV** | unterbrechungsfreie Stromversorgung: Akku überbrückt Stromausfälle, sodass der Server sauber herunterfahren oder weiterlaufen kann |
| **Netzwerk** | Ethernet (RJ-45) bzw. Glasfaser/SFP, oft mehrere Ports (Redundanz, höhere Bandbreite) |
| **NAS** | Network Attached Storage: Speicher, der über das Netzwerk bereitgestellt wird, z. B. als Backup-Ziel |

## Bauformen

| Bauform | Merkmale | Einsatz |
| --- | --- | --- |
| **Tower-Server** | sieht aus wie ein Desktop-PC; braucht pro Gerät mehr Platz; eigene Lüfter, für Einzelbetrieb gedacht; günstig in der Anschaffung | kleine Firmen, Büro ohne Serverraum |
| **Rack-Server** | genormte Breite (19 Zoll) und Höhe in **Höheneinheiten (HE/U)**; viele Server übereinander im Serverschrank; effiziente Kühlung | Serverräume, Rechenzentren |
| **Blade-Server** | sehr kompakte Einschübe (Blades) in einem gemeinsamen Gehäuse (Chassis), das Strom, Kühlung und Netzwerk teilt | hohe Dichte, große Rechenzentren |

## Warum eine USV?
- Bei Stromausfall läuft der Server weiter bzw. fährt **kontrolliert** herunter, ohne Datenverlust oder beschädigte Dateisysteme.
- Sie filtert Spannungsspitzen und Unterspannung.
- Verfügbarkeit ist für das Unternehmen wirtschaftlich entscheidend, weil Ausfälle Geld kosten.

> [!tip] Merke
> Server = **Redundanz** an jeder Stelle: Strom (USV, redundante PSU), Speicher (RAID, ECC), Austausch ohne Ausfall (Hot-Swap). Typischer Unterschied zwischen Server- und Desktop-CPU: **ECC-RAM-Unterstützung**.

## Lernfragen
> [!question]- Was ist ECC-RAM und warum setzt man es in Servern ein?
> Fehlerkorrigierender Arbeitsspeicher. Er erkennt und korrigiert einzelne Bitfehler und verhindert so Abstürze und Datenfehler im Dauerbetrieb.

> [!question]- Was bedeutet Hot-Swap?
> Komponenten wie Festplatten oder Netzteile können im laufenden Betrieb getauscht werden, ohne den Server abzuschalten.

> [!question]- Erkläre den Unterschied zwischen Tower- und Rack-Server.
> Ein Tower-Server ist ein freistehendes Gehäuse wie ein Desktop-PC: günstig, aber platzintensiv. Ein Rack-Server hat ein genormtes 19-Zoll-Format und wird mit anderen im Serverschrank gestapelt. Das spart Platz und ermöglicht eine effiziente Kühlung im Rechenzentrum.

> [!question]- Warum ist eine USV in Serverumgebungen wichtig?
> Sie überbrückt Stromausfälle und Spannungsschwankungen. Der Server bleibt verfügbar oder fährt kontrolliert herunter, sodass Datenverlust und Ausfallkosten vermieden werden.

> [!question]- Was ist ein Blade-Server?
> Ein sehr kompakter Servereinschub. Mehrere Blades sitzen in einem gemeinsamen Chassis, das Stromversorgung, Kühlung und Netzwerk bereitstellt.

## Siehe auch
- [[RAID-Level]]
- [[Mainboard-Bestandteile]]
- [[Test Server-Hardware]]
