parent: [[LF03 - Clients in Netzwerke einbinden]]
tags:
aliases: 
Reference:

---
# Abgabe_Netwerkdokumentation

21.9.2020

**Niclas Edge, Marvin Berger, Jonas Richter, Ege Bayro**

# Inhaltsverzeichnis

# IP – Internet Pool:

- 32- 128 stellige Binärzahl
- Eindeutige Adressierung
- Aufbau einer Kommunikationsverbindung

### Wo kommt die IP Adresse her?

- Adresse in Computernetzen, die auf dem Internetprotokoll basiert
- Macht Geräte adressierbar
- Mehrere IP Adressen können einem Gerät zugewiesen werden
- Kommt von einem Internet-Provider (Router)

## IP Versionen:

- **IPv4-Adressen** bestehen aus 32 Bits (4 Oktetten (Bytes))
    - 32-Bit-Adressen (z.B. 10000010010111100111101011000011)
    - 4 Blöcke mit Punkt getrennt ( 130.94.122.195)
- **IPv6-Adressen** bestehen aus 128 Bit
- Wird zur Speicherung der Adressen verwendet
    - Beispiel: 2001:db8:85a3::8a2e:370:7344

Damit ein PC im Netzwerk kommunizieren kann, braucht er von einem Internet-Provider eine IPv4 Adresse

**Lösung eines IPv4 Adressen Problems:**

Viele Geräte benötigen keine fix zugeteilte IP Adresse, da sie nicht permanent im Netz sind

**Aufteilung:**

- Netzwerk- und Hostteil
- Netzwerkteil der Adresse gleich = Rechner sind im selben Netz

130.94.122.195

**Verwaltung des Netzwerk-Adress-Teils:**

- Vergibt der Besitzer des Netzwerks
- Mehrere Netze, 1 Router
- IANA ( Internet Assigned Numbers Authority) zuständig für Vergabe

130.94.122.195

**Verwaltung Host-Adress-Teils:**

- Vergibt der Administrator (Keine doppelte Host Adresse/DHCP)

## Netzklassen:

- Seit 1993 bitvariable Routing-Verfahren
- Bestimmt die Standardnetzmaske der BS
- Maximalanzahl der Host-Adressen: 2^Anzahl Bits der Hostadresse – 2
- 2 Host-Adressen fallen weg

## Subnetz:

- Sorgt für eine Abgrenzung (eines vom Subnetz erfassten Bereich)

Subnetzmaske 255.255.255.0

Adresse: 192.168.1.23 vs 192.168.2.34

- Beide Adressen befinden sich nicht im selben Netz

Diese Adressen werden mit einem logischen „UND“ verknüpft

# DNS - Domain Name Service

### Die gelben Seiten des Internets

DNS löst IP Adressen in Internetadressen auf und umgekehrt

**Einstellung des internen DNS Servers:**

- Automatische IP Vergabe eingestellt
- Verbundene Rechner bekommen so eine Automatische IP Adresse vom DNS Server

![Abgabe_Netwerkdokumentation%20aaf5a2c271a748c9aed76904d38fa85c/Untitled.png](Referenz/Stundenplan+Notizen/Fächer%2069924945113d4f05aa161a69903bf2a7/LF03%20-%20Clients%20in%20Netzwerke%20einbinden%20(APRA)(WAEC)%2028e92381aac34159bd0c8bb1686f4f65/Abgabe_Netwerkdokumentation%20aaf5a2c271a748c9aed76904d38fa85c/Untitled.png)

## DHCP - Dynamic Host Configuration

### Zuweisung der IP Adressen im Netz

- weist einem Host automatisch TCP/IP-Daten zu

Ein Client kann ohne weiteres konfigurieren in ein bestehendes Netzwerk eingebunden werden.

- Läuft in dem Netz ein DHCP-Server, so antwortet er mit einem Satz von Konfigurationsparametern, mit denen der Host seine TCP/IP-Konfiguration durchführt

![Abgabe_Netwerkdokumentation%20aaf5a2c271a748c9aed76904d38fa85c/Untitled%201.png](Referenz/Stundenplan+Notizen/Fächer%2069924945113d4f05aa161a69903bf2a7/LF03%20-%20Clients%20in%20Netzwerke%20einbinden%20(APRA)(WAEC)%2028e92381aac34159bd0c8bb1686f4f65/Abgabe_Netwerkdokumentation%20aaf5a2c271a748c9aed76904d38fa85c/Untitled%201.png)

# Netzwerk Verkabelung

## DIN EN 50173

**Internationale Definition für:**

Anwendungsneutrale Verkabelungssysteme

- Definiert Anforderungen an Kupferkabel
- Definiert Anforderung an Lichtwellenleiter für die Verbindungstechnik

**Geltungsbereiche**:

- Geländeverkabelung
- Gebäudeverkabelung
- Etagenverkabelung

![Abgabe_Netwerkdokumentation%20aaf5a2c271a748c9aed76904d38fa85c/Untitled%202.png](Referenz/Stundenplan+Notizen/Fächer%2069924945113d4f05aa161a69903bf2a7/LF03%20-%20Clients%20in%20Netzwerke%20einbinden%20(APRA)(WAEC)%2028e92381aac34159bd0c8bb1686f4f65/Abgabe_Netwerkdokumentation%20aaf5a2c271a748c9aed76904d38fa85c/Untitled%202.png)

## Strukturierte Verkabelung

Eine strukturierte Verkabelung oder universelle Gebäudeverkabelung (UGV) ist ein einheitlicher Aufbauplan für eine zukunftsorientierte und anwendungsunabhängige Netzwerkinfrastruktur, auf der unterschiedliche Dienste (Sprache oder Daten) übertragen werden. Damit sollen teure Fehlinstallationen und Erweiterungen vermieden und die Installation neuer Netzwerkkomponenten erleichtert werden.

Eine strukturierte Verkabelung basiert auf einer allgemein gültigen Verkabelungsstruktur, die auch die Anforderungen mehrerer Jahrzehnte berücksichtigt, Reserven enthält, flexibel erweiterbar ist und unabhängig von der Anwendung genutzt werden kann. So ist es üblich, dieselbe Verkabelung für das lokale Netzwerk und die Telefonie zu benutzen.

## Bestandteile einer strukturierten Verkabelung

- standardisierte Komponenten, wie Leitungen und Steckverbindungen
- hierarchische Netzwerk-Topologie (Stern, Baum, Ring, Bus, Linie, Vermascht, Vollvermascht)
- Empfehlungen für Verlegung und Installation
- standardisierte Mess-, Prüf- und Dokumentationsverfahren

**Ziele einer strukturierten Verkabelung**

- Unterstützung aller aktuellen und zukünftigen Kommunikationssysteme
- Kapazitätsreserve hinsichtlich der Grenzfrequenz
- das Netz muss sich gegenüber dem Übertragungsprotokoll und den Endgeräten neutral verhalten
- flexible Erweiterbarkeit
- Ausfallsicherheit durch sternförmige Verkabelung
- Datenschutz und Datensicherheit müssen realisierbar sein
- Einhaltung existierender Standards

**Normen für die strukturierte Verkabelung**

[Untitled](Untitled%20Database%20ca4589d7d7f44befa968849cfbb67eb7.csv)

## TIA/EIA 568 B.1 (2001) / B.2 1 (2001)

TIA/EIA haben ihren Ursprung in der Spezifikation ungeschirmter Kupfer-Anschluss-Komponenten. TIA/EIA ist keine weltweit gültige Norm, sondern eine Industriespezifikation, die für den nordamerikanischen Markt gültig ist. Es sind darin jedoch auch die Anforderungen von EN (Europa-Norm) oder ISO/IEC (weltweit) bei den Übertragungseigenschaften der Leitungen und Steckverbindungen enthalten. Weshalb diese Norm oft weltweit eingehalten wird.

**ISO/IEC 11801 (2002) und EN 50173-1 (2003)**

In der Europa-Norm (EN) und dem weltweit gültigen ISO-Standard erfolgt die Strukturierung in Form von Hierarchieebenen. Diese Ebenen werden von Gruppen gebildet, die topologisch oder administrativ zusammengehören.

Die Verkabelungsbereiche sind in Geländeverkabelung (Primärverkabelung), Gebäudeverkabelung (Sekundärverkabelung) und Etagenverkabelung (Tertiärverkabelung) gegliedert. Die Verkabelungsstandards sind für eine geografische Ausdehnung von 3.000 m, einer Fläche von 1 Mio. qm und für 50 bis 50.000 Anwender optimiert. In jedem Verkabelungsbereich sind maximal zulässige Kabellängen festgelegt und bei der Installation einzuhalten. Viele Übertragungstechniken beziehen sich auf die definierten Kabellängen und Qualitätsanforderungen.

Hinweis: Bei allen ISO-Standards handelt es sich um Handlungsempfehlungen. Die Einhaltung einer ISO-Norm ist freiwillig. In der Regel wird die Einhaltung der ISO-Standards von verschiedenen Seiten, zum Beispiel Kooperationspartnern, Herstellern und Kunden, gefordert.

### Primärverkabelung - Geländeverkabelung

Der Primärbereich wird als Campusverkabelung oder Geländeverkabelung bezeichnet. Er sieht die Verkabelung von einzelnen Gebäuden untereinander vor. Der Primärbereich umfasst meist große Entfernungen, hohe Datenübertragungsraten, sowie eine geringe Anzahl von Stationen.
Für die Verkabelung wird in den meisten Fällen Glasfaserkabel (50 µm) mit einer maximalen Länge von 1.500 m verwendet. In der Regel sind es Glasfaserkabel mit Multimodefasern oder bei größeren Entfernungen auch Glasfaserkabel mit Singlemodefasern. Für kleinere Entfernungen werden auch schon mal Kupferkabel verwendet.
grundsätzlich gilt, den Primärbereich großzügig zu planen. Das bedeutet, das Übertragungsmedium muss bezüglich Bandbreite und Übertragungsgeschwindigkeit nach oben hin offen sein. Dasselbe gilt auch für das eingesetzte Übertragungssystem. Als Faustregel gilt 50 Prozent Reserve zum derzeitigen Bedarf der Investition.

### Sekundärverkabelung - Gebäudeverkabelung

Der Sekundärbereich wird als Gebäudeverkabelung oder Steigbereichverkabelung bezeichnet. Er sieht die Verkabelung von einzelnen Etagen und Stockwerken untereinander innerhalb eines Gebäudes vor. Dazu sind vorzugsweise Glasfaserkabel (50 µm), aber auch Kupferkabel mit einer maximalen Länge von 500 m vorgesehen.

### Tertiärverkabelung - Etagenverkabelung

Der Tertiärbereich wird als Etagenverkabelung bezeichnet. Er sieht die Verkabelung von Etagen- oder Stockwerksverteilern zu den Anschlussdosen vor. Während sich im Stockwerksverteiler ein Netzwerkschrank mit Patchfeld befindet, mündet das Kabel am Arbeitsplatz des Anwenders in einer Anschlussdose in der Wand, in einem Kabelkanal oder in einem Bodentank mit Auslass.
Für diese relativ kurze Strecke sind Twisted-Pair-Kabel vorgesehen, deren Länge auf 90 m, zzgl. 2 mal 5 m Anschlusskabel, mit einer Gesamtlänge von 100 m begrenzt ist. Alternativ kommen auch Glasfaserkabel (62,5 µm) zum Einsatz.

### Elemente der strukturierten Verkabelung

- Patchfeld (Patchpanel)
- Patchkabel
- Anschlussdosen
- Netzwerkkabel
- Verteilerschränke

Quelle : [https://www.elektronik-kompendium.de/sites/net/0908031.htm](https://www.elektronik-kompendium.de/sites/net/0908031.htm) (Zugriff 12:12)

# Kabel Wiki – Twisted -Pair-Kabel

### Leitungsaufbau:

- Besteht aus zwei miteinander verseilten Einzeladern
- Ader besteht aus Kunststoffisolierter Kupferleiter
- Je zwei Adern sind zu einem Paar verseilt
- Beidraht dient als elektrische Masseleitung
- Füllader besteht aus Kunststoff, um Hohlräume auszufüllen
- Trennelemente auch Kunststoff um auseinander zu halten

### Schirmung:

- Zwei- und vierpaarige Ausführung
- Heutzutage fast nur noch vierpaarige Schirmungen Neues Beziehungs-Schema: XX/YZZ (vierpaarige Aufführung)
- XX = Gesamtschirmung
- U= Ungeschirmt, F = Foliengeschirmt, S = Geflechtschirm, SF = Geflecht- und Folienschirm
- Y = Aderpaarschirmung, U = Ungeschirmt, F = Foliengeschirmt, S = Geflechtschirm
- ZZ = TP (TP = Twisted Pair)

### Kategorien:

- Kategorie 1: maximale Betriebsfrequenz bis 100kHz (Sprachübertragung)
- Kategorie 2: maximale Frequenzen bis 1,5 MHz (Hausverkabelung bei ISDN)
- Kategorie 3: maximale Betriebsfrequenzen bis 16 MHz (Telefonkabel (höherer Widerstand))
- Kategorie 4: maximale Übertragungsrate von 20 Mbit/s (Cat-4 wurde nicht verwendet wegen Cat- 5)
- Kategorie 5: für Signalübertragung mit hohen Datenübertragungsraten (100 MHz)
    - Wurde häufig für Fast- oder Gigabit-Ethernet verwendet
- Kategorie 6: für Betriebsfrequenzen bis 250 MHz (Sprach- und Datenübertragung & Multimedia, ATM-Netze)
- Kategorie 7: Betriebsfrequenzen bis 600 MHz (geeignet für 10-Gigabit-Ethernet)

# Ethernet

- Kabelgebundene Datenübertragungstechnologie in LAN
- Beschreibt Signalisierung für Bitübertragungsschicht
- Legt Paketformate und Protokolle fest
- Weitverbreitetster Netzwerkstandard

## IEEE 802.3 / Ethernet-Grundlagen

Ethernet ist eine Familie von Netzwerktechniken, die vorwiegend in lokalen Netzwerken (LAN), aber auch zum Verbinden großer Netzwerke (WAN) zum Einsatz kommt.
Für Ethernet gibt es eine Vielzahl an Standards, für die das Institute of Electrical and Electronics Engineers (IEEE) verantwortlich ist.

Das ursprüngliche Konzept von Ethernet sah die Vernetzung von Bürogeräten vor. Inzwischen ist Ethernet das Synonym für ein lokales Netzwerk. Die unter der Arbeitsgruppe 802.3 vorgeschlagenen und standardisierten Spezifikationen umfassen eine Vielzahl von Varianten und Anwendungsfälle.

- Ethernet für LAN in Wohnungen und Rechenzentrum
- Carrier Ethernet für MAN und WAN
- Industrial Ethernet für Produktionsumgebungen
- Ethernet in Fahrzeugen

# Einordnung in das OSI-Schichtenmodell

[Untitled](Untitled%20Database%207d5a4e8a4ad149c1b13b240c124ce79f.csv)

Bei Ethernet spricht man von einer paketvermittelnden Netzwerktechnik, deren Standards auf den Schichten 1 und 2 des OSI-Schichtenmodells die Adressierung und die Zugriffskontrolle auf unterschiedliche Übertragungsmedien definieren. Die Nutzdaten kommen bereits in Datenpaketen von den darüberliegenden Protokollen. Zum Beispiel von TCP/IP. Diese Datenpakete werden mit einem Header versehen und anschließend im Ethernet-Netzwerk übertragen.
Die Ethernet-Standards auf der OSI-Schicht 2 sind die LLC- und MAC-Teilschichten. Sie sind unabhängig von Ethernet und werden auch für andere Übertragungstechniken verwendet. Zum Beispiel Bluetooth (IEEE 802.15) oder WLAN (IEEE 802.11).

Alle Ethernet-Varianten haben eines gemeinsam: Sie basieren auf denselben Prinzipien, die ursprünglich in den Standards 802.1, 802.2 und 802.3 festgelegt wurden. Ethernet ist unter 802.3 standardisiert und baut auf 802.1 und 802.2 auf.

## Geschichtlicher Hintergrund

Ursprünglich wurde Ethernet in den siebziger Jahren im PARC (Palo Alto Research Center), im Forschungslabor der Firma Xerox, entwickelt. In Zusammenarbeit mit den Firmen DEC und Intel wurde Ethernet später zu einem offenen Standard. Dieser Standard bildete dann die Grundlage für den offiziellen 802.3-Standard des IEEE (Institute of Electrical and Electronics Engineers).

Neben Ethernet gab es mehrere Techniken für die Vernetzung. Zum Beispiel Token Ring (auf Basis von Koaxialkabel) und FDDI (auf Basis von Glasfaserkabel). Irgendwann in den 1990er Jahren hat sich Ethernet durchgesetzt. Insbesondere der einfache und kostengünstige Aufbau eines Ethernet-Netzwerks sorgte für die rasche Verbreitung auf der ganzen Welt. Von Arcnet, Token Ring, FDDI oder gar ATM und SDH spricht man heute fast nicht mehr. Heute werden fast alle Vernetzungen im LAN und WAN mit Ethernet-Technik realisiert.

## Technischer Hintergrund

Einer der Vorläufer von Ethernet war ein Funknetz mit dem Namen ALOHA, das die Hawaii-Inseln miteinander verbunden hat. Hier war das Übertragungsmedium die Luft (Äther bzw. Ether). Ethernet wurde für die gemeinsame Nutzung eines Übertragungsmediums durch viele Hosts entwickelt. Während es für ALOHA die Luft war, wurde für Ethernet als Übertragungsmedium ein Koaxialkabel gewählt, das die Rechner in einer Bus-Topologie miteinander verbunden hat.
Für die Übertragungstechnik bedeutet das, dass es nur einen Übertragungskanal gibt, den nur einer nutzen kann. Ein Zugriffsverfahren bzw. Übertragungsprotokoll muss deshalb nach dem Prinzip Listen-before-Talk (LBT) arbeiten.
Angefangen hat man in den 1980er Jahren mit 10-Megabit-Ethernet über Koaxialkabel. Es folgten verschiedene Weiterentwicklungen für Twisted-Pair-Kabel und Glasfaserkabel mit geringeren und höheren Übertragungsraten auf längeren und kürzeren Kabeln.

## Übertragungsmedium und Netzwerk-Topologie

Das ursprüngliche Ethernet basiert auf einem Koaxialkabel als Übertragungsmedium. Dabei wurden mit einem Kabel mehrere Stationen hintereinander zu einer Kette verbunden. Die Netzwerk-Topologie hat man als Bus bezeichnet.
Später wurden weitere Ethernet-Varianten für Backplanes, Twinax-Kabel, Glasfaser und Twisted-Pair entwickelt.

Der entscheidende Durchbruch von Ethernet im LAN kam durch den Umstieg von Shared- auf Switched-Media (von Bus zu Stern-Topologie) in Verbindung mit einer strukturierten Verkabelung. Gleichzeitig hat die konsequente Rückwärtskompatibilität dazu geführt, dass Investitionen bis zu einem gewissen Grad zukunftsfähig blieben. Alte Komponenten für 10 und 100 MBit/s können mit Komponenten für 1 GBit/s kombiniert werden. Im Zweifelsfall bedarf es nur eines Medienkonverters.

# Übertragungstechnik

Ethernet transportiert Daten paketweise ohne festes Zugriffsraster. Damit unterscheidet sich Ethernet von anderen paketorientierten Systemen, die mit einem festen Zeitraster jedem Teilnehmer eine Mindestbandbreite garantieren können. Deshalb bereitet Ethernet Probleme bei allen Arten von zeitkritischen Anwendungen. Bei Ethernet gibt es keine Garantie, dass die Daten innerhalb einer bestimmten Zeit den Empfänger erreichen. Das bedeutet, der Erfolg einer Übertragung ist nicht sicher. Er unterliegt nur einer gewissen Wahrscheinlichkeit. So verwerfen Ethernet-Komponenten Datenpakete, wenn nicht genug Bandbreite zur Verfügung steht.
Wegen der unzuverlässigen Übertragungstechnik ist Ethernet auf Fehlerbehandlung höherer Protokolle angewiesen. Das ist auch ein Grund, warum in bestimmten Bereichen heute noch andere Vernetzungstechniken bevorzugt werden. Im Vergleich dazu ist Ethernet eine einfach zu implementierende Vernetzungstechnik, die sich über Jahrzehnte hinweg in lokalen Netzwerken bewährt und durchgesetzt hat.

## Übertragungsgeschwindigkeit

Die tatsächliche Übertragungsgeschwindigkeit (Netto-Datenrate) von Ethernet hängt von der Geschwindigkeitsstufe und der TCP-Verbindungsqualität ab.

- Bei Fast Ethernet mit 100 MBit/s erreicht man knapp 0,094 MBit/s, also ca. 10 MByte/s.
- Bei Gigabit Ethernet mit 1 GBit/s erreicht man knapp 0,94 GBit/s, also ca. 100 MByte/s.
- Bei Gigabit Ethernet mit 2,5 GBit/s erreicht man knapp 2,4 GBit/s, also fast 300 MByte/s.
- Bei Gigabit Ethernet mit 10 GBit/s erreicht man netto 9,4 GBit/s, also umgerechnet etwas über 1.100 MByte/s.

Diese Geschwindigkeitsangaben entsprechen in etwa den zu erwartenden Durchsätzen für HTTP-Verbindungen, FTP-Downloads und Windows-Freigaben.
Die Differenz zwischen der Brutto- und Netto-Datenrate geht für die Protokoll-Header auf Layer 2 und 3 drauf.

Zum Vergleich die Übertragungsgeschwindigkeit von PC-Schnittstellen:

- USB 2.0: ca. 40 MByte/s
- USB 3.0: ca. 450 MByte/s
- SATA-Festplatten: ca. 500 MByte/s
- PCIe-SSDs: über 3.000 MByte/s

## Erweiterungen

Erweiterungen wandeln das anfangs kollisionsbehaftete Übertragungsprotokoll zu einer sicheren, redundanten, vielseitigen und schnellen Vernetzungstechnik.

- Energy Efficient Ethernet (EEE)
- hochauflösende Zeitsynchronisation (IEEE 1588v2)
- Verschlüsselung auf MAC-Ebene (MACSec)
- Energieversorgung bis 100 Watt (PoE)
- Trunking bzw. Link Aggregation
- Übertragung auf nur einem Adernpaar (Single Pair)
- Einsatz als Feldbus
- Storage-Anbindung

## CSMA / CD

Der englische Begriff Carrier Sense Multiple Access/Collision Detection bezeichnet ein asynchrones Medienzugriffsverfahren, das den Zugriff verschiedener Stationen auf ein gemeinsames Übertragungsmedium regelt.

Vom Ethernet benutzte Zugriffsverfahren

CS Carrier Sense

MA Multiple Access

CD Collision Detection

- Carrier Sense (Träger-Zustandserkennung): Jede Station prüft, ob das Übertragungsmedium frei ist.
- Multiple Access (Mehrfachzugriff): Mehrere Stationen teilen sich das Übertragungsmedium.
- Collision Detection (Kollisionserkennung): Wenn mehrere Stationen gleichzeitig senden, erkennen sie die Kollision.

**Ablauf von CSMA/CD**

Das ursprüngliche Ethernet entspricht einer Bus-Topologie an der mehrere Stationen angeschlossen sind (Multiple Access). Festgelegt ist, dass alle Stationen die Signale auf dem Bus lesen, aber nicht gleichzeitig senden dürfen. Welche der angeschlossenen Stationen senden darf, wird durch das CSMA/CD-Verfahren bestimmt, das nach dem Prinzip "Listen-before-Talk" arbeitet.

Alle Stationen hören permanent das Übertragungsmedium ab (Carrier Sense). Sie können zwischen einem freien und einem besetzten Übertragungsmedium unterscheiden. Bei einem freien Übertragungsmedium darf gesendet werden. Will eine Station senden, prüft sie, ob der Bus frei ist. Ist er frei, so beginnt die Station zu senden. Das bedeutet, sie legt das Datensignal auf den Bus.

Während der Signalübertragung überprüft die Station, ob das gesendete Signal mit dem Signal auf dem Bus identisch ist. Entspricht das gesendete Signal nicht dem abgehörten Signal, dann hat eine andere Station gleichzeitig gesendet. Die beiden Signale überlagern sich. Diesen Zustand auf dem Übertragungsmedium bezeichnet man als Kollision. Durch permanentes Prüfen des Zustands auf der Leitung kann diese Kollision erkannt werden (Collision Detection).

Wurde eine Kollision erkannt, dann wird die Übertragung abgebrochen. Der Sender, der das Störsignal zuerst entdeckt, sendet ein spezielles Signal, damit alle anderen Stationen wissen, dass das Netzwerk blockiert ist. Nach einer zufälligen Wartezeit wird wieder geprüft, ob der Bus frei ist. Ist das der Fall, wird von neuem gesendet. Der Vorgang wird so oft wiederholt, bis die Daten ohne Kollision übertragen wurden.

Konnte die Übertragung ohne Kollisionserkennung beendet werden, dann gilt die Übertragung als erfolgreich. Kamen die Daten aus irgendwelchen Gründen beim Empfänger nicht an, dann müssen diese Daten durch Protokolle, wie z. B. TCP, neu angefordert werden. Tritt dies häufiger auf, werden mehr Datenpakete gesendet. Das drückt auf die effektive Übertragungsgeschwindigkeit des Netzwerks.

**Kollisionen**

Grundsätzlich sind Kollisionen nicht als Störungen anzusehen. Kollisionen gehören im Listen-before-Talk-Betrieb zum normalen Betriebsablauf. Allerdings werden Kollisionen zu einem Problem, wenn sie Überhand nehmen. Die Anzahl der Kollisionen steigt, je mehr Stationen auf das Übertragungsmedium Zugriff haben wollen.

Durch lange Leitungen, sehr viele Stationen und Repeater (Signalaufbereiter und -verstärker) entstehen je nach Ort der Einspeisung unterschiedliche Signallaufzeiten. Sie führen dazu, dass eine Station ein freies Übertragungsmedium feststellt und ihr Signal sendet, obwohl das Signal einer anderen Station bereits unterwegs ist. Es kommt zur Kollision, also der Überlagerung von zwei Signalen.

Durch CSMA/CD ergeben sich Grenzwerte für die maximale Signallaufzeit und die Rahmengröße (Datenpaket bzw. Frame). Beides darf nicht überschritten werden. Solange die Bandbreite von Ethernet nicht mehr als 30% ausgereizt wird, machen sich Kollisionen kaum bemerkbar. Mit steigender Belastung des Netzwerks nehmen aber auch die Kollisionen zu. Hier hilft nur, die Anzahl der Stationen zu reduzieren oder das gesamte Netzwerk in Teilnetz aufzuteilen.

Wegen der Kollisionen ist es nicht möglich, die theoretische Übertragungskapazität voll auszuschöpfen. In der Praxis liegt die Nominalleistung im günstigsten Fall bei etwa 70%. Unter ungünstigeren Bedingungen sind es unter 30%. Deutlich darunter bricht das Netzwerk praktisch zusammen. Die Ursache ist einfach: Je mehr Rechner in einem Netzwerk aktiv sind, desto mehr Kollisionen treten auf. Und so sinkt der erzielbare Datendurchsatz ständig ab.

**Kollisionsdomäne**

Die Kollisionsdomäne (collision domain) umfasst ein Netzwerk oder auch nur ein Teilnetzwerk aus Leitungen, Stationen und Kopplungselementen der Schicht 1 (OSI-Referenzmodell). In der Kollisionsdomäne müssen die Kollisionen innerhalb einer bestimmten Zeit jede Station erreichen. Das ist die Bedingung, damit das CSMA/CD-Verfahren funktionieren kann. Ist die Kollisionsdomäne zu groß, dann besteht die Gefahr, dass sendende Stationen Kollision nicht bemerken können. Aus diesem Grund ist die maximale Anzahl der Station in einer Kollisionsdomäne auf 1.023 Stationen begrenzt. Außerdem gilt, dass sich maximal zwei Repeater-Paare zwischen zwei beliebigen Stationen befinden dürfen.

Um die Bedingungen für eine einwandfrei funktionierende Kollisionsdomäne einhalten zu können, wurde die 5-4-3-Repeater-Regel definiert: Es dürfen nicht mehr als fünf (5) Kabelsegmente verbunden sein. Dafür werden maximal vier (4) Repeater eingesetzt. An nur drei (3) Segmenten dürfen Endstationen angeschlossen sein.

**Hinweis:** Die Repeater-Regel gilt für 10Base2 und 10Base5 (Koaxialkabel-Netzwerk). In Twisted-Pair-Netzwerken muss man die Repeater-Regel nur beim Einsatz von Hubs beachten. Durch den konsequenten Einsatz von Switches und Routern geht man den Problemen durch das CSMA/CD-Verfahren aus dem Weg.

Wie kann man Kollisionen verhindern?

**Grundsätzlich:** Je weniger Stationen sich in einer Kollisionsdomäne befinden, desto weniger Kollisionen können auftreten.

Um Kollisionen zu vermeiden und einen höheren Datendurchsatz zu erreichen, wird ein Netz auf der Schicht 2 in mehrere Teilnetze (Subnetze) aufgeteilt. Bei der Zusammenstellung der Teilnetze ist es sinnvoll die Stationen in einem Teilnetz zusammenzuschließen, die viel miteinander kommunizieren.
Wenn man ein logisches Netz mit Switche oder Bridges aufteilt, entstehen mehrere Kollisionsdomänen. Innerhalb einer Kollisionsdomäne befindet sich dann eine einzelne Station, ein weiterer Switch oder ein Router in ein anderes Netz. Die Einrichtung von Kollisionsdomänen reduziert den Datenverlust durch Kollisionen. Das wiederum reduziert den Netzwerkverkehr, der durch wiederholte Übertragungen verursacht wird.

Wenn man generell nur mit Switche arbeitet, wird der Begriff Kollisionsdomäne nicht mehr verwendet. In einem Switch bildet jeder Port und der mit einem Kabel verbundenen Station eine eigene Kollisionsdomäne. Es handelt sich dabei um eine Punkt-zu-Punkt-Verbindung. Der Switch sorgt dafür, dass nur die Datenpakete an den Port weitergeleitet werden, über den die Ziel-MAC-Adresse des Pakets erreichbar ist.

**Halbduplex und Vollduplex**

Halbduplex-Ethernet basiert auf dem CSMA/CD-Verfahren. Es handelt sich dabei um das ursprüngliche Ethernet bis 10 MBit/s. Vollduplex-Ethernet ist eine Weiterentwicklung, die als Fast Ethernet bezeichnet wird und auf CSMA/CD verzichtet. Auch alle weiteren Ethernet-Entwicklungen arbeiten im Vollduplex-Betrieb. Die Stationen kommunizieren über Punkt-zu-Punkt-Verbindungen direkt miteinander.
Weil Fast Ethernet in der Regel im Vollduplex-Modus arbeitet und damit auf CSMA/CD verzichtet, ist eine zusätzliche Flusskontrolle erforderlich. Dafür gibt es einen eigenen Standard: IEEE 802.3x (Flow Control).

# Kabel Wiki – Twisted -Pair-Kabel

### Leitungsaufbau:

- Besteht aus zwei miteinander verseilten Einzeladern
- Ader besteht aus Kunststoffisolierter Kupferleiter
- Je zwei Adern sind zu einem Paar verseilt
- Beidraht dient als elektrische Masseleitung
- Füllader besteht aus Kunststoff, um Hohlräume auszufüllen
- Trennelemente auch Kunststoff um auseinander zu halten

### Schirmung:

- Zwei- und vierpaarige Ausführung
- Heutzutage fast nur noch vierpaarige Schirmungen

Neues Beziehungs-Schema: XX/YZZ (vierpaarige Aufführung)

- XX = Gesamtschirmung
- U= Ungeschirmt, F = Foliengeschirmt, S = Geflechtschirm, SF = Geflecht- und Folienschirm
- Y = Aderpaarschirmung, U = Ungeschirmt, F = Foliengeschirmt, S = Geflechtschirm
- ZZ = TP (TP = Twisted Pair)

### Kategorien:

Kategorie 1: maximale Betriebsfrequenz bis 100kHz (Sprachübertragung)

Kategorie 2: maximale Frequenzen bis 1,5 MHz (Hausverkabelung bei ISDN)

Kategorie 3: maximale Betriebsfrequenzen bis 16 MHz (Telefonkabel (höherer Widerstand))

Kategorie 4: maximale Übertragungsrate von 20 Mbit/s (Cat-4 wurde nicht verwendet wegen Cat- 5)

Kategorie 5: für Signalübertragung mit hohen Datenübertragungsraten (100 MHz)

Wurde häufig für Fast- oder Gigabit-Ethernet verwendet

Kategorie 6: für Betriebsfrequenzen bis 250 MHz (Sprach- und Datenübertragung & Multimedia, ATM-Netze)

Kategorie 7: Betriebsfrequenzen bis 600 MHz (geeignet für 10-Gigabit-Ethernet)