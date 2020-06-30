#Palindrome
#Checking Palindrome using Reverse string by splitting the string

def rev(s):
    b = []
    # print(type(s))
    # a = ([s[i:i+1] for i in range(0, len(s), 1)])  # In range function the number after the len is defined, it is used to declare the difference between the numbers in the range.
    a = ([s[i:i+1] for i in range(0, len(s))])
    print(a)
    print(len(a))
    for i in range(len(a)):
        b.append(a[-i-1])
    print(b)
    if a == b:
        return("Palindrome")
    else:
        return("Not a Palindrome")  
a = rev("malayalam")
print(a)
#Reverse the String

#Reverse a list 

def Reverse(lst):
    new_lst = lst[::-1]
    return new_lst

lst = [10, 11, 12, 13, 14, 15]
print(Reverse(lst))


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
