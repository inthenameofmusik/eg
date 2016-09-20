from django.conf.urls import url
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='home.html'), name='homepage'),
    url(r'^gallery/$', TemplateView.as_view(template_name='gallery.html'), name='gallery'),
    url(r'^music/$', TemplateView.as_view(template_name='music.html'), name='music')
]
