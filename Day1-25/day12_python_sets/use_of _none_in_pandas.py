import pandas as pd

data = [
    [1, "Alice", 25],
    [2, "Bob", None],       # Age missing
    [3, None, 30],            # Name missing
    [4, "David", 28],
    [5, "Eve", None]          # Age missing
]

# Column names
columns = ["ID", "Name", "Age"]

df = pd.DataFrame(data, columns=columns)

# Display DataFrame
print(df)