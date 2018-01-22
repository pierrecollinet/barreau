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

def welcome(request):
    return render(request, 'welcome.html')

def a_propos(request):
    return render(request, 'a-propos.html')

def contact(request):
    return render(request, 'contact.html')

def faq(request):
    return render(request, 'faq.html')

def formations(request):
    return render(request, 'formations.html')

def partenaires(request):
    return render(request, 'partenaires.html')
