Infos:
- Jedes VLAN hat seinen eigenen IP-Adressbereich
- VLAN: **eine** Netzwerkkarte bekommt die erste Hostadresse des jeweiligen Subnetzes, hier also **drei** Adressen


Beispiel:
Client-Adressen:
192.168.10.10/24 VLAN 10
...          .20.20/24 VLAN 20
...          .30.30/24 VLAN 30

192.168.10.1
192.168.20.1
192.168.30.1

3 fiktive Gateways auf einer Netzwerkkarte (NIC) einrichten

Wir haben eine physikalische Schnittstelle am Router:
fa0/0 

Und erschaffen drei virtuelle Schnittstellen am Router:
fa0/0.10 
fa0/0.20
fa0/0.30

**Einrichtung am Router:**
```
interface fastethernet 0/0.10
encapsulation dot1q 10
ip address 192.168.10.1 255.255.255.0
exit
```

```
interface fastethernet 0/0.20
encapsulation dot1q 20
ip address 192.168.20.1 255.255.255.0
exit
```

```
interface fastethernet 0/0.30
encapsulation dot1q 30
ip address 192.168.30.1 255.255.255.0
exit
```

Überprüfen:
```
sh ip int brief
```


Trunkline beim Switch einrichten:
```
interface fastethernet 0/4
switchport mode trunk
switchport trunk allowed vlan 10,20,30
```


---



**Befehle**:
```
Router>enable
Router#conf t
Router(config)#interface fastethernet 0/0
Router(config-if)#no shutdown

Router(config-if)#interface fastethernet 0/0.10
Router(config-subif)#encapsulation dot1q 10
Router(config-subif)#ip address 192.168.10.1 255 255 255 0
Router(config-subif)#exit

Router(config)#interface fastethernet 0/0.20
Router(config-subif)#encapsulation dot1q 20
Router(config-subif)#ip address 192.168.20.1 255.255.255.0
Router(config-subif)#exit

Router(config)#interface fastethernet 0/0.30
Router(config-subif)#encapsulation dot1q 30
Router(config-subif)#ip address 192.168.30.1 255.255.255.0
Router(config-subif)#exit

Router(config)#exit
Router#write memory

```





