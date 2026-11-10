zahl = int(input("Gebe den Wert an: "))
quersumme = 0
letzte_ziffer = 0

while zahl > 0:
    letzte_ziffer = zahl % 10
    quersumme = quersumme + letzte_ziffer
    zahl = zahl / 10
    
print(int(quersumme))