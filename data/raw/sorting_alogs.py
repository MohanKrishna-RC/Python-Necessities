import sys

# For list of integers
arr = []  

# For list of strings/chars
# lst2 = []  

arr = [int(item) for item in input("Enter the list items : ").split(",")]

# lst2 = [item for item in input("Enter the list items : ").split()]

print(arr)
# print(lst2)

#Bubble Sort

def bubbleSort(arr):
    n = len(arr)
    print(n)
    #Traverse through all array elements
    for i in range(n):

        #Last i elements are already in place
        for j in range(0,n-i-1):

            #traverse the array from 0 to n-i-1
            #Swap if the element found is greater than next element
            
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]

def selectionSort(arr):
    n = len(arr)
    for i in range(n):
        #Find the minimum element in remaining unsorted array
        min_idx = i
        for j in range(i+1,n):
            if arr[min_idx] < arr[j]:
                min_idx = j
        
        #Swap the found minimun element with the first element
        arr[i],arr[min_idx] = arr[min_idx],arr[i]

def InsertionSort(arr):
    n = len(arr)
    for i in range(1,n):
        key = arr[i]
        #Move elements of arr[0..i-1], that are greater than key, to one position ahead
        # of their current position
        j = i-1
        while j>=0 and key<arr[j]:
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = key

if __name__=="__main__":
    
    bubbleSort(arr)

    print("Bubble Sorted array is:")
    for i in range(len(arr)):
        print("%d" %arr[i])

    selectionSort(arr)
    print("Selection Sorted array is:")
    for i in range(len(arr)):
        print("%d" %arr[i])
    
    InsertionSort(arr)
    print("Insertion Sorted array is:")
    for i in range(len(arr)):
        print("%d" %arr[i])