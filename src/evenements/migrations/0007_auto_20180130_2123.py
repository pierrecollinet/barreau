# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-01-30 21:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evenements', '0006_auto_20180130_2016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='formateur',
            field=models.ManyToManyField(blank=True, null=True, to='evenements.Formateur'),
        ),
    ]
