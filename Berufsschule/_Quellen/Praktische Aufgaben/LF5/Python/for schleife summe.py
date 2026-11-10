#Programm zur Berechnung einer Zahlenfolge von 1 bis ende
ende = int(input("Bitte Reihenfolge eingeben: "))
zahlensumme = 0
zahlenprodukt = 1
for ele in range(ende+1):
    if (ele>0):
        print(ele)
        zahlensumme = zahlensumme + ele
        zahlenprodukt = zahlenprodukt * ele
        
print("Zahlensumme:", zahlensumme)
print("Zahlenprodukt:", zahlenprodukt)