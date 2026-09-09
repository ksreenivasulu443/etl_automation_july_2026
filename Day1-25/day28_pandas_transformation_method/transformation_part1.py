import numpy as np
import pandas as pd
pd.set_option('display.max_columns',None)
pd.set_option('display.width',2000)

data = {
    "Name": ["John", "Smith", "David", "Mary","Sreeni"],
    "Age": [25, 30, 28, 35,np.nan],
    "Salary": [40000, 50000, 45000, 60000,70000],
    "City": ["Bangalore", "Chennai", "Bangalore", "Hyderabad","Bangalore"]
}

df = pd.DataFrame(data=data)

# print(df)

#===============================================================================
# dataframe Statistics
#===============================================================================
# print("rows available in df", len(df))
# # print("methods in df", dir(df))
# print("num of rows and columns", df.shape)
# print("Num rows", df.shape[0])
# print("Num columns", df.shape[1])
# print("columns", df.columns, len(df.columns))
# print("="*100)
# print("df.info", df.info())
# print("="*100)
# print("df.info", df.describe())
# print("="*100)
# print(df.nlargest(2, "Salary"))
# print("="*100)
# print(df.nsmallest(1, "Salary"))
# print("="*100)
# print(df.nlargest(3, "Salary").nsmallest(1, "Salary")) # second highest salary
# print("="*100)
# print("unique values in city column", df.City.nunique())
#
# print(df.City.unique())

# DB(on-prem) DB(cloud)

# select * from onprem.table
# minus
# select * frm cloud.table

###############################################################################################
# Selection and filter
###################################################################################################

df = pd.read_parquet(r"/input_files/userdata1.parquet")

print(df)

# print(df.shape)
#
# print("top n rows")
# print(df.head(n=3))
#
# print("bottom n rows")
# print(df.tail(n=20))

# print("selecting one column")
# print(df['first_name']) # df.first_name
#
# print("selecting one/more column")
# print(df[['first_name','last_name','email']])
#
# print(df.index)

# print("0 index row")
# print(df.iloc[30:50])
#
# print(df.iloc[998::-2])

## select 0:4 index and 1 to 10 columns
print("="*100)
print(df.iloc[0:4 , 2:4])
print("="*100)
print(df.loc[0:5,['first_name','last_name',] ])

print(df.loc[df['first_name']=='John'])





