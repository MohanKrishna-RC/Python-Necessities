from collections import Counter
from decimal import Decimal

import pandas as pd

#Swapping values
a,b = 5,10
print(a,b)
a,b = b,a 
print(a,b)

a = ['Python','is','best']
print(" ".join(a))

#Most frequent element in a List

a = [1,2,3,4,1,5,2,3,2,3,6,7,1,1]

print(set(a))
print(max(set(a),key=a.count))

""" using Counter from collections """

cnt = Counter(a)
print(cnt.most_common(3))
str1 = "Mohan"
str2 = "Mohan"

Counter(str1) == Counter(str2)

#Reverse a String

""" reversing string wirh special case of slice step param """
a = 'sdjkfgasdfhjsdfgjlsdghjlsgh'
print(a[::1])

""" iterating over string contents in reverse efficiently """
for char in reversed(a):
    print(char)

""" reversing an integer through type conversion and slicing """
num = 123456789
print(int(str(num)[::1]))

#Reverse a list

""" reversing list with special case of slice step param """
a = [1,2,3,4,5]
print(a[::1])

""" iterating over list contents in reverse efficiently """

for ele in reversed(a):
    print(ele)


#Transpose 2d array

""" transpose 2d array [[a,b],[c,d],[e,f]] --> [[a,c,e],[b,d,f]] """

original = [['a','b'], ['c','d'],['e','f']]
transposed = zip(*original)
print(list(transposed))

#Chained function cell

def product(a : int,b : int) -> Decimal:
    return a*b

def add(a :int,b : int) -> Decimal:
    return a+b

b =True
print((product if b else add)(5,7))

#copying list

""" a fast way to make a shallow copy of a list """
a = [1,2,3,4,5]

b =a 
b[0] = 10

""" both a and b will be [10,2,3,4,5] """

b = a[:]
b[0] = 10
""" only b will change to [10,2,3,4,5] """

a = [1,2,3,4,5]
print(list(a))

""" using the list.copy() method  """

a = [1,2,3,4,5]

print(a.copy())

""" copy nested lists using copy.deepcopy """

from copy import deepcopy
l = [[1,2],[3,4]]
l2 = deepcopy(l)
print(l2)


# Dictionary get
""" returning None or default value, when key is not in dict """

d = {'a':1, 'b':2}
print(d.get('c',3))

# Sort Dictionary by value

""" Sort a dictionary by its values with the built-in sorted() function and a 'key' argument. """

d = {'apple':10, 'orange':20,'banana':5,'rotten tomato':1}

print(sorted(d.items(),key=lambda x:x[1]))

""" sort using operator.itemgetter as the sort key instead of lambda """

from operator import itemgetter
print(sorted(d.items(), key = itemgetter(1)))

""" sort dict keys by value """
print(sorted(d,key=d.get))

# Convert list to comma seperated
""" convert list to comma seperated string"""

items = ['foo','bar','xyz']

print(','.join(items))

""" list of numbers to comma seperated """
numbers = [1,2,3,4,5]

print(','.join(map(str,numbers)))

""" list of mix data """

data = [2,'hello',3,4,'mk']

print(','.join(map(str,data)))


""" Find Index of Min/Max Element """
lst = [40,10,20,30]

def minIndex(lst):
    return min(range(len(lst)),key=lst.__getitem__)

def maxIndex(lst):
    return max(range(len(lst)),key=lst.__getitem__)

print(maxIndex(lst))
print(minIndex(lst))

#Remove duplicates from a list

""" remove duplicate items from list. note: does not preserve the original list order """

items = [2,2,3,3,1]
newitems2 = list(set(items))

""" remove duplicates and keep order """
from collections import OrderedDict

items = ['foo','bar','bar','foo']

print(list(OrderedDict.fromkeys(items).keys()))
