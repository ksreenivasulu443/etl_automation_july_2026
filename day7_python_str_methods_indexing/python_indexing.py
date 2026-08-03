str1 = "HELLO WORLD"
#
#
# # syntax : varaible/string[index number]
# print("str1[0]", str1[0])
# print("str[1]", str1[1])
# print("str[2]", str1[2])
# print("str[3]", str1[3])
# print("str[4]", str1[4])
# print("str[5]", str1[5])
# print("str[6]", str1[6])
# print("str[7]", str1[7])
# print("str[8]", str1[8])
# print("str[9]", str1[9])
# print("str[10]", str1[10])
#
# # print("str[11]", str1[11])
#
# # IndexError: string index out of range
#
# print("str1[-1]", str1[-1])
# print("str[-2]", str1[-2])
# print("str[-3]", str1[-3])
# print("str[-4]", str1[-4])
# print("str[-5]", str1[-5])
# print("str[-6]", str1[-6])
# print("str[-7]", str1[-7])
# print("str[-8]", str1[-8])
# print("str[-9]", str1[-9])
# print("str[-10]", str1[-10])
# print("str[-11]", str1[-11])
#
# # print("str[1]", str1[-12])
#
# # first character  and Character
#
# print("first char", str1[0])
# print("last char", str1[-1])
#
# print("len(str1)", len(str1))
#
# print("last chara without using negative index", str1[len(str1)-1])
#
# print("last chara without using negative index", str1[len(str1)-len(str1)])
#
#
# str1 = "HELLO WORLD"
#
# print('str1.find("O")', str1.find("O"))
# print('str1.find("D")', str1.find("D",4,len(str1)))
#
# print('str1.find("HELLO")', str1.find("WORLD"))
#
# print('str1.find("D")', str1.find("L",-11, -1))

# print('str1.find("Z")', str1.find("Z"))
# print('str1.index("Z")', str1.index("Z"))


# print('str1.find("L")', str1.find("L"))
# print('str1.index("L")', str1.index("L"))
#
#
# print('str1.rfind("L")', str1.rfind("L"))
# print('str1.rindex("L")', str1.rindex("L"))


# str2 = 'ETL TESTING'
#
# print('str2.find("T")', str2.find("T"))
# print('str2.index(T")', str2.index("T"))
#
#
# print('str2.rfind("Z")', str2.rfind("Z"))
# print('str2.rindex("T")', str2.rindex("Z"))

composite_keys = "sno,name,phone"

print("split", composite_keys.split(","))

path = r"C:\Users\Haritha\PycharmProjects\etl_automation_july_2026\errors.txt"

print("path split", path.split("\\"))

ages = "10-20-30-40-50"

print("ages split", ages.split("-",3))

str3 = 'ETL Automation Labs'

print("count of a", str3.upper().count('A'))

#E1
#T3
#L2
#
#
# "aaabbcccccc"
# a3b2c5


str4 = "    ETL testing                               "

print("str4 ltrim", str4.lstrip(),len(str4), len(str4.lstrip()))
print("str4 rtrim", str4.rstrip(),len(str4), len(str4.rstrip()))
print("str4 trim", str4.strip(),len(str4), len(str4.strip()))

print("sreenivasulu" + "Kattubadi" + "ETL")














