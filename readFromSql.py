#readFromSql.py
import pandas as pd
import sqlalchemy as alc
import urllib

def getFromSql (tableName):
    params = urllib.parse.quote_plus(
    'DRIVER={SQL Server};'+
    'SERVER=DESKTOP-SQU7IEK;'+
    'DATABASE=pfizer;'+
    'Trusted_Connection=yes'
    )
    engine = alc.create_engine("mssql+pyodbc:///?odbc_connect=%s" % params)

    df = pd.read_sql(tableName, con=engine)
    return df

     

 