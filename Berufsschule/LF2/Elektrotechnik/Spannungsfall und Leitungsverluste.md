---
tags: [berufsschule, lf2, elektrotechnik, netzwerk]
fach: LF2
typ: thema
quelle: "[[LF2.pdf#page=51]]"
datum:
status: zu-lernen
---
# Spannungsfall und Leitungsverluste

> [!summary] Kurz & knapp
> Jede Leitung hat einen Widerstand. Fließt Strom, fällt an ihr Spannung ab ($U_V = R \cdot I$) und es entsteht Verlustwärme ($P_V = I^2 \cdot R$). Deshalb muss die Quelle etwas mehr Spannung liefern, als das Gerät braucht. Ein höherer Strom bedeutet quadratisch höhere Verluste.

## Formeln

| Was | Formel |
| --- | --- |
| Spannungsfall auf der Leitung | $U_V = R_{Ltg} \cdot I$ |
| benötigte Spannung an der Quelle | $U_{Quelle} = U_{Gerät} + U_V$ |
| Verlustleistung auf der Leitung | $P_V = U_V \cdot I = I^2 \cdot R_{Ltg}$ |
| Übertragungswirkungsgrad | $\eta = \dfrac{P_{Gerät}}{P_{Quelle}} = \dfrac{P_{Gerät}}{P_{Gerät} + P_V}$ |

```mermaid
flowchart LR
    S["Quelle / Switch: U_Quelle"] -- "I" --> L["Leitung R_Ltg: U_V, P_V"] --> G["Gerät: U_Gerät"]
```

## Beispiel (PoE-Gerät, 8 Ω Leitung, 48 V / 0,5 A)
- $U_V = 8\,\Omega \cdot 0{,}5\,\text{A} = 4\,\text{V}$
- $U_{Switch} = 48\,\text{V} + 4\,\text{V} = 52\,\text{V}$
- $P_V = (0{,}5\,\text{A})^2 \cdot 8\,\Omega = 2\,\text{W}$
- $P_{Gerät} = 48\,\text{V} \cdot 0{,}5\,\text{A} = 24\,\text{W}$ → $\eta = 24 / 26 \approx 92{,}3\,\%$

## Warum ist der Strom so wichtig?
Weil $I$ **quadratisch** in die Verluste eingeht:
- doppelter Strom → vierfache Verluste
- 2 A → 3 A (Faktor 1,5) → Verluste × 2,25 (z. B. 8 W → 18 W bei 2 Ω)

Deshalb überträgt man Energie über weite Strecken mit **hoher Spannung und kleinem Strom** ([[Spannungsebenen im Stromnetz]]), und deshalb arbeitet PoE mit ca. 48 V statt 5 oder 12 V.

## Wovon hängt der Leitungswiderstand ab?
- **Länge**: längeres Kabel → mehr Widerstand. Hin- und Rückleiter zählen beide.
- **Querschnitt**: dünnere Adern (z. B. AWG 26 bei Patchkabeln) → mehr Widerstand
- **Material**: Kupfer ist gut, kupferkaschiertes Aluminium (CCA) ist schlechter und für PoE ungeeignet.

> [!tip] Merke
> - Spannungsfall: $U_V = R \cdot I$, Verlust: $P_V = I^2 \cdot R$.
> - Die Quelle muss **Gerätespannung + Spannungsfall** liefern.
> - Hoher Strom → Erwärmung → im Extremfall **Brandgefahr**, Sicherung löst aus.

## Lernfragen
> [!question]- Wie berechnet man den Spannungsfall auf einer Leitung?
> $U_V = R_{Ltg} \cdot I$

> [!question]- Ein Gerät zieht statt 2 A plötzlich 3 A über eine 2-Ω-Leitung. Wie ändern sich die Verluste?
> Vorher $P_V = (2\,\text{A})^2 \cdot 2\,\Omega = 8\,\text{W}$, nachher $(3\,\text{A})^2 \cdot 2\,\Omega = 18\,\text{W}$, also mehr als doppelt so viel.

> [!question]- Warum nutzt PoE eine relativ hohe Spannung von ca. 48 V?
> Für die gleiche Leistung braucht man bei höherer Spannung weniger Strom. Damit sinken Spannungsfall und Verluste ($I^2 R$) auf den dünnen Netzwerkadern.

> [!question]- Welche Spannung muss ein Switch liefern, wenn das Gerät 48 V braucht und auf der Leitung 4 V abfallen?
> $48\,\text{V} + 4\,\text{V} = 52\,\text{V}$

## Siehe auch
- [[Ohmsches Gesetz]]
- [[Power over Ethernet]]
- [[Übung - Spannungsfall bei PoE und Netzwerkgeräten]]
- [[Formelsammlung Elektrotechnik]]
