#16
zahl = 30
if zahl > 10:
    print("Zahl ist größer als 10.")
    
#17
if zahl % 2 == 0:
    print("Zahl ist durch 2 teilbar.")
else:
    print("Nicht durch 2 teilbar.")
    
#18
#alter = int(input("Wie ist dein Alter?"))

#if alter >= 18:
 #   print("Du bist volljährig")
    
#else:
  #  print("Du bist leider noch minderjährig")
    
#19
#eingabe = str(input("Wie lautet das Passwort?: "))
#if eingabe == "python123":
 #   print("Zugriff erlaubt.")
#else:
 #   print("Zugriff verweigert.")
    
#20
for i in range(5):
    print(i+1)
    
#21
for i in range(5):
    print("Hallo")
    
#22
summe = 0
for i in range(1,11):
    summe += i
    
print(summe)

#23
zahl = 4

while zahl > 1:
    zahl = zahl - 1
    print(zahl)
    
#26
liste = ["rot", "blau", "lila"]
#27
print(liste[0])

#28
liste.append("rosa")
print(liste)

#29
for i in liste:
    print(i)
    
#30
def begruessung():
    print("Hallo")
    
begruessung()

#31 Addition
summe = 0
def addition(a,b):
    summe = a+b
    return summe
    
addition(5,3)

#33
def positiv(zahl):
    if zahl > 0:
        print("Die Zahl:", zahl ,"ist positiv.")
    else:
        print("Zahl ist negativ")
        
positiv(int(input("Welche Zahl möchtest du prüfen?")))

