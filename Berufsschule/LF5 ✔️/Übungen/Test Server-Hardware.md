---
tags: [berufsschule, lf5, server, übung]
fach: LF5
typ: übung
quelle: "[[LF5.pdf#page=10]]"
datum: 2025-10-07
status: zu-lernen
---
# Test Server-Hardware

> [!summary] Kurz & knapp
> Übungstest „Server-Hardware: Grundlagen und Komponenten“ mit USV, ECC-RAM, RAID, Hot-Swap, Blade-, Tower- und Rack-Server. Theorie dazu in [[Server-Hardware]] und [[RAID-Level]].

## Teil A: Multiple Choice

**1. Welche Komponente ist speziell für die unterbrechungsfreie Stromversorgung eines Servers zuständig?**
a) Netzteil, b) USV, c) RAID-Controller, d) Switch
> [!success]- Lösung
> **b) USV**

**2. Was ist ein typisches Merkmal von Server-Prozessoren im Vergleich zu Desktop-Prozessoren?**
a) Geringerer Stromverbrauch, b) Eingebaute Grafikeinheit, c) Unterstützung für ECC-RAM, d) Nur ein CPU-Kern
> [!success]- Lösung
> **c) Unterstützung für ECC-RAM**. In der Mitschrift war hier nichts markiert.

**3. Wofür steht die Abkürzung „RAID“?**
a) Random Access Integrated Device, b) Redundant Array of Independent Disks, c) Rapid Access Internal Drive, d) Remote Access Interface Device
> [!success]- Lösung
> **b) Redundant Array of Independent Disks**

**4. Welche Netzwerkschnittstelle ist in modernen Servern am häufigsten für hohe Datenübertragungsraten verbaut?**
a) VGA, b) USB, c) HDMI, d) Ethernet (RJ-45)
> [!success]- Lösung
> **d) Ethernet (RJ-45)**

**5. Was ist der Zweck eines RAID-Controllers?**
a) Steuerung der Lüftergeschwindigkeit, b) Verwaltung von Festplatten in einem RAID-Verbund, c) Überwachung der CPU-Temperatur, d) Bereitstellung von Netzwerkdiensten
> [!success]- Lösung
> **b) Verwaltung von Festplatten in einem RAID-Verbund**

## Teil B: Zuordnung

| Begriff | Beschreibung |
| --- | --- |
| 1. ECC-RAM | A. Redundante Stromversorgung bei Ausfall eines Netzteils |
| 2. Hot-Swap | B. Fehlerkorrigierender Arbeitsspeicher |
| 3. Blade-Server | C. Austausch von Komponenten im laufenden Betrieb |
| 4. Redundantes PSU | D. Kompakte Servereinheit in einem Gehäuse mit mehreren Einschüben |

> [!success]- Lösung
> 1 → B, 2 → C, 3 → D, 4 → A

## Teil C: Offene Fragen

**1. Erkläre den Unterschied zwischen einem Tower-Server und einem Rack-Server.**
> [!success]- Lösung
> - **Tower-Server:** sieht aus wie ein normaler Desktop-PC, braucht pro Gerät mehr Platz, ist mit eigenen Lüftern für den Einzelbetrieb gedacht und günstiger in der Anschaffung.
> - **Rack-Server:** genormte Größe (19 Zoll, Höheneinheiten), sodass mehrere Server übereinander im Serverschrank montiert werden. Effiziente Kühlung ist möglich, Einsatz in Serverräumen und großen Rechenzentren.

**2. Warum ist eine USV für Serverumgebungen wichtig?**
> [!success]- Lösung
> Sie überbrückt Stromausfälle und Spannungsschwankungen. Die Server laufen weiter oder fahren kontrolliert herunter, sodass kein Datenverlust und keine beschädigten Dateisysteme entstehen. Da die Verfügbarkeit der Server für das Unternehmen wirtschaftlich entscheidend ist, schützt die USV auch vor Ausfallkosten.

**3. Welche Vorteile bietet ein RAID 5 gegenüber einem RAID 0?**
> [!success]- Lösung
> - **RAID 0:** Daten werden in Blöcke aufgeteilt und abwechselnd auf mehrere Platten geschrieben. Das bringt hohe Geschwindigkeit, aber **keine Redundanz**: Fällt eine Platte aus, sind alle Daten verloren.
> - **RAID 5:**
>   - **Datensicherheit:** schützt vor dem Ausfall **einer** Festplatte (Parität)
>   - **Effiziente Speichernutzung:** Nur die Kapazität einer Platte geht für die Parität verloren (4 × 1 TB = 3 TB nutzbar)
>   - **Gute Leseleistung:** paralleles Lesen von mehreren Platten

## Siehe auch
- [[Server-Hardware]]
- [[RAID-Level]]
- [[Test Grundbegriffe Hardware und Software]]
