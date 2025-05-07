from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('drivers/', views.driver_list, name='driver_list'),
    path('teams/', views.team_list, name='team_list'),
    path('tracks/', views.track_list, name='track_list'),
    path('grandprix/', views.grand_prix_list, name='grand_prix_list'),
    path('list/', views.driver_list_grouped, name='driver_list_grouped'),
]