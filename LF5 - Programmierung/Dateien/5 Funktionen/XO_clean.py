

def ausgabeSpielfeld(spielfeldListe):
    print("-------------")
    print("| "+ str(spielfeldListe[0][0]) +" | "+ str(spielfeldListe[0][1]) +" | "+ str(spielfeldListe[0][2]) +" |")
    print("-------------")
    print("| "+ str(spielfeldListe[1][0]) +" | "+ str(spielfeldListe[1][1]) +" | "+ str(spielfeldListe[1][2]) +" |")
    print("-------------")
    print("| "+ str(spielfeldListe[2][0]) +" | "+ str(spielfeldListe[2][1]) +" | "+ str(spielfeldListe[2][2]) +" |")
    print("-------------")



spielfeld = [
 [" "," "," "],
 [" "," "," "],
 [" "," "," "]
]

isXTurn = True
ende = False
counter = 0

while (not ende and counter < 9):
    ausgabeSpielfeld(spielfeld)

    zeile = input("Zeile: ")
    if (zeile == "ende"):
        break
    spalte = input("Spalte: ")
    if (spalte == "ende"):
        break

if spieler_aktuell == 'O':
        spielzug = int(random.choice(spielfeld_KI))
    else
        spielzug = spieler_eingabe()

    zeile = int(zeile)-1
    spalte = int(spalte)-1

    if (spielfeld[zeile][spalte] == " "):
        if (isXTurn):
            spielfeld[zeile][spalte] = "X"
        else:
            spielfeld[zeile][spalte] = "O"
        isXTurn = not isXTurn
        counter = counter + 1

        if (
            (spielfeld[0][0] != " " and spielfeld[0][0] == spielfeld[0][1] and spielfeld[0][1] == spielfeld[0][2])
            or (spielfeld[1][0] != " " and spielfeld[1][0] == spielfeld[1][1] and spielfeld[1][1] == spielfeld[1][2])
            or (spielfeld[2][0] != " " and spielfeld[2][0] == spielfeld[2][1] and spielfeld[2][1] == spielfeld[2][2])
            or (spielfeld[0][0] != " " and spielfeld[0][0] == spielfeld[1][0] and spielfeld[1][0] == spielfeld[2][0])
            or (spielfeld[0][1] != " " and spielfeld[0][1] == spielfeld[1][1] and spielfeld[1][1] == spielfeld[2][1])
            or (spielfeld[0][2] != " " and spielfeld[0][2] == spielfeld[1][2] and spielfeld[1][2] == spielfeld[2][2])
            or (spielfeld[0][0] != " " and spielfeld[0][0] == spielfeld[1][1] and spielfeld[1][1] == spielfeld[2][2])
            or (spielfeld[0][2] != " " and spielfeld[0][2] == spielfeld[1][1] and spielfeld[1][1] == spielfeld[2][0])
        ):
            if (isXTurn):
                print("Spieler O hat gewonnen")
            else:
                print("Spieler X hat gewonnen")
            break
    else:
        print("Ungültiges Feld")

ausgabeSpielfeld(spielfeld)
print("ENDE")

