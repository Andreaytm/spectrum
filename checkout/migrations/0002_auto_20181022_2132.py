# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-22 21:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='postcode',
            field=models.CharField(max_length=20),
        ),
    ]
