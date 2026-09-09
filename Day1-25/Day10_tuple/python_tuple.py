

# t1 = () # Empty tuple
# t2 = tuple() # empty tuple


t1 = (1,2,3,4,1)

print("t1 tuple details", t1, type(t1), id(t1), dir(t1), t1.__sizeof__())

print("t1.count(1)", t1.count(4))

print(t1.index(4))

import sys
ls = [1,2,3,4,5,5,5,5,5,5,5,5,6,7,8,9,10]
t = (1,2,3,4,5,5,5,5,5,5,5,5,6,7,8,9,10)
print("ls details", ls, type(ls), sys.getsizeof(ls) )
print("t details", t, type(t), sys.getsizeof(t ))

import timeit

t2 = (1,'etl', True, 1+2j, 10.5 , [1,'etl',3] )

print("t2[0]", t2[0], type(t2[0]), id(t2[0]))
print("t2[1]", t2[1], type(t2[1]), id(t2[1]))
print("t2[2]", t2[2], type(t2[2]), id(t2[2]))
print("t2[3]", t2[3], type(t2[3]), id(t2[3]))
print("t2[4]", t2[4], type(t2[4]), id(t2[4]))
print("t2[5]", t2[5], type(t2[5]), id(t2[5]))
print("t2[5][0]", t2[5][0], type(t2[5][0]), id(t2[5][0]))
print("t2[5][1]", t2[5][1], type(t2[5][1]), id(t2[5][1]))


t2 = (1,'etl', True, 1+2j, 10.5 , (1,'etl',3), (1,'etl',3) )

print("t2[-1]", t2[-1][0], type(t2[-1][0]), id(t2[-1][0]))
print("t2[-2]", t2[-2][0], type(t2[-2][0]), id(t2[-2][0]))



import timeit

ls = [1,2,3,3,3,3,4,5,5,5,5,5,10,10,11,1,1,1,1,1]
t = (1,2,3,3,3,3,4,5,5,5,5,5,10,10,11,1,1,1,1,1)

a = 10
b = 20

print("time to display count of 1", timeit.timeit(f"{ls}.index(1)", number=1000000))
print("time to display count of 1", timeit.timeit(f"{t}.index(1)", number=1000000))

print("sum", timeit.timeit(f"{a+b}", number=1000000))
print("sub", timeit.timeit(f"{a*b}", number=1000000))

