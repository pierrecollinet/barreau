from django.conf.urls import include, url
from django.contrib import admin
from .views import all_events, detail_event

urlpatterns = [
    url('^$', all_events, name="list-events"),
    url('^liste$', all_events, name="list-events"),
    url('^(?P<pk>\d+)$', detail_event, name="detail-event"),

]
