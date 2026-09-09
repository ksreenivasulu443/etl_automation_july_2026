import pandas as pd

pd.set_option("display.max_columns", None)
pd.set_option("display.width", 2000)
#
# customers = pd.read_csv(filepath_or_buffer=r"C:\Users\Haritha\PycharmProjects\etl_automation_july_2026\day30_pandas_dataframes_joins\customer.csv",
#                         header=0,
#                         sep=',')
#
# orders = pd.read_csv(filepath_or_buffer=r"C:\Users\Haritha\PycharmProjects\etl_automation_july_2026\day30_pandas_dataframes_joins\orders.csv",
#                      header=0,
#                      sep=',')
#
# print(customers)
#
# print(orders)
#
# # left_join = pd.merge(left=customers,right=orders,how ='outer', on="customer_id", indicator=False)
# # print(left_join)
#
#
# join = customers.merge(orders, how ='outer', on="customer_id", indicator=True)
# print(join)


import pandas as pd

df1 = pd.DataFrame({
    "EmpID": [101, 102, 103],
    "Name": ["Ravi", "John", "Priya"]
})

df2 = pd.DataFrame({
    "EmpID": [104, 105, 106],
    "Name": ["David", "Anita", "Mike"],
    "AGe": [10,20,30]
})

print("DF1")
print(df1)

print("DF2")
print(df2)

print(pd.concat([df1, df2], axis=0))