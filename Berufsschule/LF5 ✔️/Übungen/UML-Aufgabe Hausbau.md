---
tags: [berufsschule, lf5, uml, übung]
fach: LF5
typ: übung
quelle: "[[LF5.pdf#page=17]]"
datum: 2026-06-02
status: zu-lernen
---
# UML-Aufgabe Hausbau

> [!summary] Kurz & knapp
> Übung zum [[UML-Aktivitätsdiagramm]]: Der Prozess „Hausbau“ soll als Aktivitätsdiagramm (ohne Verantwortungsbereiche) aus vorgegebenen Elementen modelliert werden.

## Aufgabe
Zeichnen Sie ein UML-Aktivitätsdiagramm für den Prozess „Hausbau“ (ohne Verantwortungsbereiche). Verwenden Sie dabei folgende Elemente:

- Aktivitätsrahmen „Hausbauprozess“
- Startknoten, Endknoten, Ablaufende ⊗
- Entscheidung mit `[Angebot]` / `[kein Angebot]`, eine weitere Raute
- je eine Gabelung und eine Vereinigung
- Aktionen: Bauplatz wählen, Bau ausschreiben, Architekt beauftragen, Bauplan entwickeln, Arbeiten von Handwerkern, Eigenarbeiten, Amtliche Bauabnahme, Einzug
- Objektknoten: Bauabnahmebestätigung

Originalblatt mit eigener Lösung: ![[LF5.pdf#page=17]]

## Lösung

> [!success]- Musterlösung (aufklappen)
> ```mermaid
> flowchart TD
>     S((Start)) --> BP([Bauplatz wählen])
>     BP --> F1[/Gabelung/]
>     F1 --> BA([Bau ausschreiben])
>     F1 --> AB([Architekt beauftragen])
>     AB --> PL([Bauplan entwickeln])
>     BA --> D1{Angebot?}
>     D1 -->|"[kein Angebot]"| X((⊗ bzw. Ende))
>     D1 -->|"[Angebot]"| J1[\Vereinigung\]
>     PL --> J1
>     J1 --> M{" "}
>     M --> F2[/Gabelung/]
>     F2 --> HW([Arbeiten von Handwerkern])
>     F2 --> EA([Eigenarbeiten])
>     HW --> J2[\Vereinigung\]
>     EA --> J2
>     J2 --> AA([Amtliche Bauabnahme])
>     AA --> D2{genehmigt?}
>     D2 -->|"[nicht genehmigt]"| M
>     D2 -->|"[genehmigt]"| OB[Bauabnahmebestätigung]
>     OB --> EZ([Einzug])
>     EZ --> E(((Ende)))
> ```
> **Ablauf in Worten:** Nach „Bauplatz wählen“ laufen Ausschreibung und Planung **parallel** (Gabelung). Gibt es kein Angebot, endet der Prozess. Liegen Angebot und Bauplan vor, werden die Zweige **vereinigt**. Danach laufen Handwerker- und Eigenarbeiten parallel. Es folgt die amtliche Bauabnahme. Wird nicht genehmigt, geht es über eine **Zusammenführung** (Raute) zurück zu den Arbeiten. Wird genehmigt, entsteht das Objekt „Bauabnahmebestätigung“, dann folgt der Einzug und der Endknoten.

> [!warning] Korrektur zur eigenen Lösung
> - **Ablaufende vor einer Vereinigung:** Endet der Zweig „kein Angebot“ mit einem Ablaufende ⊗, wartet die spätere Vereinigung für immer auf diesen Zweig. Fachlich sauberer ist hier ein **Endknoten** ◉ (der ganze Hausbau ist abgebrochen) oder eine Schleife zurück zu „Bau ausschreiben“.
> - **Rücksprung bei „nicht genehmigt“:** Die Kante sollte in eine **Zusammenführungs-Raute** münden und nicht direkt auf eine andere Kante treffen.
> - „Bau ausschreiben“ war doppelt gezeichnet. Jede Aktion kommt nur einmal vor.
> - Alles gehört in den Aktivitätsrahmen „Hausbauprozess“.

## Siehe auch
- [[UML-Aktivitätsdiagramm]]
- [[LF5 - Übersicht]]
