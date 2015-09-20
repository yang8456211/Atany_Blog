from django.conf.urls import include, url
from index import *

urlpatterns = [
    url(r'^$', 'index.views.fun'),
    url(r'^1/$', 'index.views.fun1'),
    url(r'^2/$', 'index.views.fun2'),
]