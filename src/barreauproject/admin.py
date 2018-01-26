# -*- coding: utf-8 -*-

from django.contrib import admin
from django.core.mail import send_mail

from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context

from .models import PhotoGallerie, Faq, Membre, Partenaire, NewsletterEmail, Categorie, DateIDEB


admin.site.register(PhotoGallerie)
admin.site.register(Faq)
admin.site.register(Membre)
admin.site.register(Partenaire)
admin.site.register(NewsletterEmail)
admin.site.register(Categorie)
admin.site.register(DateIDEB)
