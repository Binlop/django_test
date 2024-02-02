from django import forms
from .models import Student

class OrangeForm(forms.Form):
    """
    Класс задает общие поля для форм всех 3 типов эмбрионов
    """
    name = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'аапельсин'
        })
    )
    student = forms.ModelChoiceField(
        queryset=Student.objects.all(),
        label='Выберите лабораторию',
        widget=forms.Select(attrs={
            'class': 'form-control',
            'placeholder': "Лаборатория",
        }))
    
    class Meta:        
        fields = ['name', 'student']

class AppleForm(forms.Form):
    """
    Класс задает общие поля для форм всех 3 типов эмбрионов
    """
    name = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'ФИО яблока'
        })
    )
    student = forms.ModelChoiceField(
        queryset=Student.objects.all(),
        label='Выберите лабораторию',
        widget=forms.Select(attrs={
            'class': 'form-control',
            'placeholder': "Лаборатория",
        }))
    
    class Meta:        
        fields = ['name', 'student']

class BananaForm(forms.Form):
    """
    Класс задает общие поля для форм всех 3 типов эмбрионов
    """
    name = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'ФИО банана'
        })
    )
    student = forms.ModelChoiceField(
        queryset=Student.objects.all(),
        label='Выберите лабораторию',
        widget=forms.Select(attrs={
            'class': 'form-control',
            'placeholder': "Лаборатория",
        }))
    
    class Meta:        
        fields = ['name', 'student']

class StudentForm(forms.ModelForm):
    name = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'ФИО студента'
        })
    )
    age = forms.IntegerField(
        label='',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Возраст'
        })
    )
    school = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Школа'
        })
    )
    
    class Meta:
        model = Student     
        fields = ['name', 'age', 'school']