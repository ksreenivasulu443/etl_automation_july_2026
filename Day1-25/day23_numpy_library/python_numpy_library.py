import numpy as np
import math as m

# arr = np.array([[1, 2, 3]])
#
#
# print("arr details", arr, type(arr), id(arr))
#
# arr2 = np.array([[5, True, 1+2j, 1.2, 'etl']])
#
# print("arr2 details", arr2, type(arr2), id(arr2))
#
# ls = [5, True, 1+2j]
#
# print(ls)

# str>complex>float>int>bool

arr3 = np.array([34,3.14,1,False])

print("arr3 details", arr3,type(arr3), id(arr3))
print("array[0]", arr3[0], type(arr3[0]))
print("array[1]", arr3[1], type(arr3[1]))
print("array[2]", arr3[2], type(arr3[2]))
print("array[3]", arr3[3], type(arr3[3]))

print("methods", dir(arr3))

arr3.shape()