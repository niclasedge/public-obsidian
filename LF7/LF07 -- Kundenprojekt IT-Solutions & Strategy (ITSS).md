parent: [[LF07 - Cyber-physische Systeme ergänzen]]

---

## Kundenprojekt IT-Solutions & Strategy (ITSS)
Der Serverraum der **IT-Solutions & Strategy (ITSS)** wird derzeit nur durch ein einfaches Türöffnungssystem überwacht. Die Überwachung soll um weitere Funktionen erweitert werden: Zugangszähler, Präsenzmelder, Temperaturüberwachung und Notöffnung. Neben einer entsprechenden Alarmierung, soll auch eine Protokollierung erfolgen.

#### Leitfaden: Betriebssicheres Rechenzentrum
![[LF_7_1_Fachtext Leitfaden RZ.pdf]]
#### Grafische Symbole für Gefahrenmeldeanlage
![[LF_7_1_Fachtext Symbole VdS 2135.pdf]]
#### Schaltzeichen Elektroinstallation
![[060 Fachtext Schaltzeichen Elektroinstallation.pdf]]
![[027 Arbeitsblatt Auswahl eines Server- und Technikraums.pdf]]
#### Fachtexte
![[030 Fachtext IT-Verteilerraum.pdf]]
![[035 Fachtext Anforderungen Serverraum.pdf]]
#### Serverraum Beispiel
![[LF7_LS1_AB1 V1 Serverraum opt.pdf]]
#### Arbeitsauftrag:
![[LF7_LS1_AB1 V1.pdf]]





### Was sollte im Serverraum überwacht werden?
- Temperatur /Kühlung /Luftfeuchtigkeit /Luftdruck
- Systemleistung/Festplattenauslastung
- Stromversorgung /Ausfallsicherung
- Brandmeldeanlage
- Sicherheitsystem/Überwachung


### Gruppenaufteilung:
**Paul:**
### Wie beurteilen Sie die aktuelle Sicherheitslage? Welche Maßnahmen schlagen Sie vor?
### Welche Kabel sind vorhanden/werden benötigt? (Prüfen auf EN 50173!)

**Niclas:**
### Welche Sensoren, Aktoren und Bussysteme sind vorhanden/werden benötigt? 
- **Vorhanden**
	- Sensoren
	- Aktoren
		- Rasberry Pi, Protokollierung
	- Bussysteme
		- Ethernet
		- Verbindungen zwischen den Systemen
- **Benötigt**
	- Sensoren
		- Handerkennung
			- https://www.handvenenerkennung.com/
			- ![[Pasted image 20210914132701.png]]
			- Sicherheit: 100x sicherer als Fingerabdruck
			- Preis:
			- ![[Pasted image 20210914132637.png]]
		- Temperatur- u. Luftfeuchte-Sensoren
		- Monitoring System um die Systemleistung zu überwachen
		- Wassersensor, um Wasserschaden vorzubeugen
	- Aktoren
		- Verbindung zwischen Sensor und Klimaanlage/Löschungsanlage einrichten, ggf temperatur anpassen
		- Alarme bei einem Schwellwert via eMail an Zuständige personen schicken.
	- Bussysteme
		- LAN Verbindungen zischen Switch&Router
		- Verbindung Switch&LAN Buchse
		- Verbindung Internet(TAE Dose) zum Firewall Box
		- Verbindung Firewall Box zu Router
		- Verbindung Server zu Rasberry Pi
		- Verbindung Rasberry Pi zu Temperatur/Monitoriing
### Welche Schnittstellen/Interfaces sind vorhanden/werden benötigt? (Visualisierung z.B. mit Visio)
![[LF7_LS1_AB1 V1_flowchart.mmap]]
- **Vorhanden**
	- Eingangstür RC2 mit Türöffnungssystem
	- LAN Verindungen zwischen den Geräten
- **Benötigt**
	- Welches format haben die Sensoren zum Monitoring
	- USB von den Sensoren zum Rasberry Pi Monitoring System
	- 

Produkte:
- Monitoring Lösung:
	- **ENVIROMUX LXO Mini von NTI:** 366€
		- ![ENVIROMUX MINI](https://www.ute.de/images/virtuemart/product/rackmonitoring_nti_enviromux-mini-lxo.jpg)
		- **Mini Überwachungssystem für Serverumgebungen** überwacht wichtige Umgebungsbedingungen (wie Temperatur, Luftfeuchtigkeit und Wasseraustritt), die Netzwerk-Komponenten in Ihrem Server-Raum zerstören können.
		- **5 digitale Eingänge**
		- **IP Überwachung per PING von Netzwerkomponenten**  Es wird in einstellbaren Intervallen ein PING an bis zu 16 IP Adressen gesendet, sollte eine Antwort ausbleiben erfolgt ein Alarm
	- **IP Thermometer mit POE Feuchte u. Temperatur­überwachung - bis zu 6 Sensoren**: 295€
		- ![](https://www.ute.de/images/virtuemart/product/rackmonitoring_ip-thermometer_nti_enviromux-micro-trhp.jpg)
		- Temperaturüberwachung
		- Luftfeuchtigkeitsüberwachung
		- Überwachung ob ein Wassereinbruch vorliegt
		- Luftzugüberwachung
		- Stromüberwachung
		- Bewegungsüberwachung,
		- Überwachung von (unerlaubten) Öffnungen eines Racks oder Zutritten zum (Server-)Raum, bspw. mit Türkontaktsensor
		- Überwachung von Vibrationen, bspw. bei einem Einbruch
		- Rauch- und Kohlenmonoxid-Überwachung
	- Expert Sensor Box 7214-13 LAN-Temperatur-/ Luftfeuchte-/ Druck-Sensor (PoE) mit Relaisausgang
		- ![](https://www.ute.de/images/virtuemart/product/ueberwachung_gude_expert-sensor-box-7214-13.jpg)
		- Integrierter Temperatur-/Luftfeuchte und Luftdruck-Sensor
		- Zwei Anschlüsse für weitere optionale Sensoren
		- Passiver Signaleingang und schaltbarer Relaisausgang
		- IPv6, SNMPv3, SSL,Telnet, Radius, Modbus TCP
	- Management Software für Environment Monitoring Systeme von NTI
		- ![](https://www.ute.de/images/virtuemart/product/ueberwachung_nti_enviromux-mng-lc.jpg)
		- Intuitive Management-Software mit grafischer Oberfläche
		- Einfach zu bedienende, einheitliche Schnittstelle sowohl für die Überwachung wie auch für die Konfiguration
		- Die einzeln Geräte (Einheiten) können einzeln oder in einer Gruppe überwacht und konfiguriert werden.
**U.T.E. — dem IT-Distributor** 02302 / 28 28 3-0

**Ege:**
### Welche Entwicklungsumgebung/Library wird zusätzlich benötigt?
### Powerpoint erstellen

**Jan:**
### Müssen weitere Materialien/Geräte angeschafft werden? 
### Welche Arbeiten fallen an oder werden an Fachfirmen vergeben?