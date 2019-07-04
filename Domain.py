import pandas as pd
import sqlalchemy
import numpy as np



class Preference:
    # def __init__(self, engine, csv_file_path):
    #     return 1
    def get_df(self,file_path,delim):
        df=pd.read_csv(filepath_or_buffer=file_path,delimiter=delim)
        return self.cleanse_df(df)

    def get_df_sql(self,engine,table_name):
        sql="""select * from {}""".format(table_name)
        df=pd.read_sql_query(sqlalchemy.text(sql), con=engine)
        return df

    def cleanse_df(self,df):
        df1 = df.dropna()[(pd.to_numeric(df.user_id, errors='coerce').notnull()) & (pd.to_numeric(df['item_id'], errors='coerce').notnull())]
        df1.user_id=df1.user_id.astype(int)
        df1.item_id=df1.item_id.astype(int)
        return df1


class User:
    def get_df(self, file_path, delim):
        df = pd.read_csv(filepath_or_buffer=file_path, delimiter=delim)
        return self.cleanse_df(df)

    def get_df_sql(self, engine, table_name):
        sql = """select * from {}""".format(table_name)
        df = pd.read_sql_query(sqlalchemy.text(sql), con=engine)
        return df
    def cleanse_df(self, df):
        df1= df.dropna()[(pd.to_numeric(df.user_id, errors='coerce').notnull()) & (df.name.str.contains("\D+"))]
        df1.user_id=df1.user_id.astype(int)
        return df1


class Item:
    def get_df(self, file_path, delim):
        df = pd.read_csv(filepath_or_buffer=file_path, delimiter=delim)
        return self.cleanse_df(df)

    def get_df_sql(self, engine, table_name):
        sql = """select * from {}""".format(table_name)
        df = pd.read_sql_query(sqlalchemy.text(sql), con=engine)
        return df

    def cleanse_df(self, df):
        df1 = df.dropna()[(pd.to_numeric(df.item_id, errors='coerce').notnull()) & (df.item_name.str.contains("\D+"))]
        df1.item_id = df1.item_id.astype(int)
        return df1