---
tags: [berufsschule, lf5, datenformate]
fach: LF5
typ: thema
quelle: "[[LF5.pdf#page=13]]"
datum:
status: zu-lernen
---
# Datenformate CSV, JSON, XML

> [!summary] Kurz & knapp
> CSV, JSON und XML sind textbasierte Formate für den Austausch von Daten zwischen Programmen. **CSV** ist eine einfache Tabelle, **JSON** speichert hierarchisch mit Key-Value-Paaren und wenig Overhead, **XML** ist eine Baumstruktur aus Tags, die selbstbeschreibend und validierbar ist, aber viel Text braucht.

## Vergleich

| | CSV | JSON | XML |
| --- | --- | --- | --- |
| Struktur | Tabelle (Zeilen/Spalten) | hierarchisch: verschachtelte Objekte und Arrays | Baum aus öffnenden/schließenden Tags |
| Kennzeichen | Trennzeichen (Komma, in DE oft Semikolon); erste Zeile = Header mit Spaltennamen | Key-Value-Paare | Tag-Namen beschreiben die Bedeutung (selbstbeschreibend) |
| Datentypen | keine (alles Text) | String, Number, Boolean, Array, Object (und `null`) | keine eigenen; per Schema festlegbar |
| Validierung | nein | über JSON Schema möglich | DTD und XML Schema (XSD) |
| Overhead | sehr gering | gering (kompakt) | hoch („verbose“) |
| Typischer Einsatz | Export aus Excel/Datenbanken, Massendaten | Web-APIs (REST), Konfiguration | Dokumente, Konfiguration, ältere Schnittstellen (SOAP), Office-Formate |

## Dieselben Daten in allen drei Formaten

**CSV**
```csv
id,name,ort
1,Paul,Rendsburg
2,Erwin,Kiel
```

**JSON**
```json
{
  "benutzer": [
    { "id": 1, "name": "Paul", "ort": "Rendsburg" },
    { "id": 2, "name": "Erwin", "ort": "Kiel" }
  ]
}
```

**XML**
```xml
<benutzerliste>
  <benutzer id="1">
    <name>Paul</name>
    <ort>Rendsburg</ort>
  </benutzer>
  <benutzer id="2">
    <name>Erwin</name>
    <ort>Kiel</ort>
  </benutzer>
</benutzerliste>
```

> [!tip] Merke
> - CSV = **flach**, kann keine Verschachtelung.
> - JSON = **kompakt + typisiert**, Standard bei Web-APIs.
> - XML = **selbstbeschreibend + validierbar (DTD/XSD)**, aber aufgebläht.
> - Alle drei sind reine Textdateien und damit plattformunabhängig.

## Lernfragen
> [!question]- Welches Format eignet sich, wenn Daten verschachtelt sind (z. B. Kunde mit mehreren Bestellungen)?
> JSON oder XML, weil beide hierarchisch sind. CSV kann nur flache Tabellen abbilden.

> [!question]- Welche Datentypen kennt JSON?
> String, Number, Boolean, Array, Object (zusätzlich null).

> [!question]- Womit kann man prüfen, ob ein XML-Dokument einer festgelegten Struktur entspricht?
> Mit einer DTD oder einem XML Schema (XSD).

> [!question]- Was ist der Header einer CSV-Datei?
> Die erste Zeile. Sie enthält die Spaltennamen.

> [!question]- Nenne einen Nachteil von XML gegenüber JSON.
> XML braucht durch öffnende und schließende Tags mehr Zeichen (verbose). Die Dateien werden größer und sind schwerer zu lesen.

## Siehe auch
- [[LF5 - Übersicht]]
- [[Relationale Datenbanken]]
