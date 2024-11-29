from django.db import models

# Create your models here.
class Teacher(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"{self.surname}, {self.name}"


class Subject(models.Model):
    subject_name = models.CharField(max_length=50)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.subject_name}"
    
class Class(models.Model):
    clas_name = models.CharField(max_length=50, verbose_name="Назва класу")
    grade = models.PositiveIntegerField(verbose_name="Клас")

    def __str__(self) -> str:
        return f"{self.clas_name}, {self.grade}"
    
class Student(models.Model):
    name_sure = models.CharField(max_length=70, verbose_name="Ім'я студента, та прізвище")
    age = models.PositiveIntegerField(verbose_name="Вік студента")
    student_class = models.ForeignKey(Class, on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return f"{self.name_sure}, {self.age}, {self.student_class}"
