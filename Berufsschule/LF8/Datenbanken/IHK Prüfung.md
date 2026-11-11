
Teil A

Material:

![[Pasted image 20261111095126.png]]

![[Pasted image 20261111095139.png]]

![[Pasted image 20261111095151.png]]
![[Pasted image 20261111100833.png|579]]

![[Pasted image 20261111101020.png]]


![[Pasted image 20261111095021.png]]
```
INSERT INTO Aerzte (Vorname, Nachname, Fachgebiet)
VALUES ("Horner", "Hugo", "Allgemeinmedizin")
```

![[Pasted image 20261111095631.png]]
```
GRANT write ON NotaufnahmeManagement.Verschreibungen  TO hhorner
```

![[Pasted image 20261111101543.png]]

```
REVOKE write ON NotaufnahmeManagement.Verschreibungen FROM sklinkel
```

![[Pasted image 20261111095934.png]]

```
ALTER TABLE Aerzte ALTER COLUMN Email SET DEFAULT 'info@fit.de';
```

![[Pasted image 20261111102031.png]]

```
SELECT Patienten.PID, Patienten.Nachname, Patienten.Vorname, COUNT(Verschreibungen.PID) AS Anzahl_Verschreibungen
FROM Patienten
JOIN Verschreibungen ON Patienten.PID = Verschreibungen.PID
GROUP BY Patienten.PID, Patienten.Nachname, Patienten.Vorname
ORDER BY Anzahl_Verschreibungen DESC;
```

![[Pasted image 20261111103427.png]]

```
SELECT AVG(Anzahl_Verschreibungen) AS Durchschnitt_Verschreibungen_pro_Patient
FROM (
SELECT COUNT(Verschreibungen.PID) AS Anzahl_Verschreibungen, Patienten.PID, Patienten.Nachname, Patienten.Vorname)
FROM Patienten
JOIN Verschreibungen ON Patienten.PID = Verschreibungen.PID
GROUP BY Patienten.PID, Patienten.Nachname, Patienten.Vorname
```

