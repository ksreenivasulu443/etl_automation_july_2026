def calc(a,b,*args): # a is parameter, args variable length parameter
    print("a details", a, type(a))
    print("b details", b, type(b))
    print("args details", args, type(args) )

    total = 0
    for value in args:
        total += value # total = total +value

    return total

print(calc(10, 90))
# print(calc(2,5))
# print(calc(2,5,3,3,3,3,4,4,4,4,6,7,8,9,19,20))
# # calc(1,2)
#
# calc(1,2,3)
# calc(1,2,3,4,5,5,5,5,5,5,6,6,7,7,7)