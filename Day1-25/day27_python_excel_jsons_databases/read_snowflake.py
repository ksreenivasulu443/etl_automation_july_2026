import pandas as pd
import snowflake.connector as snow

pd.set_option('display.max_columns',None)
pd.set_option('display.width',2000)


conn=snow.connect(
    user='fedexadmin',
    password='Dharmavaram1@1@',
    account='kefeety-io28450',
    warehouse='COMPUTE_WH',
)

df = pd.read_sql(sql="select * from test_db.test_schema.customer", con= conn)

print(df)