# urls.py

from django.urls import path
from .views import UserAPIListView, UserAPIDetailView, ProfileAPIListView, ProfileAPIDetailView

urlpatterns = [
    path('users/', UserAPIListView.as_view(), name='user_list'),
    path('users/<int:pk>/', UserAPIDetailView.as_view(), name='user_detail'),
    path('profiles/', ProfileAPIListView.as_view(), name='profile_list'),
    path('profiles/<int:pk>/', ProfileAPIDetailView.as_view(), name='profile_detail'),
]
