from django.contrib import admin

from blogs.models import Blog, Tag, Comment

# Register your models here.

# admin.site.register(Blog)
# admin.site.register(Tag)
# admin.site.register(Comment)

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "date_published")
    list_filter = ("title",)
    list_per_page = 2
    fieldsets = [
     ('main', {
         'fields': [
             'title', 'author'
         ],
     }),
        ('additional', {
            'fields': ['content', 'date_published']
        })
 ]

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    date_hierarchy = "date"
    list_select_related = ("blog",)

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass