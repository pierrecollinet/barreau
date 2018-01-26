# -*- coding: utf-8 -*-

from django.contrib import admin
from django.core.mail import send_mail

from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context

from .models import PhotoGallerie, Faq, Membre, Partenaire, NewsletterEmail, Categorie, DateIDEB

from cms.admin.placeholderadmin import FrontendEditableAdminMixin


class FaqAdmin(FrontendEditableAdminMixin, admin.ModelAdmin):
    frontend_editable_fields = ("question", "reponse")

admin.site.register(PhotoGallerie)
admin.site.register(Faq, FaqAdmin)
admin.site.register(Membre)
admin.site.register(Partenaire)
admin.site.register(NewsletterEmail)
admin.site.register(Categorie)
admin.site.register(DateIDEB)
