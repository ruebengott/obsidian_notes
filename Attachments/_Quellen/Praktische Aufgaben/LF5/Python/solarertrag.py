#Tagesertrag in Wh
ertraege = [340, 200, 500, 80, 566, 242, 235]

ertrag_gesamt = 0
ertrag_gesamt_k = 0
for tagertrag in ertraege:
    ertrag_gesamt = ertrag_gesamt + tagertrag

if ertrag_gesamt > 1000:
    ertrag_gesamt_k = ertrag_gesamt / 1000
    print("Gesamtertrag in der Woche: ", ertrag_gesamt_k, "KWh")
else:
    print("Gesamtertrag in der Woche: ", ertrag_gesamt)