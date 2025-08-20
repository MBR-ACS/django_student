from django import forms
from apps.student.models import Student

class StudentForm(forms.ModelForm):
    '''django will create a form , no need to create by our own'''
    class Meta:
        model = Student
        fields = ['name', 'email', 'phone', 'city']