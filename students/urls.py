from django.urls import path
from students.views import students_portal, courses

app_name = 'students'

urlpatterns= [
    path('', students_portal, name="students"),
    path('students/<int:student_pk>/courses/', courses, name='courses')

]