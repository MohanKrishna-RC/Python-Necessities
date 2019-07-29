#Fibanocci

#Fn = Fn-1 + Fn-2
#F0 = 0, F1 = 1 
#This method is time consuming has T(n) = T(n-1) + T(n-2)0
#Recursion
def fib(n):
    if n<0:
        return("Incorrect")
    if n ==0:
        return 0 
    elif n == 1:
        return 1
    else:
        fi =  fib(n-1) + fib(n-2)
        return fi

#Method 2
#Dynamic Programming


