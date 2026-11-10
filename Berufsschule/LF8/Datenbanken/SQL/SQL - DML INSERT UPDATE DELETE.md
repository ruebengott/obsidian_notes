---
tags: [berufsschule, lf8, datenbanken, sql, dml]
fach: LF8
typ: thema
quelle: "[[normalisierung_redundant_angepasst.sqbpro]]"
datum: 2026-11-04
status: zu-lernen
---
# SQL - DML: INSERT, UPDATE, DELETE

> [!summary] Kurz & knapp
> Mit der **DML** (Data Manipulation Language) verändert man die **Daten** in den Tabellen: `INSERT INTO` fügt Datensätze ein, `UPDATE ... SET` ändert sie, `DELETE FROM` löscht sie. Bei `UPDATE` und `DELETE` bestimmt die **`WHERE`-Bedingung**, welche Zeilen betroffen sind. Fehlt sie, trifft es **alle** Zeilen. Mit `INSERT INTO ... SELECT` überträgt man Daten aus einer redundanten Tabelle in normalisierte Tabellen.

## INSERT INTO – Datensätze einfügen
```sql
-- einen Datensatz einfügen, Spalten ausdrücklich nennen
INSERT INTO Orte (ort, plz) VALUES ('Rendsburg', '24768');

-- mehrere Datensätze auf einmal
INSERT INTO Produkte (name, preis) VALUES
    ('Maus',     19.99),
    ('Tastatur', 49.90);
```
- Texte und Datumswerte stehen in **einfachen Anführungszeichen**, Zahlen ohne. Das Dezimaltrennzeichen ist der **Punkt**.
- Den Primärschlüssel `INTEGER PRIMARY KEY` lässt man weg, SQLite vergibt ihn automatisch.
- Wegen der Fremdschlüssel gilt eine **Reihenfolge**: erst `Orte`, dann `Kunden`, dann `Bestellungen`. Sonst gibt es den Fehler „FOREIGN KEY constraint failed“.

### INSERT INTO ... SELECT – Daten umziehen
Beim Normalisieren liegen die Daten schon in einer großen Tabelle (z. B. `BestellungenRoh`). Statt alles abzutippen, übernimmt man sie per Abfrage:
```sql
-- jeden Ort nur einmal übernehmen
INSERT INTO Orte (ort, plz)
SELECT DISTINCT ort, plz FROM BestellungenRoh;

-- jedes Produkt nur einmal übernehmen
INSERT INTO Produkte (name, preis)
SELECT DISTINCT produkt_name, produkt_preis FROM BestellungenRoh;
```
`DISTINCT` entfernt doppelte Zeilen. Genau das ist der Abbau von **Redundanz**.

## UPDATE – Datensätze ändern
```sql
UPDATE Produkte
SET preis = 21.99
WHERE produkt_id = 1;
```
Nach der Normalisierung steht der Preis nur noch **an einer Stelle**. Ein einziges `UPDATE` reicht, die **Änderungsanomalie** ist beseitigt. In der unnormalisierten Tabelle müsste man jede Bestellzeile mit diesem Produkt ändern.

Mehrere Spalten gleichzeitig:
```sql
UPDATE Kunden
SET email = 'neu@example.de', ort_id = 2
WHERE kunden_id = 3;
```

## DELETE – Datensätze löschen
```sql
DELETE FROM Bestellungen WHERE bestell_id = 7;
```
Löscht man die letzte Bestellung eines Kunden, bleibt der Kunde in `Kunden` erhalten. Die **Löschanomalie** ist beseitigt.

Bei aktivierten Fremdschlüsseln verweigert SQLite das Löschen eines Kunden, der noch Bestellungen hat (Standard `RESTRICT`/`NO ACTION`, siehe [[SQL - DDL Tabellen und Schlüssel anlegen]]).

> [!warning] WHERE nie vergessen
> `UPDATE Produkte SET preis = 0;` oder `DELETE FROM Kunden;` ohne `WHERE` betreffen **alle Zeilen**. Tipp: Die Bedingung zuerst mit `SELECT * FROM ... WHERE ...` testen und erst dann `UPDATE`/`DELETE` ausführen. Im DB Browser werden Änderungen erst mit **„Änderungen schreiben“** (Strg+S) dauerhaft gespeichert, vorher kann man sie verwerfen.

## Vergleich
| Befehl | Syntax | Betrifft |
|---|---|---|
| `INSERT` | `INSERT INTO t (sp1, sp2) VALUES (w1, w2);` | neue Zeile(n) |
| `UPDATE` | `UPDATE t SET sp = w WHERE bedingung;` | vorhandene Zeilen, die die Bedingung erfüllen |
| `DELETE` | `DELETE FROM t WHERE bedingung;` | vorhandene Zeilen, die die Bedingung erfüllen |

> [!tip] Merke
> - `INSERT INTO ... VALUES` bzw. `INSERT INTO ... SELECT`
> - `UPDATE ... SET ... WHERE`
> - `DELETE FROM ... WHERE`
> - **Ohne WHERE trifft es alle Zeilen!**
> - Reihenfolge wegen Fremdschlüsseln: erst die Tabelle auf der 1-Seite (Orte, Kunden, Produkte), dann die n-Seite (Bestellungen)

## Lernfragen
> [!question]- Füge den Kunden „Lena Meyer“ mit E-Mail lena@example.de aus dem Ort mit der ID 2 ein.
> ```sql
> INSERT INTO Kunden (name, email, ort_id) VALUES ('Lena Meyer', 'lena@example.de', 2);
> ```

> [!question]- Was passiert bei `DELETE FROM Bestellungen;`?
> Alle Bestellungen werden gelöscht, weil die WHERE-Bedingung fehlt. Die Tabelle selbst bleibt bestehen (anders als bei DROP TABLE).

> [!question]- Wozu dient `INSERT INTO ... SELECT DISTINCT` beim Normalisieren?
> Damit überträgt man Daten aus der redundanten Ausgangstabelle in die neuen Tabellen. DISTINCT sorgt dafür, dass jeder Ort bzw. jedes Produkt nur einmal gespeichert wird.

> [!question]- Warum schlägt ein INSERT in `Bestellungen` mit `kunden_id = 99` fehl?
> Weil es keinen Kunden mit der ID 99 gibt und der Fremdschlüssel die referenzielle Integrität prüft.

> [!question]- Wie zeigt sich die Beseitigung der Änderungsanomalie in SQL?
> Eine Preisänderung ist ein einziges UPDATE auf genau eine Zeile in `Produkte`, statt viele Bestellzeilen ändern zu müssen.

## Siehe auch
- [[SQL - DDL Tabellen und Schlüssel anlegen]]
- [[SQL - SELECT und JOIN]]
- [[Normalisierung]]
- [[Übung Normalisierung Bestellungen in SQLite]]
