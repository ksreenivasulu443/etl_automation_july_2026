# #!/usr/bin/env python
# # coding: utf-8
#
# # In[103]:
#
#
# import pandas as pd
# import cx_Oracle
# from pandasql import sqldf
# import os
# import numpy as np
# from datetime import datetime
# import psycopg2 as pg
# import pandas.io.sql as psql
# import mysql.connector
# import MySQLdb as mariadb
# import base64
# import streamlit as st
#
#
#
# connection ={}
#
# for i in range(0,connection.shape[0]):
#         #print(i)
#     if connection['Source Database Name'][i]=='ORACLE':
#             #print(connection['Database'][i])
#             #print(True)
#             dsn_tns = cx_Oracle.makedsn(connection['Source Address'][i],1521,service_name=connection['Source Database'][i])
#             conn = cx_Oracle.connect(user=connection['Source Username'][i], password=connection['Source Password'][i], dsn=dsn_tns)
#             curs = conn.cursor()
#             query= connection['Source Query'][i]
#             #print(query)
#             curs.execute(query)
#             columns=[desc[0] for desc in curs.description]
#             data=curs.fetchall()
#             #df_name='df_'+str(connection['Key'][i])
#             #print(df_name)
#     #       df_name='df'
#     #       connection['Key'][i]=pd.DataFrame(list(data),columns=columns)
#             df = pd.DataFrame(list(data),columns=columns)
#             list_of_source[connection['Source Key'][i]]=(df)
#             conn.close()
#
#     elif connection['Source Database Name'][i]=='MYSQL' :
#                 #print(True)
#                 import mysql.connector
#                 mydb =mysql.connector.connect(host=connection['Source Address'][i],user=connection['Source Username'][i],password=connection['Source Password'][i],database=connection['Source Database'][i])
#                 Src_mycursor = mydb.cursor()
#                 query= connection['Source Query'][i]
#                 Src_mycursor.execute(query)
#                 columns=[desc[0] for desc in Src_mycursor.description]
#                 data = Src_mycursor.fetchall()
#                 df = pd.DataFrame(list(data),columns=columns)
#                 # list_of_source[connection['Source Key'][i]]=(df)
#
#
#     elif connection['Source Database Name'][i]=='POSTG' :
#                 #print(True)
#                 connection1 = pg.connect(host=connection['Source Address'][i],dbname=connection['Source Database'][i],user=connection['Source Username'][i],password=connection['Source Password'][i])
#                 query= connection['Source Query'][i]
#                 df = psql.read_sql_query(query, connection1)
#                 # list_of_source[connection['Source Key'][i]]=(df)
#
#     elif connection['Source Database Name'][i]=='MARIA' :
#                 conn = mariadb.connect(user=connection['Source Username'][i],password=connection['Source Password'][i],host=connection['Source Address'][i],port=136,database=connection['Source Database'][i])
#                 query= connection['Source Query'][i]
#                 df=pd.read_sql_query(query ,conn)
#                 # list_of_source[connection['Source Key'][i]]=(df)
#
#     elif connection['Source Database Name'][i]=='CSV':
#                 print(connection['Source Query'][i])
#                 df=pd.read_csv(connection['Source Query'][i])
#                 # list_of_source[connection['Source Key'][i]]=(df)
#
#     elif connection['Source Database Name'][i]=='Mongo':
#                 client = pymongo.MongoClient(connection['Source Address'][i])
#                 db = client["local"]
#                 my_collection = db[connection['Source Query'][i]].find()
#                 print(my_collection)
#                 df = pd.DataFrame(my_collection)
#                 df = df.drop('_id',1)
#                 # list_of_source[connection['Source Key'][i]] = (df)
#
#             elif connection['Source Database Name'][i]=='EXCEL':
#                 df = pd.read_excel(connection['Source Query'][i])
#                 # list_of_source[connection['Source Key'][i]]=(df)
#
#
#
