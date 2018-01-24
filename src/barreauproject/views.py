# -*- coding: utf-8 -*-
from django.http import HttpResponse, HttpResponseRedirect, Http404, JsonResponse
from django.shortcuts import render
from django.template.loader import get_template
from django.template import Context

from django.core.mail import send_mail, EmailMultiAlternatives
from django.contrib.auth.decorators import login_required

from django.contrib.sitemaps import Sitemap
from django.conf import settings
from django.contrib import messages
from django.db.models import Q

import json
from datetime import datetime, timedelta

from .forms import ContactForm, NewsletterForm
from .models import Membre, PhotoGallerie, Categorie, Faq, Partenaire

from evenements.models import Event
def welcome(request):
    form = ContactForm(request.POST or None)
    c = {'form': form}
    if form.is_valid():
      # Get de datas
      nom     = form.cleaned_data['nom']
      email   = form.cleaned_data['email']
      sujet   = form.cleaned_data['sujet']
      message = form.cleaned_data['message']

      # Send email
      plaintext = get_template('../templates/emails/contact-form.txt')
      htmly     = get_template('../templates/emails/contact-form.html')
      subject, from_email = "Formulaire de contact - "+nom , str(email)
      to = settings.EMAILS
      d = {'nom':nom, 'email':email, 'sujet':sujet, 'message':message}
      text_content = plaintext.render(d)
      html_content = htmly.render(d)
      msg = EmailMultiAlternatives(subject, text_content, from_email, to)
      msg.attach_alternative(html_content, "text/html")
      msg.send()
      messages.success(request, "Merci, nous avons bien reçu votre message. Nous vous recontacterons dans les plus brefs délais")
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
      # Get de datas
      nom     = form.cleaned_data['nom']
      email   = form.cleaned_data['email']
      sujet   = form.cleaned_data['sujet']
      message = form.cleaned_data['message']

      # Send email
      plaintext = get_template('../templates/emails/contact-form.txt')
      htmly     = get_template('../templates/emails/contact-form.html')
      subject, from_email = "Formulaire de contact - "+nom , str(email)
      to = settings.EMAILS
      d = {'nom':nom, 'email':email, 'sujet':sujet, 'message':message}
      text_content = plaintext.render(d)
      html_content = htmly.render(d)
      msg = EmailMultiAlternatives(subject, text_content, from_email, to)
      msg.attach_alternative(html_content, "text/html")
      msg.send()
      messages.success(request, "Merci, nous avons bien reçu votre message. Nous vous recontacterons dans les plus brefs délais")
    c = {'form': form}
    return render(request, 'contact.html', c)

def faq(request):
  if request.GET and 'q' in request.GET :
    query = request.GET['q']
    faqs = Faq.objects.filter(Q(question__icontains = query)|Q(reponse__icontains = query))
  else :
    faqs = Faq.objects.all()
  nbre_faqs = len(faqs)
  n_demi = int(nbre_faqs/2) +1
  c = {'faqs':faqs, 'n_demi':n_demi}
  return render(request, 'faq.html', c)

def partenaires(request):
  partenaires = Partenaire.objects.all()
  c = {'partenaires':partenaires}
  return render(request, 'partenaires.html',c )





