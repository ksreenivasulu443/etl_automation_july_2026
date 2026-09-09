import pandas as pd
from pandasql import sqldf

pd.set_option("display.max_columns", None)
pd.set_option("display.width", 2000)

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

# inner_join = pd.merge(customers, orders, how="inner", on="customer_id")
# print("="*100)
# print(inner_join)
# print("="*100)
# print(sqldf("select customers.*, orders.order_id, orders.product_id, orders.order_date, orders.amount from customers outer join orders on customers.customer_id = orders.customer_id and orders.order_id is null"))
#
#
#
# left_join = pd.merge(customers, orders, how="left", on="customer_id")
#
# print("="*100)
# print(left_join)
# print("="*100)
#
#
# right_join = pd.merge(customers, orders, how="right", on="customer_id")
#
# print("="*100)
# print(right_join)
# print("="*100)
#
#
# full_join = pd.merge(customers, orders, how="outer", on="customer_id")
#
# print(full_join[full_join['order_id'].isnull()])

# print("="*100)
# print(right_join)
# print("="*100)

# print(
#     pd.merge(
#         customers,
#         orders,
#         how="outer",
#         on="customer_id"
#     )[lambda df: df["order_id"].isna()]
# )

#
# left_anti = pd.merge(customers, orders, how='cross', on="customer_id")
# print("="*100)
# print(left_anti)
# print("="*100)


# emp = pd.DataFrame({
#     "emp_id":[1,2,3,4],
#     "name":["John","Mike","Sara","Anna"],
#     "dept_id":[101,101,103,104],
#     "loc" : [1,2,3,4]
# })
#
# dept = pd.DataFrame({
#     "dept_no":[101,102,103],
#     "dept_name":["HR","IT","Finance"],
#     "loc" : [1,2,3]
# })
#
# print(emp)
# print(dept)
#
# inner_join = pd.merge(emp, dept, how="inner", left_on='dept_id', right_on='dept_no', suffixes=("_emp", "_dept"))
#
# print(inner_join)