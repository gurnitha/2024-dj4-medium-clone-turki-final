# src/app/page/views.py

# Django modules
from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.

def hallo_world_view(request):
    now = datetime.datetime.now()
    html = "<html><body><h1>Hello World!</h1> It is now %s.</body></html>" % now
    return HttpResponse(html)

