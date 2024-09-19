from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse

from blogs.models import Blog

def blogs_view(request):
    html = ""
    for blog in Blog.objects.all():
        blog_details_url = reverse("blog-details", args=(blog.id,))
        tags = ", ".join([tag.name for tag in blog.tags.all()])
        html += f"""
        <h3>{blog.title}</h3>
        <p>By {blog.author} on {blog.date_published}</p>
        <p>{blog.content}</p>
        <p>Tags: {tags}</p>
        <a href="{blog_details_url}">View Details</a>
        <hr>
        """
    # Return the generated HTML as an HttpResponse
    return HttpResponse(html, status=200)

def blog_details_view(request,  blog_id):
    try:
        blog = Blog.objects.get(id=blog_id)
    except Blog.DoesNotExist:
        return HttpResponse("Blog not Found" ,status=404)
    tags = ", ".join([tag.name for tag in blog.tags.all()])
    comments = ""
    for comment in blog.comments.all():
        comments += f"<p>{comment.author}: {comment.content} <small>{comment.date}</small></p>"
    html = f"""
    <h3>Blog Details</h3>
    <h2>{blog.title}</h2>
    <p>By {blog.author} on {blog.date_published}</p>
    <p>{blog.content}</p>
    <p>{tags}</p>
    <hr>
    <h4>Comments</h4>
    {comments}
    """
    return HttpResponse(html, status=200)
