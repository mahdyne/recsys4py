import pandas as pd
class SimilarityMeasure:
    def __init__(self,df_preferences):
        self.df_preferences = df_preferences
    def jaccardSim(self):
        df_user_pref_count=self.df_preferences.groupby('user_id').count().reset_index().rename(columns={'item_id':'pref_count'})
        df_user_intersection=pd.merge(self.df_preferences,self.df_preferences,left_on=['item_id'],right_on=['item_id'])
        df_users_intersection_asym=df_user_intersection[df_user_intersection.user_id_x<df_user_intersection.user_id_y]
        df_users_intersection_count=df_users_intersection_asym.groupby(['user_id_x','user_id_y']).count().reset_index().rename(columns={'item_id':'intersection_count'})
        df_user_x=pd.merge(df_user_pref_count,df_users_intersection_count,left_on='user_id',right_on='user_id_x').rename(columns={'pref_count':'pref_count_user_x'})
        df_user_x_y=pd.merge(df_user_pref_count,df_user_x,left_on='user_id',right_on='user_id_y').rename(columns={'pref_count':'pref_count_user_y'})
        df_user_x_y['jaccard_sim']=(df_user_x_y['intersection_count']*1.0)/(df_user_x_y['pref_count_user_x']+df_user_x_y['pref_count_user_y']-df_user_x_y['intersection_count'])
        df_jaccard_sim=df_user_x_y[['user_id_x','user_id_y','jaccard_sim']]
        return df_jaccard_sim
