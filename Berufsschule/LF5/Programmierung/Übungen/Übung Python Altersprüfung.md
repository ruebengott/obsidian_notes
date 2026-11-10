---
tags: [berufsschule, lf5, python, übung, verzweigung]
fach: LF5
typ: übung
quelle: "[[altersprüfung.py]]"
datum: 2026-03-24
status: zu-lernen
---
# Übung Python Altersprüfung

> [!summary] Kurz & knapp
> Übung zu [[Python Verzweigungen]]: Aus dem eingegebenen Alter wird die Geschäftsfähigkeit ermittelt. Das Programm läuft fehlerfrei, lässt sich aber mit `elif` vereinfachen.

## Aufgabe (rekonstruiert)
Schreibe ein Programm nach dem EVA-Prinzip, das ein Alter einliest und ausgibt:
- ab 18: volljährig und voll geschäftsfähig
- ab 16: minderjährig und beschränkt geschäftsfähig
- sonst: minderjährig und bedingt geschäftsfähig

## Eigene Lösung
```python
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
```

## Erklärung
- Die Eingabe wird als String gelesen und dann mit `int()` umgewandelt.
- Die verschachtelte Verzweigung prüft zuerst `>= 18`, im `else` dann `>= 16`.
- Die Reihenfolge stimmt: von der höchsten Grenze nach unten.

## Review
> [!tip] Verbesserung
> - `ergebnis = 0` ist unnötig, weil jeder Zweig `ergebnis` setzt. Außerdem wechselt die Variable den Typ von `int` zu `str`.
> - Mit `elif` wird es flacher und lesbarer.
> - Englische und deutsche Variablennamen gemischt (`age`, `ergebnis`): einheitlich bleiben.
> - Negative oder unsinnige Eingaben werden nicht abgefangen.
> ```python
> alter = int(input("Bitte Alter eingeben: "))
>
> if alter < 0:
>     ergebnis = "ungültiges Alter"
> elif alter >= 18:
>     ergebnis = "volljährig und voll geschäftsfähig"
> elif alter >= 16:
>     ergebnis = "minderjährig und beschränkt geschäftsfähig"
> else:
>     ergebnis = "minderjährig und bedingt geschäftsfähig"
>
> print("------")
> print("Altersprüfung hat ergeben:", ergebnis)
> ```

> [!info] Fachlicher Hinweis
> Nach BGB gilt: unter 7 Jahren **geschäftsunfähig**, 7 bis 17 Jahre **beschränkt geschäftsfähig**, ab 18 **voll geschäftsfähig**. Die Grenze 16 und der Begriff „bedingt geschäftsfähig“ stammen vermutlich aus der Aufgabenstellung und nicht aus dem Gesetz.

## Zum Selbsttest
> [!question]- Was gibt das Programm bei Eingabe `16` aus, was bei `15`?
> 16: „Minderjährig und beschränkt geschäftsfähig“. 15: „Minderjährig und bedingt geschäftsfähig“.

> [!question]- Schreibe die Prüfung mit den BGB-Grenzen (7 und 18).
> > [!success]- Lösung
> > ```python
> > if alter >= 18:
> >     print("voll geschäftsfähig")
> > elif alter >= 7:
> >     print("beschränkt geschäftsfähig")
> > else:
> >     print("geschäftsunfähig")
> > ```

## Siehe auch
- [[Python Verzweigungen]]
- [[Programmablaufplan und Flussdiagramm]]
- [[LF5 - Übersicht]]
