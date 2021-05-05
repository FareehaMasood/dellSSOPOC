#!/usr/bin/env python3

import django
import os
import sys
sys.path.append('/home/ubuntu/saml/ssopoc')
sys.path.append('/home/ubuntu/saml/ssopoc/dellSSO')

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings_server'
django.setup()

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()