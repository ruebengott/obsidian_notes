Unterschiedliche Subnetze haben diese Vorteile:
- Datensicherheit
- Übersichtlichkeit
- Netzperformancesteigerung (keine Broadcastabrufe)
- Hardwarekosten & Ernergiekosten senken



Befehle zur Einrichtung eines VLANs beim Switch

show mac-address-table -> Tabelle aller MAC-Adressen nach ping vom Host
show vlan brief -> Tabelle aller VLANS
shiw

conf t -> Terminal mode
vlan <ID>
name <Name>
interface fastethernet <Nr> (Abk: int fa0/1) 
interface range fastethenernet 0/3-4 (Abk: int range fa0/3-4)
switchport access clan <ID>
