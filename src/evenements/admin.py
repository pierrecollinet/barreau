# -*- coding: utf-8 -*-

from django.contrib import admin
from django.core.mail import send_mail

from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context

from .models import Formateur, Event

# Modeles liés aux formations

admin.site.register(Formateur)
admin.site.register(Event)
