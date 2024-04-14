from django.contrib import admin
from .models import Location, RequestLog, WeatherData


@admin.register(RequestLog)
class RequestLogAdmin(admin.ModelAdmin):
    list_display = ('user', 'path', 'method', 'ip_address', 'user_agent', 'requested_at', 'response_at')
    list_filter = ('user', 'method', 'ip_address', 'requested_at')
    search_fields = ('path', 'user_agent')
    readonly_fields = ('requested_at', 'response_at')


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(WeatherData)
class WeatherDataAdmin(admin.ModelAdmin):
    list_display = ['location_name', 'temperature_celsius', 'temperature_fahrenheit', 'condition_text', 'created_at']
    list_filter = ['created_at']
    search_fields = ['location_name', 'temperature_celsius', 'temperature_fahrenheit', 'condition_text']
