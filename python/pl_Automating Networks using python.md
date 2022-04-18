Parent [[Pluralsight]]
reference: [[Python]]
#Lernen_next  

Www.pluralsight.com/courses/automating-networks-python

- [ ] kurs gucken! Automating networks with python


### Prerequisites:
Course:
- Into to Networking (CCNA)
- CCIE RS - MPLS

course is similar to:
![[Bildschirmfoto 2021-09-26 um 22.39.59.png]]
- ansible is a prepackaged task execution framework


### Write log to text

```python
concat_output=""

for comand in comands:
	send_cmd(conn, command)
	concat_output+=get_output(conn) # append the new messages to the concat_outpit variable
	
#open txt file and write the output messages from the console
with open(f"{hostname}_facts.txt","w") as handle:
	handle.write(concat_output)
```


### Use Python Debuger

breakpoint() # use this in for loop or other parts of the code

step through the code
use s to step
use n to jump to next itteration
use c to continue to next breakpoint
use locals() to display local variables
use quit to exit

## Introducing Infrastructure as code
Core IAS concepts
- state declaration, declare a state that the device soud have
- abstraction, IAC solution should have a common interface to use different devices in the same manaer
- version control, use the code files as a version control. See wo executes what on what device

Idempotent
- execute many times and not make unnecessary changes