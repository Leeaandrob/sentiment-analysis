# coding: utf-8
from django.conf.urls import url

from rest_framework import routers

from core.apis import HomeAPI


router = routers.DefaultRouter()

urlpatterns = [
    url(r'^sentiment/', HomeAPI.as_view(), name='sentiment')
]
