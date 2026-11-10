#rabattstaffel
#E
lizenzen = int(input("Wieviele Lizenzen wollen Sie kaufen? (Bitte nur ganze Zahlen angeben): "))

#V
rabatt = 0
if lizenzen > 0 and lizenzen <= 10:
    rabatt = 0

if lizenzen >= 10 and lizenzen < 20:
    rabatt = 1

if lizenzen >= 20 and lizenzen < 40:
    rabatt = 2
    
if lizenzen > 41 and lizenzen < 51:
    rabatt = 3
    
if lizenzen > 51
    rabatt = 4
    

#A
print("Ihr Rabatt beträgt:", rabatt,"%")