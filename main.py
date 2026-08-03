a = 10
print(type(a))
print(globals())
b = 20
print(globals())
c = 30
print(globals())
d = 40
print(globals())
print(a+b+c+d)

e = 'Sreenivas'
f = 0
print(globals())
try:
    print(e/f)
except ZeroDivisionError:
    print("Division by zero")

print("this is last line in main.py")

a = 'sreeni'
b = 'sreeni'
