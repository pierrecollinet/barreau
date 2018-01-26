# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

from django.contrib.auth.signals import user_logged_in
from django.db.models.signals import pre_save, post_save, post_delete

from django.utils.text import slugify

from django.db import transaction

from datetime import timedelta
import datetime

class Categorie(models.Model):
  categorie = models.CharField(max_length=200)

  def __str__(self):
    return self.categorie

types = (('formation','Formation'),('conference','Conférence'),('workshop','Workshop'),)
class PhotoGallerie(models.Model):
  categorie = models.ForeignKey(Categorie)
  images = models.ImageField(upload_to = 'mes_images/')
  date = models.DateField(blank=True, null=True)
  short_description = models.TextField(blank=True, null=True)

class Faq(models.Model):
  question = models.TextField()
  reponse = models.TextField()

  def __str__(self):
    return self.question[:30]


class Membre(models.Model):
  image = models.ImageField(upload_to = 'mes_images/')
  pays = models.CharField(max_length=200)
  nom = models.CharField(max_length=200)
  url_site_web = models.CharField(max_length=200, default="https://")

  def __str__(self):
    return self.nom

class Partenaire(models.Model):
  nom = models.CharField(max_length=200)
  logo = models.ImageField(upload_to = 'mes_images/')
  pays = models.CharField(max_length=200)
  ville = models.CharField(max_length=200)

  def __str__(self):
    return self.nom

class NewsletterEmail(models.Model):
  email = models.EmailField()

  def __str__(self):
    return self.email

class DateIDEB(models.Model):
  date = models.CharField(max_length=200)
  description = models.TextField()

  def __str__(self):
    return self.description



