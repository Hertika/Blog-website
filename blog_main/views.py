# Assuming this is your views.py in the blogs app

from django.shortcuts import get_object_or_404, redirect, render
from blog_main.forms import RegistrationForm
from blogs.models import Blog, Category  # Assuming Blog model is defined in blogs/models.py
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth 

def home(request):
    
    featured_posts = Blog.objects.filter(is_featured=True, status='Published').order_by('updated_at')
    posts = Blog.objects.filter(is_featured=False, status='Published')

    # Define your GitHub URL
    github_url = "https://github.com/Hertika"
    linkedin_url ="https://www.linkedin.com/in/hertikabatra/?originalSubdomain=in"

    context = {
        'featured_posts': featured_posts,
        'posts': posts,
        'github_url': github_url, # Add GitHub URL to context
        'linkedin_url':linkedin_url,
    }

    return render(request, 'home.html', context)


def home_view(request):
    blogs = Blog.objects.all()
    categories = Category.objects.all()
    context = {
        'blogs': blogs,
        'categories': categories,
    }
    return render(request, 'home.html', context)

def blog_detail(request, pk):
    post = get_object_or_404(Blog, pk=pk)
    context = {
        'post': post,
    }
    return render(request, 'home.html', context)


def register(request):
    if request.method == 'POST':
        
       form = RegistrationForm(request.POST)
       if form.is_valid():
           form.save()
           return redirect('register')
    else:
        form = RegistrationForm()
    context={
        'form':form,
    }
    return render(request,'register.html',context)


def login(request):
    if request.method == 'POST':
        form=AuthenticationForm(request,request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            
            user=auth.authenticate(username=username,password=password)
            if user is not None:
                auth.login(request,user)
            return redirect('dashboard')
    form = AuthenticationForm()
    context={
        'form':form,
    }
    return render(request,'login.html',context)

def logout(request):
    auth.logout(request)
    return redirect('home')