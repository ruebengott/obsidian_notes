---
tags: [berufsschule, lf2, hardware, speicher]
fach: LF2
typ: thema
quelle: "[[LF2.pdf#page=9]]"
datum: 2025-12-01
status: zu-lernen
---
# Datenträgerorganisation

> [!summary] Kurz & knapp
> Eine Festplatte ist physisch in **Spuren**, **Sektoren** und **Zylinder** eingeteilt. Das Dateisystem fasst Sektoren zu **Blöcken/Clustern** zusammen, der kleinsten Einheit für Dateien. **Partitionen** teilen den Datenträger in logisch getrennte Bereiche.

> [!note] Ergänzung
> Diese Begriffe stehen als Aufgabe 5 auf dem Festplatten-Arbeitsblatt, wurden in der Mitschrift aber nicht beantwortet. Die Erklärungen hier sind Standard-Lehrbuchwissen.

## Begriffe

| Begriff | Erklärung |
| --- | --- |
| **Spur** (Track) | konzentrischer Kreis auf einer Scheibenoberfläche, auf dem Daten liegen |
| **Sektor** | kleinste physische Speichereinheit, ein Abschnitt einer Spur. Früher 512 Byte, heute meist 4096 Byte (Advanced Format). |
| **Zylinder** | alle Spuren mit **gleichem Radius** auf allen Scheiben/Seiten übereinander. Sie können ohne Bewegung des Kopfarms gelesen werden. |
| **Block** | Einheit, in der Betriebssystem/Dateisystem den Datenträger anspricht (logischer Block, LBA = Logical Block Addressing) |
| **Cluster** | Zusammenfassung mehrerer Sektoren, **kleinste Einheit, die das Dateisystem einer Datei zuweist** (z. B. 4 KB bei NTFS). Eine 1-KB-Datei belegt trotzdem einen ganzen Cluster. |
| **Partition** | logisch abgegrenzter Bereich eines Datenträgers mit eigenem Dateisystem (z. B. C: und D:). Verwaltet über [[MBR und GPT]]. |

```mermaid
flowchart LR
    D["Datenträger"] --> P["Partition(en)"]
    P --> FS["Dateisystem (NTFS, ext4, …)"]
    FS --> C["Cluster / Blöcke"]
    C --> S["Sektoren (512 B / 4 KB)"]
```

## Bei SSDs
SSDs haben keine Spuren oder Zylinder. Intern arbeiten sie mit **Pages** (lesen/schreiben) und **Blöcken** (löschen). Nach außen zeigen sie sich aber wie eine Festplatte mit logischen Blöcken (LBA). Partitionen und Cluster gibt es genauso.

> [!tip] Merke
> - Spur = Kreis, Sektor = Stück einer Spur, Zylinder = übereinanderliegende Spuren.
> - Cluster = kleinste Zuordnungseinheit des Dateisystems → „Verschnitt“ bei kleinen Dateien.
> - Partition = logischer Bereich mit eigenem Dateisystem.

## Lernfragen
> [!question]- Was ist ein Zylinder bei einer HDD?
> Die Gesamtheit aller Spuren mit gleichem Radius auf allen Scheibenoberflächen. Sie liegen übereinander und können ohne Kopfbewegung gelesen werden.

> [!question]- Was ist der Unterschied zwischen Sektor und Cluster?
> Der Sektor ist die kleinste physische Einheit des Datenträgers. Der Cluster ist ein Verbund aus Sektoren und die kleinste Einheit, die das Dateisystem einer Datei zuweist.

> [!question]- Warum belegt eine 1-KB-Datei bei 4-KB-Clustern 4 KB?
> Weil das Dateisystem nur ganze Cluster vergeben kann. Der Rest des Clusters bleibt ungenutzt (Verschnitt).

> [!question]- Wozu dienen Partitionen?
> Um einen Datenträger in logisch getrennte Bereiche aufzuteilen, z. B. für System und Daten, für mehrere Betriebssysteme oder für die EFI-Systempartition.

## Siehe auch
- [[HDD und SSD]]
- [[MBR und GPT]]
- [[BIOS und UEFI]]
