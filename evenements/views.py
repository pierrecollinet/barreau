# -*- coding: utf-8 -*-
from django.http import HttpResponse, HttpResponseRedirect, Http404, JsonResponse
from django.shortcuts import render
from django.template.loader import get_template
from django.template import Context

from django.core.mail import send_mail, EmailMultiAlternatives
from django.contrib.auth.decorators import login_required

from django.contrib.sitemaps import Sitemap
from django.contrib import messages

import json
from datetime import datetime, timedelta

from evenements.models import Event, Formateur
from barreauproject.models import NewsletterEmail

from barreauproject.forms import NewsletterForm

def all_events(request):
    evenements = Event.objects.all()
    nbre_event = len(evenements)
    n_demi = int(nbre_event/2)
    form = NewsletterForm(request.POST or None)
    if form.is_valid():
      email = form.cleaned_data['email']
      newsletter_obj = NewsletterEmail(email=email)
      newsletter_obj.save()
      messages.success(request, "Félicitation, vous entendrez parler de nous prochainement.")
    c = {'form': form, 'evenements':evenements, 'n_demi':n_demi}
    return render(request, 'evenements/liste.html', c)

def detail_event(request, pk):
    event = Event.objects.get(pk=pk)
    formateur = event.formateur.first()
    form = NewsletterForm(request.POST or None)
    if form.is_valid():
      email = form.cleaned_data['email']
      newsletter_obj = NewsletterEmail(email=email)
      newsletter_obj.save()
      messages.success(request, "Félicitation, vous entendrez parler de nous prochainement.")
    c = {'event' : event, 'formateur':formateur, 'form':form}
    return render(request, 'evenements/detail_event.html', c)
