from __future__ import annotations

from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User as auth_user
from django.db import models


class User(models.Model):
    id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    authority = models.CharField(max_length=255, choices=(
        ('admin', 'Admin'), ('standard', 'Standard')))


class RequestLog(models.Model):
    user = models.ForeignKey(auth_user, on_delete=models.CASCADE, null=True)
    path = models.CharField(max_length=255)
    method = models.CharField(max_length=10)
    ip_address = models.CharField(max_length=50)
    user_agent = models.CharField(max_length=255)
    requested_at = models.DateTimeField(auto_now_add=True)
    request_body = models.TextField(null=True)
    response_body = models.TextField(null=True)
    response_at = models.DateTimeField(null=True)

    def __str__(self):
        return f'{self.method} {self.path}'


class Location(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class WeatherData(models.Model):
    location_name = models.CharField(max_length=100, null=True)
    temperature_celsius = models.FloatField()
    temperature_fahrenheit = models.FloatField()
    condition_text = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f'{self.temperature_celsius}°C, {self.condition_text}'
