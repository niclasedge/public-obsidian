parent: [[Python]]
tags: #Lernen_next 
aliases: 
Reference:

---

## Create a class
```python
class Employee():
	emp_number=0 # Globale variable wird definiert
	raise_amount = 1.04  # class variable
	def __init__(self,first,last,pay): # Method
		self.first = first
		self.last = last
		self.pay = pay
		self.email = first+last+"@company.com"
		Employee.emp_number += 1  #ruf die globale variable auf und ändert sie, immer wenn die class aufgerufen wird
		
	def fullname(self): # Method
		return first+last
	
	def apply_raise(self):
		self.pay = int(self.pay * Employee.raise_amount) # class variable in einer Method aufrufen
```
### Objekte durch eine Class erstellen
```python
# ein Objekt erstellen:
emp1= Employee('Niclas', 'Edge', '50000')
emp2= Employee('Peter', 'Edge', '60000')
```
### Objekte und methoden einer class abrufen
```python
#gleiches Ergebnis, andere 
emp1.fullname() # objekt und Method aufrufen
Employee.fullname(emp1) # erst wird die class gerufen, dann die Methode und dann das objekt
```
### Class variables
```python
print(emp1.__dict__) # Zeigt alle daten des Objektes an

# class variable für ein Objekt ändern:
emp1.raise_amount = 1.5 # gilt nur für ein definiertes objekt

# globale class variable:
emp1.raise_amount = 1.5 # gilt nur für ein definiertes objekt
```

	

### Corey Schaefer Tutorial Series
https://www.youtube.com/watch?v=ZDa-Z5JzLYM&list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc

**ToDo:**
- [ ] Python OOP Tutorial 3: classmethods and staticmethods
- [ ] Python OOP Tutorial 4: Inheritance - Creating Subclasses
- [ ] Python OOP Tutorial 5: Special (Magic/Dunder) Methods
- [ ] Python OOP Tutorial 6: Property Decorators - Getters, Setters, and Deleters