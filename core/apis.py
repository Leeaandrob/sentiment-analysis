# coding: utf-8
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from sklearn.externals import joblib


def predict(text, fit_file='sentiment_analyst/static//bag_words_SVC.csv'):
    pipe = joblib.load(fit_file)
    words = text
    return pipe.predict([words])


class HomeAPI(APIView):
    def get(self, request):
        text = request.GET.get('text')
        response = predict(text)

        if response.tolist()[0] == '1':
            response = 'Positive'
        else:
            response = 'Negative'

        result = {'sentiment': response, 'text': text}

        return Response(result, status.HTTP_200_OK)
