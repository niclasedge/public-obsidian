'''
# U9 a
s = "Hello World"
print(s[1:4])
print(s[6:len(s)])
print(s[:])
print(s[1:100])
print(s[1:-1])
print(s[-3:])
print(s[:-3])

prefixes = "JKLMNOPQ"
suffix = "ack"
nl = ""
for letter in prefixes:
    print(letter + suffix + nl)
    nl += "\n"


txt = "Hello, welcome to my world."
x = txt.find("e", 5, 10)
print(x)

word = 'abcdefghijklmnopqrstuvwxyz'
print([word[i:i+3] for i in range(0, len(word), 3)])
#['abc', 'def', 'ghi', 'jkl', 'mno', 'pqr', 'stu', 'vwx', 'yz']

word = 'geeks, for, geeks'
print(word.split(','))
# ['geeks', ' for', ' geeks']

s = "Hello World"
print(s.replace("ll", "x").replace("Worl", "Ner"))
# Hexo Nerd
'''

#U9 b
'''
# Zählt alle buchtaben und wie oft sie vorkommen
x=input("wort zum zählen")
z=input("Buchstabe zum zählen")
for buchstabe in x:
    y= x.count(buchstabe)
    print("Der Buchstabe: "+buchstabe+" kommt "+str(y)+" mal vor")

# version mit count
x=input("wort zum zählen ")
z=input("Buchstabe zum zählen ")
y= x.count(z)
print("Der Buchstabe"+z+"ist "+str(y)+" mal vorhanden")
'''
# version ohne count
eingelesener_string=input("wort zum zählen ")
buchstabe_zaehlen=input("Buchstabe zum zählen ")
count=0
for buchstabe in eingelesener_string:
    if(buchstabe.lower()==buchstabe_zaehlen.lower()):
        count+=1
print("Der Buchstabe "+buchstabe_zaehlen+" ist "+str(count)+" mal vorhanden")