Ein CPS verbindet eingebettete Rechentechnik mit physischen Prozessen. Es erfasst Messgrößen über Sensoren, verarbeitet sie, wirkt über Aktoren zurück auf die physische Welt und ist vernetzt.

"Ist das ALLNET 3419v3 ein CPS?"

Ja, weil folgende Merkmale erfüllt werden:

- **Sensorik:** Es handelt sich um eine IP-Thermometer/Sensor-Zentrale zur Temperaturerfassung über das Netzwerk. Laut Datenblatt sind zusätzlich Temperatur, Feuchte, Gas, Rauch, Bewegung usw. über das Netzwerk erfassbar. [industry-electronics](https://industry-electronics.com/allnet/all3419-ip-msr-central-3x-i2c-1x-usb-lan-wlan-printview-520112.htm)[manualmachine](https://manualmachine.com/allnet/all3419/7639521-user-manual)
- **Steuerung und Regelung:** Das Gerät ist eine „MSR-Zentrale“, also für Messen, Steuern und Regeln. Ein Händler führt es als Temperaturregler mit kabelgebundener und drahtloser Anbindung und listet den Thermostattyp „Aktor“. [galaxus](https://www.galaxus.be/en/s2/product/allnet-all3419-ip-msr-central-3x-i2c-1x-usb-lanwlan-thermostats-17698068)[galaxus](https://www.galaxus.be/en/s2/product/allnet-all3419-ip-msr-central-3x-i2c-1x-usb-lanwlan-thermostats-17698068)
- **Vernetzung:** Es ist sowohl kabelgebunden als auch drahtlos per WLAN in Netzwerke integrierbar. Über USB lassen sich optional Funksensoren (EnOcean, Plugwise) anbinden. [galaxus](https://www.galaxus.it/en/s1/product/allnet-all3419-ip-msr-central-3x-i2c-1x-usb-lanwlan-print-servers-17698068)[industry-electronics](https://industry-electronics.com/allnet/all3419-ip-msr-central-3x-i2c-1x-usb-lan-wlan-printview-520112.htm)
- **Verteiltes System:** Mehrere ALL3419 können mit den größeren Mess- und Steuerrechnern ALL3500/3505/4500 oder ALL5000 zusammenarbeiten, um viele räumlich verteilte Werte zentral darzustellen. [manualmachine](https://manualmachine.com/allnet/all3419/7639521-user-manual)
  
  **Einschränkung:** Wenn das Gerät nur mit dem mitgelieferten Temperatursensor betrieben wird und lediglich Werte anzeigt oder aufzeichnet, fehlt der Rückkanal in die physische Welt. Dann ist es eher ein vernetztes Messgerät, also ein IoT-Gerät, als ein vollständiges CPS. Zum CPS im engeren Sinn wird es erst, wenn über angeschlossene Aktoren ein geschlossener Regelkreis entsteht, zum Beispiel beim Schalten einer Heizung oder Lüftung.
  
  Aktor = Elektrisches Steuergerät,