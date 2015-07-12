from django import forms

from school.models import Class,Student


class ClassForm(forms.ModelForm):
    
    class Meta:
        model = Class
        fields = ['name']

class StudentForm(forms.ModelForm):
    
    class Meta:
        model = Student
        fields = ['class_name','student_name','address']
    

				