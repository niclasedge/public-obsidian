#_________________________Textdateien Aufgabe_________________________#

# Aufgabe a) Datei lesen:
## Schreiben Sie ein Python-Skript, welches den Inhalt der Textdatei „test.txt“ (siehe Moodle- Kurs) auf der Konsole zeilenweise mit Hilfe einer for-Schleife ausgibt (siehe Beispiel).

datei = open('/Users/niclasedge/Documents/OneDrive/_fs13_ausbildung/05 LF05 - Programmierung/8 Textdateien/test.txt','r')
for zeile in datei:
    print(zeile)
datei.close()


# Aufgabe b)
## Bei dem Vergleich des Dateiinhalts mit der Konsolenausgabe sollte Ihnen auffallen, dass zusätzliche Leerzeilen zwischen den Zeilen produziert werden. 
## Dies liegt an den unsichtbaren Steuerzeichen \n an jedem Zeilenende in der Datei. 
## Ändern Sie Ihr Skript so ab, dass diese Steuerzeichen bei der Konsolenausgabe beseitigt werden.

datei = open('/Users/niclasedge/Documents/OneDrive/_fs13_ausbildung/05 LF05 - Programmierung/8 Textdateien/test.txt','r')
for zeile in datei:
    print(zeile[:-3])
datei.close()




# Aufgabe c)
## Kopieren Sie den Inhalt der Datei „test.txt“ in eine neue Textdatei mit beliebigem Namen um. 
## Fügen Sie in der neuen Zieldatei jedoch die Zeilennummer am Zeilenanfang mit ein.
datei1 = open('/Users/niclasedge/Documents/OneDrive/_fs13_ausbildung/05 LF05 - Programmierung/8 Textdateien/test.txt','r')

datei = open('/Users/niclasedge/Documents/OneDrive/_fs13_ausbildung/05 LF05 - Programmierung/8 Textdateien/test3.txt','w')
for zeile in datei1:
    datei.write(zeile)

datei.close()
