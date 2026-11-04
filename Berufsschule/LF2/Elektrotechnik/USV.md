---
tags: [berufsschule, lf2, elektrotechnik, usv]
fach: LF2
typ: thema
quelle: "[[LF2.pdf#page=51]]"
datum:
status: zu-lernen
---
# USV

> [!summary] Kurz & knapp
> Eine **USV (unterbrechungsfreie Stromversorgung)** überbrückt Stromausfälle und Spannungsschwankungen mit einem Akku. So können Server weiterlaufen oder sauber heruntergefahren werden. Dimensioniert wird sie über die **Gesamtleistung** der Geräte und die gewünschte **Überbrückungszeit**, unter Berücksichtigung des **Wirkungsgrads**.

## Aufgaben einer USV
- Überbrückung bei **Stromausfall** (Minuten bis Stunden)
- Schutz vor **Spannungsschwankungen**, Spannungsspitzen und kurzen Einbrüchen
- Zeit gewinnen für **geordnetes Herunterfahren** (Shutdown-Software) oder bis ein Notstromaggregat (Diesel) anläuft

## USV-Typen (nach EN 62040-3)

| Typ | Bezeichnung | Funktionsweise | Schutz |
| --- | --- | --- | --- |
| **VFD** | Offline / Standby | Geräte hängen direkt am Netz, bei Ausfall wird auf Akku umgeschaltet (kurze Umschaltzeit) | einfach, günstig |
| **VI** | Line-Interactive | wie VFD, regelt zusätzlich Spannungsschwankungen aus | mittel |
| **VFI** | Online / Doppelwandler | Strom läuft **immer** über Gleichrichter → Akku → Wechselrichter, keine Umschaltzeit | höchster Schutz, Standard im Serverraum |

## Dimensionierung – Vorgehen
1. **Gesamtleistung** aller angeschlossenen Geräte: $P_{ges} = \sum P$
2. **Benötigte Energie** für die Überbrückungszeit: $W = P_{ges} \cdot t$ (Zeit in Stunden! 20 min = 1/3 h)
3. **Wirkungsgrad** berücksichtigen: Der Akku muss mehr liefern, als bei den Geräten ankommt:
$$W_{Akku} = \frac{W}{\eta} = \frac{P_{ges} \cdot t}{\eta}$$
4. In der Praxis noch eine Reserve einplanen (Akkualterung, spätere Erweiterung, keine Tiefentladung).

**Beispiel:** 1350 W, 20 min, $\eta = 90\,\%$ → $W = 1350\,\text{W} \cdot \tfrac{1}{3}\,\text{h} = 450\,\text{Wh}$ → $W_{Akku} = 450\,\text{Wh} / 0{,}9 = 500\,\text{Wh}$. Details: [[Übung - USV-Dimensionierung]]

> [!info] VA und W
> USVs werden oft in **VA** (Scheinleistung) angegeben. Die Wirkleistung in W ist kleiner: $P = S \cdot \cos\varphi$ (Leistungsfaktor, z. B. 0,9). Eine „1500-VA-USV“ liefert also z. B. nur ca. 1350 W.

## Akkulaufzeit allgemein
$$t = \frac{W_{Akku} \cdot \eta}{P}$$
Beispiel: 240-Wh-Akku, $\eta = 85\,\%$, 50 W → $t = 204\,\text{Wh} / 50\,\text{W} \approx 4{,}1\,\text{h}$ ([[Übung - Akkulaufzeit mobiles Netzwerk]])

> [!tip] Merke
> - USV = Akku-Puffer gegen Stromausfall und Netzstörungen.
> - Für Server: **Online-USV (VFI)**.
> - $W_{Akku} = P \cdot t / \eta$ – durch $\eta$ **teilen**, weil Verluste den Bedarf erhöhen.
> - Minuten in Stunden umrechnen!

## Lernfragen
> [!question]- Wozu dient eine USV im Serverraum?
> Sie überbrückt Stromausfälle und filtert Netzstörungen, damit Server weiterlaufen oder kontrolliert herunterfahren können. So werden Datenverlust und Hardwareschäden vermieden.

> [!question]- Welcher USV-Typ bietet den besten Schutz und warum?
> Die Online-USV (VFI, Doppelwandler). Die Last wird ständig aus dem Wechselrichter versorgt, es gibt keine Umschaltzeit und Netzstörungen kommen nicht durch.

> [!question]- Wie berechnet man die minimale Akkukapazität einer USV?
> $W_{Akku} = P_{ges} \cdot t / \eta$

> [!question]- Geräte mit 600 W sollen 30 min überbrückt werden, $\eta = 0{,}9$. Welche Akkukapazität ist nötig?
> $W = 600\,\text{W} \cdot 0{,}5\,\text{h} = 300\,\text{Wh}$, $W_{Akku} = 300 / 0{,}9 \approx 333\,\text{Wh}$

## Siehe auch
- [[Wirkungsgrad]]
- [[Elektrische Leistung und Energie]]
- [[Power over Ethernet]]
- [[Spannungsebenen im Stromnetz]]
- [[Übung - USV-Dimensionierung]]
- [[Übung - Akkulaufzeit mobiles Netzwerk]]
