# Generated by Django 5.0.4 on 2024-04-14 12:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0014_userlocation'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='weather.user'),
        ),
        migrations.DeleteModel(
            name='UserLocation',
        ),
    ]