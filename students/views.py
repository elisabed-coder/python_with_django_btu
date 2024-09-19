from django.urls import reverse

from django.shortcuts import render
from django.utils.termcolors import RESET
# Create your views here.
from students.models import Student
from django.http import HttpResponse


def students_portal(request):
    html = ""
    students = Student.objects.all().prefetch_related('courses')
    for student in students:
        student.details_url = reverse('students:courses', kwargs={'student_pk': student.pk})
        html += f"""
          <h3>Student Name:{student.name}</h3>
          <p>Date of Birth:{student.date_of_birth}</p>
          <p>Age:{student.age}</p>
          <a href="{ student.details_url}">View Details</a>
          <hr>
        """
    return HttpResponse(html, status=200)



def courses(request, student_pk):
    try:
        student = Student.objects.get(pk=student_pk)
    except Student.DoesNotExist:
        return HttpResponse("Not Found",status=404)

    html =  f"""
      <h3>{student.name}</h3>
      <p>Date of Birth:{student.date_of_birth}</p>
      <p>Age:{student.age}</p>
      <h4>Courses: {", ".join(student.list_of_courses())}</h4>
    """

    return HttpResponse(html, status=200)


















