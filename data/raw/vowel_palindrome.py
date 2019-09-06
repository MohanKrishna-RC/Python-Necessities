# Python program to check if given string is vowel Palindrome 

#First check whether the string is a vowel
def vowel(c):
    v = list("aeiou")

    #If a character is in a vowel.
    if c in v:
        return True
    else:
        return False

vowel("abcuhuvmnba")


def palindrome(s):
    v = []

    #append to the list only when the letter is an vowel
    for i in s:
        if vowel(i):
            v.append(i)
    # if the length of the vowel 
    # string is 0 then print -1 
    if len(v)==0:
        return -1
    #else check if it is palindrome
    else:
        # x = v[::-1] # reverse the string
        b = []
        a = ([v[i:i+1] for i in range(0, len(s), 1)])
        print(a)
        print(len(a))
        c = [x for x in a if x]
        for i in range(len(c)):
            b.append(c[-i-1])
        print(b)

        if c == b:
            return("Palindrome")
        else:
            return("Not a Palindrome")  

s = 'abcuhuvmnba'
palindrome(s) 







classes = ['laughter', 'crying', 'clapping', 'screaming', 'wind', 'thunder', 'silence', 'footsteps', 'run']
classes[1]

s = 'y'
exec(s + " = 'mohan'")
print(y)