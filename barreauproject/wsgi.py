
"""
WSGI config for blocusassistance project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os

import sys


from django.core.wsgi import get_wsgi_application

reload(sys)
sys.setdefaultencoding("utf-8")



from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "barreauproject.settings")


application = get_wsgi_application()


try:
   # from dj_static import Cling
    from whitenoise.django import DjangoWhiteNoise
    from dj_static import Cling

   # application = Cling(get_wsgi_application())
    application = get_wsgi_application()
    application = DjangoWhiteNoise(application)

except:
    pass

