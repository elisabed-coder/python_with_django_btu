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