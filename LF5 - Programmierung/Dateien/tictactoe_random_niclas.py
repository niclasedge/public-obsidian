# ToDo:
# Doppelte eingabe vermeiden - OK
# nach jedem spielerzug einen Test machen - OK

import random

i=0


def ausgabeSpielfeld(spielfeldListe):
    print("-------------")
    print("| "+str(spielfeldListe[0][0])+" | "+str(spielfeldListe[0][1])+" | "+str(spielfeldListe[0][2])+" |")
    print("-------------")
    print("| "+str(spielfeldListe[1][0])+" | "+str(spielfeldListe[1][1])+" | "+str(spielfeldListe[1][2])+" |")
    print("-------------")
    print("| "+str(spielfeldListe[2][0])+" | "+str(spielfeldListe[2][1])+" | "+str(spielfeldListe[2][2])+" |")
    print("-------------")

def ausgabeSpielfeldGuide():
    print("-------Bitte nutzen Sie die korrekte Nummerierung für die Felder------")
    print("-------------")
    print("| [0][0] | [0][1] | [0][2] |")
    print("-------------")
    print("| [1][0] | [1][1] | [1][2] |")
    print("-------------")
    print("| [2][0] | [2][1] | [2][2] |")
    print("-------------")


spielfeld= [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]



for i in range(9): # spielzugnummer
    if (i % 2) ==0:
        try:
            # Züge in die Liste einfügen
            spielerX_1=int(input("Bitte eine Zeile für das X angeben:"))
            spielerX_2=int(input("Bitte eine Spalte für das X angeben:"))
            while True:  # Nach doppelten Feldern scannen
                if spielfeld[spielerX_1][spielerX_2] != " ":
                    print("Das Feld ist schon belegt")
                    print(ausgabeSpielfeldGuide())
                    spielerX_1=int(input("Bitte eine Zeile für das X angeben:"))
                    spielerX_2=int(input("Bitte eine Spalte für das X angeben:"))
                else:
                    spielfeld[spielerX_1][spielerX_2] = "X"
                    break  
            print(ausgabeSpielfeld(spielfeld))
        except ValueError:
            print("Bitte eine Zahl eingeben (0-1-2)")
        # check winner:
        if (spielfeld[0][0] == "X" and spielfeld[1][1] == "X" and spielfeld[2][2] == "X" 
            or spielfeld[0][0] == "X" and spielfeld[1][0] == "X" and spielfeld[2][0] == "X" 
            or spielfeld[0][1] == "X" and spielfeld[1][1] == "X" and spielfeld[2][1] == "X"
            or spielfeld[0][2] == "X" and spielfeld[1][2] == "X" and spielfeld[2][2] == "X"
            or spielfeld[2][0] == "X" and spielfeld[1][1] == "X" and spielfeld[0][2] == "X"
            or spielfeld[0][0] == "X" and spielfeld[0][1] == "X" and spielfeld[0][2] == "X"
            or spielfeld[1][0] == "X" and spielfeld[1][1] == "X" and spielfeld[1][2] == "X"
            or spielfeld[2][0] == "X" and spielfeld[2][1] == "X" and spielfeld[2][2] == "X"
        ):
            print("Spieler X hat gewonnen")
            break
        i+1
    else:
        try:
            # Züge in die Liste einfügen
            while True: # Nach doppelten Feldern scannen
                spielerO_1=random.randint(0,2)
                spielerO_2=random.randint(0,2)
                if spielfeld[spielerO_1][spielerO_2] != " ":
                    spielerO_1=random.randint(0,2)
                    spielerO_2=random.randint(0,2)
                else:
                    spielfeld[spielerO_1][spielerO_2] = "O"
                    break
            print(ausgabeSpielfeld(spielfeld))

        except ValueError:
            print("Bitte eine Zahl eingeben (0-1-2)")

        # check winner:
        if (spielfeld[0][0] == "O" and spielfeld[1][1] == "O" and spielfeld[2][2] == "O" 
            or spielfeld[0][0] == "O" and spielfeld[1][0] == "o" and spielfeld[2][0] == "O" 
            or spielfeld[0][1] == "O" and spielfeld[1][1] == "O" and spielfeld[2][1] == "O"
            or spielfeld[0][2] == "O" and spielfeld[1][2] == "O" and spielfeld[2][2] == "O"
            or spielfeld[2][0] == "O" and spielfeld[1][1] == "O" and spielfeld[0][2] == "o"
            or spielfeld[0][0] == "O" and spielfeld[0][1] == "O" and spielfeld[0][2] == "O"
            or spielfeld[1][0] == "O" and spielfeld[1][1] == "O" and spielfeld[1][2] == "O"
            or spielfeld[2][0] == "O" and spielfeld[2][1] == "O" and spielfeld[2][2] == "O"
        ):
            print("Spieler O hat gewonnen")
            break
        i+1

    if (i==9):
        print("Kein Spielzug mehr möglich - Unentschieden!")


print("Ende")