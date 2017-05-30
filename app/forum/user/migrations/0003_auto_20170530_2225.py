# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-30 22:25
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20161023_1627'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookmark',
            name='timestamp',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='categorytimestamp',
            name='timestamp',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='forumuser',
            name='resetDateTime',
            field=models.DateTimeField(default=datetime.datetime(2012, 12, 31, 23, 0, tzinfo=utc)),
        ),
    ]
