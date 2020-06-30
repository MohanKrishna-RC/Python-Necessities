import math
import numpy as np

year = input("Enter the year to be checked : ")

def check_leap(year):
    print(type(year))
    year = int(year)
    if year%100==0:
        print("Leap Year")
    elif year%4 == 0:
        print("Leap Year")
    elif year % 400 == 0:
        print("Leap Year")
    else:
        print("Not a Leap year")

print(year)
check_leap(year)
