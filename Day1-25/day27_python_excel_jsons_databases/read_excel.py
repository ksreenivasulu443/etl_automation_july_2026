import pandas as pd

pd.set_option("display.max_columns", 100)
pd.set_option("display.width", 2000)

# df_product= pd.read_excel(r"C:\Users\Haritha\PycharmProjects\etl_automation_july_2026\input_files\Contact_info.xlsx", sheet_name="product")
#
#
# df_customer = pd.read_excel(r"C:\Users\Haritha\PycharmProjects\etl_automation_july_2026\input_files\Contact_info.xlsx", sheet_name="customer")
#
# df_excel = pd.concat([ df_customer,df_product])
#
# print(df_excel)

# for i in range(2): # 0,1
#     df = pd.read_excel(r"C:\Users\Haritha\PycharmProjects\etl_automation_july_2026\input_files\Contact_info.xlsx", sheet_name=i)
#     print(df)



import pandas as pd

data = pd.read_excel(r"/input_files/Contact_info.xlsx", sheet_name=None)

print(data.keys())

print(data)



