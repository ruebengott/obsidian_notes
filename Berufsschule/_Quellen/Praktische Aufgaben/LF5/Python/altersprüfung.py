#Alterssprüfung

#Eingabe
age = input("Bitte Alter eingeben: ")


#Verarbeitung
int_age = int(age)
ergebnis = 0

if int_age >= 18:
    ergebnis = "volljährig und voll geschäftsfähig"    

else:
    if int_age >= 16:
        ergebnis= "Minderjährig und beschränkt geschäftsfähig"
    else:
        ergebnis = "Minderjährig und bedingt geschäftsfähig"

#Ausgabe
print("------") 
print("Altersprüfung hat ergeben: ", ergebnis)
