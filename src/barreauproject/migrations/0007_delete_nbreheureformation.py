# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-01-26 14:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('barreauproject', '0006_nbreheureformation'),
    ]

    operations = [
        migrations.DeleteModel(
            name='NbreHeureFormation',
        ),
    ]