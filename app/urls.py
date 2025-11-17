from django.contrib import admin
from django.urls import path
from genres.views import GenreCreateListView, GenreRetrieveUpdateDeleteView
from actors.views import ActorCreateListView, ActorRetrieveUpdateDestroyView
from movies.views import MovieCreateListView, MovieRetrieveUpdateDestroyView
from reviews.views import ReviewCreateListView, ReviewRetrieveUpdateDestroyView

urlpatterns = [
    path('admin/', admin.site.urls),

    #Genres
    path('genres/', GenreCreateListView.as_view(), name = 'genre-create-list'),
    path('genres/<int:pk>/', GenreRetrieveUpdateDeleteView.as_view(), name = 'genre-detail-update-delete' ),

    #Actors
    path('actors/', ActorCreateListView.as_view(), name= 'actor-create-list' ),
    path('actors/<int:pk>/', ActorRetrieveUpdateDestroyView.as_view(), name= 'actor-detail-update-delete'),

    #Movies
    path('movies/', MovieCreateListView.as_view(), name= 'movie-create-list' ),
    path('movies/<int:pk>/', MovieRetrieveUpdateDestroyView.as_view(), name= 'movie-detail-update-delete'),

    #Reviews
    path('reviews/', ReviewCreateListView.as_view(), name= 'review-create-list' ),
    path('reviews/<int:pk>/', ReviewRetrieveUpdateDestroyView.as_view(), name= 'review-detail-update-delete'),
    
]
