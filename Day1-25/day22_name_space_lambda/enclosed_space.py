# x = 'global x'
#
# def outer_fun():
#     y = 'local to outer fun'
#     print("globals inside outer fun space", globals()) # x,
#     print("locals inside outer fun space ", locals()) #y
#     def inner_fun():
#         z = 'local to inner fun'
#         print("globals inside inner fun space", globals()) #x
#         print("locals inside inner fun space ", locals()) #z
#         # print("Y value accessing from inner func: ", y)
#
#     inner_fun()
#
# outer_fun()
#
# a= 10
#
#
# a = 10
#
# def outer_function():
#     # 20
#     global a
#     a=20
#     print("a value inside outer function", a)
#     def inner_function():
#         a = 25
#         print("a value inside inner function", a) #25
#     inner_function()
#
# print("print a before func call", a)
# outer_function()
# print("print a after function call", a)
# print("a value outside of outer function", a) # 10


for i in range(10):

    a = 20

print("a value inside outer function", a, globals())

