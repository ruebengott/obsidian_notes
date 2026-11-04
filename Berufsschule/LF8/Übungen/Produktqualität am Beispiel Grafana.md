---
tags: [berufsschule, lf8, softwarequalität, iso25010, übung]
fach: LF8
typ: übung
quelle: "[[LF8.pdf#page=3]]"
datum:
status: zu-lernen
---
# Produktqualität am Beispiel Grafana

> [!summary] Kurz & knapp
> Rechercheauftrag zur Norm ISO/IEC 25010:2023 und Anwendung des Produktqualitätsmodells auf ein konkretes Produkt: ein **Grafana-Dashboard** für das IT-Monitoring.

## Aufgabe (Rechercheauftrag)
Recherchiert (gerne zu zweit) die Norm **ISO/IEC 25010:2023**. Sie ist eine international standardisierte Definition von Softwarequalität.
1. Aus welchen Hauptkomponenten besteht die Norm?
2. Nenne die 9 Merkmale des Produktqualitätsmodells.
3. Nenne die 5 Merkmale des Qualitätsmodells der Nutzung.
4. Wende das Produktqualitätsmodell auf eine Beispielanwendung an.

## Lösung
> [!success]- 1.–3. Aufbau der Norm
> - Zwei Hauptkomponenten: **Produktqualitätsmodell** und **Qualitätsmodell der Nutzung**
> - 9 Produktmerkmale: siehe [[ISO 25010 Produktqualität]]
> - 5 Nutzungsmerkmale: siehe [[Qualitätsmodell der Nutzung]]

> [!success]- 4. Beispielanwendung: Grafana-Monitoring-Dashboard
> | Merkmal | Anforderung an das Grafana-Dashboard |
> | --- | --- |
> | **Funktionale Eignung** | Grafana zeigt Messwerte aus verschiedenen Datenquellen an und erstellt daraus Dashboards, Diagramme und Tabellen. |
> | **Leistungseffizienz** | Dashboards und Abfragen laden schnell und brauchen möglichst wenig Systemressourcen. |
> | **Kompatibilität** | Grafana arbeitet mit den verwendeten Datenquellen und Systemen zusammen, z. B. CSV-Daten, Datenbanken oder Monitoring-Systemen. |
> | **Benutzbarkeit** | Die Oberfläche ist übersichtlich und verständlich, sodass Mitarbeiter schnell erkennen, ob es Probleme in der IT gibt. |
> | **Zuverlässigkeit** | Das Dashboard läuft stabil und aktualisiert die Daten zuverlässig, ohne abzustürzen oder falsche Werte anzuzeigen. |
> | **Sicherheit (Security)** | Nur berechtigte Personen können auf das Dashboard bzw. sensible Monitoring-Daten zugreifen. |
> | **Wartbarkeit** | Panels, Abfragen und Datenquellen lassen sich einfach ändern oder erweitern, z. B. für ein neues Monitoring-Kriterium. |
> | **Flexibilität** | Das Dashboard lässt sich an neue Anforderungen anpassen (neue Panels, Filter, Datenquellen) und problemlos auf einem anderen Server bzw. in einer anderen Umgebung betreiben. |
> | **Betriebssicherheit (Safety)** | Fehlalarme oder fehlende Alarme dürfen nicht dazu führen, dass kritische Ausfälle übersehen werden und dadurch Schaden entsteht. |

> [!warning] Korrektur
> Die eigene Ausarbeitung nutzte die **alten Begriffe** aus ISO 25010:2011: „Übertragbarkeit/Portabilität“ und „Änderbarkeit/Anpassbarkeit“ als zwei getrennte Punkte, dafür fehlte die **Betriebssicherheit (Safety)**. Nach der Version 2023 gehören Übertragbarkeit und Anpassbarkeit beide zu **Flexibilität**. Die Safety-Zeile oben ist ergänzt.

## Siehe auch
- [[ISO 25010 Produktqualität]]
- [[Qualitätsmodell der Nutzung]]
- [[LF8 - Übersicht]]
