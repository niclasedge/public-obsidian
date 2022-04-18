'''## Übung IP-Ping-Tool
Der HHBK-NetAdmin benötigt ein Tool, mit dem er die erreichbaren IP-Adressen eines Netzwerks
ermitteln kann. Mit seinen rudimentären Python-Kenntnissen hat er folgende Codezeilen
geschrieben, mit denen er die ersten paar IP-Adressen anpingen kann.

import subprocess
response = subprocess.call("ping -n 1 -w 5 192.168.111.1", stdout=subprocess.DEVNULL) 
if response == 0:
    print(">>> 192.168.111.1 ist erreichbar.") 
else:
    print(">>> 192.168.111.1 ist NICHT erreichbar.")
response = subprocess.call("ping -n 1 -w 5 192.168.111.2", stdout=subprocess.DEVNULL) 
if response == 0:
    print(">>> 192.168.111.2 ist erreichbar.") 
else:
    print(">>> 192.168.111.2 ist NICHT erreichbar.")
response = subprocess.call("ping -n 1 -w 5 192.168.111.3", stdout=subprocess.DEVNULL) 
if response == 0:
    print(">>> 192.168.111.3 ist erreichbar.") 
else:
    print(">>> 192.168.111.3 ist NICHT erreichbar.")
response = subprocess.call("ping -n 1 -w 5 192.168.111.4", stdout=subprocess.DEVNULL) 
if response == 0:
    print(">>> 192.168.111.4 ist erreichbar.") 
else:
    print(">>> 192.168.111.4 ist NICHT erreichbar.")'''

'''Aufgabe
Schreiben Sie das gewünschte Ping-Tool als Python-Skript mit Hilfe einer while-Schleife so,
dass alle IP-Adressen mit den Endungen von 1 bis 255 angepingt werden.
Erweitern Sie das Skript in einem nächsten Schritt um die Möglichkeit die
Netzwerkbasisadresse (z.B. 192.168.111.) vom Benutzer einlesen zu lassen.
Fügen Sie die Möglichkeit zur Abfrage eines IP-Adressbereichs hinzu, wobei
Start- und Endadresse vom Benutzer festgelegt werden.'''

'''import subprocess
s = int(input"Startadresse: ")
e = int(input"Ende:")
basis = input()
#basis="192.168.111."

while s <= e
    response = subprocess.call("ping -n 1 -w 5 "+basis+str(n), stdout=subprocess.DEVNULL) 
        if response == 0:
            print(">>> "+basis+str(n)+" ist erreichbar.") 
        else:
            print(">>> "+basis+str(n)+" ist NICHT erreichbar.")
        s+=1'''


        

import random

print ("Willkommen zum IP finden!")

randominteger = random.randint(1,255)

count = 1
inp = 0
ip="102.168.111."

while inp <= randominteger:
    print (ip+str(inp))s
    inp+=1
    


print ("Die IP "+ip+str(randominteger)+" ist aktiv")
print ("")
print ("Du hast " + str(count) + " Versuche benötigt.")
