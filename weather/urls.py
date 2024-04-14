from django.urls import path
from .views import UserListView, UserDetailView, LocationDetailView, LocationListView, WeatherAPIView

urlpatterns = [
    path('api/admin/user/', UserListView.as_view()),
    path('api/admin/user/<int:pk>/', UserDetailView.as_view()),
    path('api/admin/location/', LocationListView.as_view()),
    path('api/admin/location/<int:pk>/', LocationDetailView.as_view()),
    path('weather/<str:location_name>/', WeatherAPIView.as_view(), name='weather'),
]
