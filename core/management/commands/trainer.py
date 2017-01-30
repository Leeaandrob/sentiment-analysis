# coding: utf-8
import pandas as pd
import sklearn
from sklearn.externals import joblib
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.svm import SVC

from django.core.management.base import BaseCommand


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


class Command(BaseCommand):
    def handle(self, *args, **options):
        df = pd.read_csv('sentiment_analyst/static/bag_words_SVC.csv')
        print('Training...')
        train(df, 'sentiment_analyst/static/bag_words_SVC.csv')
