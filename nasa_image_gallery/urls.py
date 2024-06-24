from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_page, name='index-page'),
    path('login/', views.user_login, name='login'),
    path('home/', views.home, name='home'),
    path('buscar/', views.search, name='buscar'),

    path('favourites/', views.get_user_favourites, name='favoritos'),
    path('favourites/add/', views.saveFavourite, name='agregar-favorito'),
    path('favourites/delete/', views.deleteFavourite, name='borrar-favorito'),

    path('exit/', views.exit, name='exit'),
]
