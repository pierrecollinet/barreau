# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

from django.contrib.auth.signals import user_logged_in
from django.db.models.signals import pre_save, post_save, post_delete

from django.utils.text import slugify

from django.db import transaction

from datetime import timedelta
import datetime


class Formateur(models.Model):
  full_name = models.CharField(max_length=200)
  photo     = models.ImageField(upload_to = 'mes_images/')
  short_description = models.TextField()

  def __str__(self):
    return self.full_name

types = (('formation','Formation'),('conference','Conférence'),('workshop','Workshop'),)
class Event(models.Model):
  type = models.CharField(max_length=100, choices=types, default="formation")
  titre = models.CharField(max_length=200)
  image = models.ImageField(upload_to = 'mes_images/', blank=True, null=True)
  short_description = models.TextField()
  long_description = models.TextField()
  date = models.DateField()
  formateur = models.ManyToManyField(Formateur)
  active = models.BooleanField(default=True)

  def __str__(self):
    return self.titre

