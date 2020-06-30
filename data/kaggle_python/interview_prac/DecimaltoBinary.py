import math

def DectoBin(number):
    if number > 1:
        DectoBin(number//2)
    
    print(number%2, end=' ')

if __name__ == "__main__":
    number = int(input("\nEnter a number : "))
    DectoBin(number)

