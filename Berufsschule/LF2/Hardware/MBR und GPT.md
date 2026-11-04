---
tags: [berufsschule, lf2, hardware, firmware, speicher]
fach: LF2
typ: thema
quelle: "[[LF2.pdf#page=16]]"
datum: 2026-01-14
status: zu-lernen
---
# MBR und GPT

> [!summary] Kurz & knapp
> **MBR** (Master Boot Record) und **GPT** (GUID Partition Table) sind Partitionsschemata, die festlegen, wie ein Datenträger in Partitionen eingeteilt wird. MBR ist alt (max. 2 TiB, 4 primäre Partitionen) und gehört zum BIOS. GPT ist modern (sehr große Datenträger, bis 128 Partitionen, Sicherungskopie und CRC-Prüfsummen) und gehört zu UEFI.

## Vergleich

| Merkmal | MBR | GPT |
| --- | --- | --- |
| Name | Master Boot Record | GUID Partition Table |
| Herkunft | 1983, BIOS-Zeit | Teil des UEFI-Standards |
| max. Datenträgergröße | **2 TiB** (bei 512-Byte-Sektoren) | ca. **9,4 ZB** (praktisch unbegrenzt) |
| max. Partitionen | **4 primäre** (oder 3 + erweiterte mit logischen Laufwerken) | **128** (unter Windows, Standard) |
| Speicherort | erster Sektor (512 Byte: Bootcode + Partitionstabelle) | Header am Anfang **und Kopie am Ende** des Datenträgers |
| Datensicherheit | keine Prüfsummen, nur eine Kopie | **CRC32-Prüfsummen**, Backup-Header → Reparatur möglich |
| Partitions-IDs | 1-Byte-Typcode | eindeutige GUIDs |
| Booten | BIOS (Legacy) | UEFI (BIOS nur eingeschränkt) |

## Vorteile von GPT (Aufgabe 3)
- Unterstützung **großer Festplatten über 2 TB**
- bis zu **128 Partitionen**, keine Tricks mit erweiterten Partitionen nötig
- **höhere Datensicherheit**: CRC-Prüfsummen und redundante Partitionstabelle
- mehr Flexibilität (GUIDs, Partitionsnamen)
- UEFI nutzt das, indem es von großen Datenträgern bootet und die Bootloader auf der EFI-Systempartition findet. So lassen sich auch mehrere Betriebssysteme einfach starten.

> [!tip] Merke
> - MBR: 2 TiB, 4 primäre Partitionen, BIOS.
> - GPT: riesige Datenträger, 128 Partitionen, Backup + CRC, UEFI.
> - Neue Systeme: **UEFI + GPT**.

## Lernfragen
> [!question]- Welche Grenzen hat MBR?
> Maximal 2 TiB Datenträgergröße und maximal 4 primäre Partitionen. Es gibt keine Sicherungskopie der Partitionstabelle.

> [!question]- Warum ist GPT ausfallsicherer als MBR?
> GPT speichert die Partitionstabelle doppelt (Anfang und Ende) und sichert sie mit CRC32-Prüfsummen ab. Fehler werden erkannt und können repariert werden.

> [!question]- Welches Partitionsschema braucht man für eine 4-TB-Bootfestplatte?
> GPT (mit UEFI). MBR kann nur 2 TiB adressieren.

> [!question]- Welche Firmware gehört typischerweise zu welchem Schema?
> BIOS → MBR, UEFI → GPT.

## Siehe auch
- [[BIOS und UEFI]]
- [[Datenträgerorganisation]]
- [[HDD und SSD]]
