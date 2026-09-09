# a = float(input("Enter the value of a:(note:provide only numeric data) ")) # input function always convert provided value into str
# b = float(input("Enter the value of b: (note: provide only numeric data) "))
#
# print("a details",a , type(a))
# print("b details",b , type(b))

a = 5.0
b = 5
print("sum of a+b is", a+b) # 15
print("sub of a-b is", a-b) # 5
print("mul", a*b) # 50
print("div", a/b) #python divison always returns float output 2.0
print("floor division", a//b) # floor(a/b)
print("mod", a%b) # 0
print("power", a**b)

# These arithmetic operators follow the standard order of operations (PEMDAS/BODMAS):
# Parentheses
# Exponents
# Multiplication and Division (from left to right)
# Addition and Subtraction (from left to right)

print("(8+2)*3/2",(8+2)*3/2) # (10)*3/2 ==> 30 /2

print("(8+2)/3*2",(8+2)/3*2) # (10)/3*2 ==> 3.3333*2

print("(8+2)/(2*3)", (8+2)/(2*3)) # (10)/(2*3) ==>(10)/(6)

print("(8+2)/3**2+3*2",(8+2)/3**2+3*2) # (10)/3**2+3*2) ==> (10)/9 + 3*2 == 1.11 + 3*2 ==> 1.11 + 6



a = 20
b = 10
c = 15
d = 5


e = (a + b) * c / d
print("Value of (a + b) * c / d is ",  e) # (20+10)* 15/5 ==> (30) * 15/5 == 450/5
#Assignment
e = (a + b) * c / d
print("Value of (a + b) * c / d is ",  e)
#
e = ((a + b) * c) / d # (( 20+10) * 15) /5 ==> ((30)*15)/5 ==> 450/5
print("Value of ((a + b) * c) / d is ",  e)
# # #
e = (a + b) * (c / d)
print("Value of (a + b) * (c / d) is ",  e)
# # # #
e = a + (b * c) / d # 20 + (150) / 5
print("Value of a + (b * c) / d is ",  e)











