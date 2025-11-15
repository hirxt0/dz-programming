from django.urls import path
from . import views

urlpatterns = [
    path('', views.ship_list, name='ship_list'),
    path('ship/<int:pk>/', views.ship_detail, name='ship_detail'),
    path('fetch/', views.fetch_ships_from_api, name='fetch_ships'),
    path('search/', views.search_ships, name='search_ships'),
]