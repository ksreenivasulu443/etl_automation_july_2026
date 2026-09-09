import numpy as np
import pandas as pd
from pandasql import sqldf
pd.set_option('display.max_columns',None)
pd.set_option('display.width',2000)

# data = {
#     "Name": ["John", "Smith", "David", "Mary","Sreeni"],
#     "Age": [25, 30, 28, 35,np.nan],
#     "Salary": [40000, 50000, 45000, 60000,70000],
#     "City": ["Bangalore", "Chennai", "Bangalore", "Hyderabad","Bangalore"]
# }
#
# df = pd.DataFrame(data=data)
#
# print(df)
###############################################################################################
# filter
###################################################################################################
# df_new = df[  df['Salary']>=45000  ]
#
# print(df_new)
#
# print(df[ (df['Salary']>45000)  &  (df['Age']>=35 )  & (df['City']=="Bangalore" )] )

# print("+"*70)
# print(df.query(" Salary>45000 and Age>=35 and City == 'Bangalore' "))
# print("+"*70)


###############################################################################################
# Null value treatment
###################################################################################################


# data = {
#     "Name": [np.nan, "Smith", "David", "Mary","Sreeni"],
#     "Age": [np.nan, np.nan, 28, 35,np.nan],
#     "Salary": [None, 50000, 45000, 60000,None],
#     "City": [None, "Chennai", "Bangalore", "Hyderabad","NULL"]
# }
#
# df = pd.DataFrame(data=data)
#
# print(df)

# print(df.info())

# print(df.isnull().sum())
#
# print(df['Salary'].fillna(25000))


# print(df.fillna({'Salary':25000, 'Name':'unknwn',"Age": df.Age.mean()}, inplace=True))
#
# print(df.dropna(how='any'))
# df= df.dropna(how='all')

# print(df_new)

# print(df.dropna(subset= ['Name']))


#####################################################################################
#Aggregation functions
#####################################################################################

# df = pd.DataFrame({
#     'department': ['IT', 'IT', 'HR', 'HR', 'HR','IT'],
#     'gender': ['M', None, 'M', 'F', 'M','M'],
#     'salary': [50000, 60000, 40000, None, 70000,25000]
# })
# # count, min, max, avg, sum
#
# # print(df.describe())
#
# print(df.department.count())
#
# print("sum", df.salary.sum())
#
# print("mean", df.salary.mean())
#
# print("min", df.salary.min())
# print("max",df.salary.max())
#
# print(sqldf("select  count(1), sum(salary), avg(salary), min(salary), max(salary) from df "))
#
# print(df.groupby('department')['salary'].agg(['sum', 'min','mean','max','count']))
#
#



data = {
    "EmpID": [101, 102, 103, 101, 104, 102, 105, 103],
    "EmpName": ["John", "David", "Smith", "John", "Robert", "David", "Peter", "Smith"],
    "Department": ["IT", "HR", "Finance", "IT", "Sales", "HR", "IT", "Finance"],
    "Salary": [50000, 45000, 60000, 50000, 55000, 45000, 52000, 60000]
}

df = pd.DataFrame(data)

print(df)

print(sqldf("select EmpID, count(1) as count from df group by EmpID having count(1)>1"))

print(df.groupby('EmpID').size().reset_index(name='count').query('count>1'))


print("total count", len(df))

print(df.drop_duplicates(subset='EmpID', keep='last'))

print("after dropping duplicates count", len(df.drop_duplicates(subset='EmpID', keep='last')))



