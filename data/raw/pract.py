import pandas as pd

#Python program to illustrate
# *args for variable number of arguments
def myFun(*argv):
    for arg in argv:
        print(arg)

myFun("Creating","Hello","World","in","a","program")

# Python program to illustrate
# *args with first extra argument

def myFun1(arg1, *argv):
    print("First argument :", arg1)
    for arg in argv:
        print("Next argument through *argv :", arg)

myFun1("Creating","Hello","World","in","a","program")


# **Kwargs

# Python program to illustrate   
# *kargs for variable number of keyword arguments 

def _myFun(**kwargs):
    for key,value in kwargs.items():
        print(" %s == %s" %(key,value))

_myFun(first="Creating",second="Hello",third="World")

# Python program to illustrate  **kargs for  
# variable number of keyword arguments with 
# one extra argument.  

def _myFun1(arg1, **kwargs):  
    for key, value in kwargs.items(): 
        print ("%s == %s" %(key, value)) 
  
# Driver code 
_myFun1("Hi", first="Creating",second="Hello",third="World")

def __myFun(arg1, arg2, arg3): 
    print("arg1:", arg1) 
    print("arg2:", arg2) 
    print("arg3:", arg3) 
      
# Now we can use *args or **kwargs to 
# pass arguments to this function :  

args = ("Geeks", "for", "Geeks") 
__myFun(*args) 
  
kwargs = {"arg1" : "Geeks", "arg2" : "for", "arg3" : "Geeks"} 
__myFun(**kwargs)