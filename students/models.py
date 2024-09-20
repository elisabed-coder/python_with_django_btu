from django.db import models
from datetime import date
from django.core.exceptions import ValidationError



class Course(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    age = models.IntegerField(editable=False)
    courses = models.ManyToManyField('Course')

    def __str__(self):
        return self.name

    # make list of courses
    def list_of_courses(self):
        return [course.name for course in self.courses.all()]

    def calculate_age(self):
        today = date.today()
        return  today.year - self.date_of_birth.year - (
                (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day))

    # calculate age with date of birth
    def save(self, *args, **kwargs):
        self.age = self.calculate_age()
        super().save(*args, **kwargs)

    def clean(self):
        calculated_age = self.calculate_age()
        if calculated_age < 18:
            raise ValidationError('Age must be at least 18.')
    class Meta:
        ordering = ["name", "age"]


