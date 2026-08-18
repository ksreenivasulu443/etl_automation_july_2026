# for i in range(1,5): # Outer for loop
#     for j in range(6,11): # Inner for loop
#         print(f" i value is {i} and j value is {j}")


# for i in range(1,11): # Outer for loop
#     for j in range(1,11): # Inner for loop
#         print(f"{i}*{j} = {i*j}")

for i in range(1,10):
    print("i value", i)
    break # when loop encounters break keyword for loop will be terminated

print("outside for loop")
str1 = 'AABBBCCDEEEFFGGGHIaabcbcbZKL'
# First non-repeating character

for i in str1:
    if str1.count(i)==1:
        print("first non-repeating character", i)
        break




