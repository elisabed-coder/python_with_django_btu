from django.urls import path

from bookShop.views import bookshop

urlpatterns = [
    path('', bookshop, name='bookshop'),
]