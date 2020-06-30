import numpy as np
import sys

t = int(sys.stdin.readline())

# Return number of ways to which numbers
# that are greater than given number can
# be added to get sum.

def numberofways(n, m):

    dp = np.zeros((n + 2, n + 2))

    dp[0][n + 1] = 1

    # Filling the table. k is for numbers
    # greater than or equal that are allowed.
    for k in range(n, m - 1, -1):

        # i is for sum
        for i in range(n + 1):

            # initializing dp[i][k] to number
            # ways to get sum using numbers
            # greater than or equal k+1
            dp[i][k] = dp[i][k + 1]

            # if i > k
            if (i - k >= 0):
                dp[i][k] = (dp[i][k] + dp[i - k][k])

    return int(dp[n][m] % (10**9 + 9))

while t:
    n = sys.stdin.readline().split()
    a = numberofways(int(n[0]), int(n[1]))
    print(a)
    t = t-1
