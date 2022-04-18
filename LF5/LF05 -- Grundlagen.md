parent: [[LF05 - Datenbank]]
tags:
Reference:
date::
status::
fazit::

---

```dataview
table date, status, fazit FROM [[Ausflüge]]
```


# Grundlagen


[Grdl B DB Fachsprache FRA.pdf](Grdl_B_DB_Fachsprache_FRA.pdf)

[LF05 - Datenbank_Abgabe1](LF05%20-%20Datenbank_Abgabe1.md)

## Datenbank Entwicklung

[Grdl D DB Entwicklung INF.pdf](Grdl_D_DB_Entwicklung_INF.pdf)

Die Entwicklung einer Datenbank kann als ein Ablauf von vier Schritten angesehen werden. Dies wird im nachfolgenden Infoblatt beschrieben.

Der erste Schritt ist Aufgabe der Vertriebsabteilung, die Schritte 2, 3 und 4 ist Ihre Arbeit als Programmierer. Sie werden diese in den nächsten Schuljahren kennenlernen und selbst ausführen.

In diesem ersten Schuljahr erarbeiten Sie zunächst nur den 4. Schritt 'Datenbank programmieren' indem Sie einige SQL Befehle zur Abfrage von Daten verwenden.

## SQL Strucktur

[Grdl E SQL Struktur INF.pdf](Grdl_E_SQL_Struktur_INF.pdf)

Das eigentliche, fachliche Lernziel dieses Unterrichts, ist die Verwendung bzw. Programmierung von relationalen Datenbanken. Dies geschieht in jeder Hinsicht über die speziell dafür entwickelte und weltweit anerkannte 'Programmiersprache' namens SQL.

Nachfolgend finden Sie einige Informationen zu SQL, u.a. die Unterteilung aller Befehle von SQL in vier Sprachengruppen.

In diesem Schuljahr geht es ausschließlich um die Abfrage von Daten aus einer bestehen Datenbank, d.h. es geht hier nur um die Sprachgruppe DQL.

## Datenbank Software

[Anleitung XAMP.pdf](Anleitung_XAMP.pdf)

Für diesen Kurs wird die Datenbank Software MyQL verwendet, in Verbindung mit XAMMP, einem freeware Softwarepaket (MySQL Client & Server/ Apache Server..) .

Diese können Sie mit folgender Anleitung & folgendem Link auf Ihren Laptop runterladen, installieren und testen.

# SQL Pgrogrammierung - Skripte

[MySQL_Script_INF.pdf](MySQL_Script_INF.pdf)

SKRIPTE :

Zur Vereinfachung der Programmierung in SQL werden

[SQL Skripte](https://lernportal.hhbk.de/mod/resource/view.php?id=48324)

(Skriptdateien) erstellt. Diese sollen hier von Begin an verwendet werden. Informationen dazu finden Sie unten.

a) Erstellen Sie ein SQL-Skript, dass (zur Probe) aus nur 1 Befehl besteht. Der Befehl lautet :

SHOW DATABASES

b) Speichern Sie das Skript als unformatierte Textdatei mit dem Namen 'DBZeigen.sql'

c) Teste Sie Ihr Skript, indem Sie es ausführen !

HINWEIS :

Bitte beachten Sie, dass für MySQL-Befehle (manchmal) nur Slashes '/' bei Pfadangaben erlaubt sind.

D.h. in einer Pfadangabe von Windows müssen alle Backslashes durch Slashes ersetzt werden!

Beispiel für Pfadangaben:

C:\test\datei.xyz ist in MySQL C:/test/datei.xyz

## Erste Schritte mit dem MySql Client;

Nach der Installation können Sie Ihren MySQL-Datenbankserver am einfachsten über den Kommandozeilen-Client mysql ansprechen. Wenn Sie ein anonymes Konto eingerichtet haben, starten Sie ihn einfach durch die folgende Eingabe:

$ **mysql**

Andernfalls müssen Sie über die Option -u <Username> den Benutzernamen angeben und mittels -p festlegen, dass das Passwort abgefragt werden soll. Als Beispiel hier der MySQL-Verwaltungsbenutzer root:

$ **mysql -u root -p →** Enter password: *************

**Nachdem die Verbindung zum Datenbankserver hergestellt wurde, sehen Sie den Prompt des mysql-Clients:**

mysql>

Nun können Sie spezifische Steuerbefehle wie help (Anzeigen der Hilfe) oder quit (Beenden) eintippen oder aber die im nächsten Abschnitt besprochenen SQL-Abfragen. SQL-Abfragen können beliebig viele Zeilen lang sein (einschließlich); sie werden erst ausgeführt, wenn Sie sie mit einem Semikolon abschließen.

Bevor Sie mit einer Datenbank arbeiten können, müssen Sie diese auswählen. Dies geschieht mit Hilfe der Anweisung use <Datenbank>. Beispiel:

mysql> **use kaufhaus**

Im Auslieferungszustand enthält MySQL nur die Verwaltungsdatenbank mysql sowie die leere Demo-Datenbank test. Bevor Sie also ernsthafte Experimente unternehmen können, müssen Sie eine Datenbank anlegen. Dies geschieht mit Hilfe einer CREATE DATABASE-Abfrage, die im nächsten Abschnitt erläutert wird.

Praktisch ist außerdem die Möglichkeit, SQL-Anweisungen aus einer externen Textdatei zu importieren. Dazu dient die Anweisung source <Pfad>. Beispiel:

mysql> **source test.sql**

## GEO Datenbank :

[geo.sql](geo.sql)

In diesem Kurs sollen Datenbanken Abfragen erstellt werden. Dazu dient die Datenbank GEO als Grundlage für die verschiedenen Abfragen. Die Datenbank GEO kann mit dem nachfolgenden Skript komplett erzeugt und mit Daten gefüllt werden.

> Bitte führen Sie das Skript GEO.sql aus

> Prüfen Sie mit SHOW DATABASES ob die Datenbank GEO angelegt wurde

> Bei Problemen recherchieren Sie gerne auch im Internet

[Lösung Datenbank Aufgabe 1 Musterlösung](Lösung%20Datenbank%20Aufgabe%201%20Musterlösung.md)
