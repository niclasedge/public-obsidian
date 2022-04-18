'''Aufgabe 5b – Umgekehrtes Zahlenraten
Der Benutzer des Programmes soll sich eine ganze Zahl zwischen 0 und 100 ausdenken.
Alsdann soll der Computer versuchen, diese Zahl mit möglichst wenig Schritten zu
erraten, indem er eine ganze Zahl zwischen 0 und 100 ausgibt. Nach jeder Ausgabe des
Computers muss der Benutzer eingeben, ob die eingegebene Zahl größer oder kleiner als
die ausgedachte Zahl oder der ausgewählten Zahl gleich ist. Solange die ausgegebene
Zahl der ausgedachten Zahl nicht gleich ist, soll die Ausgabe wiederholt werden.'''


import random
print ("Das Spiel: Der Cumputer errät Deine Zahl!")

a=1
b=10
count = 0 #Versuchszähler
zahl = 50  #Die ausgangszahl für den Computer
randominteger = random.randint(1,100)
inp= ""


while inp != randominteger: #Die schleife läuft solange der Wert nicht gleich "=" ist
    print("Wir suchen: "+str(randominteger))
    print("Der computer versucht zu erraten und kommt auf: "+str(zahl)) #Das wird vor jeder ABfrage gedruckt
    inp = input("Bitte +/- oder = angeben: ") #Die Abfrage
    print ("")
    


    if inp.lower() == "ende": #wenn "ende" eingegeben wird, beendet das spiel vorzeitig
        print ("Das Spiel wird beendet.")
        input("Beliebige Taste drücken.")
        exit()

    elif inp == "+": # Wenn "+" eingegeben wird
        print ("Es war nicht: "+str(zahl)+" Deine Zahl ist größer.")
        print ("")
        randomguess = random.randint(a,b)
        zahl +=randomguess #Es wird 1 zur zahl addiert
        count += 1 #Es wird 1 zum Versuchszähler addiert

    elif inp =="-": #Wenn "-" eingegeben wird
        print ("Es war nicht: "+str(zahl)+" Deine Zahl ist kleiner.")
        print ("")
        randomguess = random.randint(a,b)
        zahl -=randomguess #Es wird 1 von der zahl subtrahiert
        count += 1 #Es wird 1 zum Versuchszähler addiert

    elif inp == "=": #Wenn "=" eingegeben wird wird die finale Aussage gedruckt
        break


print (">>>Es war die Zahl: "+str(zahl)) #Finale Aussage
print ("")
print ("Wir haben " + str(count) + " Versuche benötigt.")