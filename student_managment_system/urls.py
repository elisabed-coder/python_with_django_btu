from django.urls import path
from . import  views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>/', views.view_student, name='view_student'),
    path('add_student/', views.add_student, name='add_student'),
]