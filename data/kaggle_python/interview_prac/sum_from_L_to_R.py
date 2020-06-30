import sys

# Input the test cases and read them here

n = sys.stdin.readline().split()
# print(n)
t  = int(sys.stdin.readline())
# print(t)

while t:
	a = sys.stdin.readline().split()
	sum = 0
	for i in range(int(a[0]),int(a[1])+1):
		# print(i)
		a = int(n[i-1])
		sum+=a
	print(sum)
	sum = 0
	t = t-1
