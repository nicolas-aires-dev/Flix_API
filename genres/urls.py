from django.urls import path
from . import views

urlpatterns = [
    path('', views.GenreCreateListView.as_view(), name='genre-create-list'),
    path('<int:pk>/', views.GenreRetrieveUpdateDeleteView.as_view(), name='genre-detail-update-delete'),
]
