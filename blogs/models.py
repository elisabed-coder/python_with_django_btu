from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    date_published = models.DateTimeField
    content = models.TextField
    tags = models.ManyToManyField('Tag')

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
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    author = models.CharField(max_length=100)
    content = models.TextField

    def __str__(self):
        return self.content