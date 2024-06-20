# assignment/views.py

from django.shortcuts import render
from .models import About

def about_us(request):
    about_objects = About.objects.all()
    return render(request, 'about.html', {'about_objects': about_objects})
