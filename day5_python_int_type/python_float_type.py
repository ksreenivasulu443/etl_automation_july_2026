"""
Documentation strings
This is python_float_datatype.py create to practice flaot datatype
created by : Sreeni
created on : 21/07/2026
"""
import sys
#
# a = 10.0000001
#
# print("value of a", a)
# print("type of a ", type(a))
# print("id of a ", id(a))
# print("size of a ", a.__sizeof__())
# print("methods of a ", dir(a)) # __ underscore ==> dunder methods / special methods
# print("="*100)
# b = 10.0
# print("value of b", b)
# print("type of b ", type(b))
# print("id of b ", id(b))
#
#
# print("="*100)
c = 1e2 # 1*10**2 #1*100==> 100.0

print("value of c", c)
print("type of c ", type(c))
print("id of c ", id(c))
#
# print("="*100)
# d = 10.0
# print("value of d", d)
# print("type of d ", type(d))
# print("id of d ", id(d))


a = 0
b = 0.0

print("value of a", a)
print("type of a", type(a))
print("id of a", id(a))
print("="*100)
print("value of b", b)
print("type of b", type(b))
print("id of b", id(b))


##Use cases of float

#average
#salesaverage
#salary
#transaction amount
#weight
#currency
#interest rate
#claim amount
# tax percent
# time
# test coverage percentage


###insurance
###banking
##ecommerce/retail
##financial/wealth
#loyalty
#healthcare
#HRA


####Type conversion
print("="*100)
a = 10

converted_a = float(a) # float is type case function

print("type a", type(a), a)

print("type of converted_a", type(converted_a), converted_a)


c = 10.1

d = int(c) # int type case function

print("details of c", c, type(c))

print("detailes of d", d, type(d))
