#Rechenprogram mit Funktionen

#Funktion multiplizieren mit den Parametern zahl1 und zahl2
def multiplizieren(zahl1,zahl2):
    ergebnis = zahl1 * zahl2
    return ergebnis

def divideren(zahl1,zahl2):
    ergebnis = zahl1 / zahl2
    return ergebnis

def addieren(zahl1,zahl2):
    ergebnis = zahl1 + zahl2
    return ergebnis

def subtrahieren(zahl1,zahl2):
    ergebnis = zahl1 - zahl2
    return ergebnis


#Hauptprogramm
a = int(input("Zahl 1: "))
operation = "Welche Operation?"
b = int(input("Zahl 2: "))

if operation == *:
    funktionsergebnis1 = multiplizieren(a, b)
if operation == /:
    funktionsergebnis2 = divideren(a, b)

if operation == +:
    funktionsergebnis3 = addieren(a, b)
    
if operation == -:
    funktionsergebnis4 = subtrahieren(a, b)

#Ausgabe
print("Ergebnis der Multiplikation: ", funktionsergebnis1)
print("Ergebnis der Division: ", funktionsergebnis2)
print("Ergebnis der Addition: ", funktionsergebnis3)
print("Ergebnis der Subtraktion: ", funktionsergebnis4)

