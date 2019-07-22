from Domain import Preference, User, Item
from SimilarityMeasure import *
csv_delim=','
prefs_csv_file_path='preferences.csv'
users_csv_file_path='users.csv'
items_csv_file_path='items.csv'

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
    jaccard_sim=JaccardSim(df_cleansed_pref).calcSim()
    print(jaccard_sim)


if __name__ == '__main__':
    main()