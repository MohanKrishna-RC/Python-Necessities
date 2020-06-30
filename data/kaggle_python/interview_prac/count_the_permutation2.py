import sys

t = int(sys.stdin.readline())
def countRec(n, sum):

    # Base case
    if (n == 0):
        return (sum == 0)

    if (sum == 0):
        return 1

    # Initialize answer
    ans = 0

    # Traverse through every digit and
    # count numbers beginning with it
    # using recursion
    for i in range(0, 10):
        if (sum-i >= 0):
            ans = ans + countRec(n-1, sum-i)

    return ans


# This is mainly a wrapper over countRec. It
# explicitly handles leading digit and calls
# countRec() for remaining digits.
def finalCount(n, sum):

    # Initialize final answer
    ans = 0

    # Traverse through every digit from 1 to
    # 9 and count numbers beginning with it
    for i in range(1, 10):
        if (sum-i >= 0):
            ans = ans + countRec(n-1, sum-i)

    return ans


while t:
    n = sys.stdin.readline().split()
    a = finalCount(int(n[1]), int(n[0]))
    print(a)
    t = t-1
