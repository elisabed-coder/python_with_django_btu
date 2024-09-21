from django.db import models

# Create your models here.

class Books(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    author = models.ForeignKey('Authors', on_delete=models.CASCADE, related_name='books')
    content = models.TextField()

    def __str__(self):
        return self.title



class Authors(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def book_count(self):
        return self.books.count()
