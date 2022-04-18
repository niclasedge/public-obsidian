parent: [[FISI]]
Lehrer: Seib
Raum: C212

---
```dataview
list from [[LF09 - Netzwerke und Dienste bereitstellen]]
```
___
#### ToDo:

#### Fertig:
- Aufgabe: Analyse eines vorhandenes Kundennetzwerkes ![[005 Ausgangssituation Wittekind GmbH.pdf]]
- Aufgabe: Pflichtenheft  Wittekind fertigstellen [[LF09 -- Netwerkaufbau wiederholung]]
- Präsentation am 5.10. abgeben

https://lernportal.hhbk.de/course/view.php?id=1497 - LF7+9
https://lernportal.hhbk.de/course/view.php?id=1495 - nur LF9


## wiederholung
OSI-Modell - Referenzmodel (digital)
TCP/IP - Realer Stack, ähnelt dem OSI Model

SSID - Service Set Identifier

Wifi Band optionen
- 60 ghz - 2-3 Meter
- 2,4 Ghz
- 5ghz

Verkabelung
- Verkabelung zwischen gebäuden: Lichtwellenleiter
- Kupferkabel: bis 100m

DHCP
- Discover: client sendet anträge
- offer: 
- request: 
- ack: DHCP server akzeptiert die Auswahl

CAT8
- properties
- brandbreite
- länge




## Netzwerkadressen


## Eine Internet Timeline
![[InternetTimeline3.pdf]]

iana.org - Internetseite wo geprüft werden kann, welche IP auf wen registriert sind


### Was ist das Internet
- Netzknoten, als austauschknoten zwischen WAN
- WAN - Wired Access Network, 
	- LAN - Local Area Network

### Wer verwaltet die Internetadressen?
- ICANN, 
- Mittlerweile von Regionalen Restraren verwaltet
	- Je Kontinent eine Organisation und eine bestimmte Anzahl an Zugewiesenen 8er Blöcken(ein Block hat 16,7 mio IPv4 Adressen)
	- erste stelle -> 10.0.0.0

Prüfen wie die IPv6 Auslastung ist in der Welt
- https://ipv6ripeness.ripe.net/


RFC - Request for Comments
- Liste von diversen Anforderungen an den Provider
- Kann eingebaut werden, muss nicht umgesetzt werden
- DHCP, etc.

### Internet und WorldWideWeb - der Unterschied
Usenet, komplett andere Technik vor dem Werld Wide Web
Deepnet, unterkategorie vom WorldWideWep


### DNS
www.fachinformatiker.hhbk.de
Top Level Domain - .de
Second level-domain (SLD) - hhbk
Sub-Level-domain (subdomain) - fachinformatiker
computername (host oder dienst) - www

### Netwerkadressen
![[I1_Adressen1.pdf]]
#### Vergleich zwischen Brief und Netwerk:
**Betreffzeile** -> Ports (TCP oder UDP)
**Der Empfänger** -> IP-Adresse (IPv4 oder IPv6)
**Der Standort des Postkastens** -> Der Übergang in das "überregionale Netz" - Der Transport zum nächsten Knoten (ethernet oder WLAN)


**Punktdezimal Schreibweise:**
1100 0000   1010 1000   0001 0001   0000 0001
196   168   1   1  - IPv4


**Subnetzmaske:**


**TCP** - Aufteilen der Pakete in durchnummerierte und Port-Informationen ("Betreffzeile") hinzufügen
**IP** - Empfängeradresse und absender hinzufügen. An den "LIeferanten" übergeben 
**Ethernet oder WLAN** - Übertragen der Daten
![[Bildschirmfoto 2021-09-15 um 14.40.30.png]]

### NAT Adresse
Der Router nutzt eine NAT Tabelle um die Lokale Adresse in eine remote IP Adresse umzuwandeln, und umgekehrt.
- Komunikation wird von Endpunkten/Sockets

![[Pasted image 20210915144606.png]]



## OSI Referenzmodel
![[I1.2_Referenzmodelle.pdf]]



## Netwerkaufbau wiederholung
### toDo:
- [ ] zielbestimmung nach IST-Situation, das "Wie" fehlt 
- [ ] unter abschnitt 2  -> umfassend  
	- [ ] Was wollen wr neu machen?
- [ ] 3 = aufbau des physikalischen Netzwerkes
- [ ] (1 = ist bestimmungen)


Aufgabe: Netwerk für die Wittekid GmbH updaten für die nächsten 10 Jahre.
- Pflichtenheft
![[005 Ausgangssituation Wittekind GmbH (1) 1.pdf]]

- Logischer Netwerkplan muss als Anhang dabei sein

---
### Netzplan excel
![[Pflichtenheft netzplan.xlsx]]

### Pflichtenheft
![[Pflichtenheft - Wittekind GmbH.docx]]


### Besipiel für Inhalt und Gliederung
1. Ausgangssituation und Zielsetzung
	1. Ausgangssituation
	2. Zielsetzung
2. Funktionale Anforderungen
	1. Softwarearchitektur, Leistungen der Komponenten
	2. Anwendungsfälle 
	3. Datenmodell
	4. Abgrenzungskriterien
3. Nicht funktionale Anforderungen
	1. Einsatzumgebung der Hardware
	2. Einsatzumgebung der Software
	3. Einsatzumgebung der Orgware
	4. Datenvolumen
	5. Benutzerführung
	6. Verarbeitungsgeschwindigkeit
4. Lebenszyklus des Gesamtsystems
5. Schnittstellenübersicht
6. Lieferumfang
	1. Zu übergebende Dokumente
	2. Softwarebereitstellung
	3. Installation und Datentransfer
	4. Schulungsleistungen
	5. Supportleistungen



## Zahlensysteme

192 . 168 . 1 . 0 - Dezimalsystem

1100 0000.1010 - Binärsystem

IPv6 - Hexadezimalsystem

1001 = 9
1010 = 10 = A
1111 = 1*8+1*4+1*2+1*1 = F

Formel:
xxxx


|||||||| *1
||||||| *2
|||||| *4
||||| *8
|||| * 16
||| * 32
|| * 64
| * 128


Wert der Zahlen: 16 verschiedene Zahlen
0 - 0
1 - 1
2 - 2
...
9 - 9
10 - A
11 - B
12 - C
...
15 - F


### Alles was kommunizieren soll, muss die gleiche Netz-ID haben
- Netz ID entsteht wenn man die IP und die Subnetzmaskte übernanderlegt und Nullt
- oberhalb der Nullen der subnetzmaske müssen auch null stehen (vergleich subnetz/ip)

0001 1101 0000 1001 0001 0100 0000 0000 - 29.9.20.0 - Netz ID
0001 1101 0000 1001 0001 0111 1111 1111 - 29.9.23.255 - Broadcast
1111 1111 1111 1111 1111 1100 0000 0000 - größte Zahl des Broadcast Bereiches

1111 1111 1111 1111 1111 1111 1000 0000 - subnetz




### Aufgabe Subnetting:
![[SubnettingLeichtGemacht_FiSi.pdf]]
![[Subnetter-2b.xls]]



## Präsentation: Serverraum Aufbau
![[Serverraum_Sicherheitskonzept Gruppenpräsentation2.pptx]]


## Pflichtenheft: 

## Versandhandel Beutelschneider AG
- [ ] Präsentation der Ergebnisse
	- [ ] Analyse
		- [ ] ![[050 BeutelschneiderAG-00_v01.pkt]]
	- [ ] Planung


### Material
#### Aufgabe
![[050 Arbeitsblatt Versandhandel Beutelschneider AG.pdf]]
![[050 BeutelschneiderAG-00.pkt]]

#### Virtual Lokal Area Network (VLAN)
![[030 Infoblatt -VLAN.pdf]]
![[040 Arbeitsblatt VLAN-Konfiguration.pdf]]
![[040 Arbeitsblatt VLAN-Konfiguration.pkt]]


#### Etherchannel / einrichten
```
enable
configure t

# für die eine seite
interface range F02-6
channel-protocol lacp
channel-group 1 mode active

# für die andere gruppe
interface range F02-6
channel-protocol lacp
channel-group 1 mode passive
```



#### VLAN einrichten (portbasiert)
1. VLANs im switch definieren
	1. dem jeweiligen ethernet port ein VLAN zuweisen (access)
2. Backbone switch: Trunk aktivieren und mehrere vlans zulassen (bei Backbone aktivieren) (trunk)
3. DHCP erstellen
	1. Port basierte verteilung in jedem switch einstellen
	2. DHCP relay im switch erstellen (auf dem interface configurieren)

- [ ] DHCP erstellen
- [ ] relay einstellen





#### Statisches VLAN (option 1)
- portbasiert

#### VLAN-Tagging (option 2)
- VLAN informtionen werden von dem Switch hinzugefügt
	- basiert auf
		- portbasiert
		- macadresse

#### Um kommunikation unter den vlans ermöglichen
- **IP Subnetz**
- die nächste ebene von Layer 3 Geräten, definiert werden, dass Gerät A mit Gerät B aus anderem VLAN kommunizieren soll
	- bzw, gibt Gerät A einen anderen VLAN
- 

#### VLAN Trunk
- gleichzeitige übertrgung von daten aus mehreren VLNANs

#### Spanning Tree Protocol (STP)
![[060 Infoblatt STP.pdf]]
![[070 Arbeitsblatt Spanning Tree.pdf]]
![[080 Arbeitsblatt Spanning Tree 2.pdf]]





### IP Adressen verteilung / Subneting

![Abbildung 1: Diese Tabelle zeigt die Anzahl der Subnetze und Hosts für jedes der acht Maskenbits im dritten Oktett einer IPv4-Adresse. ](https://cdn.ttgtmedia.com/rms/German/Berechnung-von-Subnetzen-und-Hosts-deutsch_half_column_mobile.png)


### Private Adressbereich
3 Private Adressbereiche

Klasse A: 1 privates Netz mit 16.777.216 Adressen;
10.0.0.0/8

Klasse B: 16 private Netze mit jeweils 65.536 Adressen;
172.16.0.0/16 bis 172.31.0.0/16

Klasse C: 256 private Netze mit jeweils 256 Adressen;
192.168.0.0/24 bis 192.168.255.0/24


DHCP Relay
- Leitet automatisch DHCP Daten an den server weiter (wenn eingestellt)
- Muss nicht in dem jeweiligen subnetz drinnen sein



### NAT und Portforwarding

**endpunkt**: windows schreibweisen
**socket**: linkux schreibweise

**NAT**: Network address translation
- Verwandelt die Private IP über den Router zu einer public IP des Routers

### UDP - User Datagram Protocol
![Port-Struktur von UDP](https://www.elektronik-kompendium.de/sites/net/bilder/08122811.gif)



#### Ports
- eine adresse, damit das richtige Fenster genutzt wird
- http = :80
- https: :443

### 3 Wege Handshake


![[3WegeHandshake.pdf]]
d

### Lösung vorher
![[R4-NATPort.pdf]]

### Aufgabe:
![[NATPOrt3FHR.pdf]]

### Sicherheitsbedenken
- IP Spoofing
- DHCP - Starvation
	- DOS
	- Überlastet den Server mit Anfragen nach IP adressen
		- sodass alle adressen verbraucht sind
	- Dann kann der Rogue sich melden und selbst die IP vergeben
- DHCP - Server Rogue
- Arp spoofing (immitieren von MAC adressen)
	- ARP - Address Resolution Protocol
	- Fängt den "ARP Request" nach einer MAC adresse ab und spooft diesen und gibt einen "ARP Response" mit der adresse zurück und ist so im Kreislauf
- VLAN - gefälscte VLAN Tags (double tagging/VLAN hopping)
- Spanning Tree Protocoll - Rootbridge Rogue
	- feindliche Maschiene stellt sich zwischen die DHCP Anfrage und schickt schneller das Offer zurück


--- 
Diverse Grafiken



---
## OSI Model (cheat sheet)
![[OSI-Modell.pdf]]


## Struckturierte Verkabelung (cheat sheet)
![[Strukturierte_verkabelung_DINA3.pdf]]


## VLAN (cheat sheet)
![[VLANs.pdf]]

## Raid System Poster
![[RAIDPoster.pdf]]


## Prüfungsvorbereitung
- Kabel auswählen
- 



### Beispiele für Standard-Ports (TCP)
![[Bildschirmfoto 2021-12-15 um 12.52.25.png]]

### Beispiele für Standard-Ports (UDP)
![[Bildschirmfoto 2021-12-15 um 12.52.44.png]]


### Umrechnung MiB zu Bit
500 MiB zu bit umrechnen
- 500*1024*1024*8 = Bit

10 Mbit/s in bits/s umrechnen:
- 10 * 1000 * 1000 bit /s



[[LF09 - Test vorbereitung]]