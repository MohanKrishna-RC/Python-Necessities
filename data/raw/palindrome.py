#Palindrome
#Checking Palindrome using Reverse string by splitting the string

def rev(s):
    b = []
    print(type(s))
    a = ([s[i:i+1] for i in range(0, len(s), 1)])
    print(a)
    print(len(a))
    for i in range(len(a)):
        b.append(a[-i-1])
    print(b)

    if a == b:
        return("Palindrome")
    else:
        return("Not a Palindrome")  
rev("malayalam")


"""
#Palindrome

1) Find reverse of string
2) Check if reverse and original are same or not.
def reverse(s): 
	return s[::-1] 

def isPalindrome(s): 
	# Calling reverse function 
	rev = reverse(s) 

	# Checking if both string are equal or not 
	if (s == rev): 
		return True
	return False


# Driver code 
s = "malayalam"
ans = isPalindrome(s) 

if ans == 1: 
	print("Yes") 
else: 
	print("No") 

"""