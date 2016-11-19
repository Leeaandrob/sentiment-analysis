from django.conf.urls import include, url
from django.contrib import admin

from mano_id import urls as mano_id_urls

urlpatterns = [
    url(r'', include(mano_id_urls, namespace='gate_id')),
    url(r'^admin/', include(admin.site.urls)),
]
