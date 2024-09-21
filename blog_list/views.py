from django.shortcuts import render

from blog_list.models import Article


# Create your views here.

def articles(request):
    articles = Article.objects.all()
    context = {"articles": articles}
    return render(request, 'blogs/blogs_list.html', context=context)

def artice_detail(request, article_id):
    try:
        article = Article.objects.get(pk=article_id)
    except Article.DoesNotExist:
        return  render(request, "not_found_404.html")
    context = {"article": article}
    return render(request, 'blogs/blogs_details.html', context=context)

