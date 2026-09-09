

import copy

a = [1,2,[3,4]]

b = copy.copy(a) # shallow copy
c = a.copy()

d = copy.deepcopy(a)

e = a
print("details of a", a, id(a), id(a[0]), id(a[1]), id(a[2]))

print("details of b", b, id(b), id(b[0]), id(b[1]), id(b[2]))

print("details of c", c, id(c), id(c[0]), id(c[1]), id(c[2]))

print("details of d", d, id(d), id(d[0]), id(d[1]), id(d[2]))

d[0] = 'test'

print("details of a updating b[0]", a, id(a), id(a[0]), id(a[1]), id(a[2]))

print("details of e updating b[0]", e, id(e), id(e[0]), id(e[1]), id(e[2]))

print("details of b updating b[0]", b, id(b), id(b[0]), id(b[1]), id(b[2]))
#
print("details of c updating b[0]", c, id(c), id(c[0]), id(c[1]), id(c[2]))
#
print("details of d updating b[0]", d, id(d), id(d[0]), id(d[1]), id(d[2]))


f = [1,2,3]

g = copy.deepcopy(f)

print("f details", f, id(f), id(f[0]), id(f[1]))

print("g details", g, id(g), id(g[0]), id(g[1]))

g[0] = 10

print("f details", f, id(f), id(f[0]), id(f[1]))

print("g details", g, id(g), id(g[0]), id(g[1]))