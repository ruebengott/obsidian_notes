---
tags: [berufsschule, lf8, datenbanken, er-modell, übung]
fach: LF8
typ: übung
quelle: "[[LF8.pdf#page=8]]"
datum: 2026-09-09
status: zu-lernen
---
# Kompetenzcheck ER-Modell

> [!summary] Kurz & knapp
> Kompetenzcheck aus dem Lehrbuch (Kapitel 3.7.2, Moodle) zu Datenbankentwurf, ER-Modell und Überführung ins relationale Modell. Theorie dazu in [[ER-Modell]] und [[ER-Modell in Tabellen überführen]].

## Aufgabe 1: Welche Aussagen sind richtig?
a) Der Prozess des Designs von relationalen Datenbanken verläuft in mehreren Phasen.
b) Es darf keine Phase des Designprozesses übersprungen werden.
c) Am Ende der letzten Phase soll eine funktionstüchtige Datenbank stehen.
d) Das ER-Modell wird in der logischen Phase erstellt.
e) Die Normalisierung des relationalen Datenmodells ist ein Bestandteil der konzeptionellen Phase.
f) Aus einem schlechten logischen Design resultiert auch immer eine schlechte physikalische Umsetzung.

> [!success]- Lösung
> - a) richtig
> - b) richtig
> - c) richtig
> - d) **falsch**: Das ER-Modell entsteht in der **konzeptionellen** Phase.
> - e) **falsch**: Normalisiert wird in der **logischen** Phase.
> - f) richtig: Fehler aus früheren Phasen setzen sich fort.

## Aufgabe 2: Musiker und Veranstaltungen
Erstellen Sie aus folgenden Informationen ein ER-Modell. Es sollen die Auftritte von Musikern bei verschiedenen Veranstaltungen in einer Datenbank gespeichert werden. Dabei ist von Interesse, von wann bis wann welcher Musiker bei welcher Veranstaltung auftritt. Von den Musikern werden der Künstlername bzw. der Bandname erfasst. Von der Veranstaltung ist die Bezeichnung, das Veranstaltungsdatum und der Ort mit entsprechender PLZ von Bedeutung.

> [!success]- Lösung
> ```mermaid
> erDiagram
>     MUSIKER }o--o{ VERANSTALTUNG : "tritt auf (Beginn, Ende)"
>     MUSIKER {
>         string Kuenstlername PK
>     }
>     VERANSTALTUNG {
>         int VeranstaltungsNr PK
>         string Bezeichnung
>         date Veranstaltungsdatum
>         string Ort
>         string PLZ
>     }
> ```
> - Entitäten: **Musiker** (<u>Künstlername</u>) und **Veranstaltung** (<u>VeranstaltungsNr</u>, Bezeichnung, Veranstaltungsdatum, Ort, PLZ)
> - Beziehung **„tritt auf“**, Kardinalität **m:n** (ein Musiker tritt bei vielen Veranstaltungen auf, bei einer Veranstaltung treten viele Musiker auf)
> - Die Beziehung hat die Attribute **Beginn** und **Ende** („von wann bis wann“).
> - Relational: `Musiker(Künstlername)`, `Veranstaltung(VeranstaltungsNr, Bezeichnung, Datum, PLZ, Ort)`, `Auftritt(↑Künstlername, ↑VeranstaltungsNr, Beginn, Ende)`. In 3NF würde man noch `Ort(PLZ, Ortsname)` auslagern.
>
> > [!warning] Korrektur zur eigenen Lösung
> > In der eigenen Skizze fehlten die **Kardinalitäten**, die **Schlüssel** (unterstreichen), das Attribut **Ort** und die Beziehungsattribute **Beginn/Ende**.

## Aufgabe 3: Astronaut, Mission, Raumfahrzeug
Überführen Sie das folgende ER-Modell in ein relationales Modell (noch nicht normalisieren): Astronaut (<u>ANr</u>, Nachname, Vorname) **m:n** „nimmt teil“ Mission (<u>MNr</u>, Bezeichnung, Beginn, Ende) **n:1** „hat“ Raumfahrzeug (<u>RID</u>, Name, Baujahr).

![[LF8.pdf#page=8]]

> [!success]- Lösung
> - Astronaut(<u>ANr</u>, Nachname, Vorname)
> - Mission(<u>MNr</u>, Bezeichnung, Beginn, Ende, ↑RID)
> - Raumfahrzeug(<u>RID</u>, Name, Baujahr)
> - **Teilnahme(<u>↑ANr, ↑MNr</u>)**: Zwischentabelle für die m:n-Beziehung
>
> > [!warning] Korrektur zur eigenen Lösung
> > In der eigenen Lösung stand `ANr (FK)` direkt in `Mission`. Damit hätte jede Mission nur **einen** Astronauten (1:n statt m:n). Für m:n braucht man die Zwischentabelle `Teilnahme`. `RID` als FK in `Mission` war richtig (n:1).

## Aufgabe 4: Bank, Konten und Kontoinhaber
Eine Bank möchte Konten und die dazugehörigen Kontoinhaber in einer Datenbank verwalten. Von den Konten sollen die Kontonummer, der aktuelle Geldbetrag, der Kontotyp mit entsprechender Kontotypnummer und das Eröffnungsdatum erfasst werden. Von den Kontoinhabern werden folgende Daten erfasst: Inhabernummer, Nachname, Vorname, Geburtsdatum, Anschrift und Telefonnummer. Es ist möglich, dass ein Konto mehrere Kontoinhaber hat. Erstellen Sie zunächst ein ER-Modell und überführen Sie es dann in ein relationales Modell.

> [!success]- Lösung
> **ER-Modell:** Konto (<u>Kontonummer</u>, Geldbetrag, Eröffnungsdatum, Kontotyp, KontotypNr) – „hat“ – Kontoinhaber (<u>Inhabernummer</u>, Nachname, Vorname, Geburtsdatum, Anschrift, Telefonnummer)
>
> **Kardinalität:** Ein Konto kann mehrere Inhaber haben (laut Text). Realistisch kann ein Inhaber auch mehrere Konten haben, also **m:n**.
>
> ```mermaid
> erDiagram
>     KONTO }o--|{ KONTOINHABER : "hat"
>     KONTOTYP ||--o{ KONTO : "ist vom Typ"
>     KONTO {
>         int Kontonummer PK
>         decimal Geldbetrag
>         date Eroeffnungsdatum
>         int KontotypNr FK
>     }
>     KONTOTYP {
>         int KontotypNr PK
>         string Bezeichnung
>     }
>     KONTOINHABER {
>         int Inhabernummer PK
>         string Nachname
>         string Vorname
>         date Geburtsdatum
>         string Anschrift
>         string Telefonnummer
>     }
> ```
> **Relationales Modell:**
> - Konto(<u>Kontonummer</u>, Geldbetrag, Eröffnungsdatum, ↑KontotypNr)
> - Kontotyp(<u>KontotypNr</u>, Bezeichnung)
> - Kontoinhaber(<u>Inhabernummer</u>, Nachname, Vorname, Geburtsdatum, Anschrift, Telefonnummer)
> - Kontozuordnung(<u>↑Kontonummer, ↑Inhabernummer</u>)
>
> > [!warning] Korrektur zur eigenen Lösung
> > Die eigene Lösung modellierte **1:n** mit `KontoNr (FK)` in `Kontoinhaber`. Dann kann jeder Inhaber nur **ein** Konto haben. Will man nur die Aussage aus dem Text abbilden, ist das vertretbar. Üblich ist aber **m:n** mit Zwischentabelle. Außerdem gehört der „Kontotyp mit entsprechender Kontotypnummer“ in eine eigene Tabelle `Kontotyp`, sonst steht die Typbezeichnung bei jedem Konto redundant (3NF).

## Siehe auch
- [[ER-Modell]]
- [[ER-Modell in Tabellen überführen]]
- [[Normalisierung]]
- [[LF8 - Übersicht]]
