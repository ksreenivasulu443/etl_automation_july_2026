"""
#Documentation strings
#This is python_str_datatype.py create to practice str datatype
#created by : Sreeni
#created on : 23/07/2026
"""

import sys

str1 = "ETL Automation labs"

print("str1 value", str1)
print("str1 methods", dir(str1))
print("int methods", dir(10))
print("float methods", dir(10.0))


print("str_capi is",  str1.capitalize())

print("str_capi is",  str1.capitalize()) # self is memory of constructor # PVM

print("count - A", str1.count("A"))

str2 = "+91-9642295961bnfhdgsfhghetrregfdhfgd"

print("count - 9 ", str2.count("g"))

hindi = "नमस्ते"

print("count - न ", hindi.count("न"))

print("str1.lower()", str1.lower())
print("str1.upper()", str1.upper())
print("str1.title()", str1.title())
print("str1.swapcase()", str1.swapcase())
print("str1.casefold()", str1.casefold())


a = "Straße"

print("a.lower()", a.lower())
print("a.casefold()", a.casefold())

# print(a.lower() == b.lower())
# print(a.casefold() == b.casefold())

print("str1.endwith", str1.endswith("labs"))

print("str1.startwith", str1.lower().startswith("etl"))


str1 = "ETLAutomationlabs"
print(str1.isalnum())
print(str1.isalpha())


# txn_number
#
# txn_1
# txn_2
# TXN
# +91-
#
# .csv/.xlsx,/paruqet
#
# gmail.com


str1 = "bâhubali"

print("str1.lower()", str1.lower())
print("str1.casefold()", str1.casefold())




