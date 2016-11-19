# coding: utf-8
from django.views.generic import TemplateView

import requests


class HomeView(TemplateView):
    template_name = 'core/index.html'

    def get_all_comments(self):
        response = requests.get(
            'https://facebook-downloader.herokuapp.com/download/?query=nytimes'
            '/posts?fields=comments.limit(180),permalink_url&limit=5')

        return response.json()

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['comments'] = self.get_all_comments()

        return context
