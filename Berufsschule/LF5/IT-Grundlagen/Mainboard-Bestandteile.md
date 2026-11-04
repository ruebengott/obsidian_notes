---
tags: [berufsschule, lf5, hardware]
fach: LF5
typ: thema
quelle: "[[LF5.pdf#page=3]]"
datum: 2025-09-22
status: zu-lernen
---
# Mainboard-Bestandteile

> [!summary] Kurz & knapp
> Das Mainboard (Hauptplatine) **verbindet alle Komponenten** eines PCs miteinander. Auf ihm sitzen oder an ihm hängen CPU, RAM, BIOS/UEFI-Chip, Erweiterungskarten (z. B. GPU), Speicheranschlüsse (SATA, M.2) und die externen Anschlüsse.

## Komponenten auf bzw. am Mainboard

| Komponente | Aufgabe | Hinweis |
| --- | --- | --- |
| **CPU** (Prozessor) | führt Befehle aus, das „Gehirn“ des PCs | im CPU-Sockel; besteht aus Milliarden **Transistoren**; braucht einen Kühler (Lüfter) |
| **RAM** (Arbeitsspeicher) | hält laufende Programme/Daten kurzfristig bereit | flüchtig, in DIMM-Slots |
| **BIOS/UEFI** | Firmware: startet den PC, prüft die Hardware (POST), lädt den Bootloader | auf Flash-Chip des Mainboards |
| **GPU** (Grafikkarte) | Berechnung und Ausgabe der Grafik | im PCIe-Slot oder in der CPU integriert |
| **SATA-Anschlüsse** | Anschluss von HDD/SSD/optischen Laufwerken | |
| **M.2-Slot** | Anschluss schneller NVMe-SSDs | direkt auf dem Board |
| **Netzwerkkarte / LAN** | Netzwerkverbindung (RJ-45) | meist onboard |
| **Externe Anschlüsse** | HDMI, VGA, DVI, DisplayPort, USB, Audio | I/O-Blende |
| **Chipsatz / Mikrochips** | steuern die Kommunikation zwischen den Komponenten | |
| **Platine** | Leiterplatte mit Leiterbahnen, **Kondensatoren**, **Dioden** usw. | |

> [!warning] Korrektur
> In der Mitschrift stehen auch **PSU** (Netzteil) und **Gehäuse** in der Liste. Beide gehören zum PC, sind aber **nicht Teil des Mainboards**. Das Netzteil versorgt das Mainboard über den 24-Pin-ATX-Stecker mit Strom, und das Gehäuse nimmt alles auf. Auch M.2 ist kein Peripherieanschluss, sondern ein interner Steckplatz für SSDs.

> [!tip] Merke
> - Hauptaufgabe des Mainboards: **Komponenten verbinden**, also die Kommunikation über Bussysteme ermöglichen.
> - Flüchtig = RAM. Nicht flüchtig = BIOS-Flash, SSD, HDD.
> - Bussysteme, Von-Neumann-Architektur und Speicher im Detail: siehe [[LF2 - Übersicht]].

## Lernfragen
> [!question]- Was ist die Hauptaufgabe des Mainboards?
> Es verbindet alle Komponenten des Computers (CPU, RAM, Laufwerke, Erweiterungskarten, Anschlüsse) und ermöglicht über Bussysteme ihre Kommunikation.

> [!question]- Welche Aufgabe hat das BIOS bzw. UEFI?
> Es ist die Firmware des Mainboards. Sie initialisiert und prüft beim Start die Hardware (POST), stellt Grundeinstellungen bereit und startet den Bootloader des Betriebssystems.

> [!question]- Gehört das Netzteil zum Mainboard?
> Nein. Das Netzteil (PSU) ist eine eigene Komponente. Es wandelt Netzstrom (230 V AC) in die Gleichspannungen für den PC um und versorgt das Mainboard über Kabel.

> [!question]- Wo werden HDDs/SSDs angeschlossen?
> Über SATA-Anschlüsse. Schnelle NVMe-SSDs kommen direkt in den M.2-Slot des Mainboards.

> [!question]- Woraus besteht ein Prozessor im Kern?
> Aus sehr vielen Transistoren (Schaltelementen) auf einem Siliziumchip. Zur Kühlung braucht er einen Kühlkörper mit Lüfter.

## Siehe auch
- [[Hardwarekategorien]]
- [[Server-Hardware]]
- [[LF2 - Übersicht]]
- [[LF5 - Übersicht]]
