---
tags:
  - berufsschule
  - lf8
fach: LF8
typ: übung
status: zu-lernen
---
![[Pasted image 20261028100630.png]]

Land 
- Land ID
- Name
- Hauptstadt


Hauptstadt 
- Land ID
- Flussname

Fluss
- Flussname
- Länge
- Hauptstadt

---

## Lösung Aufgabe 1

### Ausgangstabelle

| LandID | Name/Hauptstadt | Flüsse |
|---|---|---|
| 1 | Deutschland/Berlin | 1. Donau (2857 km), 2. Rhein (1233 km), 3. Weser (451 km), 4. Oder (866 km), 5. Elbe (1094 km) |
| 2 | Österreich/Wien | 1. Donau (2857 km), 2. Rhein (1233 km) |
| 3 | Polen/Warschau | 1. Oder (866 km), 2. Weichsel (1047 km) |
| 4 | Tschechische Republik/Prag | 1. Elbe (1094 km), 2. Oder (866 km) |

### 1. Normalform

Die Spalte „Flüsse“ enthält mehrere Werte pro Zelle. Jede Kombination aus Land und Fluss wird eine eigene Zeile. Der Schlüssel ist `(LandID, Flussname)`.

| LandID | Name | Hauptstadt | Rang | Flussname | Länge |
|---|---|---|---|---|---|
| 1 | Deutschland | Berlin | 1 | Donau | 2857 |
| 1 | Deutschland | Berlin | 2 | Rhein | 1233 |
| 1 | Deutschland | Berlin | 3 | Weser | 451 |
| 1 | Deutschland | Berlin | 4 | Oder | 866 |
| 1 | Deutschland | Berlin | 5 | Elbe | 1094 |
| 2 | Österreich | Wien | 1 | Donau | 2857 |
| 2 | Österreich | Wien | 2 | Rhein | 1233 |
| 3 | Polen | Warschau | 1 | Oder | 866 |
| 3 | Polen | Warschau | 2 | Weichsel | 1047 |
| 4 | Tschechische Republik | Prag | 1 | Elbe | 1094 |
| 4 | Tschechische Republik | Prag | 2 | Oder | 866 |

### 2. Normalform

Teilabhängigkeiten werden aufgelöst. `Name` und `Hauptstadt` hängen nur von `LandID` ab. `Länge` hängt nur von `Flussname` ab. Die Tabelle wird in drei aufgeteilt.

**Land**

| LandID | Name | Hauptstadt |
|---|---|---|
| 1 | Deutschland | Berlin |
| 2 | Österreich | Wien |
| 3 | Polen | Warschau |
| 4 | Tschechische Republik | Prag |

**Fluss**

| Flussname | Länge |
|---|---|
| Donau | 2857 |
| Rhein | 1233 |
| Weser | 451 |
| Oder | 866 |
| Elbe | 1094 |
| Weichsel | 1047 |

**LandFluss**

| LandID | Flussname | Rang |
|---|---|---|
| 1 | Donau | 1 |
| 1 | Rhein | 2 |
| 1 | Weser | 3 |
| 1 | Oder | 4 |
| 1 | Elbe | 5 |
| 2 | Donau | 1 |
| 2 | Rhein | 2 |
| 3 | Oder | 1 |
| 3 | Weichsel | 2 |
| 4 | Elbe | 1 |
| 4 | Oder | 2 |

### 3. Normalform

Es gibt keine transitiven Abhängigkeiten mehr. Jede Nichtschlüssel-Spalte hängt direkt vom Schlüssel ab.

- **Land**: `Name` ist eindeutig und damit ein Schlüsselkandidat. `Hauptstadt` hängt nur von `LandID` ab.
- **Fluss**: `Länge` hängt nur von `Flussname` ab.
- **LandFluss**: `Rang` hängt vom gesamten Schlüssel `(LandID, Flussname)` ab.

**Ergebnis**

- `Land(LandID, Name, Hauptstadt)`
- `Fluss(Flussname, Länge)`
- `LandFluss(LandID, Flussname, Rang)`

`Rang` ist optional, wenn die Reihenfolge nicht gespeichert werden muss.


---

![[Pasted image 20261028102051.png]]


![[Pasted image 20261028102103.png]]

Die Tabellen sind bereits ausreichend normalisiert, aber man könnte die Tabellen noch weiter aufdröseln.

| Mitglied | Kontakt |
| -------- | ------- |
| MID (PK) | TelNR   |
| Name     | Email   |
|          | Adresse |

| Bauteil       | Hersteller     |
| ------------- | -------------- |
| BauteilNR(PK) | Herstellername |
| Bezeichnung   | HerstellerNR   |
| Preis         |                |


| CD       | Musiktitel     |
| -------- | -------------- |
| CDNr(PK) | TitelPosCD(PK) |
| CDName   | Titelnahme     |
| CDPreis  | Titellänge     |


---





