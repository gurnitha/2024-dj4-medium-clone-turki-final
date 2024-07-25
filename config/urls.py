# src/config/urls.py

# Django modules
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # admin
    path("admin/", admin.site.urls),
    # page
    path("", include("app.page.urls", namespace="page")),
]
