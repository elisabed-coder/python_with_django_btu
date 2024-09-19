from django.shortcuts import render
from django.http import HttpResponse

from bookShop.models import Books


# Create your views here.

def bookshop(request):
    html=""
    books = Books.objects.all().select_related('author')
    for book in books:
        html += f"""
        <h3>{book.title}</h3>
        <p>{book.author.name}</p>
        <p>Tags: {book.content}</p>
        <p>Author's Book Count: {book.author.book_count()}</p>
        """

    return HttpResponse(html, status=200)
