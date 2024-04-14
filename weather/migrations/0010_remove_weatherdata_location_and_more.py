# Generated by Django 5.0.4 on 2024-04-14 08:08
from __future__ import annotations

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0009_weatherdata_location'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='weatherdata',
            name='location',
        ),
        migrations.AddField(
            model_name='weatherdata',
            name='location',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
