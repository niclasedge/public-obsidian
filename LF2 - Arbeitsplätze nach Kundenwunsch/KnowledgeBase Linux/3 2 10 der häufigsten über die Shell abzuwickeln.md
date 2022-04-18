# 3.2 10 der häufigsten über die Shell abzuwickelnden Aufgabenstellungen/User Tasks

### System Informationen erhalten:

- Hilfetext zu einem Shell komando anzeigen - *—help*
    - Man kann auch das Manual zu einem Befehlt anzeigen - *man ls*
- informationen zum aktuellen Betriebsystem erhalten - *uname -a*
    - The uname command with the -a option prints all system information, including machine name, kernel name & version, and a few other details. Most useful for checking which kernel you're using.
- Freien Speicherplatz auf HDD/SDD ermitteln -
    - df: The df command displays filesystem disk space usage for all mounted partitions. "df -h" is probably the most useful - it uses megabytes (M) and gigabytes (G) instead of blocks to report. (-h means "human-readable")
    - du: The du command displays the disk usage for a directory. It can either display the space used for all subdirectories or the total for the directory you run it on. Example:
    - free: The free command displays the amount of free and used memory in the system. "free -m" will give the information using megabytes, which is probably most useful for current computers.
- Kurzbefehl "alias" erstellen - alias
- shell Anzeige löschen - reset - to clear terminal screen
- BS neu starten - sudo reboot
parent: [[KnowledgeBase Linux]]
tags:
aliases: 
Reference:

---

- Autocomplete - *TAB* - vervollständigt Befehle und Dateinamen

### Verzeichnisse:

- Ins Root oder Home Verzeichnis wechseln - *~*
- Inhalt eines Verzeichnisses anzeigen - *ls* - zeigt alle Dateien/Verzeichnise an, aus der aktuellen position
- Aktuelles Arbeitsverzeichnis anzeigen - *pwd*
- Verzeichnis öffnen - *cd Documents* - öffnet den Ordner "Documents"
- Verzeichnis erstellen - *mkdir testordner*
- Verzeichnis löschen - *rmdir testordner*

### Arbeiten mit Dateien:

- Inhalt einer Datei anzeigen - *cat test.txt*
- Datei kopieren - *cd filename newfilename*
- Textdatei erstellen
    - touch NewFile.txt
    - *cat > myfile.txt*
        - Datei öffnet sich direkt - zum schließen CTRL-D drücken
- Datei löschen - *rm*

### User Management:

- Anwendungen aktuallisieren - *sudo apt-get upgrade firefox*
- Adminrechte erhalten - type "*sudo*" vor einem Befehl um Ihn mit Adminrechten auszuführen
    - je nachdem kann hier das Adminpasswort verlangt werden, ist man selbst nicht der Admin
- Neuen Nutzer erstellen - adduser newuser
- User Passwort ändern - passwd newuser
- Aktuellen Nutzer wechseln - *su –p [other_user]*
- Eingerichtetes Nutzerkonto anzeigen - *id username*