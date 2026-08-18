

#syntax for loop

# for iterator in collection_of_itme:
#     statements

# ls = [10,20,30,40]

# for item in ls:
#     print(item)


# str1 = "Etl automation labs"
#
# for letter in str1:
#     if letter.isalnum(): #'E'.isalnum()
#         print(letter.upper())
#     # else:
#     #     print("special character")


# t = (1,2,3,4,5)
#
# for i in t:
#     print(f"i value is {i} and square of {i} is {i **2}")

# s ={2,3,4,4,4,5,5,5,2,2,2,4,4,4,6,1}
# fs = frozenset({2,3,4,4,4,5,5,5,2,2,2,4,4,4,6,1})
# print(s, type(s), dir(s))
#
# print("frozenset", fs, type(fs), dir(fs))
#
# for i in fs:
#     print(i)


# d = {1:'sreeni', 2:"Harini", 3:'Rahul', 4:'Ganga', 5:{'address':'4/5,Kalyan nagar','address2':'random address'}}
#
# for i in d.values():
#
#     if isinstance(i,dict):
#         for j in i.values():
#             print(j)
#     else:
#         print(i)



ls = [1,2,3,4,5]

# print(sum(ls))

sum_of_list = 0
for i in ls:
    sum_of_list += i**3 # sum_of_list = sum_of_list + i

print(sum_of_list)









