from __future__ import annotations

from django.urls import path

from .views import LocationDetailView
from .views import LocationListView
from .views import UserDetailView
from .views import UserListView
from .views import WeatherAPIView

urlpatterns = [
    path('api/admin/user/', UserListView.as_view()),
    path('api/admin/user/<int:pk>/', UserDetailView.as_view()),
    path('api/admin/location/', LocationListView.as_view()),
    path('api/admin/location/<int:pk>/', LocationDetailView.as_view()),
    path('weather/<str:location_name>/',
         WeatherAPIView.as_view(), name='weather'),
    path('locations/', LocationListView.as_view(), name='location-list'),
]
