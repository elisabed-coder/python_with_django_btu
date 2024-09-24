from lib2to3.fixes.fix_input import context

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from student_managment_system.models import Student
from student_managment_system.forms import  AddStudentForm

class StudentListView(ListView):
    model = Student
    context_object_name = 'students'
    template_name = 'students/index.html'

class StudentsDetailsView(DetailView):
    model = Student
    template_name ="students/student_details.html "
    context_object_name = 'student'



class AddStudentView(CreateView):
    model = Student
    form_class = AddStudentForm
    template_name = "students/add_student.html"
    success_url = reverse_lazy('index')


class StudentUpdateView(UpdateView):
    model = Student
    form_class = AddStudentForm
    template_name = "students/update.html"
    success_url = reverse_lazy('index')
    context_object_name = 'student'

class StudentDeleteView(DeleteView):
    model = Student
    success_url = reverse_lazy('index')
    context_object_name = 'student'
    template_name = "students/delete_student.html"

def delete_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == "POST":
        student.delete()
        return HttpResponse('Student deleted successfully')
    return render(request, 'students/delete_student.html')

