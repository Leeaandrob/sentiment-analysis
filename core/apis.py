# coding: utf-8
import requests

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class HomeAPI(APIView):
    def get_all_comments(self, page_name):
        url = 'https://facebook-downloader.herokuapp.com/download/?query={page_name}/posts?fields=comments.limit(50),permalink_url&limit=3'.format(page_name=page_name)

        response = requests.get(url)

        return response.json()

    def get(self, request):
        page_name = request.GET.get('page_name')
        result = self.get_all_comments(page_name)

        return Response(result, status.HTTP_200_OK)
