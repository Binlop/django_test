from django.shortcuts import render, redirect
from .forms import OrangeForm, AppleForm, BananaForm
from .models import Individ, Student, Teacher

# Create your views here.
def index(request):
    students = Student.objects.all()
    selected_fruit = request.GET.get('fruit', '')
    print(request.GET)
    print('что-то')
    data = {
        'title': 'Биобанк',
        'students': students
    }
    return render(request, 'main_page/index.html', data)

def single_student(request, student_id):
    student = Student.objects.get(id=student_id)
    data = {
        'student': student
    }
    return render(request, 'main_page/student.html', data)

def fruit(request):
    selected_fruit = request.GET.get('fruit', '')
    data = {
        'title': 'Биобанк',
    }
    process_doict = {'apple': AppleForm, 'banana': BananaForm, 'orange': OrangeForm}
    if selected_fruit in process_doict:
        data['form'] = process_doict[selected_fruit]
    return render(request, 'main_page/create_object.html', data)

from django.db.models import Q



def filter_students(request):
    a = dict(request.GET)
    print(a)
    filter = Q()
    for key, elem in a.items():
        if elem == ['on']:
            filter &= Q(**{f'{key}__gt':0})

        elif elem != ['']:
            filter &= Q(**{key: elem[0]})
    
    students = Student.objects.all()
    teachers = Teacher.objects.all()
    context = {
        'students': students,
        'teachers': teachers
    }
    print(Individ.objects.filter(filter))
    
    return render(request, 'main_page/list_students.html', context)

from .forms import StudentForm
def create_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    form = StudentForm()
    data = {
        'form': form,
    }
    return render(request, 'main_page/create_object.html', data)

