#Reverse string by splitting the string
def rev(s):
    b = []
    print(type(s))
    a = ([s[i:i+1] for i in range(0, len(s), 1)])
    print(a)
    print(len(a))
    for i in range(len(a)):
        b.append(a[i-1])
    print(b)
rev("aksfgakfgajkfgajkfgaf")