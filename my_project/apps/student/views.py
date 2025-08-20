from django.shortcuts import render, redirect
from django.http import HttpResponse
from apps.student.models import Student
from apps.student.forms import StudentForm
# Create your views here.
# students/views.py


def student(request):
    '''it converts from text to html format and returns as a response'''
    return HttpResponse("Hello, This is student related content!")

def list_students(request):
    students = Student.objects.all() # ORM (select * from student) 
    return render(request, 'list_students.html', {'students': students})

def add_student(request):
    '''if user submits the form by clicking the subit button, the the request is 'POST' '''
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_students')
        else:
            return redirect('students')
    else:
        form = StudentForm()
    return render(request, 'add_student.html', {'form': form})
    '''if user request to add a student , so it is GET method. then this function returns and renders the empty form.'''

def edit_student(request, id):
    student = Student.objects.get(id=id)
    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('list_students')
    else:
        form = StudentForm(instance=student)
    return render(request, 'edit_student.html', {'form': form})

def delete_student(request, id):
    student = Student.objects.get(id=id)
    if request.method == "POST":
        student.delete()
        return redirect('list_students')
    return render(request, 'delete_student.html', {'student': student})


