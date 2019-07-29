#Replace every primeth letter of a string with 0

def revpri(s):
    b = []
    #Splitting a string with a difference of "nth" letter.
    a = ([s[i:i+1] for i in range(0, len(s), 1)])
    print(a)
    print(len(a))
    for num in range(len(a)):
        if num > 1:
        # check for factors
            for i in range(2,num):
                if (num % i) == 0:
                    b.append(a[i])
                    # print(num,"is not a prime number")
                    # print(i,"times",num//i,"is",num)
                    break
            else:
                b.append(0)
                # print(num,"is a prime number")
        else:
            b.append(a[num])
            # continue
            # print(num,"is not a prime number")
    return b

revpri("sdfkjgsdfkgsdkjfgsdmfgskfgs")