parent: [[LF05 - Datenbank]]
tags:
aliases: 
Reference:

---
# Abgabe 2 Select statement:

**Aufgabe :	SELECT A**

- Bitte erstellen Sie jeweils zu jeder Aufgabe den SQL Befehl.
- Tragen Sie Ihre Lösung jeweils in den grauen Bereich der Aufgabe ein
- Laden Sie bitte Ihre Lösung im Upload hoch
1. Zeige alle Tabellen der Datenbank GEO

USE geo;

SHOW TABLES;

1. Zeige alle Daten der Tabelle Kontinent

MariaDB [geo]> SELECT * FROM kontinent;

1. Zeige alle Daten der Spalten Name und Fläche von der Tabelle Kontinent an

MariaDB [geo]> SELECT name, flaeche FROM kontinent;

1. Zeige Name und Fläche von Europa an

MariaDB [geo]> select * from kontinent where name ='Europa';

1. Zeige Name und Fläche für alle Kontinente an, mit einer Fläche von 31.000 km

MariaDB [geo]> SELECT name, flaeche FROM kontinent where flaeche = 31;

1. Zeige Name und Fläche für alle Kontinente an, die Fläche in Hektar (1km2=100 Hektar)

MariaDB [geo]> SELECT name, flaeche*100 AS flaechex100 FROM kontinent;