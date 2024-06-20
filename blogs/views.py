from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render

from .models import Blog,Category,Comment
from django.db.models import Q

def posts_by_category(request , category_id):
    #fetch the post that belong to the category with the id category_id
    posts = Blog.objects.filter(status='Published',category=category_id)
    # try except when we want to do some custom acation if the category doesnot exist
    # try:
    #  category=Category.objects.get(pk=category_id)
    # except:
    #     # redirect the user to homepage
    #     return redirect('home')
      
    #  use get object or 404 when we want to show 404 page if the category doesnot exist
    category = get_object_or_404(Category,pk=category_id)
    context={
        'posts':posts,
        'category':category,
    }
    return render(request,'posts_by_category.html',context)

# blogs/views.py

def home_view(request):
    blogs = Blog.objects.all()
    categories = Category.objects.all()
    context = {
        'blogs': blogs,
        'categories': categories,
    }
    return render(request, 'home.html', context)

def blogs(request, slug):
    single_blog = get_object_or_404(Blog, slug=slug, status='Published')
    if request.method == 'POST':
        comment=Comment()
        comment.user=request.user
        comment.blog=single_blog
        comment.comment = request.POST['comment']
        comment.save()
        return HttpResponseRedirect(request.path_info)
    
    #comments
    comments=Comment.objects.filter(blog=single_blog)
    comment_count = comments.count()
    context = {
        'single_blog': single_blog,
        'comments':comments,
        'comment_count':comment_count,
    }
    return render(request, 'blogs.html', context)


def search(request):
    keyword=request.GET.get('keyword')
    blogs=Blog.objects.filter(Q(title__icontains=keyword) | Q(short_description__icontains=keyword) | Q(blog_body__icontains=keyword),status='Published') 
    print(blogs)
    context={
        'blogs':blogs,
        'keyword':keyword,
    }
    return render(request,'search.html',context)
