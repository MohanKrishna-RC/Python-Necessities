import numpy as np
import pandas as pd
import math
import time 

a = input("Enter the String : ")

start_time = time.time()

lst = [ele for ele in a]
print("Length of the String using lst conversion : ",len(lst))

print("Total time taken : ", time.time() - start_time)


start_time1 = time.time()

print("Length of the String using library function : " , len(a))

print("Total time taken : ", time.time() - start_time1)

start_time2 = time.time()

# counter variable to count the character in a string
counter = 0
for s in a:
    counter = counter+1
print("Length of the input string is:", counter)

print("Total time taken : ", time.time() - start_time2)

