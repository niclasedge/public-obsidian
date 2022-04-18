parent: [[Privat ToDo]]
tags:
aliases: 
Reference: [[Python MOC]]
created: 2021-07-25
url: https://medium.com/pythoneers/5-powerful-functions-in-python-1804b51c4ded

---

- [ ] Lesen: 5 Powerful Functions in Python. Must know functions in Python explained… |

## 5 Powerful Functions in Python. Must know functions in Python explained… | by Swathi Arun | The Pythoneers | Jul, 2021 | Medium
> # 1. Lambda Function:

One of the most powerful functions in Python also known as the anonymous function. It is known as anonymous because we can instantiate and declare a function without a name. If you have a single operation to be executed, the lambda function is extremely useful instead of declaring a traditional function. Lambda is similar to the function, except it can only return only one expression.

> **A Python program to find the value for (a+b)^2 using lambda**

answer = lambda a, b: a**2 + b**2 + 2*(a+b)  
print(answer(3, 6))

**Note:**

-   The syntax for lambda function is `lambda arguments: expression`
-   Lambda doesn’t require a name and, returns statement lambda keyword is used.
-   Also, notice that the function is called a reference variable called the answer.
-   You can also use lambda functions inside other functions.
-   Lambda is similar to the function, except it can only return only one expression.

# 2. Map Function:

The map is a built-in Python function used by programmers to make the program simpler. This function iterates up on all the specified elements without the usage of any loops.

> **A program to add values from two lists and create a new list.**

def add_list(a,b):  
    return a+b  
output = list(map(add_list,[2,6,3],[3,4,5]))  
print(output)

**Note:**

-   Syntax for this function is `map(function,iterables)`
-   In this example, notice that a user-defined function add_list has been used to add two variables.
-   The output for this example will be another list [5, 10, 8].
-   To explore more of the map capabilities try replacing the function with lambda and instead of just a list you can also try to work with tuples, sets.

# 3. Filter Function:

The filter is a built-in Python function, which is useful when it is required to segregate any kind of data. It is used to extract or filter the data based on the given condition.

def is_positive(a):  
    return a>0  
output = list(filter(is_positive,[1,-2,3,-4,5,6]))  
print(output)

**Note:**

-   Syntax for filter is `filter(function,iterable)`
-   A user-defined function is required to return a boolean value.
-   The elements for which the function returns true, only those elements are returned by the filter function.
-   The output for the used example is a list [1, 3, 5, 6].
-   Unlike map, the filter takes only one iterable in this case, we can make a list of positive and negative numbers.

# 4. Zip Function

The zip is a built-in function that is used to extract data from different columns of the database and change it into a tuple.

user_id = ["12121","56161","33287","23244"]  
user_name = ["Mick","John","Tessa","Nick"]  
user_info = list(zip(user_name,user_id))  
print(user_info)

**Note:**

-   Syntax for this function is `zip(*iterables)`
-   It ideally combines two given data or lists into a tuple.
-   The output for this example will be [(‘Mick’, ‘12121’), (‘John’, ‘56161’), (‘Tessa’, ‘33287’), (‘Nick’, ‘23244’)].

# 5. Reduce function:

This function is used when it is required to apply the same operation to all the elements in the given list.

import functools  
def sum_two_elements(a,b):  
    return a+b  
  
numbers = [6,2,1,3,4]  
result = functools.reduce(sum_two_elements, numbers)  
print(result)

**Note:**

-   The syntax for reduce function is `functools.reduce(function, iterable)`
-   This function is not built-in, to use it import the functools module.
-   Output for this program is 16, it returns the sum of the list.