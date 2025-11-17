from django.contrib import admin
from django.urls import path
from genres.views import GenreCreateListView, GenreRetrieveUpdateDeleteView
from actors.views import ActorCreateListView, ActorRetrieveUpdateDestroy
from movies.views import MovieCreateListView, MovieRetrieveUpdateDestroy

urlpatterns = [
    path('admin/', admin.site.urls),

    #Genres
    path('genres/', GenreCreateListView.as_view(), name = 'genre-create-list'),
    path('genres/<int:pk>/', GenreRetrieveUpdateDeleteView.as_view(), name = 'genre-detail-update-delete' ),

    #Actors
    path('actors/', ActorCreateListView.as_view(), name= 'actor-create-list' ),
    path('actors/<int:pk>/', ActorRetrieveUpdateDestroy.as_view(), name= 'actor-detail-update-delete'),

    #Movies
    path('movies/', MovieCreateListView.as_view(), name= 'movie-create-list' ),
    path('movies/<int:pk>/', MovieRetrieveUpdateDestroy.as_view(), name= 'movie-detail-update-delete'),
    
]
