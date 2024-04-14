from rest_framework import serializers, generics
from weather.models import User, Location, WeatherData


class WeatherSerializer(serializers.Serializer):
    temperature = serializers.CharField(required=False)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'authority')


class WeatherDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeatherData
        fields = ['temperature_celsius', 'temperature_fahrenheit', 'condition_text']


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('id', 'name')


class LocationListView(generics.ListAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
