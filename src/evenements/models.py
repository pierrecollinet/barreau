# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

from django.contrib.auth.signals import user_logged_in
from django.db.models.signals import pre_save, post_save, post_delete

from django.utils.text import slugify

from django.db import transaction

from datetime import timedelta
import datetime

from django.core.exceptions import ValidationError

# import locale

# locale.setlocale(locale.LC_TIME,'fr_FR.UTF-8')

class Formateur(models.Model):
  full_name = models.CharField(max_length=200)
  statut = models.CharField(max_length=200, blank=True, null=True)
  photo     = models.ImageField(upload_to = 'mes_images/', blank=True, null=True)
  short_description = models.TextField(blank=True, null=True)

  def __str__(self):
    return self.full_name

types = (('formation','Formation'),('conference','Conférence'),('workshop','Workshop'),)
class Event(models.Model):
  type = models.CharField(max_length=100, choices=types, default="formation")
  titre = models.CharField(max_length=200)
  image = models.ImageField(upload_to = 'mes_images/', blank=True, null=True)
  short_description = models.TextField()
  contenu = models.TextField()
  date = models.DateField(blank=True, null=True)
  date_debut = models.DateField(blank=True, null=True)
  date_fin = models.DateField(blank=True, null=True)
  formateur = models.ManyToManyField(Formateur, blank=True, null=True)
  active = models.BooleanField(default=True)
  infos_pratiques = models.TextField(blank=True, null=True)


  def __str__(self):
    return self.titre

  class Meta:
        ordering = ["date"]

  def clean(self):
      if self.date is not None and self.date_debut is not None :
        raise ValidationError("Si vous spécifiez une date (=ponctuelle), il ne faut pas de date de début (=période). Et vice versa).")
      if self.date is not None and self.date_fin is not None :
        raise ValidationError("Si vous spécifiez une date (=ponctuelle), il ne faut pas de date de fin (=période). Et vice versa).")
      if (self.date_debut is not None and self.date_fin is None) or (self.date_fin is not None and self.date_debut is None) :
        raise ValidationError("Si vous spécifiez une date de début, il faut une date de fin (et vice versa)")
      if (self.date_debut is None and self.date is None  and self.date_fin is None ):
        raise ValidationError("il faut introduire une date ponctuelle OU une date de début et date de fin pour définir une période")

  def is_period(self):
    if self.date is not None :
      return False
    else :
      return True
  # def display_date(self):
  #   if self.date is not None :
  #     return self.date.strftime('%d %B %Y')
  #   elif self.date_debut is not None and self.date_fin is not None :
  #     return "Du " + self.date_debut.strftime('%d %B %Y') + " au " + self.date_fin.strftime('%d %B %Y')





