import math

# A recursive function to find nth catalan number
def catalan(n):
    # Base Case
    if n <= 1:
        return 1

    # Catalan(n) is the sum of catalan(i)*catalan(n-i-1)
    res = 0
    for i in range(n):
        res += catalan(i) * catalan(n-i-1)

    return res


# Driver Program to test above function
for i in range(10):
    print(catalan(i))
print("\n")

# A dynamic programming based function to find nth
# Catalan number
def catalan(n):
    if (n == 0 or n == 1):
        return 1

    # Table to store results of subproblems
    catalan = [0 for i in range(n + 1)]

    # Initialize first two values in table
    catalan[0] = 1
    catalan[1] = 1

    # Fill entries in catalan[] using recursive formula
    for i in range(2, n + 1):
        catalan[i] = 0
        for j in range(i):
            catalan[i] = catalan[i] + catalan[j] * catalan[i-j-1]

    # Return last entry
    return catalan[n]


# Driver code
for i in range(10):
    print(catalan(i), end=" ")
print("\n")
#Python program for nth Catalan Number
# Returns value of Binomial Coefficient C(n, k)


def binomialCoefficient(n, k):

    # since C(n, k) = C(n, n - k)
    if (k > n - k):
        k = n - k

    # initialize result
    res = 1

    # Calculate value of [n * (n-1) *---* (n-k + 1)]
    # / [k * (k-1) *----* 1]
    for i in range(k):
        res = res * (n - i)
        res = res / (i + 1)
    return res

# A Binomial coefficient based function to
# find nth catalan number in O(n) time


def catalan(n):
    c = binomialCoefficient(2*n, n)
    return int(c//(n + 1))


for i in range(10):
    print(catalan(i), end=" ")
