import sys

n = int(sys.stdin.readline())

# Now converting  a= ['0','1','1'] to  l = [0,1,1]
a = (sys.stdin.readline().split())
# print(a)
l = []
for i in range(0, n):
    b = int(a[i])
    l.append(b)
print(min(l))
