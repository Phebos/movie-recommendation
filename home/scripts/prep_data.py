import pandas as pd

def run():
    df = pd.read_csv('home/static/film_prep.tsv', sep='\t')

    df = df[['id', 'french_title', 'genres', 'plot', 'kw_tmdb', 'kw_imdb', 'directors']]

    df['genres'] = df['genres'].apply(lambda x: x.split(',') if not isinstance(x, float) else '')
    df['plot'] = df['plot'].apply(lambda x: x.split(' ') if not isinstance(x, float) else '')
    df['kw_imdb'] = df['kw_imdb'].apply(lambda x: x.split(',') if not isinstance(x, float) else '')
    df['kw_tmdb'] = df['kw_tmdb'].apply(lambda x: x.split(',') if not isinstance(x, float) else '')
    df['directors'] = df['directors'].apply(lambda x: x.split(',') if not isinstance(x, float) else '')

    df['genres'] = df['genres'].apply(lambda x:[i.replace(' ','') for i in x])
    df['plot'] = df['plot'].apply(lambda x:[i.replace(' ','') for i in x])
    df['kw_tmdb'] = df['kw_tmdb'].apply(lambda x:[i.replace(' ','') for i in x])
    df['kw_imdb'] = df['kw_imdb'].apply(lambda x:[i.replace(' ','') for i in x])
    df['directors'] = df['directors'].apply(lambda x:[i.replace(' ','') for i in x])

    df['genres'] = df['genres'].apply(lambda x:[i.lower() for i in x])
    df['plot'] = df['plot'].apply(lambda x:[i.lower() for i in x])
    df['kw_tmdb'] = df['kw_tmdb'].apply(lambda x:[i.lower() for i in x])
    df['kw_imdb'] = df['kw_imdb'].apply(lambda x:[i.lower() for i in x])
    df['directors'] = df['directors'].apply(lambda x:[i.lower() for i in x])

    df['tags'] = df['genres'] + df['plot'] + df['kw_tmdb'] + df['kw_imdb'] + df['directors']

    df = df[['id', 'french_title','tags']]
    df['tags'] = df['tags'].apply(lambda x:' '.join(x))

    df.to_csv('home/static/reco.tsv', sep = '\t', index = False)

    print('Le script s\'est exécuter correctement.')