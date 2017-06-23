from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.champion, name='champion'),
    url(r'^reccent_update/$', views.champion, name='reccent_update'),
    url(r'^all_data/$', views.all_data),
    url(r'^reccent_update_champion/$', views.reccent_update_champion),
]
