#lambda syntax

# lambda par1, par2,...parn : expression


# add_l = lambda a,b : a+b
#
# print(add_l(10,20))
#
# def add_f(a,b):
#     return a+b, a*b

#
# col_name = ' First Name '
#
# def clean_col_name(col):
#     return col.strip().lower().replace(' ', '_')
#
# print("traditions fun", clean_col_name(col_name))
#
# clean_col_name_l = lambda col: col.strip().lower().replace(' ', '_')
#
# print("lambda" , clean_col_name_l(col_name))


# col_names = [' First_name ', 'Last_Name  ', 'Age   ', 'Full name   ', '    email']
#
# def clean_col_with_tradi(col_names):
#     updated_col_name =[]
#     for i in col_names:
#         updated_col_name.append(i.strip().lower().replace(' ', '_'))
#     return updated_col_name
#
# print(clean_col_with_tradi(col_names))
#
clean_col_name_l = lambda col: col.strip().lower().replace(' ', '_')
#
# # print(clean_col_name_l(col_names))
#
# print(list(map(clean_col_name_l,col_names)))

col_names = [' First_name ', 'Last_Name  ', 'Age   ', 'Full name   ', '    email']
def display_cols_ends_with_keyword(col_names,keyword):
    ends_with_name_cols =[]
    for i in col_names:
        if i.strip().lower().endswith(keyword):
            ends_with_name_cols.append(i.strip().lower().replace(' ',''))
    return ends_with_name_cols

print(display_cols_ends_with_keyword(col_names,'name'))

col_names = [' First_name ', 'Last_Name  ', 'Age   ', 'Full name   ', '    email']

lambda_filter_keyword = lambda col : col.strip().lower().endswith('name')

print(list(map(clean_col_name_l,  list(filter(lambda_filter_keyword,col_names)))))


from functools import reduce

numbers = range(1,11) # [55]
result = reduce(lambda x, y: x + y, numbers)
print(result)  # Output: 15


