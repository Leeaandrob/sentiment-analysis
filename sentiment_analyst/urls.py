from django.conf.urls import include, url
from django.contrib import admin

from core import urls as core_urls
from core.views import HomeView

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^api/', include(core_urls, namespace='api')),
]
