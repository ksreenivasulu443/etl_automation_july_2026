"""
Documentation strings
This is python_print.py create to practice print messages
created by : Sreeni
created on : 16/07/2026
updated by : Rahul
updated on: 17/07/2027
changes on 17/07/2027 : changed the logic + to -
"""
# print('Hello, Welcome to ETL Automation labs', end='-')
#
# print('Good morning')

# ctrl + /
# ctrl + /

# a = 10
# b = 20

# print(a)
# print(b)

#
# print(a,b, sep = '|', end='=')
# print(a*b)
#
# c = 30
#
# print(c)
#
#
# d = 40
# e = 60
# f = 70
# l = 100
#
# print(a,b,c,d,e,f,l, sep = '-')


# print("sreeni", a)  ## 'sreeni' + ' ' + str(10)
#
# print(10)

#print("Value of a is", a, "Value of b is", b )
#
# print("sum of a and b is", a+b)
#
#
# # Formatting print messages
#
#
# print(f"Value of a is {a} and Value of b is {b} " )
#
# souce_count = 10.5
# target_count = 9
#
# print(f"Source count is {souce_count} and target count is {target_count}", sep ='|')

# a = 1
# b = 2
# c = 3
#
# print("value of a is", a, sep=' | ', end=' - ')
# print("value of b is", b, end=' - ')
# print("value of c is", c)
# print("this is end of print")
#
# str1 = "I don't  care "
#
#
# print("Hello")

# print(object="Hello",
#       sep=' ',
#       end='\n',
#       file=sys.stdout,
#       flush=False)

from datetime import datetime

log_file = open(r'C:\Users\Haritha\PycharmProjects\etl_automation_july_2026\output.csv','a')

print(datetime.now(), "Hello, Welcome to ETL Automation labs","Good morning",sep='|',file=log_file)


#Flush


import time

print("Loading...", end="", flush=True)

time.sleep(5)

print("Done")

import time

print("Loading...", end="")

time.sleep(5)


env
























