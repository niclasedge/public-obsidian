'''Aufgabe 5 - Zahlenraten
Schreiben Sie ein Programm, bei dem der Benutzer eine zufällig generierte Zahl erraten soll.
Anforderungen:
• Beim Starten des Spiels kann der Benutzer eine Zahl als Obergrenze festlegen (z.B. 100).
• Die Anzahl der Rateversuche wird vom Programm mitgezählt und zum Schluss ausgegeben.
• Bei einem falschen Rateversuch wird ausgegeben, ob die gesuchte Zahl größer oder kleiner
ist als die letzte eingegebene Zahl.
• Die Programmausführung wird beendet, sobald der Benutzer die richtige Zahl erraten oder
„ende“ eingegeben hat.

Hinweis: Zufallszahlen generieren
Um eine Zufallszahl in Python zu generieren gibt es die random-Funktionen.
Um diese nutzen zu können, müssen Sie am Anfang Ihres Programms die Zeile
import random einfügen. Das folgende Beispiel zeigt, wie zufällige ganze Zahlen zwischen
1 und 20 generiert werden.
Beispiel:
import random
zufallszahl = random.randint(1,20)
print(zufallszahl)'''


import random
import time

print ("Willkommen zum Zahlraten!")
x = int(input(("Bitte Obergrenze für Zahl zum Raten eingeben: ")))

randominteger = random.randint(1,x)

count = 1

inp = 0

while inp != randominteger:

    inp = input("Bitte Zahl raten: ")
    print ("")
    time.sleep(0.5)

    if inp.lower() == "ende":
        print ("Das Spiel wird beendet.")
        input("Beliebige Taste drücken.")
        exit()
    elif int(inp) > x:
        print("Zahl ist über der Obergrenze")

    elif int(inp) > randominteger:
        print ("Das war falsch! Die gesuchte Zahl ist kleiner.")
        print ("")
        count += 1

    elif int(inp) < randominteger:
        print ("Das war falsch! Die gesuchte Zahl ist größer.")
        print ("")
        count += 1

    elif int(inp) == randominteger:
        break


print ("Das war die richtige Zahl!")
print ("")
print ("Du hast " + str(count) + " Versuche benötigt.")