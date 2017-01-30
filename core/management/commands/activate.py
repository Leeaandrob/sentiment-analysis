# coding: utf-8
import csv
import unicodedata
from nltk.corpus import stopwords
from pandas import DataFrame

import sklearn
from sklearn.externals import joblib
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.svm import SVC

from django.core.management.base import BaseCommand


def pre_processor(text, cat):
    stops = set(stopwords.words("english"))
    words = text.lower().split()
    words = ' '.join([w for w in words if w not in stops])
    return words, cat


def remove_nonlatin(string):
    new_chars = []
    for char in string:
        if char == '\n':
            new_chars.append(' ')
            continue
        try:
            if unicodedata.name(unicode(char)).startswith(('LATIN', 'SPACE')):
                new_chars.append(char)
        except:
            continue
    return ''.join(new_chars)


def train(df, fit_file):
    df = df.dropna()
    train_size = 0.8
    X_train, X_test, Y_train, Y_test = sklearn.model_selection.train_test_split(
        df.text, df.sentiment, train_size=train_size
    )

    model = SVC()
    vect = CountVectorizer(analyzer="word",
                           tokenizer=None,
                           preprocessor=None,
                           stop_words=None)

    pipe = Pipeline([('vect', vect), ('svc', model)])
    pipe.fit(X_train, Y_train)
    pipe.fit(df.text, df.sentiment)
    joblib.dump(pipe, fit_file)


def predict(text, fit_file):
    pipe = joblib.load(fit_file)
    words = text
    return pipe.predict([words])


class Command(BaseCommand):
    def handle(self, *args, **options):
        csvfile = open('sentiment_analyst/static/us_sentiment.csv', 'r')
        reader = csv.reader(csvfile)
        data = [row for row in reader]
        texts = [(text[1], text[3]) for text in data[2:]]
        new_data_text = [pre_processor(text[1], text[0])
                         for text in texts]
        new_data_text = new_data_text[1:]
        df = DataFrame(new_data_text)
        df.columns = ['text', 'sentiment']
        df.to_csv('sentiment_analyst/static/bag_words_SVC.csv',
                  sep=';', encoding='utf-8')
        train(df, 'entiment_analyst/static/bag_words_SVC.csv')
