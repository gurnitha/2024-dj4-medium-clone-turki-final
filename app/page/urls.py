# src/app/page/urls.py

# Django modules
from django.urls import path

# Locals
from app.page import views 

app_name = "page"

urlpatterns = [
    path("", views.hallo_world_view),
]
