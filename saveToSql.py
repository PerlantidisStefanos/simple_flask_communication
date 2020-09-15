#saveToSql.py
import pandas as pd
import pyodbc
import sqlalchemy as alc
from sqlalchemy import create_engine
import urllib

data = [['Alex',10,5],['Bob',12,5],['Clarke',13,6]]
df = pd.DataFrame(data,columns=['Name','Age','Value'],dtype=float)
print (df)

#save dataframe to MS SQL 
params = urllib.parse.quote_plus(
    'DRIVER={SQL Server};'+
    'SERVER=DESKTOP-SQU7IEK;'+
    'DATABASE=pfizer;'+
    'Trusted_Connection=yes'
)
engine = alc.create_engine("mssql+pyodbc:///?odbc_connect=%s" % params)
 
df.to_sql(name='PersonData', con=engine, if_exists = 'append', index=False)
 