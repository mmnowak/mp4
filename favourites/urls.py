from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('view_favourites/', views.view_favourites, name='view_favourites'),
    path('add_favourite/<int:product_id>/',
         views.add_favourite, name='add_favourite'),
    path('remove_favourite/<product_id>/<redirect_from>/',
         views.remove_favourite,
         name='remove_favourite'),
]
