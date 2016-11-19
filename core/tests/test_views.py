# coding: utf-8
from unittest.mock import patch

from django.test import TestCase
from django.urls import reverse


class HomeViewTest(TestCase):
    @patch('core.views.HomeView.get_all_comments')
    def test_correct_response(self, _comments):
        response = self.client.get(reverse('home'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/index.html')

    @patch('core.views.HomeView.get_all_comments')
    def test_comments_context_in_html(self, _comments):
        response = self.client.get(reverse('home'))

        self.assertIn('comments', response.context)
        _comments.assert_called_once_with()
