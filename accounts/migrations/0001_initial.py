# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-12 18:31
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=50)),
                ('address1', models.CharField(max_length=40)),
                ('address2', models.CharField(max_length=40)),
                ('county', models.CharField(max_length=40)),
                ('town_or_city', models.CharField(max_length=40)),
                ('postcode', models.CharField(max_length=20)),
                ('country', models.CharField(max_length=40)),
                ('phone_number', models.CharField(max_length=40)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
