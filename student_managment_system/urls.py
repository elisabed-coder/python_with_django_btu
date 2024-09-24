from django.urls import path
from . import  views

urlpatterns = [
    path('', views.StudentListView.as_view(), name='index'),
    path('<int:pk>/', views.StudentsDetailsView.as_view(), name='view_student'),
    path('add_student/', views.AddStudentView.as_view(), name='add_student'),
    path('<int:pk>/update/', views.StudentUpdateView.as_view(), name='update_student'),
    path('<int:pk>/delete/', views.StudentDeleteView.as_view(), name='delete_student'),
]