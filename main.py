# import pandas as pd
#
# df = pd.read_json(r"C:\Users\Haritha\PycharmProjects\etl_automation_july_2026\input_files\employee.json")
#
# print(df)
#
#
# import json
# import pandas as pd
#
# with open(r"C:\Users\Haritha\PycharmProjects\etl_automation_july_2026\input_files\Complex.json", "r") as file:
#     data = json.load(file)
#
# print(data)
#
# df = pd.json_normalize(data)
#
# print(df)
import pandas as pd
df = pd.read_excel(r"C:\Users\Haritha\PycharmProjects\etl_automation_july_2026\input_files\Master_Test_Template.xlsx")
print(df)