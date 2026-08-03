ls1 = [] # Empty list
ls2 = list() # empty list

print("ls1 detail", ls1, type(ls1), id(ls1), ls1.__sizeof__(), dir(ls1))
#
#
print("ls2 detail", ls2, type(ls2), id(ls2), ls2.__sizeof__(),dir(ls2))
#
#
# t1 = () # Empty tuple
# t2 = tuple() # empty tuple
#
# print("t1 tuple details", t1, type(t1), id(t1), dir(t1), t1.__sizeof__())
#
#
# #int, float, str
#
# print("t2 tuple detail", t2, type(t2), id(t2), dir(t2), t2.__sizeof__())


ls1.append(1)

print("ls1 detail after append 1", ls1, type(ls1), id(ls1),  ls1.__sizeof__())

ls1.append(2)
print("ls1 detail after append 2", ls1, type(ls1), id(ls1),  ls1.__sizeof__())

# ls1.clear()
# print("ls1 detail after clear", ls1, type(ls1), id(ls1),  ls1.__sizeof__())

ls2.append(1)
print("ls2 detail", ls2, type(ls2), id(ls2), ls2.__sizeof__(),dir(ls2))

ls1.extend([3,4,5])
print("ls1 detail after extend [3,4,5] ", ls1, type(ls1), id(ls1),  ls1.__sizeof__())


ls1.insert(0,1)

print("ls1 detail insert(1,101) ", ls1)


ls3 = [1,1,1,1,1,1,2,2,2,'etl','etl', 10.5, 3.14, True, 1+3j]

print("ls3", ls3)

ls3.insert(1,'sreeni')

ls3.insert(5,'sreeni')

print("ls3", ls3)


ls3.insert(-5,'etl testing')

print("ls3", ls3)

#palindrome string

str1 = 'MADAM' # 1221, 141, 8778

str2 = 121

print(str1[::-1], str1, str1 == str1[::-1])

print(str(str2)[::-1], str2, str(str2) == str(str2)[::-1])

ls = [1,2,3,4,5]

print("ls", ls)

ls.pop(1)

print("ls after pop", ls)
ls.extend(['Hari', 'Ravi'])
print("ls after extend", ls)
ls.remove('Hari')
print("ls after remove", ls)


cars = ['Ford', 'BMW', 'Volvo']
print("cars", cars)
cars.sort(reverse=True)
print("cars after sort", cars)



fruits = ['apple', 'banana', 'cherry']
print("fruits", fruits)
fruits.reverse()
print("fruits after", fruits)

# Creating columns  - ['col1', 'col2','col3']

columns = "col1, col2, col3"

pkey = ['col1','col2']

not_null_columns = ['col3','col5']


