# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-01-30 20:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evenements', '0003_auto_20180129_0956'),
    ]

    operations = [
        migrations.AddField(
            model_name='formateur',
            name='statut',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
