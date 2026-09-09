#syntax

# def function_name():
#     #python statements
#     return result1

#function definition
def calc(a,b): # a & b are two parameters
    print("a values", a)
    print("b values", b)
    print("sum of a & b is", a+b)


# function call

# calc(a=1,b=2) # a & b are two arguments
# print("="*100)
# calc(a=100,b=200)
# print("="*100)
# calc(a=25,b=45)


# def even_or_odd(num):
#     if num % 2 == 0:
#         print("Even")
#     else:
#         print("Odd")
#
#
# print(globals())
#
#
# even_or_odd(num=5)



def even_or_odd(ls):
    for num in ls:
        if num % 2 == 0:
            print(f"{num} is Even")
        else:
            print(f"{num} is Odd")


even_or_odd(ls=[1,2,3,4,4,5])



