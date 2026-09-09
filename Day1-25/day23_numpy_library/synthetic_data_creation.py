import numpy as np
import pandas as pd

n = 100

name_pool = np.array(["Alex", "Ravi", "Priya", "John", "Sara", "Meena", "David", "Amit", "Kiran", "Lara"])
names = np.random.choice(name_pool, size=n)

# print(names)
#
# print("names", names)

customer_id = np.arange(1,n+1)

ages = np.random.randint(1000, 10000000000, size=n)
# print("ages", ages)

salaries = np.random.randint(30000, 120001, size=n)

# print("salaries",salaries)


tiers = np.random.choice(["Silver", "Gold", "Platinum"], size=n)

# print("tiers", tiers)

data = np.column_stack((customer_id,names,ages,salaries, tiers))

print("data", data)

df = pd.DataFrame(data=data, columns=['customer_id','Full_name','age','salary','tier'])

print(df.head(100))