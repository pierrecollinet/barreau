from django.conf.urls import include, url
from django.contrib import admin

from barreauproject.views import welcome, a_propos, contact , faq, partenaires

urlpatterns = [
    url('^$', welcome),
    url('^accueil$', welcome, name="welcome"),
    url('^a-propos$', a_propos, name="a-propos"),
    url('^contact$', contact, name="contact"),
    url('^faq$', faq, name="faq"),
#    url('^partenaires$', partenaires, name="partenaires"),
    url('^partenaires$', partenaires, name="partenaires"),
    url('^chercher$', faq, name="chercher"),

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
from django.conf.urls.static import static
print('-------------------')
print(settings.MEDIA_ROOT)
print(settings.MEDIA_URL)
if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]
