from .models import Class, Teacher, Subject, Student
from django.forms import ModelForm, TextInput, NumberInput, Select

class ClassForm(ModelForm):
    class Meta:
        model = Class
        fields = ["clas_name", "grade"]
        widgets = {
            "clas_name": TextInput(attrs={
                'class': 'form-control',
                'placeholder':'Введіть назву класу'
            }),
            "grade": NumberInput(attrs={
                'class': 'form-control'
            })
            }
        
class TeacherForm(ModelForm):
    class Meta:
        model = Teacher
        fields = ["name", "surname"]
        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder':'Введіть ім’я викладача'
            }),
            "surname": TextInput(attrs={
                'class': 'form-control',
                'placeholder':'Введіть прізвище викладача'
            })
            }
        
class SubjectForm(ModelForm):
    class Meta:
        model = Subject
        fields = ["subject_name", "teacher"]
        widgets = {
            "subject_name": TextInput(attrs={
                'class': 'form-control',
                'placeholder':'Введіть назву предмета'
            }),
            "teacher": Select(attrs={
                'class': 'form-control',
                'placeholder':'Викладач'
            })
            }
        
class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ["name_sure", "age", "student_class"]
        widgets = {
            "name_sure": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введіть ім’я студента та прізвище'
            }),
            "age": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Вік студента'
            }),
            "student_class": Select(attrs={
                'class': 'form-control',
            })
            }