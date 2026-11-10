#rabattstaffel
#E
lizenzen = int(input("Wieviele Lizenzen wollen Sie kaufen? (Bitte nur ganze Zahlen angeben): "))

#V
rabatt = 0
if lizenzen <= 10:
    rabatt = 0
else:
    if lizenzen <= 20:
        rabatt = 1
    else:
        if lizenzen <= 40:
            rabatt = 2
        else:
            if lizenzen <= 51:
                rabatt = 3
            else:
                rabatt = 4
    
#A
print("Ihr Rabatt beträgt:", rabatt,"%")