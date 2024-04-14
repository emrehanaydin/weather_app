# Generated by Django 5.0.4 on 2024-04-08 15:48
from __future__ import annotations

import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
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
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
            ],
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(
                    max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(
                    blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False,
                 help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.',
                 max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True,
                 max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True,
                 max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True,
                 max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False,
                 help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(
                    default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(
                    default=django.utils.timezone.now, verbose_name='date joined')),
                ('user_type', models.CharField(choices=[('admin', 'Admin'), (
                    'standard', 'Standard')], default='standard', max_length=10, verbose_name='User Type')),
                ('groups', models.ManyToManyField(blank=True, related_name='custom_user_groups',
                 related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.',
                 related_name='custom_user_permissions', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(
                    auto_now_add=True, verbose_name='Timestamp')),
                ('message', models.TextField(verbose_name='Message')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL,
                 to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
        migrations.CreateModel(
            name='MenuPermission',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('requires_admin', models.BooleanField(
                    default=False, verbose_name='Requires Admin')),
                ('menu', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE,
                 related_name='permission', to='weather.menu')),
            ],
        ),
    ]
