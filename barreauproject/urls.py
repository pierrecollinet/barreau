from django.conf.urls import include, url
from django.contrib import admin

from barreauproject.views import welcome, a_propos, contact , faq, partenaires

urlpatterns = [
    url('^$', welcome),
    url('^welcome$', welcome, name="welcome"),
    url('^a-propos$', a_propos, name="a-propos"),
    url('^contact$', contact, name="contact"),
    url('^faq$', faq, name="faq"),
    url('^partenaires$', partenaires, name="partenaires"),

    # CMS
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('cms.urls')),
    url(r'^admin/', admin.site.urls),

    # other intern app
    url(r'^fondateurs/', include('fondateur.urls')),
    url(r'^evenements/', include('evenements.urls')),
]

from django.views.static import serve
from django.conf import settings
if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]
