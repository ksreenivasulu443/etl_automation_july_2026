def calc(a,b,c=0): # a,b,c are parameter, c is default parameter
    print("a value is", a)
    print("b value is", b)
    print("c value is", c)
    return a+b+c

calc(40,50,70) #40,50,70 are positional arguments

calc(40,b=70,c=100)

