from django.contrib import admin

from bookshop.models import Books, Authors

# Register your models here.

admin.site.register(Books)
admin.site.register(Authors)