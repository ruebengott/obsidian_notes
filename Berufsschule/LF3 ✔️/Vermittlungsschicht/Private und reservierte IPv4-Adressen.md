---
tags: [berufsschule, lf3, ipv4]
fach: LF3
typ: thema
quelle: "[[LF3.pdf#page=26]]"
datum: 2025-11-03
status: zu-lernen
---
# Private und reservierte IPv4-Adressen

> [!summary] Kurz & knapp
> Die IANA hat bestimmte IPv4-Bereiche für besondere Zwecke reserviert. Die drei **privaten Bereiche** (RFC 1918) **10.0.0.0/8, 172.16.0.0/12 und 192.168.0.0/16** dürfen ohne Registrierung im LAN/WLAN genutzt werden, tauchen aber **im öffentlichen Internet nicht auf**.

## Private Adressbereiche (LAN/WLAN)

| Bereich | CIDR | von – bis | frühere Klasse |
|---|---|---|---|
| 10.0.0.0 | /8 | 10.0.0.0 – 10.255.255.255 | Class A (1 Netz) |
| 172.16.0.0 | /12 | 172.16.0.0 – 172.31.255.255 | Class B (16 Netze) |
| 192.168.0.0 | /16 | 192.168.0.0 – 192.168.255.255 | Class C (256 Netze) |

Die Präfixlänge ist nur die **Mindestangabe**. Die Subnetzmaske darf größer sein, man darf also z. B. 192.168.1.0/24 oder 10.10.10.8/30 bilden.

> [!info] Warum private Adressen?
> IPv4-Adressen sind knapp (2³² ≈ 4,3 Mrd.). Private Adressen können in jedem LAN wiederverwendet werden. Für den Zugang ins Internet übersetzt der Router sie per **NAT** in seine öffentliche Adresse.

## Weitere reservierte Bereiche

| Bereich | Zweck | RFC |
|---|---|---|
| 0.0.0.0/8 | „dieses“ Netz. 0.0.0.0/32 = der Host selbst, nur als Quelladresse (z. B. bei der DHCP-Aushandlung, bevor der Host eine Adresse hat) | 5735 |
| 127.0.0.0/8 | **Loopback**: Pakete verlassen den Host nicht (127.0.0.1 = localhost) | 1700 |
| 169.254.0.0/16 | **APIPA**/Zeroconf: automatische Selbstkonfiguration, wenn kein DHCP-Server antwortet. Nur im lokalen Netz | 3927 |
| 192.0.2.0/24, 198.51.100.0/24, 203.0.113.0/24 | Beispieladressen für Dokumentationen | 5737 |
| 198.18.0.0/15 | Tests von Netzwerkkomponenten | 2544 |
| 224.0.0.0/4 | **Multicast** (Sender an mehrere ausgewählte Empfänger) | 3171 |
| 255.255.255.255/32 | **Limited Broadcast**: nur als Zieladresse, wird nicht aus dem Netz geroutet | 1700 |

Für Europa verwaltet **RIPE** die öffentlichen IP-Adressen. Endkunden erhalten sie über ihren Provider.

> [!tip] Merke
> - Privat: **10/8, 172.16/12, 192.168/16**. Achtung: 172.16 bis **172.31**!
> - 127.x = Loopback, 169.254.x = APIPA (Hinweis: DHCP hat nicht funktioniert)
> - Private Adressen werden im Internet nicht geroutet → NAT

## Lernfragen
> [!question]- Nenne die drei privaten IPv4-Adressbereiche mit CIDR.
> 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16.

> [!question]- Ist 172.32.5.1 eine private Adresse?
> Nein. Der private /12-Bereich reicht nur von 172.16.0.0 bis 172.31.255.255.

> [!question]- Ein PC hat die Adresse 169.254.12.7. Was ist wahrscheinlich passiert?
> Er hat keine Antwort vom DHCP-Server bekommen und sich per APIPA selbst eine Adresse gegeben.

> [!question]- Wofür steht 127.0.0.1?
> Loopback (localhost). Pakete an diese Adresse verlassen den Host nicht.

> [!question]- Warum darf man innerhalb des privaten Bereichs eine größere Subnetzmaske wählen?
> Die angegebene Präfixlänge ist nur die Mindestangabe für den ganzen Bereich. Man darf ihn beliebig in kleinere Subnetze aufteilen.

## Siehe auch
- [[IPv4-Adresse vs. MAC-Adresse]]
- [[Subnetting]]
- [[DHCP]]
