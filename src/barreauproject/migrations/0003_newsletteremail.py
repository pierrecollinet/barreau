# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-01-23 15:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barreauproject', '0002_auto_20180123_1249'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsletterEmail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]