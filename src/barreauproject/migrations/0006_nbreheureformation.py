# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-01-26 14:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barreauproject', '0005_dateideb'),
    ]

    operations = [
        migrations.CreateModel(
            name='NbreHeureFormation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_heures', models.CharField(max_length=200)),
            ],
        ),
    ]