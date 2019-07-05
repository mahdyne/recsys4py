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
    df_cleansed_pref=preference.get_cleansed_df(prefs_csv_file_path,csv_delim)
    print(df_cleansed_pref)

    user=User()
    df_cleansed_user=user.get_cleansed_df(users_csv_file_path,csv_delim)
    print(df_cleansed_user)

    item=Item()
    df_cleansed_item=item.get_cleansed_df(items_csv_file_path,csv_delim)
    print(df_cleansed_item)

if __name__ == '__main__':
    main()