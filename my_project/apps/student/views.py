from django.shortcuts import render, redirect
from django.http import HttpResponse
from apps.student.models import Student
from apps.student.forms import StudentForm
# Create your views here.
# students/views.py


def student(request):
    return HttpResponse("Hello, This is student view!")

def list_students(request):
    students = Student.objects.all()
    return render(request, 'list_students.html', {'students': students})

def add_student(request):
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


