from __future__ import annotations

import requests
from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Location
from .models import WeatherData
from .serializer import LocationSerializer
from .serializer import UserSerializer
from .serializer import WeatherDataSerializer
from .serializer import WeatherSerializer
from weather_app import settings


class WeatherAPIView(APIView):
    def get(self, request, location_name):
        try:
            url = f'{settings.WEATHER_API_URL}{location_name}'
            response = requests.get(url)

            if response.status_code == 200:
                data = response.json()
                if data and 'current' in data:
                    current_data = data['current']
                    if 'temp_c' in current_data and 'condition' in current_data:
                        location, created = Location.objects.get_or_create(
                            name=location_name)

                        weather_data, _ = WeatherData.objects.update_or_create(
                            location_name=location,
                            defaults={
                                'temperature_celsius': current_data['temp_c'],
                                'temperature_fahrenheit': current_data['temp_f'],
                                'condition_text': current_data['condition']['text'],
                            },
                        )

                        serializer = WeatherDataSerializer(weather_data)
                        return Response(serializer.data)
                    else:
                        return Response('Weather data is incomplete.', status=status.HTTP_400_BAD_REQUEST)
                else:
                    return Response(
                        'Unable to fetch data from API or invalid data.',
                        status=status.HTTP_400_BAD_REQUEST,
                    )
            else:
                return Response('Unable to retrieve weather information.', status=response.status_code)
        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class LocationListView(APIView):
    def get(self, request):
        locations = Location.objects.all()
        context = {'locations': locations}

        return render(request, 'city_query.html', context)


class LocationDetailView(generics.RetrieveAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
