parent: [[LF05 - Datenbank]]
tags:
aliases: 
Reference:

---
# LF05 - Datenbank_Abgabe1

Niclas Edge & Marvin Berger

### Fragen : Fachsprache Datenbanken

Zum Einstieg in die Thematik Datenbanken sind zunächst die wichtigsten Begriffe
aus der Fachsprache zu erlernen um eine Grundlage für eine gemeinsame
professionelle Erarbeitung zu schaffen.

### **a) Beantworten Sie folgende Fragen :**

**1.) Ermitteln Sie die ausgeschriebenen Begriffe folgender**

Abkürzungen :

 DB - **DataBase**
 DBS - **DataBaseSystem**
 DBMS - **DataBase Management System**

**2.) Bestimmen Sie den Zusammenhang zwischen den o.a. Begriffen und geben Sie dazu eine Grafik an !**

Der Aufbau eines Datenbanksystems(DBS) besteht aus einer Datenbank (DB), welche die Datenbasis darstellt, und aus einem Datenbankmanagementsystem (DBMS). Das DBMS definiert die Art wie die Daten verbunden sind und abgerufen werden.

### Beispiel Xampp:

In Xampp wird der Server gestartet, das **Datenbanmanagementsystem**.

Datenbanksystem

Datenbank

![LF05%20-%20Datenbank_Abgabe1%2084edba2d24c54654800c41f93a94f26a/Untitled.png](Referenz/Stundenplan+Notizen/Fächer%2069924945113d4f05aa161a69903bf2a7/LF05%20-%20Datenbank%20(ABO)%20fea7b1a68d4b4c0198fd08757a874b7f/LF05%20-%20Datenbank_Abgabe1%2084edba2d24c54654800c41f93a94f26a/Untitled.png)

**3.) Recherchieren Sie welche Datenbank Modelle es gibt (4 Modelle)
und sortieren Sie sie chronologisch !**

1. **Hirarchisches Model:** Das hierarchische Modell organisiert Daten in einer baumähnlichen Struktur, in der jeder Eintrag eine einzige übergeordnete Einheit oder einen Stamm hat.

    ![LF05%20-%20Datenbank_Abgabe1%2084edba2d24c54654800c41f93a94f26a/Bildschirmfoto_2020-09-11_um_18.06.58.png](Bildschirmfoto_2020-09-11_um_18.06.58.png)

2. **Objekt Orientiertes Modell (NoSQL):** 

    Dieses Modell definiert eine Datenbank als Ansammlung von Objekten oder wiederverwendbaren Software-Elementen mit assoziierten Funktionen und Methoden. Es gibt mehrere Arten von objektorientierten Datenbanken:

    Eine **Multimedia-Datenbank** enthält Medien wie zum Beispiel Bilder, die nicht in einer relationalen Datenbank gespeichert werden könnten.

    Eine **Hypertext-Datenbank** ermöglicht das Verweisen von Objekten auf andere Objekte. Sie eignet sich zum Organisieren vieler isolierter Daten, ist aber nicht gerade ideal für die numerische Analyse.

    Das objektorientierte Datenbankmodell ist das bekannteste post-relationale Datenbankmodell, da es Tabellen einschließt, aber nicht darauf beschränkt ist. Diese Modelle werden auch als hybride Datenbankmodelle bezeichnet.

    ![LF05%20-%20Datenbank_Abgabe1%2084edba2d24c54654800c41f93a94f26a/Bildschirmfoto_2020-09-11_um_12.16.20.png](Bildschirmfoto_2020-09-11_um_12.16.20.png)

    3. **Relationales Model:** Das Modell erfasst außerdem die Arten der Beziehungen zwischen diesen Tabellen, darunter 1:1-, 1:m-, und n:m-Beziehungen.

    ![LF05%20-%20Datenbank_Abgabe1%2084edba2d24c54654800c41f93a94f26a/Bildschirmfoto_2020-09-11_um_18.12.01.png](Bildschirmfoto_2020-09-11_um_18.12.01.png)

    4. **Entity-Relationship-Model:** 

    Dieses Modell erfasst die Beziehungen zwischen realen Entitäten auf ähnliche Weise wie ein Netzwerkmodell, ist aber nicht so direkt an die physische Datenbankstruktur gebunden. Stattdessen wird es oft für das konzeptionelle Datenbankdesign verwendet.

    Hier werden die Personen, Orte und Dinge, zu denen Datenpunkte gespeichert werden, als Entitäten bezeichnet. Jede davon hat bestimmte Attribute, die zusammen ihre Domäne bilden. Die Kardinalität bzw. die Beziehungen zwischen den Entitäten wird/werden ebenfalls dargestellt.

    ![LF05%20-%20Datenbank_Abgabe1%2084edba2d24c54654800c41f93a94f26a/Bildschirmfoto_2020-09-11_um_18.10.36.png](Bildschirmfoto_2020-09-11_um_18.10.36.png)

**4.) Welches Datenbankmodell hat Edgar F. Codd entwickelt und wann ?**

- Der Mathematiker Edgar J Codd entwickelte ende der 60er Anfang der 70er das ERM Model (relationales Modell)

**5.) Geben Sie die Anforderungen & Bedingungen an die ein DBS
erfüllen muss ! Welche davon sind zudem gesetzlich vorgeschrieben ?**

Gesetzlich wird **Datensicherheit** für Datenbanken gefordert

**Datensicherheit**: Die gesetzlich geforderte Datensicherheit umfasst:

- die Verfügbarkeit von Daten
- die Konsistenz von Daten
1. **Verfügbarkeit**: ist die Möglichkeit alle Daten eingeben, ändern, löschen und abfragen zu können. Erst wenn diese Möglichkeiten gegeben sind spricht man von einer Datenbank.
2. **Konsistenz & Integrität:** Eine Datenbank ist integer oder konsistent, falls sie Widerspruchsfreiheit garantiert. D.h. alle gespeicherten oder abgefragten Daten sind eindeutig und fehlerfrei.

Ebenfalls Mustitasking/Multiuser betrieb sind voraussetzungen für eine funktionierende Datenbank.

**6.) Ermitteln Sie für folgende Eigenschaften die Begriffe aus der**

Fachsprache für Datenbanken :

- Widerspruchsfreiheit - Konsistenz, Ist bei dem kein Widerspruch entsteht, also eine kein Ausdruck die nicht gleichzeitig negiert werden kann.
- Dauerhafte Speicherung - Persistenz, alles womit man Informationen sichern kann (Bsp. Papier, Bücher, USB-Stick aber auch die Speicherung aller Tonaufnahmen.)
- Gültigkeit, Richtigkeit - Integrität, beruht nicht auf Wahrheit, sondern auf logische Form.

### **b) Gleichen Sie Ihre Lösungen mit Ihrer Gruppe ab und laden Sie**

(jeder Schüler einzeln) die endgültige Lösung in Ihrem MOODLE
Account hoch!