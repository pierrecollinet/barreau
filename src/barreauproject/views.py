# -*- coding: utf-8 -*-
from django.http import HttpResponse, HttpResponseRedirect, Http404, JsonResponse
from django.shortcuts import render
from django.template.loader import get_template
from django.template import Context

from django.core.mail import send_mail, EmailMultiAlternatives
from django.contrib.auth.decorators import login_required

from django.contrib.sitemaps import Sitemap

import json
from datetime import datetime, timedelta

from .forms import ContactForm, NewsletterForm
from .models import Membre, PhotoGallerie, Categorie, Faq

from evenements.models import Event
def welcome(request):
    form = ContactForm(request.POST or None)
    c = {'form': form}
    if form.is_valid():
      print('Send email')
    return render(request, 'welcome.html', c)

def a_propos(request):
  categories = Categorie.objects.all()
  membres = Membre.objects.all()
  photos = PhotoGallerie.objects.all()
  c = {'membres':membres, 'categories':categories, 'photos':photos}
  return render(request, 'a-propos.html', c)

def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
      print('Send email')
    c = {'form': form}
    return render(request, 'contact.html', c)

def faq(request):
  faqs = Faq.objects.all()
  nbre_faqs = len(faqs)
  n_demi = int(nbre_faqs/2)
  c = {'faqs':faqs, 'n_demi':n_demi}
  return render(request, 'faq.html', c)

def partenaires(request):
    return render(request, 'partenaires.html')
