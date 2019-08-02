# First level of basic code
"""
def add(x,y):
    return x + y

def sub(x,y=10):
    return x - y

print("add(10)",   add(10))
print("add(20,30)",  add(20,30))
print("add(20,30)",  sub(20,30))

"""

#Trying to print the time taken
"""
def timer(func,x,y=10):
    before = time()
    z = func(x,y)
    after = time()
    print("time_taken-->",after-before)
    return z

def add(x,y):
    return x + y

def sub(x,y=10):
    return x - y

print("add(10)",   timer(add,10))
print("add(20,30)", timer(add,20,30))
print("add(20,30)",  sub(20,30))
"""

#Printing time in a little 
# better way, defining a seperate function
"""
def timer(func):
    def f(x,y=10):
        before = time()
        rv = func(x,y)
        after = time()
        print("time_taken-->",after-before)
        return rv
    return f

def add(x,y):
    return x + y
add = timer(add)

def sub(x,y=10):
    return x - y
sub = timer(sub)

print("add(10)",   add(10))
print("add(20,30)", add(20,30))
print("add(20,30)",  sub(20,30))
"""

#Using decorator for time
"""from time import time

def timer(func):
    def f(x,y=10):
        before = time()
        rv = func(x,y)
        after = time()
        print("time_taken-->",after-before)
        return rv
    return f

@timer
def add(x,y):
    return x + y


@timer
def sub(x,y=10):
    return x - y


print("add(10)",   add(10))
print("add(20,30)",  add(20,30))
print("add(20,30)",  sub(20,30))

"""

# *args and **kwargs are so powerful
# they're there for arbitrary for to write
# functions that can take any arbitrary parameter
# spec and forward it to any fashion.


"""from time import time

def timer(func):
    def f(*args,**kwargs):
        before = time()
        rv = func(*args,**kwargs)
        after = time()
        print("time_taken-->",after-before)
        return rv
    return f

n = 2
def ntimes(f):
    def wrapper(*args,**kwargs):
        for _ in range(n):
            print('running {.__name__}'.format(f))
            z = f(*args,**kwargs)
        return z
    return wrapper

@ntimes
def add(x,y):
    return x + y

@ntimes
def sub(x,y):
    return x - y

print("add(10)",   add(10))
print("add(20,30)",  add(20,30))
print("add(20,30)",  sub(20,30))

"""

# we can run function within a function.


from time import time

def timer(func):
    def f(*args,**kwargs):
        before = time()
        rv = func(*args,**kwargs)
        after = time()
        print("time_taken-->",after-before)
        return rv
    return f

def ntimes(n):
    def inner(f):
        def wrapper(*args,**kwargs):
            for _ in range(n):
                print('running {.__name__}'.format(f))
                z = f(*args,**kwargs)
            return z
        return wrapper
    return inner

@ntimes(2)
def add(x,y):
    return x + y

@ntimes(2)
def sub(x,y):
    return x - y

print("add(10)",   add(10))
print("add(20,30)",  add(20,30))
print("add(20,30)",  sub(20,30))

