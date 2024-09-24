from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from student_managment_system.models import Student
from student_managment_system.forms import  AddStudentForm

# Create your views here.
def index(request):
    return render(request, 'students/index.html', {
        'students': Student.objects.all(),
    })


def view_student(request, id):
    student = get_object_or_404(Student, pk=id)
    return render(request, 'students/student_details.html', {'student': student})


def add_student(request):
    if request.method == "POST":
       form = AddStudentForm(request.POST)
       if form.is_valid():
           form.save()
           return HttpResponse('Student added successfully')
    else:
        form = AddStudentForm()
    return render(request, 'students/add_student.html', {'form': form})


def update_student(request, id):
    student = get_object_or_404(Student, pk=id)
    if request.method == "POST":
        form = AddStudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return HttpResponse('Student updated successfully')
    else:
        form = AddStudentForm(instance=student)
    return render(request, 'students/update.html', {'form': form})


def delete_student(request, id):
    student = get_object_or_404(Student, pk=id)
    if request.method == "POST":
        student.delete()
        return HttpResponse('Student deleted successfully')
    return render(request, 'students/delete_student.html')

