# single line
# multiline json
# complex( Nested json)

import pandas as pd
from pandasql import sqldf
import json

pd.set_option("display.max_columns", 100)
pd.set_option("display.width", 2000)

#
# df = pd.read_json(r"C:\Users\Haritha\PycharmProjects\etl_automation_july_2026\input_files\employee.json")
#
# print(df)
#
# print(sqldf("select * from df where department='IT'"))


df = pd.read_json(r"/input_files/Complex.json")
print(df)

# with open(r"C:\Users\Haritha\PycharmProjects\etl_automation_july_2026\input_files\Complex.json", "r") as file:
#     data = json.load(file)

# print(data)
# print(type(data))
#
# df = pd.json_normalize(data)
#
# print(df)

