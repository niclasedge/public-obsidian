parent: [[LF05 - Programmieren]]
tags:
aliases: 
Reference:

---
# Jupyter Notebook

# Intro to Python 3

## Austauschen von Namen und Alter mit Hilfe von Variablen

```python
name = "tim";
alter = "22";
print(name + " ist ein Schueler am Heinrich-Hertz-Berufskolleg.");
print("Dieses Jahr ist " + name +" " + alter +  " Jahre alt geworden.");
print(name+" Lehrer bringen Ihm dort das Programmieren bei.");
print("Das hat bisher in "+alter+" Jahren noch niemand geschafft.");

```

```
tim ist ein Schueler am Heinrich-Hertz-Berufskolleg.
Dieses Jahr ist tim 22 Jahre alt geworden.
tim Lehrer bringen Ihm dort das Programmieren bei.
Das hat bisher in 22 Jahren noch niemand geschafft.

```

### Aufforderung vom User zur Eingabe von Namen und Alter

```python
name = input("Name des Schuelers: ");
alter = input("Alter des Schuelers: ");
print(name + " ist ein Schueler am Heinrich-Hertz-Berufskolleg.");
print("Dieses Jahr ist " + name +" " + alter +  " Jahre alt geworden.");
print(name+" Lehrer bringen Ihm dort das Programmieren bei.");
print("Das hat bisher in "+alter+" Jahren noch niemand geschafft.");

```

```
Name des Schuelers: tim
Alter des Schuelers: 22
tim ist ein Schueler am Heinrich-Hertz-Berufskolleg.
Dieses Jahr ist tim 22 Jahre alt geworden.
tim Lehrer bringen Ihm dort das Programmieren bei.
Das hat bisher in 22 Jahren noch niemand geschafft.

```

# Übung 1a

Testen verschiedener Befehle in Python

```python
zahl = 123 print(zahl)

```

```
  File "<ipython-input-3-a47a27673ce6>", line 1
    zahl = 123 print(zahl)
                   ^
SyntaxError: invalid syntax

```

```python
zahl = 123; print(zahl);
```

```
123
```

```python
;;
```

```
---------------------------------------------------------------------------

TypeError                                 Traceback (most recent call last)

<ipython-input-5-72f854f54d1b> in <module>
----> 1 ("")("")

TypeError: 'str' object is not callable
```

```
();();

```

```
_ = 123

```

```
1steZahl = 123

```

```
  File "<ipython-input-8-98c0fd4df1d4>", line 1
    1steZahl = 123
           ^
SyntaxError: invalid syntax

```

```
_2teZahl = "123";
print(_2teZahl)

```

```
123

```

```
var = ((()))
print(var)

```

```
()

```

```
var = ("") + ("")
print(var)

```

leere zuweisung, aber gültig

```
int(zahl = 1)

```

```
---------------------------------------------------------------------------

TypeError                                 Traceback (most recent call last)

<ipython-input-16-7d1ab2d12c7b> in <module>
----> 1 int(zahl = 1)

TypeError: 'zahl' is an invalid keyword argument for this function

```

```
zahl = str(float(int("123")*0.5))
print(zahl)

```

```
61.5

```

```
s = 2 + "" + 1;
print(s)

```

```
---------------------------------------------------------------------------

TypeError                                 Traceback (most recent call last)

<ipython-input-1-576f291982ca> in <module>
----> 1 s = 2 + "" + 1;
      2 print(s)

TypeError: unsupported operand type(s) for +: 'int' and 'str'

```

# Übung 1b

```python
a=4
b=10
d=2.5 
e=b*d 
f=b/4 
g=b%3
a+=1
b*=1
print(a);
print(b);
print(d);
print(e);
print(f);
print(g);
```

```
5
10
2.5
25.0
2.5
1
```

## Aufgabe 2

Erstellen Sie ein Skript zur Ermittlung der Gesamtanzahl und der Durchschnittsnote von Klassenarbeiten. Als Datenbasis soll dazu jeweuls die Anzahl der einzelnen Noten vom Benutzer eingegeben werden.

```
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

```
wieviele note 1 gibt es?2
wieviele note 2 gibt es?2
wieviele note 3 gibt es?2
wieviele note 4 gibt es?2
wieviele note 5 gibt es?2
wieviele note 6 gibt es?2
3.5
```

## Aufgabe 3

**a) Aus einer vom Benutzer eingegebenen Minutenanzahl soll der ganzzahlige Anteil in Stunden und die Restminuten berechnet und ausgegeben werden.**

```python
zahl=input("Geben sie eine minutenzahl ein: ")

stunden=int(float(zahl)/60);
print("Stunden: "+str(stunden))
minuten=(float(zahl)%60);
print("minuten: "+str(minuten))

restzeit=("Stunden: "+str(stunden)+", "+"Minuten: "+str(int(minuten)))
print("restzeit= "+str(restzeit))
```

```
Geben sie eine minutenzahl ein: 8232
Stunden: 137
minuten: 12.0
restzeit: Stunden: 137, Minuten: 12
```

**b) Erweitern Sie das Skript aus Aufgabenteil a) so, dass Jahre, Tage, Stunden und Restminuten berechnet und ausgegeben werden. Gehen Sie davon aus, dass ein Jahr 365 Tage hat.**

```python
zahl=input("Geben sie eine Minutenzahl ein:")

minuten=int(float(zahl)%60);
stunden=(int(float(zahl)/60)%24);
tage=(int(float(zahl)/1440)%31);
monate=(int(float(zahl)/43805)%12);
jahre=int(float(zahl)/525600);

minutenzujahr=("Jahr:"+str(jahre)+", "+"Monate: "+str(monate)+", "+"Tage: "+str(tage)+", "
               +"Stunden:"+str(stunden)+", "+"Minuten:"+str(minuten));
print(minutenzujahr);
```

```
Geben sie eine Minutenzahl ein:823782382
Jahr:1567, Monate:1, Tage: 28, Stunden:2, Minuten:22

```

# Verzweigung

### Einseitige Auswahl (Einseitige Verzweigung)

Bei einer einseitigen Auswahl wird ein Anweisungsblock in Abhängigkeit einer Bedingung ausgeführt. Die einseitige Auswahl ist dadurch gekennzeichnet, dass nach einer Bedingungsabfrage durch einen Ausdruck eine Anweisung oder ein Anweisungsblock ausgeführt wird oder nicht.

```python
is_male = True
if is_male:
    print("Du bist ein Mann.")
```

```
Du bist ein Mann.
```

```python
is_male = True
if is_male:
    print("ist ein mann")
else:
    print("ist kein mann")
```

```
ist ein mann

```

## Vergleichsoperatoren

```
# == ist Gleich
eingabe = input("Bist Du ein Mann? ")
if eingabe == "ja":
    print("Du bist ein Mann!")

```

```
Bist Du ein Mann? ja
Du bist ein Mann.

```

```
# != ist ungleich
eingabe = input("Bist Du ein Mann? ")
if eingabe != "ja":
    print("Du bist kein Mann.")

```

```
  File "<ipython-input-14-224f6bb92d81>", line 3
    print("Du bist ein Mann.")
    ^
IndentationError: unexpected indent

```

```
# > größer als
vermögen = int(input("Wie viel Geld besitzt Du? "))
if vermögen > 999999:
    print("Du bist Millionär!")

```

```
Wie viel Geld besitzt Du? 1000000
Du bist Millionär!

```

```
# < keliner als
vermögen = int(input("Wie viel Geld besitzt Du? "))
if vermögen < 1000000:
    print("Du bist kein Millionär!")

```

```
Wie viel Geld besitzt Du? 91
Du bist kein Millionär!

```

```
# >= größer als oder gleich
vermögen = int(input("Wie viel Geld besitzt Du? "))
if vermögen >= 1000000: 
        print("Du bist Millionär!")

```

```
Wie viel Geld besitzt Du? 011

```

# Übung 2a

```
var_zahl=9
var="g"
betrag=41
zeichen="a"
zahl1=-1
zahl2=-2

if var_zahl<=10:
    print("kleiner oder gleich 10");
if var != "T":
    print("ungleich 'T")
if betrag >=0:
    print("betrag ist größer oder gleich 0")
if betrag >=20 or betrag <=40:
    print("betrag liegt zwischen 20 und 40")
if zeichen == "a" or zeichen=="b":
    print("zeichen ist gleich a oder B")
if zahl1<0 or zahl2<0:
    print("negative zahl")

```

```
kleiner oder gleich 10
ungleich 'T
betrag ist größer oder gleich 0
betrag liegt zwischen 20 und 40
zeichen ist gleich a oder B
negative zahl

```

# Übung 2b - (Un)Gerade Zahl

Pgrogramm zum testen auf ungrade Zahl

```
zahl = int (input ("Gib eine Zahl ein: "))
is_zahl = zahl % 2 == 0 
if is_zahl:
        zahl = is_zahl ;
        print (" Diese Zahl ist gerade! ")
else :
        print (" Diese Zahl ist ungerade! ")
if zahl <= 0 :
    print ("ungültig ")
else:
    print ("alles okay ")

```

```
Gib eine Zahl ein: 2
 Diese Zahl ist gerade! 
alles okay 

```

## Mehrseitige Auswahl (mehrseitige Verzweigung):

elif = else if
für alternative Schreibweisen

Bei einer mehrseitigen Auswahl werden mehr als zwei mögliche Anweisungsblöcke in Abhängigkeit von einer Bedingung ausgewertet, wobei davon genau nur ein Anweisungsblock ausgeführt wird.

```
eingabe = input("Ist heute Montag: ")
if eingabe == "ja": 
    print("Heute ist Montag.")
elif eingabe == "Ja": 
    print("Heute ist Montag.")
elif eingabe == "JA": 
    print("Heute ist Montag.")
elif eingabe == "jA": 
    print("Heute ist Montag.")
else:
    print("Heute ist nicht Montag")

```

```
Ist heute Montag: ja
Heute ist Montag.

```

## Mehrstufige Auswahl

Bei einer mehrstufigen Auswahl wird einer von mehreren Anweisungsblöcken in Abhängigkeit von einer oder mehreren Bedingungen ausgeführt. Sie können die mehrstufige Auswahl verwenden, wenn es mehr als zwei Auswahlmöglichkeiten gibt. Die Bedingungen müssen nicht voneinander abhängen.

```
eingabe = input("Ist heute Montag: ") 
eingabe2 = input("Ist es sonnig: ")
if eingabe == "ja":
    if eingabe2 == "ja":
        print("Heute ist ein sonniger Montag.") 
    else:
        print("Heute ist ein grauer Montag.") 
else:
    print("Heute ist nicht Montag") 
    if (eingabe2 == "ja"):
        print("Es ist sonnig.") 
    else:
        print("Es ist nicht sonnig")

```

```
Ist heute Montag: ja
Ist es sonnig: nein
Heute ist ein grauer Montag.

```

### Logische Operatoren

OR AND , alternative zu elif
Logische Operatoren haben grundsätzlich die Funktion, boolesche Bedingungen zu verknüpfen. Es existieren 2 logische Operatoren: and und or.

```
eingabe = input("Ist heute Montag: ")
if eingabe == "ja" or eingabe == "Ja" or eingabe == "JA" or eingabe == "jA": 
    print("Heute ist Montag.")
else:
    print("Heute ist nicht Montag")

```

```
Ist heute Montag: ja
Heute ist Montag.

```

```
eingabe = input("Ist heute Montag: ")
if eingabe != "ja" and eingabe != "Ja" and eingabe != "JA" and eingabe != "jA": 
    print("Heute ist nicht Montag.")
else:
    print("Heute ist Montag")

```

```
Ist heute Montag: ja
Heute ist Montag

```

# Übung 3a

```
a= 2
b= 3
c= 2
d = a< b 
print(d) 
print(a <= c) 
print(a == b) 
print(a == c) 
print(b != c) 
if(a > c):
    print("Hey!") 
if(a >= c):
    print("Hi!")
```

```
True
True
False
True
True
Hi!

```

```
print(False and False)
print(False and True)
print(True and False)
print(True and True)

```

```
False
False
False
True

```

```
print(False or False)
print(False or True)
print(True or False)
print(True or True)

```

```
False
True
True
True

```

```
print(not True)
print(not False)
print(not not True)

```

```
False
True
True

```

```
print(2 < 3 or 1 > 0)
print(2 > 3 and 4 <= 4 or 1 > 0)

```

```
True
True

```

# 3b Taschenrechner

mit loop

```
while True:
    zahl1 = input("Zahl 1: ")
    vorgang = input("Rechenvorgang: ") 
    zahl2 = input("Zahl 2:")

    zahl1=int(zahl1)
    zahl2=int(zahl2)

    if(vorgang=="+"):
        print("Deine Rechnung", zahl1,"+", zahl2)
        print("Ergebnis=", zahl1+zahl2)
    elif(vorgang=="-"):
        print("Deine Rechnung", zahl1,"-", zahl2)
        print("Ergebnis=", zahl1-zahl2)
    elif(vorgang=="/"):
        print("Deine Rechnung", zahl1,"/", zahl2)
        print("Ergebnis=", zahl1/zahl2)
    elif(vorgang=="*"):
        print("Deine Rechnung", zahl1,"*", zahl2)
        print("Ergebnis=", zahl1*zahl2)
    else:
        print("ungültiges Ergebnis")
        
    jein=input("willst Du weiterrechnen? (Ja/Nein)")
    jein=str("jein")
    
    if jein=="Nein" or jein=="nein":
        print("tschüs")
        
        break
    

```

```
Zahl 1: 4
Rechenvorgang: +
Zahl 2:6
Deine Rechnung 4 + 6
Ergebnis= 10
willst Du weiterrechnen? (Ja/Nein)Nein

```

### mit ergebniswert weiterrechnen

```
while True:
    zahl1 = input("Zahl 1: ")
    vorgang = input("Rechenvorgang: ") 
    zahl2 = input("Zahl 2:")

    zahl1=int(zahl1)
    zahl2=int(zahl2)

    if(vorgang=="+"):
        print("Deine Rechnung", zahl1,"+", zahl2)
        print("Ergebnis=", zahl1+zahl2)
    elif(vorgang=="-"):
        print("Deine Rechnung", zahl1,"-", zahl2)
        print("Ergebnis=", zahl1-zahl2)
    elif(vorgang=="/"):
        print("Deine Rechnung", zahl1,"/", zahl2)
        print("Ergebnis=", zahl1/zahl2)
    elif(vorgang=="*"):
        print("Deine Rechnung", zahl1,"*", zahl2)
        print("Ergebnis=", zahl1*zahl2)
    else:
        print("ungültiges Ergebnis")
        
    jein=input("willst Du weiterrechnen? (Ja/Nein)")
    jein=str("jein")
    
    if jein=="Nein" or jein=="nein":
        print("tschüs")
        
        break

```

# 3c Hundejahre

Kinder und Hundeliebhaber stellen sich häufig die Frage, wie alt ihr Hund wohl wäre, wenn er kein Hund, sondern ein Mensch wäre. Landläufig rechnet man Hundejahre in Menschjahre um, indem man das Alter des Hundes mit 7 multipliziert. Je nach Hundegröße und Rasse sieht die

Umrechnung jedoch etwas komplizierter aus, z.B.:

- Ein einjähriger Hund entspricht in etwa einem 14-jährigen Menschen
- 2 Jahre eines Hundes entsprechen 22 Jahre eines Menschen.
- Ab dann entspricht ein Hundejahr jeweils 5 Menschenjahren.

Schreibe Sie ein Python-Programm, welches die Eingabe für das Alter eines Hundes verlangt und nach obiger Regel das Hundealter in Menschenjahren berechnet.

```
try:
    hundealter = input("Hundealter: ")

    if (int(hundealter) == 1):
        print("Der Hund ist 14 Menschenjahre alt")
    elif (int(hundealter) == 2):
        print("Der Hund ist 22 Menschenjahre alt")
    elif (int(hundealter) >= 3):
        hundealter=(((int(hundealter)-2)*5)+22)
        print("Der Hund ist ",hundealter,"Menschenjahre alt")
except ValueError:
    print("Dies ist keine Zahl..")

```

```
Hundealter: 6
Der Hund ist  42 Menschenjahre alt

```

# Aufgabe 4 Fussball Jahreszahl ermitteln

Schreiben Sie ein Skript, welches bei Eingabe einer Jahreszahl ermittelt, ob in diesem Jahr eine Europa- oder Weltmeisterschaft in Fußball stattfand bzw. stattgefunden hat.

- Europameisterschaften finden seit 1958 in allen Jahren statt, deren Jahreszahl sich ganzzahlig durch 4 teilen lassen (z.B. 2008; 2012; ..).
- Um 2 Jahre versetzt findet alle vier Jahre die Fußball-Weltmeisterschaft statt (seit 1930).
- Berücksichtigen Sie, dass die EM 2020 auf das Jahr 2021 verschoben wurde.

```
jahr = int(input("Geben Sie eine Jahreszahl ein: "))

if jahr%4 == 0 and jahr >= 1958 and jahr != 2020:
    print("EM Jahr")
elif jahr%4 == 2 and jahr >= 1930:
    print("WM Jahr")
elif jahr == 2020:
    print("Die EM2020 wurde aus Coronagründen auf 2021 verschoben")
elif jahr == 2021:
    print("Die EM 2020 wurde aus Coronagründen auf dieses Jahr verschoben")

else:
    print("keine EM oder WM in diesem Jahr")

```

```
Geben Sie eine Jahreszahl ein: 2021
Die EM 2020 wurde aus Coronagründen auf dieses Jahr verschoben

```

```

```