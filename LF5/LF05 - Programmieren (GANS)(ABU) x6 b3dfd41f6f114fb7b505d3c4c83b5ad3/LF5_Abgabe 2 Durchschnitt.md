parent: [[LF05 - Programmieren]]
tags:
aliases: 
Reference:

---
# LF5_Abgabe 2 Durchschnitt

Erstellen Sie ein Skript zur Ermittlung der Gesamtanzahl und der Durchschnittsnote von Klassenarbeiten. Als Datenbasis soll dazu jeweils die Anzahl der einzelnen Noten vom Benutzer eingegeben werden.

```python
note1=float(input("wieviele note 1 gibt es?"));
note2=float(input("wieviele note 2 gibt es?"));
note3=float(input("wieviele note 3 gibt es?"));
note4=float(input("wieviele note 4 gibt es?"));
note5=float(input("wieviele note 5 gibt es?"));
note6=float(input("wieviele note 6 gibt es?"));

summe=(note1*1+note2*2+note3*3+note4*4+note5*5+note6*6);
anzahl=(note1+note2+note3+note4+note5+note6);

durchschnitt = (summe/anzahl);

print(durchschnitt);
```