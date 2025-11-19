from django.urls import path
from . import views

urlpatterns = [
    path('', views.MovieCreateListView.as_view(), name= 'movie-create-list' ),
    path('<int:pk>/', views.MovieRetrieveUpdateDestroyView.as_view(), name= 'movie-detail-update-delete'),
]