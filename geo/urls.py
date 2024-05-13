# from django.contrib import admin
from django.urls import path

from . import views

app_name = 'geo'

urlpatterns = [
    path('', views.homepage, name='index'),
    path('<int:geonameid>',
         views.get_city_by_geonameid, name='city_by_geonameid'),
    path('<int:page>/<int:paginate_by>',
         views.get_city_list, name='get_city_list'),
    path('<slug:city1>/<slug:city2>',
         views.get_cities_info, name='get_cities_info'),
]
