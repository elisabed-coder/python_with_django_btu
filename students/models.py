from django.db import models
from datetime import date

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    age = models.IntegerField(editable=False)
    courses = models.ManyToManyField('Course')

    def __str__(self):
        return self.name

    def list_of_courses(self):
        return [course.name for course in self.courses.all()]

    def save(self, *args, **kwargs):
        today = date.today()
        self.age = today.year - self.date_of_birth.year - (
                    (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day))
        super().save(*args, **kwargs)


class Course(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

