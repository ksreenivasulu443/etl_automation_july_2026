"""
Documentation strings
This is python_int_datatype.py create to practice int datatype
created by : Sreeni
created on : 21/07/2026
"""
import sys
#
a = 10

print("value of a", a)
print("type of a ", type(a))
print("id of a ", id(a))
print("size of a ", a.__sizeof__())
# print("methods of a ", dir(a)) # __ underscore ==> dunder methods / special methods
#
# print("bit length of a ", a.bit_length()) # a variable.functionname()
#
# print("="*100)
# b = 10
#
# print("value of b", b)
# print("type of b ", type(b))
# print("id of b ", id(b))
#
#
# print("="*100)
# c = 10
#
# print("value of c", c)
# print("type of c ", type(c))
# print("id of c ", id(c))
#
# print("="*100)
# d = 10.0
# print("value of d", d)
# print("type of d ", type(d))
# print("id of d ", id(d))

print("#"*100)
e = -1000003353443634653653354232543254325423542352435454365654645

print("value of e", e)
print("type of e ", type(e))
print("id of e ", id(e))
print("size of a ", sys.getsizeof(e))
print("size of a ", e.__sizeof__())

# when you create a vriable with whole number python automatically
# assigns int type( positive whole number , negative whole number, 0

f = -10
print("value of f", f)
print("type of f ", type(f))
print("size of f ", sys.getsizeof(f))
print("id of f ", id(f))


###usecases
number_of_student  = 100
employee_id = 1
source_count = 9
target_count = 8
record_count =25
sales_amount
number_of_week
day_of_month
sequence_number_gen
marks = 90
number_of_floor = 4
