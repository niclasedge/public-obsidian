'''for - Schleife
Der zweite Schleifentyp ist die sog. for-Schleife. Die Syntax ist etwas komplexer als die der while-
Schleife und sieht wie folgt aus:
for Variable in Sequenz:
    Anweisung1
    Anweisung2
    ...

Die for-Syntax hat einen unterschiedlichen Charakter zu den for-Schleifen, die man aus den
meisten anderen Programmiersprachen kennt. In Python dient die sie zur Iteration über eine
Sequenz von Objekten, während sie in anderen Sprachen meist nur "eine etwas andere while-Schleife"
ist.

range()-Funktion
Mit Hilfe der range()-Funktion lässt sich ein Bereich angeben, welcher für die for-Schleife
zur Iterationen genutzt werden kann. Die Syntax von range()lautet:

range(endwert) -
Liefert einen Bereich von 0 bis zum angegebenen Endwert mit einer Erhöhung (Schrittweite von 1).
Das folgende Beispiel gibt die ganzen Zahlen von 1 bis 9 auf der Konsole aus.
for i in range(10):
    print(i)
    
range(startwert, endwert) -
Liefert einen Bereich vom angegebenen Startwert bis zum Endwert mit einer Schrittweite (Erhöhung) von 1.
Das folgende Beispiel gibt die ganzen Zahlen von 10 bis 19 auf der Konsole aus.
for i in range(10, 20):
    print(i)
    
range(startwert, endwert, schrittweite) -
Liefert einen Bereich vom angegebenen Startwert bis zum Endwert mit einer angegebenen Schrittweite (Erhöhung),
welche auch größer als 1 sein kann. Das folgende Beispiel gibt die Zahlen 10 und 15 auf der Konsole aus.
for i in range(10, 20, 5):
    print(i)'''


'''Übung 6a:
Welche Ausgaben werden durch die folgenden Programmfragmente erzeugt?

for i in range(4, 24, 4):
    print(i // 4)
= 1 2 3 4 5
   
for i in range(10,0):
     print(i)
=keine ausgabe

for i in range(33, 21, -3):
    print(i)

j=1
for i in range(0,10):
    print(j)
    j = j*2
1
2
4
8
16
32
64
128
256
512

j=1
for i in range(0,11):
    j = j*i
    print(j)


j=1
for i in range(1,11):
    j = j*i
    print(j)
'''

j=1

for i in range(6)
    print("X"*j)
    j+=1