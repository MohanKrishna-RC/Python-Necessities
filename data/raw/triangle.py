import re

num = int(input("Enter number of stars : "))

def lef_shift_traingle(num):
    for i in range(num):
        # print(i)
        for j in range(0,i+1):
            # print(j)
            print("*",end=" ")
        print("\r")

def inv_traingle(num):
    for i in range(num):
        # print(i)
        for j in range(i,num):
            # print(j)
            print("*",end=" ")
        print("\r")

def mid_triangle(num):
    k = num - 1

    for i in range(0,num):

        for j in range(0,k):
            print(end=" ")
        # print(i)
        k = k - 1
        
        for j in range(0,i+1):
            # print(j)
            print("* ",end="")
        print("\r")

def ri_shift_tri(num):
    k = 2*num - 1
    for i in range(num):
        for j in range(0,k):
            print(end=" ")
        # print(i)
        k = k-2
        for j in range(0,i+1):
            # print(j)
            print("*",end=" ")
        print("\r")

def inv_ri_shift_tri(num):
    k = 2*num - 1
    for i in range(num):
        for j in range(k-num,num):
            print(end=" ")
        # print(i)
        k = k-2
        for j in range(i,num):
            # print(j)
            print("*",end=" ")
        print("\r")

def diagonal(num):
    k = 2*num - 1
    for i in range(num):
        for j in range(0,k):
            print(end=" ")
        # print(i)
        k = k-2
        for j in range(num,num+1):
            # print(j)
            print("*",end=" ")
        print("\r")

if __name__=='__main__':
    diagonal(num)
    print("\n")
    ri_shift_tri(num)
    print("\n")
    lef_shift_traingle(num)
    print("\n")
    mid_triangle(num)
    print("\n")
    inv_ri_shift_tri(num)
    print("\n")
    inv_traingle(num)