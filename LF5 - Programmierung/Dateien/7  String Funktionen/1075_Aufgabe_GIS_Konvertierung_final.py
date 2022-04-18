count=1
eingabedatei=input('Bitte geben Sie den Dateipfad an:')
#eingabedatei='/Users/niclasedge/Documents/OneDrive/_fs13_ausbildung/05 LF05 - Programmierung/7  String Funktionen/source.txt'
datei = open(eingabedatei,'r')
ausgabedatei=eingabedatei.replace('txt','csv')
ausgabedatei=open(ausgabedatei,'w')

for zeile in datei:
    if zeile != '\n':
        zeile=str(count)+" "+zeile
        zeile=zeile.replace('IP','')
        zeile=zeile.replace('AR','')
        zeile=zeile[0:-19]
        zeile_mit_komma=zeile.replace(' ', ';')
        zeile_mit_komma=zeile_mit_komma.rstrip(';')+'\n'
        ausgabedatei.write(zeile_mit_komma)
        count+=1
        print(str(count)+"\t"+zeile_mit_komma)
datei.close()