# class Polynomial:
#     def __init__(self,*coeffs):
#         self.coeffs = coeffs

#     def __repr__(self):
#         return 'Polynomial(*{!r})'.format(self.coeffs)
# p1 = Polynomial(1,2,3)
# p2 = Polynomial(3,4,3)
# p1.coeffs = 1,2,3 # x^2 + 2x + 3
# p2.coeffs = 3,4,3 # x^2 + 4x + 3

"""
We cannot deliberately add two polynomials directly
in python that simply. So we can define a method 
add to make that easy for us """

class Polynomial:
    def __init__(self,*coeffs):
        self.coeffs = coeffs

    def __repr__(self):
        return 'Polynomial(*{!r})'.format(self.coeffs)
    
    def __add__(self,other):
        return Polynomial(*(x+y for x,y in zip(self.coeffs, other.coeffs)))

    def __len__(self):
        return len(self.coeffs)

    def __call_(self):
        pass
p1 = Polynomial(1,2,3)
p2 = Polynomial(3,4,3)

"""
The methods with double underscores are often call dunder methods
They can be called as data model methods
"""
"""
There has always been a common pattern,
There is a top level function or some top level syntax,
and there is a correspondind underscore function.
The exact arguments the underscore function takes will be determined
in the documentation. ( data model and python)
"""

"""
Everytime we time we want to implement a custom
behaviour on a python object we do it by implementing a underscore
function which ties to some top level 
syntax or function and we implement in interms of
that thing itself """

# x + y --> __add__
# init x --> __init__
# reper(x) --> __repr__
# x() --> __call__

