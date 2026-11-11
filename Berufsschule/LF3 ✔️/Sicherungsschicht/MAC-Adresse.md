---
tags: [berufsschule, lf3, mac-adresse, schicht-2]
fach: LF3
typ: thema
quelle: "[[LF3.pdf#page=5]]"
datum: 2025-09-15
status: zu-lernen
---
# MAC-Adresse

> [!summary] Kurz & knapp
> Die MAC-Adresse (**Media Access Control**) ist die 48 Bit lange Hardware-Adresse einer Netzwerkschnittstelle auf OSI-Schicht 2. Sie besteht aus 24 Bit Herstellerkennung (**OUI**) und 24 Bit Gerätekennung (**OUA**). Die ersten beiden Bits legen den Adresstyp fest (I/G und U/L).

## Allgemeines
- **Synonyme:** Hardware-Adresse, Ethernet-Adresse, physikalische Adresse
- Definiert von der **IEEE** (Institute of Electrical and Electronics Engineers) in IEEE 802. Gilt unabhängig von der Übertragungstechnik, z. B. für Ethernet (802.3), WLAN (802.11) und Bluetooth (802.15).
- Dient der **weltweit eindeutigen Identifizierung** einer Netzwerkschnittstelle.
- Jede Netzwerkkarte hat eine eigene MAC-Adresse, auch virtuelle Netzwerkkarten (z. B. bei VMs).
- Wird vom **Hersteller** fest konfiguriert und lässt sich in der Regel nicht verändern. Per Software kann sie aber überschrieben werden.
- Jeder [[Ethernet-Frame]] enthält **Ziel-MAC** und **Quell-MAC**. Der Empfänger vergleicht die Ziel-MAC mit seiner eigenen. Stimmt sie überein, gibt er den Frame an die höhere Schicht weiter, sonst verwirft er ihn.

## Aufbau (48 Bit = 6 Oktette)

| Bezeichnung | I/G | U/L | OUI | OUA |
|---|---|---|---|---|
| Bit | 1. | 2. | 3.–24. | 25.–48. |
| Bedeutung | Herstellerkennung (24 Bit) | ← | ← | Gerätekennung (24 Bit) |

- **I/G-Bit (Individual/Group):**
  - 0 = Individualadresse (**Unicast**): genau eine Netzwerkkarte wird adressiert
  - 1 = Gruppenadresse (**Multicast**): mehrere Netzwerkkarten werden adressiert
- **U/L-Bit (Universal/Local):**
  - 0 = universell, weltweit eindeutig (vom Hersteller vergeben)
  - 1 = lokal verwaltet (z. B. per Software/Administrator vergeben)
- **OUI (Organizationally Unique Identifier):** Die IEEE vergibt die ersten 24 Bit an Hersteller. Weil die ersten beiden Bits bei universellen Unicast-Adressen 0 sind, werden sie oft zum OUI dazugezählt.
- **OUA (Organizationally Unique Address), Bit 25–48:** Diese Gerätenummer vergibt der Hersteller selbst. Er muss nur sicherstellen, dass jede Adresse nur einmal vorkommt. Pro OUI sind **2²⁴ ≈ 16,7 Mio.** Adressen möglich.

**Adressraum:** 2⁴⁸ ≈ 281,5 Billionen Adressen. Laut Prognose reicht das bis etwa zum Jahr 2100.

**Kombinationen der 2 Typ-Bits:** 2² = 4 Kombinationen (Unicast/universell, Multicast/universell, Unicast/lokal, Multicast/lokal).

> [!warning] Korrektur
> Die ursprüngliche Mitschrift enthielt folgende Fehler:
> 1. „2 Bit Typfestlegung + **22–24 Bit Gerätekennung**“: Richtig sind 2 Bit Typ + 22 Bit Herstellerkennung = 24 Bit **OUI**, danach 24 Bit **Gerätekennung (OUA)**.
> 2. „**25.–28. Bit**: OUA“: Richtig ist **25.–48. Bit**.
> 3. „Herstellerkennungen beginnen deshalb **immer mit 00**“: Nicht die ersten zwei *Hex-Ziffern* sind 00, sondern nur die ersten zwei *Bits* in Übertragungsreihenfolge (I/G = 0, U/L = 0). In der üblichen hexadezimalen (kanonischen) Schreibweise sind das die **beiden niederwertigsten Bits des ersten Oktetts**. Beispiel: `AC-DE-48-…`, AC = 1010 11**00**. Man erkennt eine universelle Unicast-Adresse also an der **zweiten** Hex-Ziffer 0, 4, 8 oder C. Siehe [[MAC-Adresse - Darstellung und kanonische Form]].
> 4. Die Mitschrift begründete den Anfang „11“ der Broadcast-Adresse damit, dass sie „von Software erzeugt“ sei. Tatsächlich ist die Broadcast-Adresse einfach **FF-FF-FF-FF-FF-FF**, also alle 48 Bit = 1. Dass dabei auch I/G = 1 (Gruppe) gilt, ist folgerichtig. Siehe [[MAC-Broadcast und Multicast]].

## Offene Fragen aus dem Unterricht
- **Was sind Frames?** Datenrahmen auf Schicht 2, siehe [[Ethernet-Frame]].
- **Wofür steht IEEE?** Institute of Electrical and Electronics Engineers. Dieser Berufsverband normiert u. a. Ethernet und WLAN.
- **Broadcaststurm?** Broadcasts werden endlos im Netz weitergeleitet, z. B. bei Schleifen zwischen Switches, und legen das Netz lahm. Siehe [[MAC-Broadcast und Multicast]].

> [!tip] Merke
> - 48 Bit, 6 Oktette, Hex-Schreibweise `XX-XX-XX-YY-YY-YY`.
> - Die ersten 24 Bit sind die Herstellerkennung (OUI), die letzten 24 Bit die Gerätekennung.
> - Bit 1 = I/G (0 Unicast, 1 Multicast). Bit 2 = U/L (0 universell, 1 lokal).
> - OSI-Schicht 2. Wird von Switches zur Weiterleitung im LAN verwendet.

## Lernfragen
> [!question]- Wie lang ist eine MAC-Adresse und wie ist sie aufgebaut?
> 48 Bit (6 Byte). Bit 1 ist das I/G-Bit, Bit 2 das U/L-Bit, Bit 3–24 der OUI (zusammen 24 Bit Herstellerkennung). Bit 25–48 sind die Gerätekennung (OUA).

> [!question]- Was bedeuten I/G-Bit und U/L-Bit?
> I/G: 0 = Individual-/Unicast-Adresse, 1 = Gruppen-/Multicast-Adresse. U/L: 0 = universell (weltweit eindeutig, vom Hersteller), 1 = lokal verwaltet.

> [!question]- Wer vergibt den OUI und wer die Gerätekennung?
> Den OUI vergibt die IEEE an den Hersteller. Die Gerätekennung (OUA) vergibt der Hersteller selbst und muss dabei die Eindeutigkeit sicherstellen.

> [!question]- Wie viele MAC-Adressen gibt es theoretisch?
> 2⁴⁸ ≈ 281,5 Billionen.

> [!question]- Was macht eine Netzwerkkarte mit einem Frame, dessen Ziel-MAC nicht ihre eigene ist?
> Sie verwirft ihn. Ausnahmen sind Broadcast, abonnierte Multicasts und der Promiscuous Mode.

## Siehe auch
- [[MAC-Adresse - Darstellung und kanonische Form]]
- [[MAC-Broadcast und Multicast]]
- [[MAC-Randomisierung]]
- [[IPv4-Adresse vs. MAC-Adresse]]
- [[Ethernet-Frame]]
