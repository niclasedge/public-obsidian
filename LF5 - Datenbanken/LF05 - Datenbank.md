parent: [[FISI]]
Lehrer: Abu
Raum: 

---
```dataview
list from [[LF05 - Datenbank]]
```
---
# LF05 - Datenbank (ABO)

Aufgabe: klausur 28.5.21

**Login via Terminal Mac OSX:**

/Applications/XAMPP/xamppfiles/bin/mysql -u root

### Jupyter Notebook
![[01 Verbinden.ipynb]]

---

# Jahr 1
## [[LF05 -- Grundlagen]]
## [[LF05 -- DDL - Datenbank Struktur]]
## [[LF05 -- DDL - Datenbank Aufbau]]
## [[LF05 -- DQL - Datenbank Abfrage]]
## [[LF05 -- Distinct]]
## [[LF05 -- Where]]
## [[LF05 -- Like]]
## [[LF05 -- Scalar Funktionen]]
## [[LF05 -- Aggregatfunktionen]]
## [[LF05 -- Subselect]]
## [[LF05 -- Join]]

--- 
# Jahr 2
## Datenbank erstellen
### ERM Model Überblick
![[ERM A Einführung INF.pdf]]

![[ERM B Aufbau INF.pdf]]

![[ERM X1 Entwicklung FOL.pdf]]

### Aufgabe:
![[ERM X1 Entwicklung UEB.pdf]]

1. Bestimmen Sie in Ihrer Gruppe alle benötigten Attribute (z.B. KundenNr, KundenName, Buch..??..usw.). 
2. Fassen Sie zusammengehörige Attribute zu Gruppen, also zu Entitäten, zusammen und geben Sie jeder Entität einen aussagekräftigen Namen (z.B. Entität ‚Kunde‘). Achten Sie darauf, dass der Name einer Entität immer in Einzahl ist, also z.B. Kunde (nicht Kunden !!) 
3. Erstellen Sie ein ERM (Entity-Relationship.-Modell) indem Sie die von Ihnen bestimmten Entitäten grafisch darstellen und mit ihren Namen beschriften. Zeichnen Sie die Beziehungen zwischen den Entitäten ein, bestimmen Sie Verben die die Beziehung beschreiben und tragen Sie diese ebenfalls in das ERM ein. (! Tragen Sie bitte noch keine Kardinalitäten ein !) 
4. Bereiten Sie die Präsentation Ihres Ergebnisses vor, um im Klassenverband die Kardinalitäten für Ihr ERM gemeinsam zu ermitteln.


![[ERM X2 Entwicklung UEB.pdf]]

### Aufgabe 2 ERM:
![[FS23 ERM.docx]]

Jeder Kauf hat einen Kunden
Jeder Kunde kann mehrere Käufe haben

Jeder Kauf kann mehrere Bücher haben.
Jedes Buch kann mehrere käufe haben

### Aufgabe 3 Relationship shema (RS)
![[RS aus ERM INF.pdf]]

![[UPLOAD ERM BVH.xlsx]] Lösung

### Aufgabe 4 ERM + RS:
![[00 HHBK Inventar AUF.pdf]]

![[HHBKINV_ERM.docx]]
![[HHBKINV_RS.xlsx]]

``` sql
## SKRIPT starten via: "source H:\HHBKINV.sql"

# Datenbank löschen, wenn vorhanden
drop database if exists HHBKINV;

# Datenbank erstellen
create database HHBKINV;

# Datenbank aktivieren
USE HHBKINV;

# Erstelle die Tabelle Raum 
CREATE table Raum (
	RaumNr VARCHAR(10) PRIMARY KEY,
	Etage VARCHAR(10)
);

# Erstelle die Tabelle Betreuer
CREATE table Betreuer(
	Kuerzel VARCHAR(4),
	Datum INT,
	PRIMARY KEY(Kuerzel)
);

# Erstelle die Tabelle Geraet
CREATE table Geraet(
	AnlageNr VARCHAR(10) PRIMARY KEY,
	SerienNr VARCHAR(10),
	Bezeichnung VARCHAR(10),
	Bemerkung VARCHAR(10),
	RaumNr VARCHAR(10),
	FOREIGN KEY (RaumNr) REFERENCES Raum(RaumNr)
);

# Erstelle die Zwischentabelle RaumBetreuer	
CREATE table RaumBetreuer(
	Kuerzel VARCHAR(4),
	RaumNr VARCHAR(10),
 	FOREIGN KEY (Kuerzel) REFERENCES Betreuer(Kuerzel),
	FOREIGN KEY (RaumNr) REFERENCES Raum(RaumNr),
	PRIMARY KEY (Kuerzel, RaumNr)
);

# Zeige alle Tabellen in der Datenbank
show tables;

# Beschreibe die einzelne Tabelle
describe Betreuer;
describe Raum;
describe Geraet;
describe RaumBetreuer;
```



## Tabelle befüllen

show columns from raum;

insert into Raum values ('A1','1B');


insert into Betreuer values ('BERG',2020);
insert into Betreuer values ('BAYR',2021);


insert into Geraet values ('1','2','Projektor','ist kaputt', 'A1');
insert into Geraet values ('2','4','Laptop','funktioniert', 'A1');

insert into RaumBetreuer values ('BERG', 'A1');

insert into RaumBetreuer values ('EDGE', 'B1');


## Datenbank Normalisieren 
Datenbank muss aus, rechlicher sicht, in der 3. Normalisierungsform aufgebaut werden

### Normalform 1
- Atomar
### Normalform 2
- voll Funkitonal vom Primärschlüssel abhängig
### Normalform 3
- Keine funktionale Abhängigkeiten von nicht primärschlüssel Spalten


![[NOR A DB Anomalien INF.pdf]]
![[NOR B Einführung INF.pdf]]
![[NOR C Grundlagen FRA.docx]]
![[NOR D Normalformen INF.pdf]]

#### Fragen : Normalisierung von Datenbanken
_Zum Einstieg in die Thematik der Normalisierung von Datenbanken sind hier in Frageform die wichtigsten grundlegenden Informationen zu erarbeiten._

a) Was versteht man allgemein unter ‚Normalisierung einer Datenbank’ ?
- Schrittweise Umstellung und Zerlegung der vorhandenen Datenbanktabellen

b) Was ist das Ziel einer Normalisierung ?
- Ziel: Befreiung der Datenbank von Redundanzen

c) Wieviel Normalformen gibt es insgesamt ?
5 + Boyce Codd Normalform = 6

d) Wieviel Normalformen werden bei einer Datenbank angewandt ?
- Bis zu 6, rationale Datenbanken nur bis NF3 überführt

e) Muss eine Datenbank normalisiert werden ? (Deine Meinung & Begründung in Kurzform)
- Ja damit keine Anomalien entstehen und um die Konsistenz der Daten und die eindeutige Selektion zu gewährleisten
- Vermeidung von unnötiger Speichernutzung

f) Was passiert durch die Normalisierung mit den Tabellen einer Datenbank ?
- Tabellen werden aufgeteilt, so dass keine Redundant bestehen bleibt

g) Welche negativen Einflüsse kann die Normalisierung auf Datenbanken haben ?
- Performance Einbußen durch erhöhte Tabellen/ Spaltenanzahl
- Komplexer und fehleranfälliger

h) Was bedeutet Denormalisierung ?
- Normalisierung wieder rückgängig machen 

i) Was bedeutet im Zusammenhang mit Datenbanken der Begriff ‚Konsistenz ?
- Korrektheit der gespeicherten Daten

j) Was bedeutet im Zusammenhang mit Datenbanken der Begriff ‚Redundanz’ ?
- Überflüssige Duplikate von Informationen

k) Wie hängen Konsistenz und Redundanz voneinander ab ?
- Um Redundanz zu verringern, müssen die Datensätze einzigartig und konsistent sein

l) Was hat die Normalisierung mit diesen zwei oben genannten Begriffen zu tun ?
- Konsistenzerhöhung durch Redundanzvermeidung

Ø Beantworten Sie bitte folgende Fragen. Tragen Sie dazu Ihre Antworten in diesem Dokument direkt unter der jeweiligen Frage ein. :
Ø Gleichen Sie Ihre Antworten mit Ihrer Gruppe ab
Ø LAden Sie bitte (**jeder** einzeln) Ihre gemeinsame Lösung im Upload hoch als : **NORFragen.docx**




## Normalform anpassen

![[00 HHBK Inventar Normalisierung A AUF.pdf]]
![[FS23 HHBKINV RS.xlsx]]