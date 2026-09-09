import pandas as pd

# ============================================================
# DATAFRAME 1: CUSTOMERS
# ============================================================

customers = pd.DataFrame({
    "customer_id": [101, 102, 103, 104, 105, 106],
    "region": ["South", "North", "South", "West", "East", "North"],
    "customer_name": ["Ravi", "John", "Priya", "David", "Anita", "Mike"]
})

print("=" * 100)
print("CUSTOMERS")
print(customers)


# ============================================================
# DATAFRAME 2: ORDERS
# ============================================================

orders = pd.DataFrame({
    "order_id": [1001, 1002, 1003, 1004, 1005, 1006],
    "cust_id": [101, 102, 103, 103, 105, 107],
    "order_region": ["South", "North", "South", "North", "East", "West"],
    "order_amount": [5000, 3000, 4500, 2000, 7000, 1500]
})

print("=" * 100)
print("ORDERS")
print(orders)


# ============================================================
# DATAFRAME 3: CUSTOMER ADDRESS
# ============================================================

customer_address = pd.DataFrame({
    "cust_no": [101, 102, 103, 104, 105, 108],
    "area": ["South", "North", "South", "West", "West", "East"],
    "city": ["Bangalore", "Delhi", "Hyderabad", "Mumbai", "Pune", "Chennai"],
    "pincode": [560001, 110001, 500001, 400001, 411001, 600001]
})

print("=" * 100)
print("CUSTOMER ADDRESS")
print(customer_address)


# ============================================================
# INNER JOIN
# customers + orders
#
# customers.customer_id = orders.cust_id
# customers.region      = orders.order_region
# ============================================================

inner_join = pd.merge(
    customers,
    orders,
    how="inner",
    left_on=["customer_id", "region"],
    right_on=["cust_id", "order_region"]
)

print("=" * 100)
print("INNER JOIN")
print(inner_join)


# ============================================================
# LEFT JOIN
# ============================================================

left_join = pd.merge(
    customers,
    orders,
    how="left",
    left_on=["customer_id", "region"],
    right_on=["cust_id", "order_region"]
)

print("=" * 100)
print("LEFT JOIN")
print(left_join)


# ============================================================
# RIGHT JOIN
# ============================================================

right_join = pd.merge(
    customers,
    orders,
    how="right",
    left_on=["customer_id", "region"],
    right_on=["cust_id", "order_region"]
)

print("=" * 100)
print("RIGHT JOIN")
print(right_join)


# ============================================================
# FULL OUTER JOIN
# ============================================================

outer_join = pd.merge(
    customers,
    orders,
    how="outer",
    left_on=["customer_id", "region"],
    right_on=["cust_id", "order_region"],
    indicator=True
)

print("=" * 100)
print("FULL OUTER JOIN")
print(outer_join)


# ============================================================
# LEFT ANTI JOIN
# Customers having NO matching order
# ============================================================

left_anti = pd.merge(
    customers,
    orders,
    how="left",
    left_on=["customer_id", "region"],
    right_on=["cust_id", "order_region"],
    indicator=True
).query('_merge == "left_only"')

print("=" * 100)
print("LEFT ANTI JOIN")
print(left_anti)


# ============================================================
# JOIN CUSTOMERS + CUSTOMER ADDRESS
#
# customers.customer_id = customer_address.cust_no
# customers.region      = customer_address.area
# ============================================================

customer_details = pd.merge(
    customers,
    customer_address,
    how="inner",
    left_on=["customer_id", "region"],
    right_on=["cust_no", "area"]
)

print("=" * 100)
print("CUSTOMERS + ADDRESS")
print(customer_details)


# ============================================================
# THREE DATAFRAME JOIN
# Customers + Orders + Customer Address
# ============================================================

result = pd.merge(
    customers,
    orders,
    how="left",
    left_on=["customer_id", "region"],
    right_on=["cust_id", "order_region"]
)

result = pd.merge(
    result,
    customer_address,
    how="left",
    left_on=["customer_id", "region"],
    right_on=["cust_no", "area"]
)

print("=" * 100)
print("THREE DATAFRAME JOIN")
print(result)