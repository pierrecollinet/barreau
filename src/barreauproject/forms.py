# -*- coding: utf-8 -*-
from django import forms
from django.forms import widgets

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Div,Submit, HTML, ButtonHolder
from crispy_forms.bootstrap import FieldWithButtons, StrictButton
from crispy_forms.layout import MultiWidgetField


from django.forms.extras.widgets import SelectDateWidget
from django.utils.translation import gettext as _
import datetime

from barreauproject.models import NewsletterEmail
class ContactForm(forms.Form):
    nom = forms.CharField(max_length=100)
    email = forms.EmailField()
    sujet = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea(attrs={'rows':4}))

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False
        self.helper.form_class = 'form-horizontal'
        self.helper.layout = Layout(
                                Field('nom', placeholder='NOM & PRENOM'),
                                Field('email', placeholder='ADRESSE EMAIL'),
                                Field('sujet', placeholder='SUJET'),
                                Field('message', placeholder='MESSAGE'),
                                )
        self.helper.add_input(Submit('submit', 'Envoyer', css_class='btn btn-common'))


class NewsletterForm(forms.Form):
    email = forms.EmailField()

    def __init__(self, *args, **kwargs):
        super(NewsletterForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False
        self.helper.form_class = 'form-horizontal'
        self.helper.layout = Layout(
                                FieldWithButtons(
                                  Field('email', placeholder='Adresse Email', css_class="col-xs-6 width100pp"),
                                  StrictButton("GO", type="submit", css_class="btn btn-round col-xs-6", id="mon-bouton"),
                                  css_class="col-xs-12"
                                  ),
                                )
        # self.helper.add_input(ButtonHolder(
        #                           Submit('submit', 'Envoyer', css_class='input-group-btn'))
        #                                 )
    def clean(self):
        cleaned_data=super(NewsletterForm, self).clean()
        email = cleaned_data.get('email')

        if len(NewsletterEmail.objects.filter(email=email)) != 0 :
          raise forms.ValidationError("Il semblerait que vous soyiez déjà inscrit à notre Newsletter")
