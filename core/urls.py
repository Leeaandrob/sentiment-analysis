# coding: utf-8
from django.conf.urls import url

from rest_framework import routers

from core.apis import HomeAPI, ActivateView


router = routers.DefaultRouter()

urlpatterns = [
    url(r'^activate/$', ActivateView.as_view()),
    url(r'^comments/', HomeAPI.as_view(), name='comments')
]
