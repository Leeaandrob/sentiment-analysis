# coding: utf-8
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class HomeAPI(APIView):
    def get(self, request):
        text = request.GET.get('text')
        result = {'sentiment': 0, 'text': text}

        return Response(result, status.HTTP_200_OK)
