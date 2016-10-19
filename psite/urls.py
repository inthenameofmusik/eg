from django.conf.urls import url
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    url(r'^$', views.home_page, name='homepage'),
    url(r'^gallery/$', views.gallery, name='gallery'),
    url(r'^music/$', views.tracks, name='music'),
    url(r'^send_message/$', views.send_message, name='send_message')
]
