import pandas as pd
from home.models import Film
from result.models import Vote

# Read CSV file into a DataFrame
csv_file_path_film = 'home/static/liste_film_django_trad.tsv'
df_film = pd.read_csv(csv_file_path_film, sep='\t')

def run():
# Iterate through the DataFrame and create model instances
    for indexF, rowF in df_film.iterrows():

        # Create the Film instance
        film = Film(
            id = rowF['id'],
            original_title = rowF['original_title'],
            french_title = rowF['french_title'],
            romanized_title = rowF['romanized_title'],
            country = '',
            language = rowF['language'],
            release_year = rowF['release_year'],
            runtime = rowF['runtime'],
            genres = rowF['genres'],
            prod_comp = rowF['production_companies'],
            prod_countries = rowF['production_countries'],
            avg_rating = rowF['avg_rating'],
            count_rating = rowF['vote_count'],
            directors = rowF['directors'],
            writers = rowF['writers'],
            poster = rowF['poster_path'],
            plot = rowF['plot'],
        )

        vote = Vote(
            id = rowF['id'],
            original_title = rowF['original_title'],
            french_title = rowF['french_title'],
            vote_count = 0,
        )

        print(indexF)

        #to save the current film
        film.save()
        vote.save()

    print("Film, and vote data has been loaded into the Django database.")