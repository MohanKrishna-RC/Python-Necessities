import os
import math

def square(x):
    return x*x

#functions are first-class objects

f = square #Here we're assigning the function to some variable just like any other variables.
print(f(4))

def sumof(f,x,y):
    return f(x) + f(y)

print(sumof(square,3,4))
print(sumof(len,"hello","python"))
print(sumof(len,"hello  ","  python")) # while calculating len of the strings we have to include the spaces also.

# And nothing stops us from returning a function from a function call.

def make_adder(x):
    print("Hell")
    def add(y):
        print("Hekk")
        return x+y
    return add

adder = make_adder(3)
print(adder)
print(adder(4)) 

""" Since the function add is defined inside the make_adder function. it'll have access to the variables of that function.
So the code in the add function can access the variable x in the enclosed scope.

when make_adder is called with 3 argument, it returns an add function with x set to 3. when we call make_adder again, it returns a different add fucntion,
with possibly different value of x.
"""

#Functions can take variable number of arguments

def strjoin(sep,*words):
    return sep.join(words)

print(strjoin("-","one","two"))
print(strjoin("-","one","two","three"))

""" The above strkoin function receives its first argument in the variable sep and all
other arguments pacaked as a tuple in the variable words.

It is also possible to do the reverse of that. If we have a list (or tuple) of 
arguments that we want to pass to a function, we can unpack them when making the function call.
"""
def add(x,y,z):
    return x+y*z

args = [3,4,5]
print(add(*args))

def info(*args):
    print("[INFO]",*args)

def warn(*args):
    print("[WARN]",*args)
info("connection established")
warn("hand shake failed. retrying...")

""" DECORATOR is just a syntactic sugar


@decorator
def func():
    ...

def func():
    ...

func = decorator(func)

"""

#The decorator takes a function as argument and returns a function back,
#possibly a new function.

def trace(f):
    def g(x):
        print(f.__name__,x)
        return f(x)
    return g

# This trace function takes a function as argument and returns a new function that behaves like original function,
#except it prints the function name and argument for every call.

@trace
def sqaure(x):
    return x*x

@trace
def double(x):
    return x+x

print(square(4))
print(square(5))

print(double(4))
print(double(5))

""" Lets try to write decorator that takes any number of arguments.
"""

def trace(f):
    def g(*args):
        print(f.__name__,args)
        return f(*args)
    return g

@trace
def square(x):
    return x*x

@trace
def sum_of_squares(x,y):
    return square(x) + square(y)

print(sum_of_squares(3,5))



level = 0
def trace(f):
    def g(*args):
        global level
        # pretty print indicating the level
        prefix = "|  " * level + "|--"
        strargs = ", ".join(repr(a) for a in args)
        print("{} {}({})".format(prefix, f.__name__, strargs))
        # increment the level before calling the function
        # and decrement it after the call
        level += 1
        result = f(*args)
        level -= 1
        return result
    return g


@trace
def square(x):
    return x*x

@trace
def sum_of_squares(x,y):
    return square(x) + square(y)

print(sum_of_squares(3,5))


@trace
def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
print(fib(5))
