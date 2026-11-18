
[Kurs: IT25-LF-WiPo-GadeT | Moodle BBZ RD-ECK](https://moodle.bbz-rd-eck.de/course/view.php?id=1995#module-52116)

![[Pasted image 20261118095310.png]]

Ideen: Ticketsystem, Nutzer & Berechtigungssystem

**Vorbereitung für ein IT-Ticketsystem**

Problembeschreibung:
Unsere IT Abteilung bekommt derzeit alle Tickets über Mail, sodass viele Anliegen untergehen und nicht gut bearbeitet werden können.
Dementsprechend soll ein zentrales IT-Ticket Portal dort Abhilfe schaffen.

Wer: Mitarbeiter und IT-ler

| ticket            |
| ----------------- |
| **ticket_id**     |
| type              |
| caller            |
| category          |
| state             |
| priority          |
| assigned_user     |
| short_information |
| information       |

| user    |
| ------- |
| user_id |
| role    |
| contact |


---
Tabellen mit Datensätzen:

| type     |
| -------- |
| incident |
| request  |

| category    |
| ----------- |
| hardware    |
| software    |
| network     |
| permissions |

| state       |
| ----------- |
| in progress |
| on hold     |
| new         |
| closed      |

| priority |
| -------- |
| high     |
| middle   |
| low      |
| critical |

| roles    |
| -------- |
| customer |
| admin    |

| caller  |
| ------- |
| user_id |

| assigned_user |
| ------------- |
| user_id       |



![[Pasted image 20261118103828.png]]

1. String, Integer
2. überwiegend atomar
3. immer 1:n
4. user_id, ticket_id
5. alles muss eingegeben werden außer die ID
6. Mittels IDs
7. Ja, Customer und Admin
8. ja

![[Pasted image 20261118104446.png]]

siehe oben (relationales Datenmodell)

