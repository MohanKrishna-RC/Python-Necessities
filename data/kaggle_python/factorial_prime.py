import math
import pandas as pd
import numpy as np


def prime(num):
    if num >= 1:
        root_num = int(math.sqrt(num))
        # print(root_num)
        for i in range(2, root_num+1, 1):
            # print(i)
            if (num % i) == 0:
                print("Number is not prime")
                break
        else:
            print("Prime Number")

lst = []
def prime_in_range(num_till):
    for i in range(num_till+1):
        if i>=1:
            root_num = int(math.sqrt(i))
            for j in range(2,root_num,1):
                if i%j==0:
                    # print("Not Prime Number")
                    break
            else:
                lst.append(i)

def factorial(num):
    """This is a recursive function that calls
   itself to find the factorial of given number"""

    if num == 1:
        return num
    else:
        # print("lofh")
        return num * factorial(num-1)


if __name__ == "__main__":
    num = int(input("Enter number to find  : "))

    prime(num)
    prime_in_range(num)
    print("Prime Numbers in the Range : ", lst)
    if num < 0:
        print("Factorial cannot be found for negative numbers")
    elif num == 0:
        print("Factorial of 0 is 1")
    else:
        print("Factorial of", num, "is: ", factorial(num))

