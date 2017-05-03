from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.all_champion, name='champion'),
    url(r'^reccent_update/$', views.reccent_update),
]
