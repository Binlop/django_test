from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField('ФИО', max_length=255)
    age = models.IntegerField('Возраст')
    school = models.CharField('Школа', max_length=255)

    def __str__(self) -> str:
        return self.name

class Teacher(models.Model):
    name = models.CharField('ФИО', max_length=255)
    age = models.IntegerField('Возраст')
    school = models.CharField('Школа', max_length=255)
    count_students = models.IntegerField('КОл-во учеников')
    
    def __str__(self) -> str:
        return self.name
    
class Individ(models.Model):
    mutation_chromosome = models.CharField('Тип мутации', max_length=255)
    number_chromosome = models.IntegerField('Номер хромосомы')
    individ_age = models.IntegerField('Возраст индивида')
    full_name = models.CharField('ФИО', max_length=255)
    count_blood = models.IntegerField('Кровь')
    count_dna = models.IntegerField('ДНК')
    count_chorion = models.IntegerField('Хорион')
    student = models.OneToOneField(Student, on_delete=models.PROTECT, null=True)
    teacher = models.OneToOneField(Teacher, on_delete=models.PROTECT, null=True)


    def __str__(self) -> str:
        return self.full_name