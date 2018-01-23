# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-01-23 12:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('formation', 'Formation'), ('conference', 'Conférence'), ('workshop', 'Workshop')], default='formation', max_length=100)),
                ('titre', models.CharField(max_length=200)),
                ('image', models.ImageField(blank=True, null=True, upload_to='mes_images/')),
                ('short_description', models.TextField()),
                ('long_description', models.TextField()),
                ('date', models.DateField()),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Formateur',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=200)),
                ('photo', models.ImageField(upload_to='mes_images/')),
                ('short_description', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='formateur',
            field=models.ManyToManyField(to='evenements.Formateur'),
        ),
    ]
