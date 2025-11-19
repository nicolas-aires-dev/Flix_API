from django.urls import path
from . import views

urlpatterns = [
    path('', views.ActorCreateListView.as_view(), name= 'actor-create-list' ),
    path('<int:pk>/', views.ActorRetrieveUpdateDestroyView.as_view(), name= 'actor-detail-update-delete'),
]