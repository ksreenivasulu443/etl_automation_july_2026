import pandas as pd
import pyodbc
from pandasql import sqldf
#
pd.set_option("display.max_columns", 100)
pd.set_option("display.width", 2000)

######################################################################
#Reading source data
# csv(ADLS) and Azure sql server
######################################################################

source = pd.read_csv(r"/Day1-25/day26_python_read_excel_files_databases/CustomerLanding_202608310826.csv")

print(source)
######################################################################
#Reading target data
######################################################################

conn = pyodbc.connect(
    "DRIVER={ODBC Driver 18 for SQL Server};"
    "SERVER=sqlfedexdev.database.windows.net;"
    "DATABASE=fedexdb;"
    "UID=fedexadmin;"
    "PWD=Dharmavaram1@;"
)

query = " select * from bronze.CustomerLanding where CustomerID=1001"

target = pd.read_sql(query, conn)

print(target)

conn.close()

######################################################################
#comparing source and target
######################################################################
diff = sqldf("select CustomerName from source except select CustomerName from target")
duplicate = sqldf("select CustomerID, count(1) from target group by CustomerID having count(1)>1")
counts = sqldf("select  'source_count', count(1) from source union all select 'target_count', count(1) from target")
print(source.dtypes)
print(target.dtypes)

print("=="*100)
print(diff)
print("=="*100)

print("=="*100)
print(duplicate)
print("=="*100)

print("=="*100)
print(counts)
print("=="*100)

print(target.shape)

print(source.compare(target))




