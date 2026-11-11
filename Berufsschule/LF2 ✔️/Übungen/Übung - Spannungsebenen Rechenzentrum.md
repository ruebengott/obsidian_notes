---
tags: [berufsschule, lf2, elektrotechnik, übung]
fach: LF2
typ: übung
quelle: "[[LF2.pdf#page=56]]"
datum:
status: zu-lernen
---
# Übung - Spannungsebenen Rechenzentrum

> [!summary] Kurz & knapp
> Arbeitsblatt „Spannungsebenen“: Leistungsbedarf eines Rechenzentrums inkl. Notstromsystem berechnen, Trafo-Wirkungsgrade berücksichtigen und erklären, warum Hochspannung für den Transport genutzt wird.

## Aufgabe
Ein mittelständisches Unternehmen plant ein Rechenzentrum am Stadtrand. Der Strom kommt mit **110 kV** (Hochspannung) zum Umspannwerk, wird auf **10 kV** (Mittelspannung) und im Unternehmen auf **400 V** (Niederspannung) transformiert.

Anforderungen:
- 50 Server à 500 W
- 10 Netzwerkswitches à 150 W
- 5 Klimaanlagen à 2000 W
- 1 Notstromsystem (USV + Dieselgenerator), das zusätzlich **15 %** der Gesamtleistung benötigt

Außerdem: Wirkungsgrad jedes Transformators **98 %**, zwei Stufen (110 kV → 10 kV, 10 kV → 400 V), Dauerbetrieb 24 h/Tag.

1. Ermitteln Sie die gesamte Leistungsaufnahme aller Geräte ohne das Notstromsystem.
2. Ermitteln Sie die für das Notstromsystem erforderliche Mehrleistung.
3. Ermitteln Sie den Gesamtleistungsbedarf des Rechenzentrums.
4. Berechnen Sie mit den Trafo-Wirkungsgraden, wie viel Leistung auf der 110-kV-Ebene bereitgestellt werden muss.
5. Ermitteln Sie den täglichen Energieverbrauch in kWh.
6. Erklären Sie, warum Energie über weite Strecken mit hoher Spannung transportiert wird und nicht mit 400 V.
7. Beschreiben Sie, welche Probleme für IT-Systeme bei Spannungsschwankungen oder Ausfällen entstehen können.

> [!success]- Lösung
> **1.**
> - Server: $50 \cdot 500\,\text{W} = 25\,\text{kW}$
> - Switches: $10 \cdot 150\,\text{W} = 1{,}5\,\text{kW}$
> - Klima: $5 \cdot 2000\,\text{W} = 10\,\text{kW}$
> - Summe: $\mathbf{36{,}5\,kW}$
>
> **2.** $0{,}15 \cdot 36{,}5\,\text{kW} = \mathbf{5{,}475\,kW} \approx 5{,}48\,\text{kW}$
>
> **3.** $36{,}5\,\text{kW} + 5{,}475\,\text{kW} = \mathbf{41{,}975\,kW} \approx 41{,}98\,\text{kW}$
> (In der Aufgabe steht „Gesamtenergieverbrauch“. Gemeint ist hier die Gesamt**leistung**. Die Energie folgt in Aufgabe 5.)
>
> **4.** $\eta_{ges} = 0{,}98 \cdot 0{,}98 = 0{,}9604$
> $P_{110\,\text{kV}} = \dfrac{41{,}975\,\text{kW}}{0{,}9604} \approx \mathbf{43{,}71\,kW}$
> (Schrittweise: $41{,}975 / 0{,}98 = 42{,}83\,\text{kW}$ auf 10 kV, $42{,}83 / 0{,}98 = 43{,}71\,\text{kW}$ auf 110 kV)
>
> **5.**
> - Verbrauch der Geräte: $W = 41{,}975\,\text{kW} \cdot 24\,\text{h} \approx \mathbf{1007{,}4\,kWh}$ pro Tag
> - Aus dem Netz (inkl. Trafoverluste): $43{,}71\,\text{kW} \cdot 24\,\text{h} \approx \mathbf{1049\,kWh}$ pro Tag
>
> **6.** $P = U \cdot I$: Bei hoher Spannung fließt für dieselbe Leistung ein viel kleinerer Strom. Die Leitungsverluste $P_V = I^2 \cdot R$ sinken dadurch quadratisch, und man kann dünnere, günstigere Leitungen verwenden. Mit 400 V wären Ströme und Verluste über weite Strecken enorm.
>
> **7.** Abstürze und ungeplante Neustarts, Datenverlust und beschädigte Dateisysteme/Datenbanken, Hardwareschäden durch Überspannung (Netzteile, Mainboards), Ausfall von Diensten und damit wirtschaftlicher Schaden. Schutz: [[USV]], Notstromaggregat, Überspannungsschutz, redundante Einspeisung.

> [!note] Hinweis zur Mitschrift
> In der Mitschrift steht bei 3. ein schwer lesbarer Wert („41,58 kW“ oder „41,98 kW“). Richtig ist **41,975 kW ≈ 41,98 kW**. Aufgabe 4 wurde dort nicht zu Ende gerechnet.

## Siehe auch
- [[Spannungsebenen im Stromnetz]]
- [[Wirkungsgrad]]
- [[USV]]
- [[Elektrische Leistung und Energie]]
