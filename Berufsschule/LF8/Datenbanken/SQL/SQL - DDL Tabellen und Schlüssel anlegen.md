---
tags: [berufsschule, lf8, datenbanken, sql, ddl]
fach: LF8
typ: thema
quelle: "[[normalisierung_redundant_angepasst.sqbpro]]"
datum: 2026-11-04
status: zu-lernen
---
# SQL - DDL: Tabellen und Schlüssel anlegen

> [!summary] Kurz & knapp
> Mit der **DDL** (Data Definition Language) legt man die **Struktur** einer Datenbank fest: `CREATE TABLE` erzeugt eine Tabelle mit Spalten und **Datentypen**, `PRIMARY KEY` und `FOREIGN KEY ... REFERENCES` setzen die Schlüssel um, die beim [[ER-Modell in Tabellen überführen|Überführen]] und [[Normalisierung|Normalisieren]] entstanden sind. `ALTER TABLE` ändert eine Tabelle, `DROP TABLE` löscht sie. Im Unterricht wird **SQLite** mit dem Programm **DB Browser for SQLite** genutzt.

## SQL-Befehlsgruppen
| Gruppe | Bedeutung | Befehle |
|---|---|---|
| **DDL** – Data Definition Language | Struktur anlegen und ändern | `CREATE`, `ALTER`, `DROP` |
| **DML** – Data Manipulation Language | Daten einfügen, ändern, löschen | `INSERT`, `UPDATE`, `DELETE` → [[SQL - DML INSERT UPDATE DELETE]] |
| **DQL** – Data Query Language | Daten abfragen | `SELECT` → [[SQL - SELECT und JOIN]] |

## CREATE TABLE
```sql
CREATE TABLE Orte (
    ort_id INTEGER PRIMARY KEY,   -- Primärschlüssel, zählt in SQLite automatisch hoch
    ort    TEXT NOT NULL,
    plz    TEXT NOT NULL
);
```
- Jede Spalte hat einen **Namen** und einen **Datentyp**.
- Mehrere Spalten werden durch **Komma** getrennt, der Befehl endet mit **Semikolon**.
- `-- ...` ist ein Kommentar.

## Datentypen (SQLite)
| Typ | Inhalt | Beispiel |
|---|---|---|
| `INTEGER` | Ganzzahl | IDs, Menge |
| `REAL` | Kommazahl | Preis `19.99` |
| `TEXT` | Zeichenkette | Name, E-Mail, **PLZ** |
| `NUMERIC` | Zahl oder Datum, je nach Wert | |
| `BLOB` | Binärdaten | Bilder |

> [!info] SQLite vs. andere DBMS
> SQLite kennt nur diese wenigen Speicherklassen. In MySQL, PostgreSQL oder MS SQL gibt es genauere Typen, z. B. `VARCHAR(100)` (Text mit max. 100 Zeichen), `DECIMAL(8,2)` (Geldbeträge exakt), `DATE` (Datum). SQLite speichert ein Datum als `TEXT` im Format `'YYYY-MM-DD'`.

> [!tip] PLZ als TEXT
> Eine Postleitzahl ist keine Rechengröße und kann mit **0** beginnen (`01067` Dresden). Als `INTEGER` würde die führende Null verloren gehen. Deshalb `TEXT`.

## Einschränkungen (Constraints)
| Constraint | Wirkung |
|---|---|
| `PRIMARY KEY` | eindeutig und nicht leer, identifiziert jeden Datensatz |
| `NOT NULL` | Spalte darf nicht leer sein |
| `UNIQUE` | Wert darf nur einmal vorkommen (z. B. E-Mail) |
| `DEFAULT wert` | Standardwert, wenn nichts angegeben wird |
| `CHECK (bedingung)` | Wert muss die Bedingung erfüllen, z. B. `CHECK (preis >= 0)` |
| `FOREIGN KEY ... REFERENCES` | Wert muss in der referenzierten Tabelle existieren |

## Primärschlüssel und Fremdschlüssel
```sql
CREATE TABLE Kunden (
    kunden_id INTEGER PRIMARY KEY,
    name      TEXT NOT NULL,
    email     TEXT UNIQUE,
    ort_id    INTEGER NOT NULL,
    FOREIGN KEY (ort_id) REFERENCES Orte(ort_id)
);
```
- Der **Fremdschlüssel** `Kunden.ort_id` verweist auf den Primärschlüssel `Orte.ort_id`. Das setzt die 1:n-Beziehung „ein Ort hat viele Kunden“ um (FK auf die n-Seite).
- Die Datenbank prüft dann die **referenzielle Integrität**: Ein Kunde mit `ort_id = 99` wird abgelehnt, wenn es den Ort 99 nicht gibt.

**Zusammengesetzter Primärschlüssel** (z. B. bei einer m:n-Zwischentabelle):
```sql
CREATE TABLE LandFluss (
    land_id   INTEGER,
    flussname TEXT,
    PRIMARY KEY (land_id, flussname),
    FOREIGN KEY (land_id)   REFERENCES Land(land_id),
    FOREIGN KEY (flussname) REFERENCES Fluss(flussname)
);
```

> [!warning] Fremdschlüssel in SQLite einschalten
> SQLite prüft Fremdschlüssel nur, wenn sie eingeschaltet sind: `PRAGMA foreign_keys = ON;`. Im DB Browser ist das unter *Einstellungen → Datenbank → Fremdschlüssel* standardmäßig aktiv (im Projekt `normalisierung_redundant_angepasst` steht `foreign_keys="1"`).

### ON DELETE / ON UPDATE
Was passiert mit abhängigen Datensätzen, wenn der referenzierte Datensatz gelöscht wird?
| Option | Wirkung |
|---|---|
| `RESTRICT` / `NO ACTION` (Standard) | Löschen wird verweigert, solange es abhängige Datensätze gibt |
| `CASCADE` | abhängige Datensätze werden mitgelöscht bzw. mitgeändert |
| `SET NULL` | der Fremdschlüssel wird auf `NULL` gesetzt |

```sql
FOREIGN KEY (kunden_id) REFERENCES Kunden(kunden_id) ON DELETE RESTRICT
```

## ALTER TABLE und DROP TABLE
```sql
ALTER TABLE Kunden ADD COLUMN telefon TEXT;      -- Spalte ergänzen
ALTER TABLE Kunden RENAME TO Kunde;              -- Tabelle umbenennen
DROP TABLE IF EXISTS BestellungenRoh;            -- Tabelle samt Daten löschen
```
`DROP TABLE` löscht **Struktur und Daten** endgültig. Erst ausführen, wenn die Daten in die neuen Tabellen übernommen wurden.

## Sicht (VIEW)
Eine **View** ist eine gespeicherte `SELECT`-Abfrage, die wie eine Tabelle benutzt werden kann. Sie speichert keine eigenen Daten.
```sql
CREATE VIEW Bestelluebersicht AS
SELECT k.name, k.email, o.ort, o.plz, p.name AS produkt, p.preis, b.datum
FROM Bestellungen b
JOIN Kunden   k ON b.kunden_id  = k.kunden_id
JOIN Orte     o ON k.ort_id     = o.ort_id
JOIN Produkte p ON b.produkt_id = p.produkt_id;
```
So sieht man nach der Normalisierung wieder alles in einer Tabelle, ohne Redundanz zu speichern (siehe [[SQL - SELECT und JOIN]]).

> [!tip] Merke
> - DDL = Struktur: `CREATE`, `ALTER`, `DROP`
> - Jede Tabelle braucht einen **Primärschlüssel**
> - Beziehungen über **`FOREIGN KEY (spalte) REFERENCES Tabelle(spalte)`**, FK auf der n-Seite
> - In SQLite: `PRAGMA foreign_keys = ON;`
> - PLZ, Telefonnummer → `TEXT`; Geld → `REAL` (SQLite) bzw. `DECIMAL(8,2)`

## Lernfragen
> [!question]- Was ist der Unterschied zwischen DDL und DML?
> DDL legt die Struktur fest (CREATE, ALTER, DROP), DML verändert die Daten in dieser Struktur (INSERT, UPDATE, DELETE).

> [!question]- Schreibe ein CREATE TABLE für `Produkte(produkt_id, name, preis)`.
> ```sql
> CREATE TABLE Produkte (
>     produkt_id INTEGER PRIMARY KEY,
>     name       TEXT NOT NULL,
>     preis      REAL NOT NULL CHECK (preis >= 0)
> );
> ```

> [!question]- Was bewirkt ein Fremdschlüssel?
> Er verknüpft zwei Tabellen und sichert die referenzielle Integrität: Es dürfen nur Werte eingetragen werden, die als Primärschlüssel in der referenzierten Tabelle existieren.

> [!question]- Warum speichert man eine PLZ nicht als INTEGER?
> Weil führende Nullen verloren gingen (01067 → 1067) und man mit einer PLZ nicht rechnet.

> [!question]- Was ist eine View?
> Eine gespeicherte Abfrage, die wie eine Tabelle gelesen werden kann, aber keine eigenen Daten speichert.

## Siehe auch
- [[SQL - DML INSERT UPDATE DELETE]]
- [[SQL - SELECT und JOIN]]
- [[ER-Modell in Tabellen überführen]]
- [[Normalisierung]]
- [[Übung Normalisierung Bestellungen in SQLite]]
