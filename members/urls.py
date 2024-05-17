from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('contactWithUs/', views.contactWithUs, name='contactWithUs'),
    path('entertainment/', views.entertainment, name='entertainment'),
    path('submit/', views.submit, name='submit'),
    path('entertainment/movies/', views.movies, name='movies'),
    path('entertainment/songs/', views.songs, name='songs'),
    path('entertainment/books/', views.books, name='books'),
   
    
]
