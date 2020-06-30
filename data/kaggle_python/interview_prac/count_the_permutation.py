import sys

t = int(sys.stdin.readline())


# Python3 function to calculate nCr % p

def ncr(n, r, p):
    # initialize numerator and denominator
    num = den = 1
    for i in range(r):
        num = (num * (n - i)) % p
        den = (den * (i + 1)) % p
    return (num * pow(den,p - 2,p)) % p


while t:
    n = sys.stdin.readline().split()
    a = ncr(int(n[0]),int(n[1]),(10**9 + 9))
    print(a)
    a = 0
    t = t-1
# # p must be a prime
# # greater than n
# n, r, p = 10, 2, 13
# print("Value of nCr % p is",
#       ncr(n, r, p))


