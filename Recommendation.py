import pandas as pd
class Recommendation:
    def __init__(self,df_preferences,df_similarities):
        self.df_preferences = df_preferences
        self.df_similarities = df_similarities
    def gen_k_rec(self):
        df_pref_similarities = pd.merge(self.df_preferences, self.df_similarities, left_on=['user_id'], right_on=['user_id_y']).rename(columns={'item_id':'prefer_user_y'}).drop('user_id',1)
        df_k_rec=df_pref_similarities.groupby(['user_id_x','prefer_user_y']).apply(lambda x: x['jaccard_sim'].sum()/len(x)).reset_index()
        return df_k_rec




