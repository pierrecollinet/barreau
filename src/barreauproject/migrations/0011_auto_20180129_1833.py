# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-01-29 18:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barreauproject', '0010_auto_20180129_1832'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dateideb',
            options={'ordering': ['date']},
        ),
        migrations.AddField(
            model_name='dateideb',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
