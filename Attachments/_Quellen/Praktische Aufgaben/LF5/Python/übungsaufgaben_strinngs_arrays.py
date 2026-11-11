#Übungsaufgaben strings und arrays
#1
name = "Moritz"
print(name)

#2
text = "Hallo Welt"
print(text[0])

#3
print(text[-1])

#4
l_essen = "Pizza"
print(len(l_essen))

#5
print(text.upper())

#6
print(text.lower())

#7
print(text.find("Python"))

#16
liste = ["rot", "grün", "blau"]

#17
print(liste[0])

#18
print(liste[-1])

#19
liste.append("gelb")
print(liste)

#20
liste.remove("gelb")
print(liste)

#21
liste[1] = "türkis"
print(liste)

#22
print(len(liste))

#23
for i in liste:
    print(i)
    
#24
summe = 0
zahlen = [3,3,4,3]
for i in zahlen:
    summe = summe+i
    
print(summe)

#25
if "rosa" in liste:
    print("true")
else:
    print("false")