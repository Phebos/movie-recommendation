import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
import nltk
import spacy
from sklearn.metrics.pairwise import cosine_similarity

def run():
    df = pd.read_csv('home/static/reco.tsv', sep='\t')

    nltk.download('popular')

    nlp = spacy.load('en_core_web_sm')

    def clean_lem(text):
        tokens = nltk.word_tokenize(text)
        tokens = [w for w in tokens if not w in nltk.corpus.stopwords.words("english")]

        lemma = nlp(' '.join(tokens))
        tokens = [w.lemma_ for w in lemma]

        return " ".join(tokens)

    df['tags'] = df['tags'].apply(clean_lem)


    cv = CountVectorizer(max_features = 5000, stop_words='english')
    vectors = cv.fit_transform(df['tags']).toarray()
    similarity = cosine_similarity(vectors)

    np.save('result/static/recommendation.npy', similarity)

    print('Le script s\'est exécuter correctement.')