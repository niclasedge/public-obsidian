parent: [[Dokumentation]]
tags: #todo 
Reference: [[Python]]
date::
status::
fazit::

---

```dataview
table date, status, fazit FROM [[Ausflüge]]
```


Setup:
install spinx
```
sphinx-quickstart
```
![[Bildschirmfoto 2021-09-01 um 12.57.41.png]]


## Neue Code Dateien hinzufügen
Man muss eine neue .rst Datei erstellen lassen, diese wird dann vom "make htm" mit genutzt

```
sphinx-apidoc -o /Users/niclasedge/projects/dw-5-script-workflow/dgk_reporting_code/docs /Users/niclasedge/projects/dw-5-script-workflow/dgk_reporting_code/
```

### Neue Sphinx html erstellen
```
sphinx-build -b html "/Users/niclasedge/projects/dw-5-script-workflow/dgk_reporting_code sqlite/docs" "/Users/niclasedge/projects/dw-5-script-workflow/dgk_reporting_code sqlite/"
```



https://samnicholls.net/2016/06/15/how-to-sphinx-readthedocs/

## Include your README and CHANGELOG



### Export PDF:
```
pip install rinohtype
```
```
sphinx-build -b rinoh . _build      
```


### convert .md to .rts

pandoc test.md -f markdown -t rst -o test.rst



#### Syntax

### Template für Documenting:
```python
"""

:Zweck: Diese Funktion kann abgerufen werden, und gibt Datumswerte für Jahr, Monat und Quartal aus.

:Wie: Das datetime standart python modul wird hauptsächlich genutzt.

:param input: Ein Datumswert.

:param output: Ein Wochen/Monats/Quartalswert für das angegebene Datum. Zur weiteren Nutzung zur erstellung von SQL Befehlen für das jeweilige Datum.

  

:Beispielnutzung:

>>> jahr=str(Datum.jahr), kw=str(Datum.woche), quartal=str(Datum.quartal), monat=str( Datum.monat), letzter_monat=str(Datum.letzter_monat)

  

.. todo:: Notizen für die Funktion erstellen

"""
```

![[Bildschirmfoto 2021-09-18 um 09.30.37.png]]


## Examples
[](https://docs.typo3.org/m/typo3/docs-how-to-document/master/en-us/WritingReST/Admonitions.html#examples "Permalink to this headline")

### See also

.. seealso::
   `Admonitions <http://docutils.sourceforge.net/0.7/docs/ref/rst/directives.html#admonitions>`__


### Note

.. note::
   A note



### Tip

.. tip::
   A tip


### Important

.. important::
   Some important information which should be considered.



### Warning

.. warning::
   Some text pointing out something that people should be warned about.



### Attention

.. attention::
   A attention
