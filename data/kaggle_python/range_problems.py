from itertools import chain
import pandas as pd
import numpy as np
import math

# Given a list of elements, the task is to print element in group of k till n-iteration in circular range.

"""
Input: list = [1, 2, 3, 4, 5, 6, 7], k = 3, n =10
Output: 
[1, 2, 3]
[4, 5, 6]
[7, 1, 2]
[3, 4, 5]
[6, 7, 1]
[2, 3, 4]
[5, 6, 7]
[1, 2, 3]
[4, 5, 6]
[7, 1, 2]

Input: list = [10, 20, 30, 40, 50, 60, 70], k = 4, n = 5
Output: 
[10, 20, 30, 40]
[50, 60, 70, 10]
[20, 30, 40, 50]
[60, 70, 10, 20]
[30, 40, 50, 60]

"""
# Python code to print element in group
# of 5 till 9 iteration in circular range.

# Importing
from itertools import cycle


# Using chain method
print("Concatenating the result")
res = chain(range(5), range(10, 20, 2))

for i in res:
    print(i, end=" ")  # Output 1,2,3,4,10,12,14,16,18
    
# list initialization
List = [90, 99, 192, 0, 43, 55]

List1 = ['Geeks', 'for', 'geeks', 'is', 'portal']

# Defining no of iterations
n = 4

# Defining no of grouping   # Here the grouping is based on the 
k = 6 

for index, *ans in zip(range(n), *[cycle(List)] * k): 

    # printing ans
    print(index,ans)

for index, *ans in zip(range(n), *[cycle(List1)] * k):
    # printing ans
    print(index,ans)
