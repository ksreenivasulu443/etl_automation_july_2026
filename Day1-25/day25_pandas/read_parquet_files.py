from ctypes.macholib import framework

import pandas as pd

pd.set_option("display.max_columns", None)
pd.set_option("display.width", 2000)

df  = pd.read_parquet(r"/Day1-25/day25_pandas/userdata1.parquet")

print(df)

print(df.columns)
#
#
# Pandas
# extract ( readcsv, readjson, readexcel,read database)
# transformation
# load
#
# pytest
# small framework
#
# pyspark(Datbaricks)
# pyspark
# github
#
#
# 1. read csv1
# 2. read db
