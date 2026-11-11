duration= input("Gebe deine Beschäftigungsdauer ein: ")
int_duration = int(duration)

if int_duration < 1:
    prämie = 0
else:
    if int_duration < 2:
        prämie = 50
    else:
        if int_duration < 4:
            prämie = 100
        else:
            prämie = 150 + 10* (prämie-4)

print("Deine Prämie ist: ", prämie)
        
        
        
        