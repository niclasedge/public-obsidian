parent: [[KnowledgeBase Linux]]
tags:
aliases: 
Reference:

---
# 3.1 Syntax und des Aufbaus der Linux Shell Befehle. (Kommando, Attribut, Option)

## **So setzt sich ein Linux Befehl zusammen:**

Ein Linux Befehl besteht immer aus einem Kommando

```
cd

```

Meist kommt auch noch nein Attribut dazu

```
cd documents

```

und je nach Wunsch, kann auch eine Option angefügt werden

```
cd documents -o

```

# **Befehle**

Übersicht der gängigsten Shellbefehle nach Verwendung sortiert.Mehr Informationen über den zu den jeweiligen Befehlen findet ihr unter Ausführlich oder in der jeweiligen Manpage des Befehles. Nicht alle Befehle und Programme sind auf jedem Betriebssystem vorhanden und können sich teilweise in der Verwendung unterscheiden.

Beispielhaft https://www.shellbefehle.de/befehle/ls [jeweiliger Befehl, falls in der DB vorhanden]

## **Datei und Verzeichnis Befehle**

**Befehl  Beschreibung**

Ls                    Auflistung von Verzeichnissen (Inhalt eines Verzeichnis anzeigen)

Cd                   Verzeichnis wechseln

Cp                   Eine Datei oder Verzeichnis kopieren

mv                  Eine Datei verschieben oder umbenennen

chmod            Zugriffsrechte einer Datei oder eines Verzeichnisses ändern

chown            Eigentümer und Gruppe einer Datei oder Verzeichnisses ändern

dd                   Daten blockweise kopieren klonen, löschen, Images erstellen, uvm…

diff                  Vergleich des Inhalts zweier Dateien Zeile für Zeile

df                    Freien Festplatten-Speicher und inodes aller eingehängten Laufwerke anzeigen

du                   Speicherverbrauch eines Verzeichnisses anzeigen

grep                Dateien durchsuchen

lsof                 Anzeige geöffneter Dateien

mount            Dateisystem einhängen

pwd                Zeigt das aktuelle Arbeitsverzeichnis an

umount          Dateisystem aushängen

mkdir             Ein Verzeichnis / Ordner erstellen

rm                   Dateien und Verzeichnisse löschen

rmdir              Ein Verzeichnis löschen

rsync              Datensynchronisation / Datenübertragung Lokal oder Remote

ftp                   FTP starten

sftp                 SFTP starten

scp                  Sicheres übertragen von Daten

shred              Sicheres löschen von Daten

## **Datei Suchen**

**Befehl  Beschreibung**

find                       Dateien nach Datum, Größe, Anderung, Name und Muster suchen.

grep                      Text innerhalb einer Datei oder ausgabe suchen

locate                    Schnelles suchen von Dateien mittels locatedb Datenbank

whereis                 Suchen von Programmen in vordefinierten Verzeichnissen

which                    Lokalisiert ein Programm welches sich im PATH befindet

## **Datei packen und entpacken (komprimieren)**

**Befehl  Beschreibung**

bunzip2                 Dekomprimert bz2 Dateien

bzip2                     Komprimiert Dateien im bz2 Format

compress               Komprimiert Dateien

gunzip                   Dekomprimert gz Dateien

gzip                       Komprimiert Dateien im gz Format

tar                          Erstellen von Tar Archiven

uncompress           Dekomprimiert Dateien

unzip                      Dekomprimiert Zip Dateien

zip                          Komprimiert Dateien im Zip Format

## **System Befehle**

**Befehl  Beschreibung**

free                       Auslastung des Arbeitsspeichers anzeigen

uptime                  Zeigt an wie lange das System läuft

date                      Zeigt das System Datum und die System Zeit an

ps                           Zeigt den Status eines Prozesses

pstree                   Zeigt alle Prozesse in einer Baum Ansicht an

uname                  Systeminformationen anzeigen

top                         Zeigt die auf dem System laufenden Prozesse „live“ an

kill                          Einen Prozess sofort beenden

killall                      Mehrere Prozesse mit einem bestimmten Namen beenden

clear                      Den Bildschirm der Konsole leeren

man                      Systemhandbuch (manual oder manpage) zu einem Befehl, Anwendung oder Datei (manual)

reboot                  Das System neutstarten

shutdown              Das System Herunterfahren

wall                        Allen verbundenen Benutzern eine Nachricht senden

which                    Ein Kommando lokalisieren (Pfad zum Kommando anzeigen)

## **Benutzer und Gruppen verwalten**

**Befehl  Beschreibung**

chfn                       Informationen eine Users bearbeiten

id                           Anzeige der Benutzer ID und Gruppen ID (Kennung)

last                         Die letzten logins nach Datum und Uhrzeit anzeigen

login                      Benutzer (neu)anmelden

who                       Die aktuell auf dem System eingeloggten User anzeigen

whoami                Anzeige des Benutzer mit dem gerade gearbeitet wird

passwd                  Passwort einen Benutzers ändern

su                          Als Admin anmelden, oder SU + Benutzername den Benutzer wechseln

sudo                      Einen Befehl als admin ausführen

useradd               Einen Benutzer anlegen

userdel                 Einen Benutzer löschen

usermod             Einen Benutzer ändern

groupadd            Eine Benutzergruppe anlegen

groupdel             Eine Benutzergruppe löschen

groupmod          Eine Benutzergruppe ändern

## **Netzwerk Befehle**

**Befehl  Beschreibung**

ping                       Datenpakete an eine IP senden (zum Prüfen der Verbindung)

traceroute          Ein Datenpaket verfolgen

netstat                 Listet alle aktuellen benutzten Ports auf

nslookup             Namensauflösung

dig                         DNS lookup Werkzeug

ifconfig                 Status und Konfiguration der Netzwerkschnittstelle

## **Hardware Befehle**

**Befehl  Beschreibung**

lscpu                     CPU Informationen anzeigen

lshw                      Hardware Informationen anzeigen

lspci                       PCI-Hardware Informationen anzeigen

lsusb                     USB Hardware Informationen anzeigen

## **Sonstige Befehle**

**Befehl  Beschreibung**

tar          Komprimieren und Dekomprimieren von Dateien

zip          Komprimieren von Zip Archiven

unzip     Dekomprimieren von Zip Archiven

head     Ausgabe der ersten Zeilen einer Datei

tail          Ausgabe der letzten Zeilen einer Datei

less        Scrollfähige Anzeige einer Textdatei

xargs     Standardeingabe in Befehlszeilen umzuwandeln

wget     Dateien aus dem Web herunterladen, unterstüzt HTTP, HTTPS und FTP

curl        Dateien von oder zu einem Server übertragen

ssh         Sichere Verbindung zu einem anderen System herstellen

cal          Ruft einen einfachen Kalender auf