import numpy as np
import os
import glob
import time
# from time import process_time 

def get_cubes(numbers):
    cubes = []
    for number in numbers:
        cubes.append(number*number*number)
    return cubes

if __name__ == "__main__":
    t1_start = time.time()
    cubes = get_cubes([1,2,3,4,5])
    t1_stop = time.time()
    print("Elapsed time:", t1_stop, t1_start)  
   
    print("Elapsed time during the whole program in seconds:", 
                                         t1_stop-t1_start)  
    print(type(cubes))
    for cube in cubes:
        print(cube)


# Note : The returned object belongs to the list class. We can write the method using generators.

