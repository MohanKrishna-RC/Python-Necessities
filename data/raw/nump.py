import numpy as np
from time import process_time 

py_list = [i for i in range(10000)]

start = process_time()

py_list = [i+2 for i in py_list]

end = process_time()
# print(py_list)
print(round(end-start,5))

np_array = np.array([i for i in range(10000)])

start = process_time()

np_array+=2
end = process_time()
# print(py_list)
print(round(end-start,5))

""" DOT PRODUCT """

list1 = [i for i in range(10000)]
list2 = [i for i in range(10000)]

start = process_time()

dot = 0

for i,j in zip(list1,list2):
    dot+=i*j

end = process_time()

print(round(end-start,5))


arr1 = np.array([i for i in range(10000)])
arr2 = np.array([i for i in range(10000)])

start = process_time()

arr = np.dot(arr1,arr2)

end = process_time()

print(round(end-start,5))


""" CONCATENATION """

list1 = [i for i in range(10000)]
list2 = [i for i in range(10000)]

start = process_time()

list1+=list2

end = process_time()

print(round(end-start,5))


arr1 = np.array([i for i in range(10000)])
arr2 = np.array([i for i in range(10000)])

start = process_time()

arr = np.concatenate((arr1,arr2),axis=0)

end = process_time()

print(round(end-start,5))

""" Deletion """

py_list = [i for i in range(10000)]

start = process_time()

del(py_list)

end = process_time()
# print(py_list)
print(round(end-start,5))

np_array = np.array([i for i in range(10000)])

start = process_time()

del(np_array)

end = process_time()
# print(py_list)
print(round(end-start,5))