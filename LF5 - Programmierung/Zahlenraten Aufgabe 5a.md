parent: [[LF05 - Programmieren]]
tags:
aliases: 
Reference:

---
# Zahlenraten Aufgabe 5a

```jsx
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
```