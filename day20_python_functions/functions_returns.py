# def calc(a,b,c):
#     print(f"{a} + {b} + {c} = {a+b+c}")
#     return a+b+c,a*b*c,17,'sreeni'
#
#
# # function_return  = calc(2,4,3) # function call will execute function body 6,
# #
# # print(function_return) # calc function doesn't have return when there is return in function it return None
#
#
# print(calc(1,2,3))
#
# returns = calc(1,2,3)
#
# print(returns, type(returns), returns[0], returns[1], returns[2], returns[3])
from debugpy.launcher import output

from day14_control_flows.if_else import target_count


# def calc(a,b,c):
#     return a+b, a*b, a/c
#
#
# print(calc(1,2,3))
#
# output = calc(1,2,3)
# print(output)
#
# output1,output2,output3 = calc(1,2,3)
#
# print(output1, type(output1))
# print(output2, type(output2))
# print(output3, type(output3))


# function should take two params and compare two values whether
# they are equal or not if it is equal we should print status PASS not FAIL


def count_check(source_count,target_count):
    print("source_count is", source_count)
    print("targte_count is", target_count)
    if source_count == target_count:
        status = "PASS"
    else:
        status = "FAIL"

    return status

count_check(source_count=10, target_count=10)


