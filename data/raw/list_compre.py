import pandas as pd
import math
import numpy as np


# x = []

# def exp(x):
#     a = math.pow(6,x)
#     b = math.pow(4,x)
#     c = math.pow(8,x)
    
#     c = a + b

#     return c

# d = exp(x)
# print(d)
class _triplets:
    def _pythagorean_triplets(self):
        return [(a,b,c) for a in range(1,30) for b in range(1,30) for c in range(1,30)if a**2 + b**2 == c**2]

    def _cube_triplets(self):
        return [(a,b,c,d) for a in range(1,30) for b in range(1,30) for c in range(1,30) for d in range(1,30) if a**3 + b**3 == c**3 + d**3]
    
    def _ramanu_triplets(self):
        return [(a,b,c,d) for a in range(1,30) for b in range(1,30) for c in range(1,30) for d in range(1,30) if a**3 + b**3 == c**3 + d**3 and a**3 + b**3 == 1729]

class _alphabets:
    def _uppercase(self):
        """ Converting lowercase letters in a string to uppercase."""
        
        colors = ["pink", "white", "blue", "black", "purple"]
        return [color.upper() for color in colors]

    def _lowercase(self):
        colors = ['PINK', 'WHITE', 'BLUE', 'BLACK', 'PURPLE']
        return [color.lower() for color in colors]

    def _swap_names(self):
        """ Swapping the first and the last name in a given list. """

        presidents_usa = ["George Washington", "John Adams","Thomas Jefferson","James Madison","James Monroe","John Adams","Andrew Jackson"]
        split_names = [name.split(" ") for name in presidents_usa]
        swapped_list = [split_name[1] + " " + split_name[0] for split_name in split_names]
        return swapped_list


class _nested_list_compr:
    
    def _create_matrix(self):
        matrix = [[j * j+i for j in range(3)] for i in range(3)]
        return matrix
    def _set_compr(self):
        """ 
        The list includes a lot of duplicates, and there are names with only a single letter. 
        What we want is a list that consists of names that are longer than one letter and have only the first letter capitalized.
        To accomplish such a task, we turn to set comprehensions.
        """
        
        names = [ 'Arnold', 'BILL', 'alice', 'arnold', 'MARY', 'J', 'BIll' ,'maRy']
        {name.capitalize() for name in names if len(name) > 1}

cl = _triplets()
py = cl._cube_triplets()
cb = cl._pythagorean_triplets()
rm = cl._ramanu_triplets()

col = _alphabets()
ck = col._uppercase()
cp = col._lowercase()
sp = col._swap_names()

nl = _nested_list_compr()
mx = nl._create_matrix()

print(mx)


