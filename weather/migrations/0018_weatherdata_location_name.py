# Generated by Django 4.2.11 on 2024-04-14 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0017_weatherdata_location_name_weatherdata_update_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='weatherdata',
            name='location_name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
