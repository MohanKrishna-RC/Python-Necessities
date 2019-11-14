""" map() """
""" map() is a built-in Python function used to apply a function to a sequence of elements like a list or dictionary. 
It’s probably the cleanest and most readable way to apply some sort of operation to your data. """

#Example: Square the numbers in a list.

import pandas as pd
import numpy as np

nums = [1,2,3,4,5]

def square_nums(x):
    return x**2

squares = []

for num in nums:
    squares.append(square_nums(num))

print("non pythonic approach", squares)

x = map(square_nums,nums)

print("Pythonic", x)
print("Pythonic", list(x))


""" zip() """ 
""" It enables you to iterate over two or more lists at the same time. 
This can come in handy when working with dates and times. """

first = [1, 3, 8, 4, 9]
second = [2, 2, 7, 5, 8]
# Iterate over two or more list at the same time
for x, y in zip(nums, squares):
    for i,j in zip(first,second):
        print(x*i+y*j)

""" filter()""" 
""" filter() function is in a way similar to map() — it also applies a function to some sequence, 
the difference being that filter() will return only those elements that are evaluated as True."""

number = [1,2,3,4,5,6,7,8,9,10]

def even(x):
    return x%2==0

#Non-Pythonic
even_nums = []
even_bool = []

for num in number:
    even_bool.append(even(num))
    if even(num):
        even_nums.append(num)

print("Non Pythonic", even_bool)
print("Non Pythonic", even_nums)

""" any() takes only one argument. returns True if any item in an iterable are true, otherwise it returns False. """

y = any(even_bool)
print(y)

""" all()  takes only one argument. returns True if all items in an iterable are true, otherwise it returns False. """
y = all(even_bool)
print(y)

#Pythonic
x = filter(even,number)
print("pythonic", list(x))

""" enumerate() """

for i,j in enumerate(even_bool):
    print(i,j)

