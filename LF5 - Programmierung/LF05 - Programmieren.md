parent: [[FISI]]
Lehrer: Gans
Raum: 

---
```dataview
list from [[LF05 - Programmieren]]
```
# LF05 - Programmieren (GANS)(ABU) x6


```dataview
table date, status, fazit FROM [[LF05 - Programmieren]]
```




### Python Syntax

- Change between Python 2 and 3 in Anaconda

    ## Anaconda >= 4.1.0

    Since version 4.1.0, anaconda includes a special package `nb_conda_kernels` that detects conda environments with notebook kernels and automatically registers them. This makes using a new python version as easy as creating new conda environments:

    ```
    conda create -n py27 python=2.7 ipykernel
    conda create -n py36 python=3.6 ipykernel
    ```

    After a restart of jupyter notebook, the new kernels are available over the graphical interface. Please note that new packages have to be explicitly installed into the new environments. The [Managing environments](http://conda.pydata.org/docs/using/envs.html) section in conda's docs provides further information.

    ## Manually registering kernels

    Users who do not want to use `nb_conda_kernels` or still use older versions of anaconda can use the following steps to manually register ipython kernels.

    configure the `python2.7` environment:

    ```
    conda create -n py27 python=2.7
    conda activate py27
    conda install notebook ipykernel
    ipython kernel install --user
    ```

    configure the `python3.6` environment:

    ```
    conda create -n py36 python=3.6
    conda activate py36
    conda install notebook ipykernel
    ipython kernel install --user
    ```

    After that you should be able to choose between `python2`and `python3` when creating a new notebook in the interface.

    Additionally you can pass the `--name` and `--display-name` options to `ipython kernel install` if you want to change the names of your kernels. See `ipython kernel install --help` for more informations.

## Neu Programmiersprache → Python

[https://developers.google.com/edu/python/?hl=en](https://developers.google.com/edu/python/?hl=en)

- Aufgabe 1:

    [1021_A1_Eingaben_und Ausgaben.pdf](1021_A1_Eingaben_und_Ausgaben.pdf)

    [1020_INF_Eingaben_und Ausgaben.pdf](1020_INF_Eingaben_und_Ausgaben.pdf)

    ```python
    name = input("Name des Schuelers: ")
    alter = input("Alter des Schuelers: ")

    print(name + " ist ein Schueler am Heinrich-Hertz-Berufskolleg.\nDieses Jahr ist " + name +" " + alter +  " Jahre alt geworden.\n"+name+" Lehrer bringen Ihm dort das Programmieren bei.\nDas hat bisher in "+alter+" Jahren noch niemand geschafft.")
    ```

- Umwandeln von Datentypen: Casten

    →zum Beispiel eine Zahl in text umwandeln: str(123)

    alter = 22

    str(alter)

    int() - ganze Zahlen, ohne rundung

    float() - zahlen mit nachkommastelle

    Modulo= Rest einer Division = %
    Division mit Rest //

in Python 3 Division and Type Conversion: muss mit float werden passieren!

- Aufgabe 2+3:

    [LS03-LF05_Aufgabe2.pdf](LS03-LF05_Aufgabe2.pdf)

    [LF5_Abgabe 2 Durchschnitt](LF5_Abgabe%202%20Durchschnitt.md)

    [LF5_Abgabe 3 Zeitumrechner](LF5_Abgabe%203%20Zeitumrechner.md)

    [Jupyter Notebook](Referenz/Stundenplan+Notizen/Fächer%2069924945113d4f05aa161a69903bf2a7/LF05%20-%20Programmieren%20(GANS)(ABU)%20x6%20b3dfd41f6f114fb7b505d3c4c83b5ad3/Jupyter%20Notebook.md)

# Lernen mit Stichworten:

- Wie nennt man das umwandeln von Datentypen, und welche gibt es?

    →Casten

    str() wandelt in Buchstaben um

    int() wandelt in ganze Zahlen um, ohne zu runden

    float() wandelt in Zahlen mit Kommastellen um

- Was macht der Modulo Operator?

    % = Modulo Operator

    gibt den Restwert aus, der bei einem Teilvorgang übrig bleibt

- Mehrseitige Verzweigung
- Einseitige Verzeigung
- Mehrseitige Verschachtelung

- Aufgabe 2a: Grundlagen Verzweigungen

    var_zahl ist kleiner oder gleich 10 : < =

    var ist ungleich 'T': ! =

    betrag ist größer oder gleich 0: > =

    betrag liegt zwischen 20 und 40: 
    (20 inklusive, 40 exklusive)

    zeichen ist gleich "a" oder "b"

    Negation von: zahl1 > 0 oder zahl2 > 0

    ```jsx
    zahl = int (input ("Gib eine Zahl ein: "));
    is_zahl = zahl % 2 == 0 ;
    if is_zahl:
            zahl = is_zahl ;
            print (" Diese Zahl ist gerade! ");
    else :
            print (" Diese Zahl ist ungerade! ");
    if zahl <= 0 :
        print ("ungültig ")
    else:
        print ("alles okay ")
    ```

- Test fragen:

    Welche 3 regeln hat das Print statement

    Nennen sie alle Cash Typen und die formel

    Welche Art kommt aus einem indoor statement

    Funktioniert: Var +=5?

- Test Block 1

    ![LF05%20-%20Programmieren%20(GANS)(ABU)%20x6%20b3dfd41f6f114fb7b505d3c4c83b5ad3/3C89AEF7-3E93-4FFB-B951-E6904D750ABB.jpeg](3C89AEF7-3E93-4FFB-B951-E6904D750ABB.jpeg)

    ![LF05%20-%20Programmieren%20(GANS)(ABU)%20x6%20b3dfd41f6f114fb7b505d3c4c83b5ad3/9ED6AFB2-22F4-4697-BA24-985FACD73392.jpeg](9ED6AFB2-22F4-4697-BA24-985FACD73392.jpeg)

    ![LF05%20-%20Programmieren%20(GANS)(ABU)%20x6%20b3dfd41f6f114fb7b505d3c4c83b5ad3/9D55F67B-C7DE-46C9-91FC-46FF6E4B2C81.jpeg](9D55F67B-C7DE-46C9-91FC-46FF6E4B2C81.jpeg)

    ![LF05%20-%20Programmieren%20(GANS)(ABU)%20x6%20b3dfd41f6f114fb7b505d3c4c83b5ad3/412BEBF3-DDD2-4735-BB2B-149D674EE6B5.jpeg](412BEBF3-DDD2-4735-BB2B-149D674EE6B5.jpeg)

    ![LF05%20-%20Programmieren%20(GANS)(ABU)%20x6%20b3dfd41f6f114fb7b505d3c4c83b5ad3/B7A1CCBC-76C3-4985-93CB-57D21DF806EF.jpeg](B7A1CCBC-76C3-4985-93CB-57D21DF806EF.jpeg)

# Block 2

- Zahlenraten

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

[Zahlenraten Aufgabe 5a](Zahlenraten%20Aufgabe%205a.md)