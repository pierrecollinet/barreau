from django.conf.urls import include, url
from django.contrib import admin

from barreauproject.views import welcome, a_propos, contact , faq, formations, partenaires

urlpatterns = [
    url('^$', welcome),
    url('^welcome$', welcome, name="welcome"),
    url('^a-propos$', a_propos, name="a-propos"),
    url('^contact$', contact, name="contact"),
    url('^faq$', faq, name="faq"),
    url('^formations$', formations, name="formations"),
    url('^partenaires$', partenaires, name="partenaires"),


    url(r'^admin/', include(admin.site.urls)),

]

