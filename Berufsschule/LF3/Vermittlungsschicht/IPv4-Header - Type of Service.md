---
tags: [berufsschule, lf3, ipv4-header, qos]
fach: LF3
typ: thema
quelle: "[[LF3.pdf#page=41]]"
datum:
status: zu-lernen
---
# IPv4-Header: Type of Service (ToS)

> [!summary] Kurz & knapp
> Das 8-Bit-Feld **Type of Service** (das „Prioritätsfeld“) steuert, wie Router gleichzeitig zu sendende Pakete **priorisieren**, und kennzeichnet die Eigenschaften eines Pakets. Heute wertet man die ersten **6 Bit als DSCP** (DiffServ Code Point) aus, die letzten 2 Bit als **ECN**.

## Ursprüngliche Struktur (RFC 791/1349)

| Bit | 0–2 | 3 | 4 | 5 | 6 | 7 |
|---|---|---|---|---|---|---|
| Feld | Precedence | D (Delay) | T (Throughput) | R (Reliability) | C (Monetary Cost) | 0 (reserviert) |

- **Precedence (3 Bit):** Vorrang des Pakets, 0 = niedrig (Routine) … 7 = hoch (Network Control), z. B. für Echtzeitanwendungen
  `000 Routine · 001 Priority · 010 Immediate · 011 Flash · 100 Flash Override · 101 CRITIC/ECP · 110 Internetwork Control · 111 Network Control`
- **Delay:** zulässige Verzögerung (1 = minimieren)
- **Throughput:** 1 = maximaler Datendurchsatz
- **Reliability:** 1 = hohe Zuverlässigkeit (niedrige Fehlerrate, hohe Datenqualität)
- **Monetary Cost:** finanzieller Aufwand (1 = minimieren). Wird in der Praxis nicht bewertet
- Bit 7: reserviert, immer 0

## Heutige Nutzung: DiffServ (RFC 2474 / 3168)
| Bit 0–5 | Bit 6–7 |
|---|---|
| DSCP (DiffServ Code Point) | ECN (Explicit Congestion Notification) |

Typische DSCP-Werte:

| Verkehrsart | DSCP | QoS-Profil |
|---|---|---|
| Network control | 56 (CS7) | Platinum |
| Inter-network control | 48 (CS6) | Platinum |
| Voice (VoIP) | 46 (EF, Expedited Forwarding) | Platinum |
| Interactive video | 34 (AF41) | Gold |
| Streaming video | 32 (CS4) | Gold |
| Mission critical | 26 (AF31) | Gold |
| Call signaling | 24 (CS3) | Gold |
| Transactional | 18 (AF21) | Silver |
| Network management | 16 (CS2) | Silver |
| Bulk data | 10 (AF11) | Bronze |
| **Best effort** | **0 (BE)** | Silver |
| Scavenger | 8 (CS1) | Bronze |

Laut Lehrbuchfolie: **0 = Best Effort**, **46 = Expedited Forwarding** (VoIP-Datenstrom). Der Wert 40 wird dort als „Expedited Flow“ für VoIP genannt.

Original: ![[LF3.pdf#page=41]]

> [!tip] Merke
> - ToS = 8 Bit, „Prioritätsfeld“ für Quality of Service
> - Heute: 6 Bit DSCP + 2 Bit ECN
> - DSCP 0 = Best Effort, DSCP 46 (EF) = Sprache/VoIP

## Lernfragen
> [!question]- Wozu dient das Type-of-Service-Feld?
> Es steuert die Priorisierung von Paketen durch Router (Quality of Service) und kennzeichnet Eigenschaften wie Verzögerung, Durchsatz und Zuverlässigkeit.

> [!question]- Wie viele Bit werden heute als DSCP ausgewertet?
> Die ersten 6 Bit.

> [!question]- Welcher DSCP-Wert ist typisch für VoIP?
> 46 (EF, Expedited Forwarding).

> [!question]- Was bedeutet Precedence 000 bzw. 111?
> 000 = Routine (niedrigste Priorität), 111 = Network Control (höchste Priorität).

## Siehe auch
- [[IPv4-Header]]
- [[Ethernet-Frame]] (PCP-Priorität im VLAN-Tag als Schicht-2-Gegenstück)
