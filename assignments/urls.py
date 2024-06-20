# assignment/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.about_us, name='about_us'),
    # Add other URLs as needed for your project
]
