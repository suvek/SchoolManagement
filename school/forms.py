from django import forms

from school.models import Class,Student


class ClassForm(forms.ModelForm):
    
    class Meta:
        model = Class
        fields = ['name']

    

				