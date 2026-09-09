import numpy as np

# print("np.random.rand()", np.random.rand()) #between 0 to 1 ( float value)
#
# print("np.random.rand()", np.random.rand()) #between 0 to 1 ( float value)
#
# print("np.random.rand(5)", np.random.rand(5)*100) # 1D array
#
# print("np.random.rand(3,4)", np.random.rand(10,5)*10)


print("np.random.randint(1,7)", np.random.randint(1,7)) # random integer between 0 to 9

print("np.random.randint(1,100,5)", np.random.randint(1,100, 5)) # 1 min , 100 -max , 5 values generate
print("np.random.randint(1,100,(10,3))", np.random.randint(18,100, (10,3)))

arr = np.array(['silver','gold', 'platinum',1,2,3])

print("random choice", np.random.choice(arr), type(np.random.choice(arr)))