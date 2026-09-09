""""doc string"""
from prompt_toolkit.key_binding.bindings.named_commands import uppercase_word

#syntax range
#
# range(start, stop, step)
#
# r = range(10) ## range(0,10,1) # generates number 0 to 9 with step-1 0,1,2,3,4,5,6,7,8,9
#
# r = range(1,10) # range(1,10,1) # generates number 1 to 9 with step-1 1,2,3,4,5,6,7,8,9
# r = range(1,10,2) #range(1,10,2) # generates numbers 1 to 9 with step-2 1,3,5,7,9


# r = range(10) # 0,1,2,3,4,5,6,7,8,9
#
# print("r details", r, type(r), id(r), dir(r))
#
# print(r.start, r.stop, r.step, r.count(7), r.index(5))

# ls = [0,1,2,3,4,5,6,7,8,9,10]
#
# r = range(0,11)
#
# print("ls details", ls, type(ls), id(ls), ls.__sizeof__())
# print("r details", r, type(r), id(r), r.__sizeof__())

#
# for i in ls:
#     print(i)

#
# for i in r:
#     print(i)


# Display even numbers and odd numbers 1-50
# create code to display sum of even numbers, odd number and total sum for numbers between 1-10

# for i in range(1,51):
#     if i % 2 == 0:
#         print(f"{i} is even")
#     else:
#         print(f"{i} is odd")

# for i in range(0,51,4):
#     print(i)


# odd_sum = 0
# even_sum = 0
# total_sum = 0
#
# for num in range(1,11):
#     if num % 2 == 0:
#         even_sum = even_sum + num
#     else:
#         odd_sum = odd_sum + num
#
#     total_sum = total_sum + num
#
#
# print("odd sum", odd_sum)
# print("even sum", even_sum)
# print("total sum", total_sum)


str1 = 'AABBBCCDEEEFFGGGHIaabcbcbD'
# First non-repeating character

unique_char =  set(str1)

print(unique_char)

# print how many time each character is present in str1
# Display whether character is lower or uppercase
# Display output in A2B3C2D1
# Display whether character is vowel or consonant
# First non-repeating character

# for char in unique_char:
#     unique_char =  set(str1)
#     print(f"{char} count is {str1.count(char)}")

# for char in unique_char:
#     if char.isupper():
#         print(f"{char} is uppercase")
#     elif char.islower():
#         print(f"{char} is lowercase")
#     else:
#         print(f"{char} is NOT Alphabet")


# Nested for loops

# for :
#     for :
#         for :
#             for




















