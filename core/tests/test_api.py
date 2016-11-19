# coding: utf-8
from unittest.mock import patch

from django.urls import reverse

from rest_framework.test import APITestCase, APIClient


class CommentsApiView(APITestCase):
    @patch('core.apis.HomeAPI.get_all_comments')
    def _get_comments_from_query_string(self, _comments):
        client = APIClient()

        response = client.get(reverse('api:comments'),
                              {'page_name': 'nytimes'})

        self.assertEqual(response.status_code, 200)
        _comments.assert_called_with()
