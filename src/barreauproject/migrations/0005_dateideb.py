# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-01-26 09:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barreauproject', '0004_auto_20180123_1629'),
    ]

    operations = [
        migrations.CreateModel(
            name='DateIDEB',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=200)),
                ('description', models.TextField()),
            ],
        ),
    ]