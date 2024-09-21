from django.http import HttpResponse
from django.urls import reverse

from blogs.models import Blog

def blogs_view(request):
    html = ""
    blogs = Blog.objects.all().prefetch_related('tags')
    for blog in blogs:
        blog_details_url = reverse("blog-details", args=(blog.id,))
        html += f"""
        <h3>{blog.title}</h3>
        <p>By {blog.author} on {blog.date_published}</p>
        <p>{blog.content}</p>
        <p>Tags: {blog.get_tag_list()}</p>
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
    comments = ""
    for comment in blog.comments.all():
        comments += f"<p>{comment.author}: {comment.content} <small>{comment.date}</small></p>"
    html = f"""
    <h3>Blog Details</h3>
    <h2>{blog.title}</h2>
    <p>By {blog.author} on {blog.date_published}</p>
    <p>{blog.content}</p>
    <p>{blog.get_tag_list()}</p>
    <hr>
    <h4>Comments</h4>
    {comments}
    """
    return HttpResponse(html, status=200)

