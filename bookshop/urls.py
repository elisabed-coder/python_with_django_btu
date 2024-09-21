from django.urls import path

from bookshop.views import bookshop

urlpatterns = [
    path('', bookshop, name='bookshop'),
]