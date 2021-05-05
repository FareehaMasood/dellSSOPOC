import datetime

from django.http import HttpResponse
from django.shortcuts import render

import django_saml2_auth.views
from django.views import View

# Create your views here.


class Samlsso(View):

    def get(self, request, *args, **kwargs):
        now = datetime.datetime.now()
        html = "<html><body>SSO update: It is now %s.</body></html>" % now
        print("Get request")
        print(request)
        return HttpResponse(html)

    def post(self, request, *args, **kwargs):

        return None
