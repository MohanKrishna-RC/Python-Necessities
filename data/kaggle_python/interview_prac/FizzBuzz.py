import sys

"""
Example : 

Input:
2     (Test cases)
3     (Size of array)
0 1 1 (input)
3
0 1 2

"""
# To store no of test cases here (2).
# To store input here (0 1 1)  and (0 1 2).
t = int(sys.stdin.readline())
# print(t)

l = []
while t:
    #To store the size of array here (3).
    n = int(sys.stdin.readline())
    #Here i have used sys.stdin.readline() to take input 0 1 1 than split to get a= ['0','1','1'].
    a = (sys.stdin.readline().split()) #Now converting  a= ['0','1','1'] to  l = [0,1,1]
    print(a)
    for i in range(0, n):
        b = int(a[i])
        l.append(b)
        #Do your job with the list l here just print !
    print(l)
    l = []  # empty list for next input ie (0 1 2).
    t = t-1

# our problem 
"""
Input : 
2  ( Test Cases)
3 15  (input string)
"""
# To store no of test cases here (2).

# t=int(sys.stdin.readline()) 
# # To store input here 3 15.
# # print(t)
# #Here i have used sys.stdin.readline() to take input 3 15 than split to get a= ['3', '15'].
# a = (sys.stdin.readline().split())
# # print(a)
# for k in range(t):
#     for i in range(1,int(a[k])+1):
#         if i % 3 == 0 and i % 5 == 0:
#             print("FizzBuzz")
#         elif i%3==0:
#             print("Fizz")
#         elif i%5 == 0:
#             print("Buzz") 
#         else:
#             print(i)
