---
tags: [berufsschule, lf2, hardware, speicher]
fach: LF2
typ: thema
quelle: "[[LF2.pdf#page=9]]"
datum: 2025-12-01
status: zu-lernen
---
# HDD und SSD

> [!summary] Kurz & knapp
> Eine **HDD** speichert Daten **magnetisch** auf rotierenden Scheiben, die ein Schreib-/Lesekopf mechanisch abtastet. Sie ist günstig pro TB, aber langsam und stoßempfindlich. Eine **SSD** speichert **elektronisch** in Flash-Zellen. Sie hat keine beweglichen Teile, ist sehr schnell und robust, ihre Zellen vertragen aber nur begrenzt viele **Schreibzyklen**.

## HDD vs. SSD (Aufgabe 1)

| Merkmal | HDD (Hard Disk Drive) | SSD (Solid State Drive) |
| --- | --- | --- |
| Speicherprinzip | magnetisch auf rotierenden Scheiben | elektronisch in Flash-Speicherzellen (NAND) |
| bewegliche Teile | ja (Spindel, Kopfarm) | nein |
| Geschwindigkeit | ca. 100–250 MB/s, Zugriffszeit einige ms | SATA ca. 550 MB/s, NVMe (PCIe) mehrere GB/s, Zugriffszeit < 0,1 ms |
| Stoßempfindlichkeit | hoch (Headcrash) | gering |
| Geräusch, Wärme, Strom | laut, mehr Strom | lautlos, sparsam |
| Preis pro TB | günstig | teurer |
| Verschleiß | mechanisch (Lager, Motor) | begrenzte Schreibzyklen der Zellen |
| typischer Einsatz | große Datengräber, Backups, NAS | Betriebssystem, Programme, Laptops |

> [!warning] Korrektur
> In der Mitschrift steht „HDD: physischer Speicher, langlebig – SSD: digitaler Speicher, hält nicht ewig“. Das ist missverständlich:
> - **Beide** speichern Daten physisch und digital (als Bits). Der Unterschied ist **magnetisch** (HDD) vs. **elektronisch/Flash** (SSD).
> - Auch HDDs halten nicht ewig. Sie verschleißen **mechanisch**. Moderne SSDs erreichen im normalen Büroalltag meist eine ähnliche oder höhere Lebensdauer als HDDs.

## Umdrehungsgeschwindigkeit (Aufgabe 2)
- Angabe in **U/min** (rpm), typisch **5400, 7200, 10 000 oder 15 000 U/min**
- Je schneller die Scheibe dreht, desto schneller kommt der gesuchte Sektor unter den Kopf (geringere **Latenz**) und desto höher ist die **Datenrate**.
- Nachteile höherer Drehzahl: mehr Lärm, Wärme und Stromverbrauch

## Lebensdauer einer SSD (Aufgabe 3)
Flash-Zellen verschleißen bei jedem **Schreib-/Löschvorgang**. Gemessen bzw. angegeben wird die Lebensdauer über:
- **TBW** (Terabytes Written): garantierte Gesamtschreibmenge, z. B. 600 TBW
- **DWPD** (Drive Writes Per Day): wie oft die SSD pro Tag komplett beschrieben werden darf (Garantiezeit)
- **P/E-Zyklen** (Program/Erase) pro Zelle: SLC > MLC > TLC > QLC
- **Wear Leveling** verteilt die Schreibvorgänge gleichmäßig auf alle Zellen und verlängert so die Lebensdauer. Der Zustand lässt sich über **S.M.A.R.T.**-Werte auslesen.

## Aufbau einer HDD (Aufgabe 4)

![[LF2.pdf#page=9]]

| Nr. | Komponente | Funktion |
| --- | --- | --- |
| 1 | Magnetscheibe (Platter) | Datenspeicherung auf der magnetischen Beschichtung |
| 2 | Spindel mit Spindelmotor | dreht die Scheiben mit konstanter Geschwindigkeit (U/min) |
| 3 | Schreib-/Lesekopf | liest und schreibt die Daten berührungslos (schwebt auf einem Luftpolster) |
| 4 | Schreib-/Lesearm (Kopfarm) | trägt den Kopf und bewegt ihn über die Spuren |
| 5 | Achse des Kopfarms | Drehpunkt, um den der Arm schwenkt |
| 6 | Anschlüsse | Daten- und Stromanschluss (SATA) |
| 8 | Aktuator (Schwingspulenmotor) | bewegt den Kopfarm schnell und präzise |

> [!note] Hinweis
> In der Mitschrift sind nur 1–5 beschriftet (4 und 5 beide als „Achse“). Die Zuordnung für 4–8 oben ist die übliche Lehrbuchbeschriftung und wurde **ergänzt**. Die Nummer 7 (Pfeil links unten ohne Zahl) zeigt vermutlich auf Jumper/Anschlussbereich. Bitte mit dem Original-Arbeitsblatt abgleichen.

## Begriffe (Aufgabe 5)
Die Begriffe Spur, Zylinder, Sektor, Block, Cluster und Partition werden in [[Datenträgerorganisation]] erklärt. In der Mitschrift waren sie noch unbeantwortet.

> [!tip] Merke
> - HDD = magnetisch + mechanisch. SSD = Flash + ohne bewegliche Teile.
> - Höhere Drehzahl → kürzere Zugriffszeit, höhere Datenrate.
> - SSD-Lebensdauer: TBW / P/E-Zyklen, Wear Leveling.
> - Für das Betriebssystem: SSD. Für große, günstige Datenmengen: HDD.

## Lernfragen
> [!question]- Nenne drei Unterschiede zwischen HDD und SSD.
> Speicherprinzip (magnetisch vs. Flash), bewegliche Teile (ja vs. nein), Geschwindigkeit (SSD viel schneller). Außerdem: Preis pro TB (HDD günstiger), Stoßfestigkeit (SSD besser).

> [!question]- Wie wirkt sich die Umdrehungsgeschwindigkeit einer HDD auf die Leistung aus?
> Je höher die Drehzahl (z. B. 7200 statt 5400 U/min), desto kürzer die Wartezeit auf den Sektor und desto höher die Datenrate.

> [!question]- Wie wird die Lebensdauer einer SSD angegeben?
> Über die Anzahl möglicher Schreibzyklen, meist als TBW (Terabytes Written) oder DWPD.

> [!question]- Was ist Wear Leveling?
> Ein Verfahren des SSD-Controllers, das Schreibvorgänge gleichmäßig auf alle Flash-Zellen verteilt, damit keine Zelle vorzeitig verschleißt.

> [!question]- Welche Aufgabe hat der Aktuator in einer HDD?
> Er bewegt den Kopfarm mit dem Schreib-/Lesekopf schnell und präzise über die Spuren der Magnetscheibe.

## Siehe auch
- [[Datenträgerorganisation]]
- [[Speicherarten]]
- [[PCIe]]
- [[MBR und GPT]]
- [[Hardwarekategorien]]
