---
tags: [berufsschule, lf3, udp, schicht-4]
fach: LF3
typ: thema
quelle: "[[LF3.pdf#page=54]]"
datum:
status: zu-lernen
---
# UDP (User Datagram Protocol)

> [!summary] Kurz & knapp
> UDP ist ein **verbindungsloses** Transportprotokoll (OSI-Schicht 4) mit einem nur **8 Byte** großen Header. Es gibt keine Bestätigungen, keine erneute Übertragung und keine Reihenfolgesicherung. Dadurch ist UDP **schnell**, aber **unzuverlässig**. Typisch für Echtzeitanwendungen wie Streaming, Gaming, VoIP, DNS und DHCP.

## UDP-Header (4 Felder × 16 Bit = 8 Byte)

| Bit 0–15 | Bit 16–31 |
|---|---|
| Quell-Port (Source Port) | Ziel-Port (Destination Port) |
| Länge (Length) | Prüfsumme (Checksum) |

| Feld | Größe | Bedeutung |
|---|---|---|
| Quell-Port | 16 Bit | Port der sendenden Anwendung. Optional, kann auf 0 gesetzt werden |
| Ziel-Port | 16 Bit | Port der empfangenden Anwendung |
| Länge | 16 Bit | Länge von UDP-Header **plus** Nutzdaten in Byte |
| Prüfsumme | 16 Bit | Prüfung der Datenintegrität von Header und Daten |

## Ports
- Portnummern sind 16 Bit lang → **2¹⁶ = 65.536** Portnummern (**0–65.535**)
- Port 0 ist reserviert, also 65.535 nutzbare Ports
- Well-known Ports 0–1023 (z. B. DNS 53, DHCP 67/68), registrierte 1024–49151, dynamische 49152–65535

## Fehlerbehandlung
- Fehlerhafte Datagramme werden in der Regel **verworfen**. Es gibt **keine erneute Übertragung**.
- **Vorteil:** wenig Overhead, keine Wartezeiten → hohe **Geschwindigkeit**, geringe Latenz. Wichtig z. B. für Online-Gaming.
- **Nachteil:** keine fehlerfreie, vollständige Übertragung garantiert. Für **Dateidownloads** ist UDP daher ungeeignet, die Dateien könnten unvollständig ankommen.
- **Geeignet für:** Livestreaming, Online-Gaming, Videokonferenzen, VoIP, DNS-Abfragen, DHCP
- **Ungeeignet für:** Dateiübertragung, E-Mail, Webseiten (→ [[TCP-Header|TCP]])

> [!warning] Korrektur
> In der Mitschrift stand „UDP = User-**Data**-Protocol“. Richtig ist **User Datagram Protocol**.

> [!tip] Merke
> - UDP: verbindungslos, 8 Byte Header, keine Bestätigung, schnell
> - 4 Felder à 16 Bit: Quell-Port, Ziel-Port, Länge, Prüfsumme
> - Ports: 16 Bit → 0–65.535
> - Protokollnummer im IP-Header: 17 (0x11)

## Lernfragen
> [!question]- Wie groß ist der UDP-Header und aus welchen Feldern besteht er?
> 8 Byte: Quell-Port, Ziel-Port, Länge und Prüfsumme (je 16 Bit).

> [!question]- Warum gibt es 65.536 Portnummern?
> Das Portfeld ist 16 Bit lang: 2¹⁶ = 65.536 (0–65.535).

> [!question]- Was passiert bei UDP mit fehlerhaften Paketen?
> Sie werden verworfen und nicht erneut übertragen.

> [!question]- Nenne drei typische Anwendungen für UDP und begründe.
> Livestreaming, Online-Gaming, VoIP/Videokonferenzen. Hier ist geringe Verzögerung wichtiger als die Vollständigkeit, ein verlorenes Paket fällt kaum auf. Außerdem DNS und DHCP (kurze Anfrage/Antwort).

> [!question]- Auf welcher OSI-Schicht arbeitet UDP?
> Auf Schicht 4 (Transportschicht).

## Siehe auch
- [[TCP-Header]]
- [[Übung Fragebogen UDP]]
- [[OSI-Schichtenmodell]]
- [[DNS]] · [[DHCP]]
