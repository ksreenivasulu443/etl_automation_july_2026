def calc(a, **kwargs):
    print("kwargs", kwargs, type(kwargs))
    print("a", a, type(a))

    total = 0

    for value in kwargs.values():
        total += value
    return total

print(calc(100, k=10,l=40,m=100, n=200))