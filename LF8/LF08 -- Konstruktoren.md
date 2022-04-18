parent: [[LF08 - Anwendungsentwicklung]]

--
![[I_Konstruktoren.pdf]]

Konstruktoren
- haben den gleichen Namen wie die Klasse
- hat keinen Rückgabewert, "void" ist nicht nötig

Konstrutor mit Übergabewert
```c#
public Person(string n, string m) 
{
	this.vorname = n;
	this.nachname = m;
}
```

![[A_Konstruktoren.pdf]]

Klassen haben:
- attribute 
- **methoden**
	- kann einen Rückgabewert haben
- **konstrukoren**, errstellt oder verändert daten
	- muss den gleichen Namen haben wie die Klasse
	- muss beim erzeugen aufgerufen werden, mit new
	- können keinen rückgabewert ausgeben

### Instanzattribute
- ähnlich wie in python variablen

### Klassenattribute
- static
- ist für die ganze klasse gleich

### Instanzmethode
```c#
Drucke objFilm01.GetTitle()
```