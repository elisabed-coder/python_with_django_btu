from django.http import HttpResponse
from django.shortcuts import render
from student_managment_system.models import Student

# Create your views here.
def index(request):
    return render(request, 'students/index.html', {
        'students': Student.objects.all(),
    })


def view_student(request, id):
    student = Student.objects.get(pk=id)
    context = {'student': student}
    return render(request, 'students/student_details.html', context)


def add_student(request):
    if request.method == 'POST':
       Student.objects.create(
           student_number = request.POST['student_number'],
           first_name=request.POST['first_name'],
           last_name=request.POST['last_name'],
           email = request.POST['email'],
           field_of_study=request.POST['field_of_study'],
           gpa=request.POST['gpa'],
       )
       return HttpResponse('Student added successfully')
    return render(request, 'students/add_student.html')
