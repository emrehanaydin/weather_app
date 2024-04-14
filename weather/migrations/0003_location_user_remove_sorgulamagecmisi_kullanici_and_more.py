# Generated by Django 5.0.4 on 2024-04-09 09:56
from __future__ import annotations

import django.db.models.deletion
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0002_kullanici_lokasyon_sorgulamagecmisi_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255, unique=True)),
                ('password', models.CharField(max_length=255)),
                ('authority', models.CharField(choices=[
                 ('admin', 'Admin'), ('standard', 'Standard')], max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name='sorgulamagecmisi',
            name='kullanici',
        ),
        migrations.RemoveField(
            model_name='sorgulamagecmisi',
            name='lokasyon',
        ),
        migrations.CreateModel(
            name='QueryHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('query_time', models.DateTimeField(auto_now_add=True)),
                ('ip_address', models.CharField(max_length=255)),
                ('result', models.TextField()),
                ('duration', models.IntegerField()),
                ('status', models.CharField(max_length=255)),
                ('location', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='weather.location')),
                ('user', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='weather.user')),
            ],
        ),
        migrations.DeleteModel(
            name='Kullanici',
        ),
        migrations.DeleteModel(
            name='Lokasyon',
        ),
        migrations.DeleteModel(
            name='SorgulamaGecmisi',
        ),
    ]
