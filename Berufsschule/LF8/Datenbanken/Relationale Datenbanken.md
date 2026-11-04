---
tags: [berufsschule, lf8, datenbanken]
fach: LF8
typ: thema
quelle: "[[LF8.pdf#page=7]]"
datum:
status: zu-lernen
---
# Relationale Datenbanken

> [!summary] Kurz & knapp
> Eine **relationale Datenbank** ist eine Sammlung von Tabellen (Relationen), die über **Schlüssel** miteinander verknüpft sind. Verwaltet wird sie von einem **Datenbankmanagementsystem (DBMS)**, z. B. MySQL, PostgreSQL oder MS SQL Server. Abgefragt wird sie mit SQL.

## Was ist eine Datenbank?
Eine Datenbank ist eine **strukturierte, dauerhafte Sammlung zusammengehöriger Daten**. Das **DBMS** verwaltet sie: Es regelt Speicherung, Abfrage, gleichzeitigen Zugriff mehrerer Benutzer, Rechte und Datensicherheit. Datenbank und DBMS zusammen nennt man **Datenbanksystem (DBS)**.

## Vorteile der Speicherung in Tabellen
- einheitliche, übersichtliche **Struktur**: jeder Datensatz hat dieselben Attribute
- Daten lassen sich leicht **suchen, sortieren, filtern**
- jeder Wert hat einen festen Platz und einen festen Datentyp
- Tabellen lassen sich über Schlüssel **verknüpfen**, sodass Daten nicht doppelt gespeichert werden müssen

## Fachbegriffe

| Alltagsbegriff | Fachbegriff | Beispiel (Tabelle `benutzer`) |
| --- | --- | --- |
| Tabelle | **Relation** / Tabellenname | `benutzer` |
| Spalte / Spaltenüberschrift | **Attribut** | `Vorname` |
| Zeile | **Datensatz** (Tupel) | `Lindemann, Erwin, lindemannerwin71@…, 1971-09-18` |
| Zelle / Tabelleneintrag | **Datenwert** (Attributwert) | `lindemannerwin71@…` |
| eindeutige Kennung | **Primärschlüssel (PK)** | z. B. `BenutzerID` |
| Verweis auf andere Tabelle | **Fremdschlüssel (FK)** | z. B. `KontoNr` in `Kontoinhaber` |

| Name | Vorname | Email | GebDat |
| --- | --- | --- | --- |
| Winkelmann | Paul | winkelpaul80@… | 1980-10-02 |
| **Lindemann** | **Erwin** | **lindemannerwin71@…** | **1971-09-18** |
| Heubel | Monika | heubel.m@elgoog.com | 1993-01-15 |
| Faas | Sigrid | faas.sig@oohay.de | 1983-05-02 |

## Atomare Datenwerte
**Atomar** heißt: Jeder Datenwert ist **unteilbar** und enthält genau eine Information.
- nicht atomar: `Adresse = "Hauptstr. 5, 24768 Rendsburg"` → atomar: `Straße`, `Hausnr`, `PLZ`, `Ort`
- nicht atomar: `Flüsse = "Donau, Rhein, Elbe"` (mehrere Werte in einer Zelle)

Atomare Werte sind die Voraussetzung für die 1. Normalform, siehe [[Normalisierung]].

## Warum keine Tabellenkalkulation als Datenbank?
- **Kein Mehrbenutzerbetrieb:** Die Datei ist gesperrt, solange sie jemand bearbeitet („Dokument wird verwendet … schreibgeschützt öffnen“).
- Es gibt **keine Beziehungen und keine referenzielle Integrität** zwischen Tabellen. Dadurch entstehen leicht Redundanz und Widersprüche (Anomalien).
- **Keine Datentyp-/Eingabeprüfung** und keine feingranularen Zugriffsrechte
- schlechte Performance und Unübersichtlichkeit bei großen Datenmengen
- keine Transaktionen, unsicheres Backup/Recovery

> [!tip] Merke
> **Tabelle = Relation, Spalte = Attribut, Zeile = Datensatz, Zelle = Datenwert.** Der Primärschlüssel identifiziert einen Datensatz eindeutig, der Fremdschlüssel verweist auf den Primärschlüssel einer anderen Tabelle.

## Lernfragen
> [!question]- Was ist eine relationale Datenbank?
> Eine Sammlung von Tabellen (Relationen), deren Datensätze über Primär- und Fremdschlüssel miteinander verknüpft sind. Sie wird von einem DBMS verwaltet.

> [!question]- Benenne die Fachbegriffe für Tabelle, Spalte, Zeile und Zelle.
> Relation/Tabellenname, Attribut, Datensatz (Tupel), Datenwert.

> [!question]- Was bedeutet „atomar“? Gib ein Gegenbeispiel.
> Jeder Datenwert ist unteilbar und enthält genau eine Information. Gegenbeispiel: Eine Spalte „Adresse“ mit Straße, PLZ und Ort in einem Feld.

> [!question]- Welche Probleme entstehen, wenn man eine Datenbank mit Excel umsetzt?
> Kein gleichzeitiger Zugriff mehrerer Benutzer (Datei gesperrt), keine echten Beziehungen und keine referenzielle Integrität, Redundanz und Inkonsistenzen, keine Typprüfung, kaum Rechteverwaltung, schlechte Performance bei großen Datenmengen.

> [!question]- Was ist der Unterschied zwischen Primär- und Fremdschlüssel?
> Der Primärschlüssel identifiziert jeden Datensatz einer Tabelle eindeutig. Der Fremdschlüssel ist ein Attribut, das auf den Primärschlüssel einer anderen Tabelle verweist und so die Beziehung herstellt.

## Siehe auch
- [[ER-Modell]]
- [[ER-Modell in Tabellen überführen]]
- [[Normalisierung]]
- [[Datenformate CSV JSON XML]]
- [[LF8 - Übersicht]]
