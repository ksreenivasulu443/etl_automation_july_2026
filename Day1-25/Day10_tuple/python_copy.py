# a = [1,2,3]
# b = a # memory copy/reference
#
# # print("a",a, id(a))
# # print("b",b, id(b))
#
# # a.append(4)
# # b.extend([5,6])
# #
# # print("a after append",a)
# # print("b after append",b)
#
# c = a.copy() # copy/deepcopy
#
# print("a",a, id(a))
# print("b",b, id(b))
# print("c",c, id(c))
#
# a.append(4)
#
# print("a after append",a, id(a))
# print("b after append",b, id(b))
# print("c after append",c, id(c))


import copy
a = (1,2,(3,4))
b = copy.copy(a)

print("a", a, id(a))
print("b", b, id(b))

b[2][0] = 99
b[0] = 5

print("a after", a, id(a))
print("b after", b, id(b))



