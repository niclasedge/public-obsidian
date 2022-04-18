parent: [[FISI]]
Lehrer: Seib, Pukr
Raum: 

---
```dataview
table Lehrer, Raum, fazit FROM [[LF07 - Cyber-physische Systeme ergänzen]]
```
---

### todo

### Fertig
- Grafik fertig machen 
- Präsentation am 5.10. abgeben


https://lernportal.hhbk.de/course/view.php?id=1494

[[LF07 -- Infos]]




### Verkabelung in Serverraum
- Unter Boden, mit abnehmbaren Boden
- Kabelkanal an der Wand
- Öggnung im Boden

## [[LF07 -- Kundenprojekt IT-Solutions & Strategy (ITSS)]]

## Abgabe Pflichtenheft:
![[Pflichtenheft - Wittekind GmbH_Bayro, Edge, Patzer.docx]]


# Jahr 2 Block 2

## Sensoren und Aktoren

           

1. Sensoren können nach Bauweise und Funktion eingeteilt werden. Im Folgenden werden einige Sensorarten aufgezählt.

### Induktive Sensoren
- arbeiten berührungslos
- Der dahinter befindente Oszylator erzeugt mittels Schwingkreis ein magnetisches Wechselfeld, das aus der aktiven Fläche des Sensors austritt.
- Einsatz
	- Messung von Abständen
	- Messung von Bandmitten
	- Messung von Breiten / Dicken
	- Erkennung von Welligkeit der Oberfläche
	- Positionskontrolle und AUsrichtung

### Kapazitive Sensoren
- Funktion beruht auf der Änderung des elektrischen Feldes in der Umgebung vor seiner Sensorelektrode (aktive Zone).
- Es wird die Kapazität zwischen der aktiven Elektrode und derm elektrischen Erdpotenzial gemessen
- Hohe Signalstabilität und Auflösung
- Einsatz:
	- Wegmessung
	- Abstandsmessung
	- Positionsmessaufgaben
	- Dickenmessung


### Optische Sensoren/Lasersensoren
- Über eine Lichtquelle sendet ein optisxher Sensor einen (sichtbaren oder infraroten) Lichtstrahl aus
- Zu unterscheiden sind dabei Reflexionstypen bzw. Lichttaster oder Lichtschranken.
- Reflexionstyp
	- wird eingesetzt um von einem Zielobjekt reflektierten Lichtstrah zu erfassen
- Lichtschrankentyp
	- detektiert eine Unterbrechnung der Lichtachse zwischen baugleich getrenntem Sender und Empfänger

### Magnetsensoren
- berührungslose schaltende Sensor
- erfassung von Magneten und ferromagnetischen Objeklten
- Erkennt im welchen Winkel das äußere Magnetfeld zum Sensor steht
- Einsatz:
	- Weg und Winkelmessung
	- Bestimmung magnetischer Felder
	- Hochdynamische Strommessung

### Ultraschall Sensoren           
- Sind in der Lage Objekte berüphrungslos zu erkennen
- Unabhängig von Licht, Farbe, Staub, Rauch, Material
- entfernung zu messen
- Sensor strahlt zyklisch einen Schallimpult aus 
- Einsatz:
	- Wird häufig in der Industrie genutzt, da sie millimetergenaue Messungen erlauben
	- Kann ohne Problem im Innen und Außen bereich eingesetzt werden


## Rasperry Pi
![[Erste Schritte mit dem Raspberry Pi.pdf]]


### Aufgabe 1: 
Betrachten Sie nun die Abbildung und beschreiben Sie welche GPI- Os der Raspberry Pi besitzt. Beachten Sie dabei auch die Farbge- bung der unterschiedlichen Ein- und Ausg ̈ange und beschreiben Sie ihre Funktion.

Schwarz: Erdung
Grün: Input/Output
Rot: 5 Volt Strom
Organge: 3,5Volt Strom
Serielle Datenschnittstellen: unterstützen diverse geräte
Gelb: UART Schnittstelle zum empfangen von Daten
Blau I2C
Lila: SPI
weiss: Pins für EEPRRoms - zugreifen auf den read only memory


### Aufgabe 2: 
Welche Funktion hat der eingefu ̈gte Vorwiderstand?
- hemmt den Stromfluß

### Aufgabe 3: 
Erstellen Sie mit Hilfe der Anleitung ein Programm, welches die LED 10 mal blinken l ̈asst und dokumentieren Sie ihr Vorgehen und den Programmiercode.

### Aufgabe 4
Nun ver ̈andern Sie das Programm, dass die LED so lange blinkt, bis eine beliebige Taste gedru ̈ckt wird. Dokumentieren Sie auch hier ihre Vorgehensweise und den Programmiercode.

### Aufgabe 5
Bringen Sie nun mit Hilfe des Tasters die Diode zum Leuchten. Dokumentieren Sie auch hier ihre Vorgehensweise und den Pro- grammiercode.

### Aufgabe 6



## Projekt Dokumentation
duesseldorf.ihk.de/ausbildung/ausbildungspruefungen/besonderheiten-bei-abschlusspruefungen/it-berufe-2599068

### Handreichnung
Vorlage von der IHK für die Dokumentationen
![[m6-it-berufe-handreichung-data.pdf]]


### Rasperry Pi Sensor Kit
![[Bedienungsanleitung-1413759-joy-it-senkit-x40-sensorkit-1-st.pdf]]
![[Tutorial_Sensor.pdf]]