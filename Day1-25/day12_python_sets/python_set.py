
s = {1,2.5, 1+3j, 'test', 2.5, 6,7,19,12,6}

print("s details", s)
print("type of s", type(s))
print("methods in set type", dir(s))

# print(s[0])

# s.add(7)
#
# print(s)


# s2 = {} or dict() #dict

s2 = set()

print("s2 details", s2)
print("type of s2", type(s2))

s2.add(5)

print("s2 details after add", s2)

s2.add(6)

print("s2 details after  2nd time add", s2)


print("s", s)

print("s2", s2)

s2.update(s)

print("s2", s2)



columns = ['id', 'name', 'phone', 'address','address']


# unique_cols = []

# for i in columns:
#     if i not in unique_cols:
#         unique_cols.append(i)
#
#
# # print("columns", columns)
# print("unique_cols", unique_cols)

unique_cols = list(set(columns))

print("columns", columns)
print("unique_cols", unique_cols)


