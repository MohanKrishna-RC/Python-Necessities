# Find the Ascii value of user input  string.

# define ASCII_value() function with user-input string  as argument.

def ASCII_value(charInput):

    print("\nASCII value :", end = ' ')
    
    #Getting each character of the user input string

    for i in range(len(charInput)):

        #Finding the ASCII value of each character using the ord() function and converting it to the string and printing it,
        print(str(ord(charInput[i])),end='  ')

if __name__ == "__main__":
    userInput = input("\nENTER ANY CHARACTER : ")
    ASCII_value(userInput)