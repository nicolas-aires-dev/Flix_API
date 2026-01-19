from django.urls import path
from . import views

urlpatterns = [
    path('', views.ReviewCreateListView.as_view(), name='review-create-list'),
    path('<int:pk>/', views.ReviewRetrieveUpdateDestroyView.as_view(), name='review-detail-update-delete'),
]
