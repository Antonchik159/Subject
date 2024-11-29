from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('subject', views.subject, name='subjects'),
    path('teacher', views.teacher, name='teachers'),
    path('student', views.student, name='students'),
    path('clas', views.clas, name='classes'),
    path('create', views.create, name='create'),
    path('create_teacher', views.create_teach, name='create_teacher'),
    path('create_subject', views.create_subject, name='create_subject'),
    path('create_student', views.create_student, name='create_student')
]