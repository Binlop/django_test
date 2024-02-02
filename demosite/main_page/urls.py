from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('form', views.fruit, name='fruit_form'),
    path('filter_students', views.filter_students, name='filter_students'),
    path('create_student', views.create_student, name='create_student'),
    path('student_<int:student_id>', views.single_student, name='single_student'),
]