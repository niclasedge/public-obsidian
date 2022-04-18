parent: [[LF02 - Arbeitsplätze nach Kundenwunsch]]
tags:
aliases: 
Reference:

---
# LF2 Aufgabe Virtualisierung

**Bereich 1: 1. Hälfte Seite 8 -10 '[Virtualisierung](https://lernportal.hhbk.de/mod/resource/view.php?id=13816) mit und ohne BS'**

Prokreis6: Niclas Edge, Anna Zelt, Thomas Rommel, Luke Jammers

# Virtualisierung mit und ohne Betriebssystem

Aufgrund der immer leistungsstärkeren PCs können mittlerweile ohne Probleme mehrere Virtuelle Mashinen auf einem Rechner gleichzeitig genutzt werden. Dies ist besonders interessant für Firmen, die für Mittarbeiter im Home-Office, mit Hilfe von Virtuellen Maschinen, keine Firmenlaptops zu verfügung stellen müssen, da man sie auf die Virtuellen Maschinen über eine Internetseite auf dem Privatrechner von zuhause einwählen kann.

Da die virtuellen Maschinen "nur" Digital sind kann die Anzahl der Maschinen schnell hochskaliert werden. Voraussetzung dafür ist natürlich eine passenden Infrastruktur, die die Rechenleistung und die Speicherkapazität dazu besitzt.

## Vor und Nachteile von Virtualisierung:

### Vorteile für Firmen:

- Weniger kosten für dedizierte Firmenlaptops, da diese durch Remoteverbindung zu Virtuellen Maschinen erstetzt werden können
- Schnelle Skalierbarkeit der Maschinen bei Bedarf
- Einteilung der Ressourcen bei bedarf
- Vereinfachtes Management der Systeme (keine Hardware beim User)

### Vorteile für Privatuser:

- schnelle Einrichtung verschiedener Betriebssysteme
- Verbindung via Remote zu einem Firmenrechner

## Die Hardware Grenzen bei Virtualisierung:

- Die verbindung der Virtualisierungssoftware zu der internen Hardware (Soundtkarte, USB-Ports) stellt oft Probleme dar
- Unterstützung der Hardwarespezifischen Features, wie besondere Features einer Grafikkarte.
- Treiber sind hier das entscheidende Bindeglied.

### **Wann lohnt sich Server-Virtualisierung?**

- Virtualisierungslösung realistische Konsolidierungsraten von 1:5 bis 1:100
- sinken die Betriebskosten (Energie, Platz, Klimatisierung)

### Verschiedene Techniken um Gastbetriebssysteme in einer virtuellen Umgebung zu starten

- **Typ2 Hypervisor**
    - Auch Virtual Machine Monitor genannt
    - Voraussetzung: ausgewachsenes Betriebssystem
    - Verwaltungssoftware
        - Kontrolle über die virtuelle Maschine
        - Starten und Anhalten der virtuellen Maschine
        - Weist entsprechende Ressourcen zu
    - Beispiel: Virtualisierungs-Tools wie Vmware Player, Workstation, Virtualbox und Microsoft Virtual-PC
- **Typ1 Hypervisor**
    - Läuft direkt auf der Hardware und ersetzt dabei das Betriebssystem
    - Einsatzgebiet: Server, Rechenzentren
    - Beispiel: Vmware ESX/ESXi, Oracle VM Server und Citrix Xenserver
- **Mischformen**
    - Beispiel: Hyper-V und KVM (Linux Kernel)
    - Virtualisierungsfunktionen sind Teil des Betriebssystems
    - Betriebssystem kann sich selbst virtualisieren und mehrere unabhängige Instanzen starten

# Prozessoren

- Bei allen Methoden werden die Befehle von der Virtualisierungsschicht abgefangen bevor Sie von der CPU empfangen werden
- Grund dafür ist das Design der x86 CPUs, den nur das Betriebssystem darf CPU Instruktionen verwenden, die später gestarteten Anwendungen nicht
- Das Betriebssystem hat so weiterhin die Kontrolle über die Anwendungen
    - Der Ring 0 in der CPU umfasst den Zugriff auf Interrupts und Speicher
    - Die Ringe 1, 2 und 3, die darüber liegen, nennt man User-Mode
- Betriebssystemtreiber können in Ring 1 und 2 arbeiten während Normale Programme der Betriebssysteme nur im 3. Ring arbeiten
- **Hypervisor**
    - können Befehle einer virtuellen Maschine analysieren und so umbauen, dass Sie im 3. Ring ausgeführt werden können.
    - Bei Komplett Visualisierungen kommt es zu einem großen Leistungsverlust.

## 5 Probleme die bei Virtualisierung auftreten können

1. Zu wenig Storrage: Ein zu knapp bemessenes Sorrage-System kann schnell zum Engpass in virtuellen Umgebungen werden.
2. Kosten der Virtualisierung: Ein weit verbreiteter Irrtum bei der Einführung von Virtualisierung ist, dass die IT danach kaum noch Geld kostet.
3. Zuviele Virtuelle Maschinen: Da die Erstellung virtueller Maschinen relativ simpel ist, kann es schnell zu einem Überschuss an Maschinen kommen. Das erschwert die effiziente Nutzung von IT-Ressourcen.
4. Features und lizenzen unklar: Etliche IT-Verantwortliche, die Virtualisierung einführen wollen, sind nich ausreichend über die diversen Features der Virtualisierungs-Plattformen und deren Lizensierungsbedingungen informiert.
5. Backup und Recovery unterschätzt: Für die Virtualisierung muss ein neuer Ansatz für Backup und Recovery bei ausfällen von kritischen Anwendungen erdacht werden.

### Die beliebtesten Virtualisierungssoftware

- Oracle Hypervisor
- VMWare
- Virtualbox
- Hyper-V