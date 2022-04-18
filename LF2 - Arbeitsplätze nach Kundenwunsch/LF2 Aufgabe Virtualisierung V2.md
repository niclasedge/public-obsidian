parent: [[LF02 - Arbeitsplätze nach Kundenwunsch]]
tags:
aliases: 
Reference:

---
# LF2 Aufgabe Virtualisierung V2

LF2: Virtualisierung Handout

**Prokreis6: Niclas Edge, Anna Zelt, Thomas Rommel, Luke Jammers** 

Aufgrund der immer leistungsstärkeren PCs können mittlerweile ohne Probleme mehrere Virtuelle Maschinen auf einem Rechner gleichzeitig genutzt werden. Dies ist besonders interessant für Firmen, die für Mittarbeiter im Home-Office, mit Hilfe von Virtuellen Maschinen, keine Firmenlaptops zur Verfügung stellen müssen, da man sie auf die Virtuellen Maschinen über eine Internetseite auf dem Privatrechner von zuhause einwählen kann.

Da die virtuellen Maschinen "nur" Digital sind kann die Anzahl der Maschinen schnell hochskaliert werden. Voraussetzung dafür ist natürlich eine passende Infrastruktur, die die Rechenleistung und die Speicherkapazität dazu besitzt.

## Vor und Nachteile der Virtualisierung:

### **Vorteile für Firmen:**

- Weniger kosten für dedizierte Firmenlaptops, da diese durch Remoteverbindung zu Virtuellen Maschinen ersetzt werden können
- Schnelle Skalierbarkeit der Maschinen bei Bedarf
- Einteilung der Ressourcen bei bedarf
- Vereinfachtes Management der Systeme (keine Hardware beim User)

### **Vorteile für PrivatUser:**

- schnelle Einrichtung verschiedener Betriebssysteme
- Verbindung via Remote zu einem Firmenrechner

## **Die Hardware Grenzen bei Virtualisierung:**

- Die Verbindung der Virtualisierungssoftware zu der internen Hardware (Soundkarte, USB-Ports) stellt oft Probleme dar
- Unterstützung der Hardwarespezifischen Features, wie besondere Features einer Grafikkarte.

 
- Treiber sind hier das entscheidende Bindeglied.

### **Wann lohnt sich Server-Virtualisierung?**

- Virtualisierungslösung realistische Konsolidierungsraten von 1:5 bis 1:100
- sinken die Betriebskosten (Energie, Platz, Klimatisierung)

## Verschiedene Techniken

Um Gastbetriebssysteme in einer virtuellen Umgebung zu starten

**Typ2 Hypervisor** 

- Auch Virtual-Machine Monitor genannt
- Voraussetzung: ausgewachsenes Betriebssystem
- Verwaltungssoftware
    - Kontrolle über die virtuelle Maschine
    - Starten und Anhalten der virtuellen Maschine
    - Weist entsprechende Ressourcen zu
- Beispiel: Virtualisierungs-Tools wie Vmware Player, Workstation, Virtualbox und Microsoft Virtual-PC

**Typ1 Hypervisor** 

- Läuft direkt auf der Hardware und ersetzt dabei das Betriebssystem
- Einsatzgebiet: Server, Rechenzentren
- Beispiel: Vmware ESX/ESXi, Oracle VM Server und Citrix Xenserver

**Mischformen** 

- Beispiel: Hyper-V und KVM (Linux Kernel)
- Virtualisierungsfunktionen sind Teil des Betriebssystems
- Betriebssystem kann sich selbst virtualisieren und mehrere unabhängige Instanzen starten

## Prozessoren

- Bei allen Methoden werden die Befehle von der Virtualisierungsschicht abgefangen bevor Sie von der CPU empfangen werden
- Grund dafür ist das Design der x86 CPUs, denn nur das Betriebssystem darf CPU-Instruktionen verwenden, die später gestarteten Anwendungen nicht
- Das Betriebssystem hat so weiterhin die Kontrolle über die Anwendungen
    - Der Ring 0 in der CPU umfasst den Zugriff auf Interrupts und Speicher
    - Die Ringe 1, 2 und 3, die darüber liegen, nennt man User-Mode
- Betriebssystemtreiber können in Ring 1 und 2 arbeiten während Normale Programme der Betriebssysteme nur im 3. Ring arbeiten

**Hypervisor** 

- können Befehle einer virtuellen Maschine analysieren und so umbauen, dass Sie im 3. Ring ausgeführt werden können.
- Bei Komplett Visualisierungen kommt es zu einem großen Leistungsverlust.

## 5 Probleme die bei Virtualisierung auftreten können

1. **Zu wenig Storage:** Ein zu knapp bemessenes Storage-System kann schnell zum Engpass in virtuellen Umgebungen werden.
2. **Kosten der Virtualisierung:** Ein weit verbreiteter Irrtum bei der Einführung von Virtualisierung ist, dass die IT danach kaum noch Geld kostet.
3. **Zu viele Virtuelle Maschinen:** Da die Erstellung virtueller Maschinen relativ simpel ist, kann es schnell zu einem Überschuss an Maschinen kommen. Das erschwert die effiziente Nutzung von IT-Ressourcen.
4. **Features und Lizenzen unklar:** Etliche IT-Verantwortliche, die Virtualisierung einführen wollen, sind nicht ausreichend über die diversen Features der Virtualisierungs-Plattformen und deren Lizensierungsbedingungen informiert.
5. **Backup und Recovery unterschätzt:** Für die Virtualisierung muss ein neuer Ansatz für Backup und Recovery bei ausfällen von kritischen Anwendungen erdacht werden.

## Die beliebtesten Virtualisierungssoftware

Oracle VM Server Hypervisor

- Beschleunigte Bereitstellung
- Hochverfügbare Lösungen für den gesamten Stack
- Effiziente Arbeitsspeicher-Zuweisung
- Extrem skalierbar
- Typ1 Hypervisor

VMWare

- Keine große Auswahl an Betriebssystemen
- Nicht so ausgereift wie andere Anbieter
- Virtualbox
- Freeware

Hyper-V

- Microsoft Lösung
- Virtualisierungsfunktionen sind Teil des Betriebssystems
- Betriebssystem kann sich selbst virtualisieren und mehrere unabhängige Instanzen starten

Citrix Xenserver

- Typ 1 Hypervisor

### Wichtige Begriffe:

- **Simulieren**: Steht für wirklichkeitstreu nachahmen.
- **Emulieren**: Steht für nachahmen, also wird die Wirklichkeitstreue vernachlässigt
- **Virtualisieren**: Steht für nicht-physisch