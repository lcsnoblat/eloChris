from django.conf.urls import url, patterns
from django.contrib import admin

from main import views
from eloChris import settings

urlpatterns = [
    url(r'^$', views.index, name='url_index'),
    url(r'^admin/', admin.site.urls)
]
