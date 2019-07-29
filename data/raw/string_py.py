#Reverse string by splitting a string by 1 letter
def rev(s):
    b = []
    print(type(s))
    #Split a string for every nth letter
    # a = ([s[i:i+n] for i in range(0, len(s), n)])
    a = ([s[i:i+1] for i in range(0, len(s), 1)])
    print(a)
    print(len(a))
    for i in range(len(a)):
        b.append(a[i-1])
    print(b)
rev("aksfgakfgajkfgajkfgaf")

