# src/app/page/views.py

# Django modules
from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.

def home_view(request):
    return render(request, "page/index.html")
