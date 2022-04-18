parent: [[learn_udemy - Automate the boring stuff with Python]]
tags:
aliases: 
Reference:
date:: 
status:: fertig
fazit:: 

---

# Abschnitt 1: Python Basics

## Lesson 1
Explain what you are trying to do, not just what you did.
If you get an error message, specify the point at which the error happens. (Including the line number.)
Copy and paste the entire error message and your code to a pastebin site like pastebin.com or gist.github.com.
Explain what you’ve already tried to do to solve your problem.
List the version of Python you’re using.

## Lesson 2
An instruction that evaluates to a single value is an expression. An instruction that doesn't is a statement.
- IDLE is an editor.
- The interactive shell window has the >>> prompt.
- The file editor window is where you enter code for complete programs.
- Data types: int, float, string
- Strings hold text and begin and end with quotes: 窶路ello world!'
- Values can be stored in variables: spam = 42
- Variables can be used anywhere values can be used in expressions: spam + 1


```python
#Expressions
2+2
```

**Order of Operations:**
1. Parentheses ()
2. Multiplication/Division * /
3. Addition/Substraction + -


```python
#multiply strings
'alice'*3
```

**Variable**
Has an Assignemnt Statement and contains the defined Value

Epression = evaluate to a value
Statement = does not evaluate to a value


```python
spam=43
spam
```


```python
spam=10
spam=spam+1
print(spam)
```

## Writing your first Program
- Type programs into the file editor (not in the interactive shell window with the >>> prompt)
- The execution starts at the top and moves down.
- Comments begin with a # character and are ignored by Python; they are notes & reminders for the programmer.
- Functions are like mini-programs in your program.
- The print() function displays the value passed to it.
- The input() function lets users type in a value.
- The len() function takes a string value and returns an integer value of the string's length.
- The int(), str(), and float() functions can be used to convert values' data type.


```python
#This Program says hello and asks for my name
print('hello world:')
print('what is your name?') #asks for their name
myname=input()

print('My Name is '+myname)
print('the legth of your name is '+str(len(myname)))
myage=input()
print('you will be '+str(int(myage)+1)+' in a year')
```

## Practice Questions
1. Which of the following are operators, and which are values?

*
'hello'
-88.8
-
/
+
5

2. Which of the following is a variable, and which is a string?

spam
'spam'

3. Name three data types.

4. What is an expression made up of? What do all expressions do?

5. This chapter introduced assignment statements, like spam = 10. What is the difference between an expression and a statement?

6. What does the variable bacon contain after the following code runs?

bacon = 20
bacon + 1

7. What should the following two expressions evaluate to?

'spam' + 'spamspam'
'spam' * 3

8. Why is eggs a valid variable name while 100 is invalid?

9. What three functions can be used to get the integer, floating-point number, or string version of a value?

10. Why does this expression cause an error? How can you fix it?

'I have eaten ' + 99 + ' burritos.'

Extra credit: Search online for the Python documentation for the len() function. It will be on a web page titled “Built-in Functions.” Skim the list of other functions Python has, look up what the round() function does, and experiment with it in the interactive shell.