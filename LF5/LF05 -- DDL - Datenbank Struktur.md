parent: [[LF05 - Datenbank]]

# SQL DDL - Datenbank Struktur
### SQL DDL - Datenbank Struktur

Bevor man Daten einer Datenbank abfragen kann, müssen erst der Aufbau bzw. die Tabellen und die Datenstruktur bekannt sein. Dazu benötigt man einige Befehle von DDL (Data Definition Language).

> Informieren Sie Sich zu DDL im unten gegebenen Informationsblatt

> Vergessen Sie nicht die Anwendung des SQL Befehls 'USE'

> Ermitteln Sie den Aufbau der Datenbank GEO :

a) Welche Tabellen hat die Datenbank

b) Welche Spalten haben die einzelnen Tabellen

> Erstellen Sie zu allen obigen Abfragen das Skript GEODDL.sql

> Testen Sie Ihr Skript und laden Sie es im UPLOAD hoch

[Abgabe 2 Select statement:](Abgabe%202%20Select%20statement.md)

- **Datenbank Intro**

    **Start XAMP:**

    sudo /Applications/XAMPP/xamppfiles/xampp start

    **Login to mysql via terminal:**
    /Applications/XAMPP/xamppfiles/bin/mysql -u root

    show databases; **# to show all databases**

    `Use geo;` **# to open the geo DB**

    `Show tables;` **# show tables in the DB**

    show databases;

    Show Columns FROM fluss; # ** show the column types**

    - Show Columns FROM kontinent;
    - Show Columns FROM land;
    - Show Columns FROM ort;
    - Show Columns FROM stadtfluss;
    - SELECT * FROM fluss;  # **select all columns and content**
    - SELECT * FROM kontinent;
    - SELECT * FROM land;
    - SELECT * FROM ort;
    - SELECT * FROM stadtfluss;

- **Aufgabe 2:**
    - Bitte erstellen Sie jeweils zu jeder Aufgabe den SQL Befehl.
    - Tragen Sie Ihre L旦sung jeweils in den grauen Bereich der Aufgabe ein
    - Laden Sie bitte Ihre L旦sung im Upload hoch

    **1. Zeige alle Tabellen der Datenbank GEO**

    `USE geo;SHOW TABLES;`

    **2. Zeige alle Daten der Tabelle Kontinent**

    `MariaDB [geo]> SELECT * FROM kontinent;`

    **3. Zeige alle Daten der Spalten Name und Fl辰che von der Tabelle Kontinent an**

    `MariaDB [geo]> SELECT name, flaeche FROM kontinent;`

    **4. Zeige Name und Fl辰che von Europa an**

    `MariaDB [geo]> select * from kontinent where name ='Europa';`

    **5. Zeige Name und Fl辰che f端r alle Kontinente an, mit einer Fl辰che von 31.000 km**

    `MariaDB [geo]> SELECT name, flaeche FROM kontinent where flaeche = 31;`

    **6. Zeige Name und Fl辰che f端r alle Kontinente an, die Fäche in Hektar (1km2=100 Hektar)**

    `MariaDB [geo]> SELECT name, flaeche*100 AS flaechex100 FROM kontinent;`

source /Users/niclasedge/Documents/OneDrive/LF05\ -\ Datenbank/04\ DDL\ Einführung/info.sql

[SQL sample Queries](SQL%20sample%20Queries.md)

Queries:

select * from land join ort on (land.lnr=ort.lnr);

- Geo DB ERM Diagram

    ![LF05%20-%20Datenbank%20(ABO)%20fea7b1a68d4b4c0198fd08757a874b7f/GEO_DB_ERM_Diagram.png](GEO_DB_ERM_Diagram.png)