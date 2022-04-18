parent: [[LF05 - Programmieren]]
tags:
aliases: 
Reference:

---
# LF5_Abgabe 3 Zeitumrechner

**a) Aus einer vom Benutzer eingegebenen Minutenanzahl soll der ganzzahlige Anteil in Stunden und die Restminuten berechnet und ausgegeben werden.**

```python
zahl=input("Geben sie eine minutenzahl ein:")

stunden=int(float(zahl)/60);
print("stunden: "+str(stunden))
minuten=(float(zahl)%60);
print("minuten: "+str(minuten))

restzeit=(str(stunden)+","+str(minuten))
print("restzeit: "+str(restzeit))
```

**b) Erweitern Sie das Skript aus Aufgabenteil a) so, dass Jahre, Tage, Stunden und Restminuten berechnet und ausgegeben werden. Gehen Sie davon aus, dass ein Jahr 365 Tage hat.**

```python
zahl=input("Geben sie eine Minutenzahl ein:")

minuten=(float(zahl)%60);
stunden=(int(float(zahl)/60)%24);
tage=(int(float(zahl)/1440)%31);
monate=(int(float(zahl)/43805)%12);
jahre=int(float(zahl)/525600);

minutenzujahr=("Jahr:"+str(jahre)+", "+"Monate:"+str(monate)+", "+"Tage: "+str(tage)+", "
               +"Stunden:"+str(stunden)+", "+"Minuten:"+str(minuten));
print(minutenzujahr);
```