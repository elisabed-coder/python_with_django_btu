from django.shortcuts import render

from blogs.models import Blog


# Create your views here.

def blog_list(request):
    return render(request, 'blogs/blogs_list.html')