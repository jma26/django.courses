from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^courses/add$', views.add),
    url(r'^courses/(?P<id>\d+)/confirm$', views.confirm),
    url(r'^courses/(?P<id>\d+)/remove$', views.remove)
]