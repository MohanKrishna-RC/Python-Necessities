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
from collections import Counter

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

def product(a,b):
    return a*b

def add(a,b):
    return a+b

b =True
print((product if b else add)(5,7))

