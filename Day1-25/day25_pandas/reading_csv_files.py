import pandas as pd

from pandasql import sqldf
from streamlit.proto import Snow_pb2

# polars
# duckdb
#######################################################################################################################
#Read csv using pandas with header
#######################################################################################################################

# df = pd.read_csv(filepath_or_buffer=r"C:\Users\Haritha\PycharmProjects\etl_automation_july_2026\day25_pandas\customer_with_header.csv",
#                  sep=',',
#                  header=0)
#
# # df = pd.read_csv(filepath_or_buffer="C:\\Users\\Haritha\\PycharmProjects\\etl_automation_july_2026\\day25_pandas\\customer_with_header.csv")
# #
# # df = pd.read_csv(filepath_or_buffer="C:/Users/Haritha/PycharmProjects/etl_automation_july_2026/day25_pandas/customer_with_header.csv")
#
# print(df)
#######################################################################################################################
#Reading csv file(with out header)
#######################################################################################################################


# df_without_header = pd.read_csv(r"C:\Users\Haritha\PycharmProjects\etl_automation_july_2026\day25_pandas\customer_with_out_header.csv",
#                                 sep=',',
#                                 names= ['CustomerId', 'FirstName', 'Email', 'City', 'Country'])
# print(df_without_header)


#######################################################################################################################
#Reading csv file(with n header)
#######################################################################################################################


# df_with_n_header = pd.read_csv(r"C:\Users\Haritha\PycharmProjects\etl_automation_july_2026\day25_pandas\customer_with_two_header.csv",
#                                 sep='|',
#                                 header = 2,
#                                 names=['Sno', 'FirstName', 'Email', 'City', 'Country'], nrows=1
#                                 )
# print(df_with_n_header)


#######################################################################################################################
#query df using sqldf
#######################################################################################################################
# print(sqldf("select * from df_with_n_header where sno=1"))
#
#
# print(sqldf("select sno, upper(firstname) as name, substr(email,1 ,4) as username from df_with_n_header"))
#
# print(sqldf("select sno, count(1) from df_with_n_header group by sno having count(1)>1 "))


df_fix = pd.read_fwf(filepath_or_buffer=r"/Day1-25/day25_pandas/customer_fixed_width.csv",
                     widths=[5,20,15,10], header=None, names=['sno','name', 'city','country'], dtype={'sno':str,'name':str,'city':str,'country':str})

print(df_fix)

print(df_fix.dtypes)


