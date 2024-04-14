from rest_framework import serializers
from weather.models import User, Location, WeatherData


class WeatherSerializer(serializers.Serializer):
    temperature = serializers.CharField(required=False)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'authority')


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('id', 'name')

class WeatherDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeatherData
        fields = ['temperature_celsius', 'temperature_fahrenheit', 'condition_text']

