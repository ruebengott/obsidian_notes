---
tags: [berufsschule, lf3, übung, udp]
fach: LF3
typ: übung
quelle: "[[LF3.pdf#page=54]]"
datum:
status: zu-lernen
---
# Übung: Fragebogen zu UDP

Arbeitsauftrag: Erst alleine (40 min), dann im Austausch mit der Klassengruppe (15 min) beantworten. Ergebnisse mit Quellen-URLs in einem Textdokument festhalten. Die Antworten wurden vom Lehrer bestätigt (CryptPad-Link im Original).

## Fragen
1. Was bedeutet die Abkürzung UDP ausgeschrieben?
2. Auf welcher OSI-Schicht arbeitet UDP?
3. Aus welchen Elementen ist ein UDP-Header aufgebaut und wie viele Byte umfasst er?
4. Welche Bedeutung haben die Elemente und wie groß sind sie?
5. Nenne mindestens drei typische Anwendungen für UDP.
6. Wie groß ist die Anzahl der möglichen Ports? Warum ist das so?
7. Was passiert, wenn bei Datenpaketen über UDP Fehler auftreten? Beschreibe Vor- und Nachteile dieser Fehlerbehandlung. Leite daraus ab, welche Anwendungen für UDP geeignet sind und welche nicht.

> [!success]- Lösung
> **1.** **User Datagram Protocol**
>
> **2.** OSI-Schicht **4** (Transportschicht)
>
> **3./4.** Vier feste Felder à 16 Bit (2 Byte) = **8 Byte**:
> | Feld | Größe | Bedeutung |
> |---|---|---|
> | Quell-Port | 16 Bit | Port der sendenden Anwendung, optional (0 bei Nichtbedarf) |
> | Ziel-Port | 16 Bit | Port der empfangenden Anwendung |
> | Länge | 16 Bit | Länge von UDP-Header + Nutzdaten in Byte |
> | Prüfsumme | 16 Bit | Prüfung der Datenintegrität von Header und Daten |
>
> **5.** Livestreaming, Online-Gaming, Videokonferenzen/VoIP (außerdem DNS, DHCP)
>
> **6.** Das Portfeld ist 16 Bit groß → 2¹⁶ = **65.536** Portnummern (0–65.535). Port 0 ist reserviert, also sind 65.535 nutzbar.
>
> **7.** Fehlerhafte Datagramme werden in der Regel **verworfen** und **nicht erneut gesendet**.
> - Vorteil: kein Overhead durch Bestätigungen/Wiederholungen → hohe Geschwindigkeit, geringe Latenz (wichtig z. B. beim Online-Gaming)
> - Nachteil: keine fehlerfreie, vollständige Übertragung garantiert
> - Geeignet: Echtzeitanwendungen (Streaming, Gaming, VoIP), bei denen ein verlorenes Paket kaum stört
> - Ungeeignet: **Dateidownloads**, E-Mail, Webseiten, also alles, was vollständig ankommen muss (→ TCP)

> [!warning] Korrektur
> - Frage 1: In der eigenen Antwort stand „User-**Data**-Protocol“. Richtig ist **User Datagram Protocol**.
> - Frage 6: In der eigenen Antwort stand „65.535 Ports insgesamt“. Genau sind es 65.536 Portnummern (0–65.535), davon 65.535 nutzbar (ohne Port 0).

Quellen im Original: elektronik-kompendium.de (UDP), checkpoint.com (What is UDP).

## Siehe auch
- [[UDP]]
- [[TCP-Header]]
