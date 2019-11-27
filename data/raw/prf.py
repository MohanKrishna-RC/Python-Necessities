import pandas as pd
import math
import numpy as np


x = []

def exp(x):
    a = math.pow(6,x)
    b = math.pow(4,x)
    c = math.pow(8,x)
    
    c = a + b

    return c

d = exp(x)
print(d)