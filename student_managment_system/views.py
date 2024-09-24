from django.http import HttpResponse
from django.shortcuts import render
from student_managment_system.models import Student
from student_managment_system.forms import  AddStudentForm

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
    if request.method == "POST":
       form = AddStudentForm(request.POST)
       if form.is_valid():
           # data = form.cleaned_data
           # Student.objects.create(
           #     student_number = data['student_number'],
           #     first_name = data['first_name'],
           #     last_name = data['last_name'],
           #     email = data['email'],
           #     field_of_study = data['field_of_study'],
           #     gpa = data['gpa'],
           # )
           form.save()
       return HttpResponse('Student added successfully')
    else:
        form = AddStudentForm()
    return render(request, 'students/add_student.html', {'form': form})
