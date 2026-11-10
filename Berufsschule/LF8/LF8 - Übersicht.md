---
tags: [berufsschule, lf8]
fach: LF8
typ: übersicht
quelle: "[[LF8.pdf]]"
status: zu-lernen
---
# LF8 – Daten systemübergreifend bereitstellen

← [[Berufsschule]]

> [!info] Inhalt
> Zwei Blöcke: **Softwarequalität** (ISO/IEC 25010) und **Datenbanken** (relationales Modell, ER-Modell, Normalisierung, SQL). Quellen: OneNote-Export `LF8.pdf`, Moodle-Kurs BBZ (Kapitel 3.7.2) und Arbeitsblatt „3.2.1.2 Relationale Datenbanken“ (inf-schule).

## 1. Softwarequalität
1. [[Qualitätsbegriff]]: Was ist Qualität? Acht Sichtweisen, funktionale und nicht-funktionale Anforderungen
2. [[ISO 25010 Produktqualität]]: Die 9 Produktqualitätsmerkmale der ISO/IEC 25010:2023
3. [[Qualitätsmodell der Nutzung]]: Die 5 Merkmale der Nutzungsqualität und die Abgrenzung zur Produktqualität

## 2. Datenbanken
4. [[Relationale Datenbanken]]: Fachbegriffe (Relation, Attribut, Datensatz, Datenwert), atomare Werte, warum kein Excel
5. [[ER-Modell]]: Entwurfsphasen, Chen-Notation, Kardinalitäten
6. [[ER-Modell in Tabellen überführen]]: Regeln für 1:1, 1:n, m:n (Zwischentabelle)
7. [[Normalisierung]]: Anomalien, 1NF, 2NF, 3NF

### SQL (SQLite, DB Browser for SQLite)
8. [[SQL - DDL Tabellen und Schlüssel anlegen]]: CREATE TABLE, Datentypen, Primär- und Fremdschlüssel, View
9. [[SQL - DML INSERT UPDATE DELETE]]: Daten einfügen, ändern, löschen; INSERT ... SELECT
10. [[SQL - SELECT und JOIN]]: Abfragen, WHERE, GROUP BY, INNER und LEFT JOIN

## Übungen
- [[Produktqualität am Beispiel Grafana]]: Rechercheauftrag ISO 25010 und Anwendung auf ein Monitoring-Dashboard
- [[Kompetenzcheck ER-Modell]]: Aussagen zu den Entwurfsphasen, ER-Modelle (Musiker, Bank), Überführung (Astronauten)
- [[Übungsaufgaben]]: Normalisierung von Ländern und Flüssen (1NF bis 3NF) sowie Mitglieder
- [[Datenbank Aufgaben]]: Bestellungen zerlegen (Kunde, Produkt, Bestellung)
- [[Übung Normalisierung Bestellungen in SQLite]]: BestellungenRoh bis zur 3NF in SQLite, mit Korrektur und SQL-Lösung

## Verwandte Lernfelder
- [[LF5 - Übersicht]]: Datenformate CSV/JSON/XML, UML
