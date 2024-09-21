from lib2to3.fixes.fix_input import context

from django.shortcuts import render

from blog_list.models import Blog


# Create your views here.

def blog_list(request):
    all_Blogs = Blog.objects.all()
    context = {"blogs": all_Blogs}
    return render(request, 'blogs/blogs_list.html', context=context)