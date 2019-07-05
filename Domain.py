import pandas as pd
import sqlalchemy
import numpy as np

from DAO import DAO


class Preference(DAO):
    def cleanse_df(self,df):
        df_dropped_nan=df.dropna(axis=0,how='any')[df.item_id!='1']
        df1=df_dropped_nan[df_dropped_nan.user_id.apply(lambda x: x.isnumeric())]
        df2 = df1[df1.item_id.apply(lambda x: x.isnumeric())]
        df2.item_id = df2.item_id.astype(int)
        df2.user_id=df2.user_id.astype(int).copy()
        return df2
    def get_cleansed_df(self,file_path,delim):
        df=DAO.get_df(self,file_path,delim)
        cleansed_df=self.cleanse_df(df)
        return cleansed_df


class User(DAO):
    def cleanse_df(self, df):
        df_dropped_nan = df.dropna(axis=0, how='any')
        df1 = df_dropped_nan[df_dropped_nan.user_id.apply(lambda x: x.isnumeric())]
        df1.name= df1.name.str.replace("\d+",'')
        df2=df1[df1.name!='']
        df2.user_id=df2.user_id.astype(int)
        return df2
    def get_cleansed_df(self,file_path,delim):
        df=DAO.get_df(self,file_path,delim)
        cleansed_df=self.cleanse_df(df)
        return cleansed_df

class Item(DAO):
    def cleanse_df(self, df):
        df_dropped_nan = df.dropna(axis=0, how='any')
        df1 = df_dropped_nan[df_dropped_nan.item_id.apply(lambda x: x.isnumeric())]
        df1.item_name = df1.item_name.str.replace("\d+", '')
        df2 = df1[df1.item_name != '']
        df2.item_id = df2.item_id.astype(int)
        return df2

    def get_cleansed_df(self,file_path,delim):
        df=DAO.get_df(self,file_path,delim)
        cleansed_df=self.cleanse_df(df)
        return cleansed_df