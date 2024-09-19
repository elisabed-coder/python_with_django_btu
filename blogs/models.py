import datetime
from email.policy import default

from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    date_published = models.DateTimeField(default=datetime.datetime.now)
    content = models.TextField(default="No content available")  # Added default value
    tags = models.ManyToManyField('Tag')

    def get_tag_list(self):
        tags = ", ".join([tag.name for tag in self.tags.all()])
        return tags

    def __str__(self):
        return self.title

# class BlogTag(models.Model):
#     blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
#     tag = models.ForeignKey('Tag', on_delete=models.CASCADE)
#
#     def __str__(self):
#         return f"{self.tag} {self.blog}"
#

class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=100)
    content = models.TextField(default="No content yet")
    date = models.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return self.content