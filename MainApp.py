from sqlalchemy import create_engine
import numpy as np
from Domain import Preference, User, Item

csv_delim=','
prefs_csv_file_path='/home/m-nematpour/wd/ws/python/recsys/preferences.csv'
users_csv_file_path='/home/m-nematpour/wd/ws/python/recsys/users.csv'
items_csv_file_path='/home/m-nematpour/wd/ws/python/recsys/items.csv'

prefs_db_table_name='preferences'
users_db_table_name='users'
items_db_table_name='items'

dbname = "data"
user = "postgres"
host = "192.168.88.134"
password = "1234567890"
port = 5432
connection_url = 'postgresql://{}:{}@{}:{}/{}'.format(user, password, host, port, dbname)

#engine = create_engine(connection_url)

def main():
    jaccard_sim()

def jaccard_sim():
    preference=Preference()
    user=User()
    item=Item()
    pref_df=preference.get_df(prefs_csv_file_path,csv_delim)
    user_df=user.get_df(users_csv_file_path,csv_delim)
    item_df=item.get_df(items_csv_file_path,csv_delim)
    print(item_df)

if __name__ == '__main__':
    main()