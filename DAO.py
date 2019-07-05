import pandas as pd
import sqlalchemy

class DAO:
    def get_df(self,file_path,delim):
        df=pd.read_csv(filepath_or_buffer=file_path,delimiter=delim)
        return df

    def get_df_sql(self,engine,table_name):
        sql="""select * from {}""".format(table_name)
        df=pd.read_sql_query(sqlalchemy.text(sql), con=engine)
        return df