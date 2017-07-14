from django.conf.urls import url

from . import views

app_name = 'importcsv'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^uploadcsv/$', views.uploadcsv, name='uploadcsv'),
    url(r'^importcategories/$', views.importcategories, name='importcategories'),
    url(r'^api/$', views.api, name='api'),
]
