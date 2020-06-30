"""
Variable Assignment : we assign a value to the variable using the "=" operator.
In python we need not declare the variable before assigning to it unless like other IDEs

We needn't tell Python what type of value variable is going to refer to. In fact we can refer the variable to a different  sort of thing like a string or boolean.
"""

"""
The * operator can be used to multiply two numbers (3 * 3 evaluates to 9), but amusingly enough, we can also multiply a string by a number, to get a version that's been repeated that many times.
Python offers a number of cheeky little time-saving tricks like this where operators like * and + have a different meaning depending on what kind of thing they're applied to. (The technical term for this is operator overloading)
"""

type(0) # output : integer (int)
type(19.95) # output : float # A float is a number with a decimal place - very useful for representing things like weights or proportions.

# Built-in functions 
"""
1. print()
2. type()
"""

print(float(10))
print(int(3.33))
# They can even be called on strings!
print(int('807') + 1)
