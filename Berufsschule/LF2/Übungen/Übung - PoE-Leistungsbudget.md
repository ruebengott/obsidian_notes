---
tags: [berufsschule, lf2, elektrotechnik, poe, übung]
fach: LF2
typ: übung
quelle: "[[LF2.pdf#page=51]]"
datum:
status: zu-lernen
---
# Übung - PoE-Leistungsbudget

> [!summary] Kurz & knapp
> IT-Übungsaufgabe 1: Prüfen, ob das PoE-Budget eines Switches für alle angeschlossenen Geräte reicht. Auch in [[LF2 - Elektrotechnik.pdf#page=2]].

## Aufgabe
Ein 24-Port-Switch unterstützt PoE mit einem Gesamtbudget von **370 W**. Angeschlossen sind:
- 8 IP-Kameras à 12 W
- 6 Access Points à 18 W
- 4 VoIP-Telefone à 7 W

a) Berechne die gesamte benötigte PoE-Leistung.
b) Reicht das Leistungsbudget des Switches aus?
c) Wie viel Reserve bleibt oder fehlt?
d) Berechne den Strom(verbrauch) des Switches bei 230 V (ohne Eigenverbrauch).

> [!success]- Lösung
> **a)**
> - Kameras: $8 \cdot 12\,\text{W} = 96\,\text{W}$
> - Access Points: $6 \cdot 18\,\text{W} = 108\,\text{W}$
> - Telefone: $4 \cdot 7\,\text{W} = 28\,\text{W}$
> - $P_{ges} = 96 + 108 + 28 = \mathbf{232\,W}$
>
> **b)** Ja, $232\,\text{W} \le 370\,\text{W}$.
>
> **c)** Reserve: $370\,\text{W} - 232\,\text{W} = \mathbf{138\,W}$
>
> **d)** $I = \dfrac{P}{U} = \dfrac{232\,\text{W}}{230\,\text{V}} \approx \mathbf{1{,}01\,A}$
>
> *Praxis-Hinweis:* Der tatsächliche Netzstrom ist etwas höher, weil das Switch-Netzteil Verluste hat und der Switch selbst Strom braucht. Beides soll laut Aufgabe ignoriert werden.

## Siehe auch
- [[Power over Ethernet]]
- [[Elektrische Leistung und Energie]]
- [[Übung - Spannungsfall bei PoE und Netzwerkgeräten]]
