# urls.py

from django.urls import path, include
from rest_framework import routers
from . import views
from .api import UserAPIListView, UserAPIDetailView, ProfileAPIListView, ProfileAPIDetailView

# API Router
router = routers.DefaultRouter()
router.register(r'users', UserAPIListView, basename='users')
router.register(r'profiles', ProfileAPIListView, basename='profiles')

# URL Patterns
urlpatterns = [
    # Login and Logout Views
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # Register View
    path('register/', views.register_view, name='register'),

    # Dashboard View
    path('dashboard/', views.dashboard_view, name='dashboard'),

    # Profile Views
    path('profile/', views.profile_view, name='profile'),
    path('update-profile/', views.update_profile_view, name='update_profile'),

    # API Views
    path('api/', include(router.urls)),
    path('api/users/<pk>/', UserAPIDetailView.as_view(), name='user_detail'),
    path('api/profiles/<pk>/', ProfileAPIDetailView.as_view(), name='profile_detail'),

    # JSON Response View
    path('json-response/', views.json_response_view, name='json_response'),

    # CSV Response View
    path('csv-response/', views.csv_response_view, name='csv_response'),
]
