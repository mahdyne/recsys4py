import pandas as pd
class JaccardSim:
    def __init__(self,df_preferences):
        self.df_preferences = df_preferences

    def calcSim(self):
        df_user_pref_count=self.df_preferences.groupby('user_id').count()
        df_user_intersection=pd.merge(self.df_preferences,self.df_preferences,left_on=['item_id'],right_on=['item_id'])
        df_users_intersection_asym=df_user_intersection[df_user_intersection.user_id_x<df_user_intersection.user_id_y]
        df_users_intersection_count=df_users_intersection_asym.groupby(['user_id_x','user_id_y']).count().reset_index()
        return df_users_intersection_count