from django.conf.urls import include, url
from django.contrib import admin

from barreauproject.views import welcome

urlpatterns = [
    url('^$', welcome),
    url('^welcome$', welcome, name="welcome"),
    url(r'^admin/', include(admin.site.urls)),

]
