---
tags: [berufsschule, lf3, ipv4-header, ttl]
fach: LF3
typ: thema
quelle: "[[LF3.pdf#page=42]]"
datum:
status: zu-lernen
---
# IPv4-Header: Time to Live (TTL)

> [!summary] Kurz & knapp
> Die **TTL** (8 Bit) verhindert, dass IP-Pakete endlos im Netz kreisen. Jeder Router verringert sie um **1**. Bei **0** wird das Paket verworfen. Am TTL-Wert einer Ping-Antwort kann man abschätzen, wie viele Router dazwischen liegen und welches Betriebssystem antwortet.

## Funktionsweise
- Der Sender setzt einen **Startwert** (8 Bit → max. 255).
- Jeder Router auf dem Weg zieht **1** ab (früher: „Lebensdauer in Sekunden“, praktisch ein **Hop-Zähler**).
- Erreicht die TTL **0**, verwirft der Router das Paket und schickt eine ICMP-Meldung „Time Exceeded“ an den Absender. So entsteht kein „unzustellbarer Datenmüll“, und Routing-Schleifen führen nicht zum Netzzusammenbruch (network meltdown).
- Der Befehl `ping` zeigt die TTL des **Antwortpakets** (echo reply) an. `tracert`/`traceroute` nutzt die TTL gezielt, um den Weg anzuzeigen.

## Typische Startwerte
| System | Start-TTL |
|---|---|
| Linux / macOS / Unix | 64 |
| Windows | 128 |
| Router / Netzwerkgeräte (z. B. Cisco) | 255 |

## Ping-Beispiele aus dem Material (A pingt B, gleiche Strecke)
| Fall | Antwort-TTL | Auswertung |
|---|---|---|
| B ist ein Router | 251 | 255 − 251 = 4 Hops |
| B ist ein Windows-Rechner | 124 | 128 − 124 = 4 Hops |
| B ist ein Ubuntu-Linux-Rechner | 60 | 64 − 60 = 4 Hops |

```text
Pinging B [1.1.1.1] with 32 bytes of data:
Reply from 1.1.1.1: bytes=32 time=18 ms TTL=124
```

> [!warning] Korrektur
> Das englische Material (openmaniak) erklärt die Werte so: „Startwert ist immer 255, Windows **zieht 128 ab**, Ubuntu **192**“ (255 − 3 − 128 = 124). Das ist so nicht richtig, auch wenn die Zahlen zufällig passen. Tatsächlich setzt **das antwortende System** seinen eigenen Startwert (Windows 128, Linux 64, Router 255), und jeder Router dazwischen zieht 1 ab. Alle drei Beispiele ergeben damit **4 Hops**.

> [!tip] Merke
> - TTL = 8 Bit, jeder Router −1, bei 0 verwerfen
> - Zweck: Pakete sollen nicht endlos kreisen (Routing-Schleifen)
> - Start-TTL: Linux 64, Windows 128, Router 255
> - Hops = Start-TTL − empfangene TTL

## Lernfragen
> [!question]- Wozu dient die TTL?
> Sie verhindert, dass Pakete endlos im Netz kreisen (z. B. bei Routing-Schleifen). Bei 0 wird das Paket verworfen.

> [!question]- Ein Ping liefert TTL=57. Welches System antwortet vermutlich und über wie viele Hops?
> Wahrscheinlich Linux (Start 64): 64 − 57 = 7 Hops.

> [!question]- Was macht ein Router mit einem Paket, dessen TTL auf 0 sinkt?
> Er verwirft es und sendet eine ICMP-„Time Exceeded“-Nachricht an den Absender.

> [!question]- Welcher maximale Wert ist für die TTL möglich und warum?
> 255, denn das Feld ist 8 Bit groß (2⁸ − 1).

> [!question]- Welcher Befehl nutzt die TTL, um den Weg eines Pakets anzuzeigen?
> `tracert` (Windows) bzw. `traceroute` (Linux).

## Siehe auch
- [[IPv4-Header]]
- [[Routing und Default Route]]
- [[Übung IPv4-Header Traceanalyse 1]]
