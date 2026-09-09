import pandas as pd
import numpy as np

print("=" * 60)
print("1. DATAFRAME FROM DICTIONARY")
print("=" * 60)

data = {
    "customer_id": [101, 102,105],
    "name": ["John", "David", "Smith"],
    "age": [25, 30, 35]
}

df = pd.DataFrame(data)
print(df)

#
# print("\n" + "=" * 60)
print("2. DATAFRAME FROM LIST")
print("=" * 60)

data = [
    [101, "John", 25],
    [102, "David", 30],
    [103, "Smith", 35]
]

df = pd.DataFrame(
    data,
    columns=["customer_id", "name", "age"]
)
#
print(df)


print("\n" + "=" * 60)
print("3. DATAFRAME FROM TUPLE")
print("=" * 60)

data = (
    (101, "John", 25),
    (102, "David", 30),
    (103, "Smith", 35)
)

df = pd.DataFrame(
    data,
    columns=["customer_id", "name", "age"]
)

print(df)
#

print("\n" + "=" * 60)
print("4. DATAFRAME FROM SET")
print("=" * 60)

data = {101, 102, 103, 104}

df = pd.DataFrame(
    data,
    columns=["customer_id"]
)

print(df)
#
#
# print("\n" + "=" * 60)
# print("5. DATAFRAME FROM SET OF TUPLES")
# print("=" * 60)
#
# data = {
#     (101, "John"),
#     (102, "David"),
#     (103, "Smith")
# }
#
# df = pd.DataFrame(
#     list(data),
#     columns=["customer_id", "name"]
# )
#
# print(df)
#
#
# print("\n" + "=" * 60)
# print("6. DATAFRAME FROM NUMPY ARRAY")
# print("=" * 60)
#
# data = np.array([
#     [101, 25],
#     [102, 30],
#     [103, 35]
# ])
#
# df = pd.DataFrame(
#     data,
#     columns=["customer_id", "age"]
# )
#
# print(df)
#
#
# print("\n" + "=" * 60)
# print("7. NUMPY ARRAY WITH MULTIPLE DATA TYPES")
# print("=" * 60)
#
# data = np.array([
#     [101, "John", 25],
#     [102, "David", 30],
#     [103, "Smith", 35]
# ])
#
# df = pd.DataFrame(
#     data,
#     columns=["customer_id", "name", "age"]
# )
#
# print(df)
#
# # Convert columns back to numeric
# df["customer_id"] = df["customer_id"].astype(int)
# df["age"] = df["age"].astype(int)
#
# print("\nAfter datatype conversion:")
# print(df)
# print(df.dtypes)
#
#
# print("\n" + "=" * 60)
# print("8. DATAFRAME FROM PANDAS SERIES")
# print("=" * 60)
#
# customer_id = pd.Series([101, 102, 103])
# name = pd.Series(["John", "David", "Smith"])
# age = pd.Series([25, 30, 35])
#
# df = pd.DataFrame({
#     "customer_id": customer_id,
#     "name": name,
#     "age": age
# })
#
# print(df)
#
#
# print("\n" + "=" * 60)
# print("9. DATAFRAME FROM MULTIPLE NUMPY ARRAYS")
# print("=" * 60)
#
# customer_id = np.array([101, 102, 103])
# name = np.array(["John", "David", "Smith"])
# age = np.array([25, 30, 35])
#
# df = pd.DataFrame({
#     "customer_id": customer_id,
#     "name": name,
#     "age": age
# })
#
# print(df)
#
#
# print("\n" + "=" * 60)
# print("10. DATAFRAME FROM LIST OF DICTIONARIES")
# print("=" * 60)
#
# data = [
#     {
#         "customer_id": 101,
#         "name": "John",
#         "age": 25
#     },
#     {
#         "customer_id": 102,
#         "name": "David",
#         "age": 30
#     },
#     {
#         "customer_id": 103,
#         "name": "Smith",
#         "age": 35
#     }
# ]
#
# df = pd.DataFrame(data)
#
# print(df)
#
#
# print("\n" + "=" * 60)
# print("11. DATAFRAME FROM NESTED DICTIONARY")
# print("=" * 60)
#
# data = {
#     "customer_id": {
#         0: 101,
#         1: 102,
#         2: 103
#     },
#     "name": {
#         0: "John",
#         1: "David",
#         2: "Smith"
#     },
#     "age": {
#         0: 25,
#         1: 30,
#         2: 35
#     }
# }
#
# df = pd.DataFrame(data)
#
# print(df)
#
#
# print("\n" + "=" * 60)
# print("12. LIST OF TUPLES")
# print("=" * 60)
#
# customers = [
#     (101, "John", 25),
#     (102, "David", 30),
#     (103, "Smith", 35)
# ]
#
# columns = [
#     "customer_id",
#     "name",
#     "age"
# ]
#
# df = pd.DataFrame(
#     customers,
#     columns=columns
# )
#
# print(df)
#
#
# print("\n" + "=" * 60)
# print("13. USING ZIP()")
# print("=" * 60)
#
# customer_id = [101, 102, 103]
# name = ["John", "David", "Smith"]
# age = [25, 30, 35]
#
# data = zip(
#     customer_id,
#     name,
#     age
# )
#
# df = pd.DataFrame(
#     data,
#     columns=[
#         "customer_id",
#         "name",
#         "age"
#     ]
# )
#
# print(df)
#
#
# print("\n" + "=" * 60)
# print("14. DICTIONARY OF LISTS")
# print("=" * 60)
#
# data = {
#     "id": [101, 102, 103],
#     "name": ["John", "David", "Smith"],
#     "salary": [50000, 60000, 70000]
# }
#
# df = pd.DataFrame(data)
#
# print(df)
#
#
# print("\n" + "=" * 60)
# print("15. DICTIONARY OF TUPLES")
# print("=" * 60)
#
# data = {
#     "customer_id": (101, 102, 103),
#     "name": ("John", "David", "Smith"),
#     "age": (25, 30, 35)
# }
#
# df = pd.DataFrame(data)
#
# print(df)
#
#
# print("\n" + "=" * 60)
# print("16. DATAFRAME WITH DIFFERENT DATA TYPES")
# print("=" * 60)
#
# data = {
#     "customer_id": [101, 102, 103],
#     "name": ["John", "David", "Smith"],
#     "age": [25, 30, 35],
#     "salary": [50000.50, 60000.75, 70000.25],
#     "active": [True, False, True]
# }
#
# df = pd.DataFrame(data)
#
# print(df)
# print("\nData Types:")
# print(df.dtypes)
#
#
# print("\n" + "=" * 60)
# print("17. EMPTY DATAFRAME")
# print("=" * 60)
#
# df = pd.DataFrame()
#
# print(df)
#
#
# print("\n" + "=" * 60)
# print("18. DATAFRAME WITH SPECIFIED COLUMNS")
# print("=" * 60)
#
# df = pd.DataFrame(
#     columns=[
#         "customer_id",
#         "name",
#         "email",
#         "age"
#     ]
# )
#
# print(df)
#
#
# print("\n" + "=" * 60)
# print("19. DATAFRAME FROM 2D NUMPY ARRAY")
# print("=" * 60)
#
# data = np.arange(1, 13).reshape(4, 3)
#
# df = pd.DataFrame(
#     data,
#     columns=["A", "B", "C"]
# )
#
# print(df)
#
#
# print("\n" + "=" * 60)
# print("20. PRACTICAL ETL TEST DATA EXAMPLE")
# print("=" * 60)
#
# customer_data = [
#     (1001, "John", "Male", "john@gmail.com", 25),
#     (1002, "David", "Male", "david@gmail.com", 30),
#     (1003, "Priya", "Female", "priya@gmail.com", 28),
#     (1004, "Smith", "Male", "smith@gmail.com", 35)
# ]
#
# df = pd.DataFrame(
#     customer_data,
#     columns=[
#         "customer_id",
#         "name",
#         "gender",
#         "email",
#         "age"
#     ]
# )
#
# print(df)
#
# print("\nData Types:")
# print(df.dtypes)
#
# print("\nNumber of Rows:")
# print(len(df))
#
# print("\nNumber of Columns:")
# print(len(df.columns))
#
# print("\nColumn Names:")
# print(df.columns.tolist())
#
# print("\nShape:")
# print(df.shape)
#
#
# print("\n" + "=" * 60)
# print("ALL EXAMPLES COMPLETED")
# print("=" * 60)