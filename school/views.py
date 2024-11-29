from django.shortcuts import render, redirect
from .models import Subject, Teacher, Student, Class
from .forms import ClassForm, TeacherForm, SubjectForm, StudentForm

# Create your views here.
def index(request):
    return render(request, 'school/index.html')

def subject(request):
    subjects = Subject.objects.all()
    return render(request, 'school/subject.html', {'subject':subjects})

def teacher(request):
    teachers = Teacher.objects.all()
    return render(request, 'school/teachers.html', {'teacher': teachers})

def student(request):
    students = Student.objects.all()
    return render(request, 'school/students.html', {'student': students})

def clas(request):
    classes = Class.objects.all()
    return render(request, 'school/classes.html', {'clas': classes})

def create(request):
    if request.method == 'POST':
        form = ClassForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('classes')
        else:
            return redirect('home')

    form = ClassForm()
    context = {'form': form}
    return render(request, 'school/create.html', context)

def create_teach(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('teachers')
        else:
            return redirect('home')

    form = TeacherForm()
    context = {'form': form}
    return render(request, 'school/create_teacher.html', context)

def create_subject(request):
    if request.method == 'POST':
        form = SubjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('subjects')
        else:
            return redirect('home')

    form = SubjectForm()
    context = {'form': form}
    return render(request, 'school/create_subject.html', context)

def create_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('students')
        else:
            return redirect('home')

    form = StudentForm()
    context = {'form': form}
    return render(request, 'school/create_student.html', context)