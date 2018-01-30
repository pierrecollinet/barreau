# -*- coding: utf-8 -*-

from django.contrib import admin
from django.core.mail import send_mail

from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context

from .models import Formateur, Event

from cms.admin.placeholderadmin import FrontendEditableAdminMixin

# Modeles liés aux formations

class EventAdmin(FrontendEditableAdminMixin, admin.ModelAdmin):
    frontend_editable_fields = ("titre", "short_description", "long_description", "formateur", "type", "image", "date","date_debut", "date_fin", "active")
    filter_horizontal = ("formateur",)

class FormateurAdmin(FrontendEditableAdminMixin, admin.ModelAdmin):
    frontend_editable_fields = ("full_name", "short_description", "photo")

admin.site.register(Formateur, FormateurAdmin)
admin.site.register(Event,     EventAdmin)
