# -*- coding: utf-8 -*-
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404, JsonResponse
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from django.template.loader import get_template
from django.template import Context

from django.core.mail import send_mail, EmailMultiAlternatives
from django.contrib.auth.decorators import login_required

from django.contrib.sitemaps import Sitemap
from django.conf import settings
import json
import json as simplejson

from datetime import datetime, timedelta
from django.contrib.auth.decorators import user_passes_test

@user_passes_test(lambda u: u.is_superuser)
def dashboard(request):
  c = {}
  return render(request, 'fondateurs/tableau-de-bord.html', c)
