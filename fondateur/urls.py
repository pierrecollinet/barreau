from django.conf.urls import include, url
from django.contrib import admin
from .views import dashboard

urlpatterns = [
    url('^$', dashboard, name="tableau-de-bord"),
    url('^tableau-de-bord$', dashboard, name="tableau-de-bord"),
]
