# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-28 16:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0003_auto_20181028_1608'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='author',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
