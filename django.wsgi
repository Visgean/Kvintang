import os
import sys


path = '/home/visgean'
if path not in sys.path:
    sys.path.append(path)


os.environ['DJANGO_SETTINGS_MODULE'] = 'kvintang.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()


