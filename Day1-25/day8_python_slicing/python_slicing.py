"""
#Documentation strings
#This is py is created to practice  slicing datatype
#created by : Sreeni
#created on : 23/07/2026
"""

str1 = 'ETL AUTOMATION'

# In python slicing is genric concept used to featch the group of characters, few values from collection datatype(list, tuple, numpy array, dictionary, dataframe)
# Slicing syntax
# variable_name/str[start:stop:step]


#  variable/string[start:stop:step] # start, stop and step are integer
#  **start**: The index of the first character to include in the slice (default is 0).
#  **stop**: The index where slicing stops (exclusive). till last
#  **step**: The interval between characters in the slice (default is 1).

print("str1[:]", str1[::]) # str1[0:len(str1):1]

print("str1[4:]", str1[4:]) # str1[4:len(str1):1]

print("str1[:10]", str1[:10])  # str1[0:10:1]

print(str1[3:5])

print("str1[4:20]", str1[4:20])

print("str1[15:20]", str1[15:20])

print("str1[2:2:1]", str1[2:2:1])

print("str1[2:3:1]", str1[2:3:1])


print("str1[4:13:2]", str1[4:13:2])

print("str1[0::3]", str1[0::3])


print("str1[13:0:]", str1[13:0:1])

print("str1[13:0:]", str1[10:5:1], len(str1[10:5:1])) # here step is +ve, we will get blank if start is greater than stop value(only when step +ve)


print("str1[13:0:]", str1[10:5:-1])

print("str1[-1:-10:1]", str1[-1:-10:1])

print(str1[-10:-1:1])

# stop calculation

# 1. if step is +ve  ==> stop = stop-1
# 2. if step is -ve ==> stop = stop+1

dob = '16-05-2000' #dd-mm-yyyy

print("day",dob[0:2])
print("month",dob[3:5])
print("year",dob[-4::1])


# email = 'kats.123r@gmail.com'
# print("email last 3 char",email[-10:])
#
# username : before @
# provider : after @ and before .
# domain : from reverse after first .

print("str1[5:-5:1]",str1[5:-5:1])


l = ['a','b','c',"1"]


print("".join(l)) # syntx for join : "sep".join(collection datatype)

pkey = ['customer_id', 'customer_name', 'age']

query =  f"""select  {",".join(pkey)} from table"""

print(query)


myTuple = ("John", "Peter", "Vicky")

x = "#".join(myTuple)

print(x)