import os
import sys

sys.path.append('/var/www/')
sys.path.append('/var/www/kvintang')


os.environ['DJANGO_SETTINGS_MODULE'] = 'kvintang.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()


