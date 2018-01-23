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

def welcome(request):
    print('first modif')
    form = ContactForm(request.POST or None)
    c = {'form': form}
    if form.is_valid():
      print('Send email')
    return render(request, 'welcome.html', c)

def a_propos(request):
    return render(request, 'a-propos.html')

def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
      print('Send email')
    c = {'form': form}
    return render(request, 'contact.html', c)

def faq(request):
    return render(request, 'faq.html')

def formations(request):
    form = NewsletterForm(request.POST or None)
    if form.is_valid():
      print('form valide..register this guy')
    c = {'form': form}
    return render(request, 'formations.html', c)

def partenaires(request):
    return render(request, 'partenaires.html')
