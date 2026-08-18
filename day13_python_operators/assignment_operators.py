# a = 10 # = is the assignment operators
# b = 'ETL'
# source_count = 10
# pkey = ['sno','first_name'] # = assignment operator pkey --> variable and list of values ['sno','first_name']
#
# x=y=z=10
# # x=10
# # y=10
# # z=10
# print(x, id(x))
# print(y, id(y))
# print(z, id(z))
#
# k,l,m = 1,2,3
#
# # k = 1
# # l = 2
# # m = 3
#
# print(k)
# print(l)
# print(m)
#


a = 10
print("a details", a)
a += 5 # a = a+5==> a = 10+5
print("a details after a+=5", a)

a += 2 # a = a+2 ==> a= 15+2

print("a details after a+=2", a)


a -= 5 # a = a-5 ==> a = 17-5
print("a details after a=-5", a)

x = 4

x *= 5 # x = x * 5
print("x details after x*=5", x)


y = 4

y /= 2 # y = y/2 ==> y = 4/2
print("y details after y/=2", y)


z = 20

z **= 2 # z = z ** 2 ==> z = 20 ^2

print("z details after z**=2", z)


k = 10

k %= 3  # k = k % 3
print("k details after k%=2", k)