l = ["Apfel","Test","kiwi","orangen","papaya"]
#a = input("Was möchtest du hinzufügen? ")
#l.append(a)
l.insert(0, "Ananas")
#b = input("Was möchtest du entfernen? ")
#l.remove(b)
l.sort()
anzahl = len(l)

print("Obstkorb")
print("="*22)

for element in l:
    print(element)

print("="*22)
print("Liste über Index: ")

for i in range(anzahl):
    print(i, l[i], "\t\t", anzahl-i-1, l[anzahl-i-1])