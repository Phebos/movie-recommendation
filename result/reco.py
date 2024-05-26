import numpy as np
import pandas as pd

def recommend(id):
    # reco = np.load('result/static/recommendation.npy')
    reco = np.load('result/static/recommendation.npy')
    df_ml = pd.read_csv('result/static/movies.tsv', sep='\t')

    list_id = []

    movie_index = df_ml[df_ml['id']==id].index[0]
    distances = reco[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse= True, key= lambda x:x[1])[1:6]

    for i in movies_list:
        list_id.append(df_ml.iloc[i[0]].id)
    
    return(list_id)