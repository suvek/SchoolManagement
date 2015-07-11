from django.db import models

# Create your models here.
class Class(models.Model):
	"""Class data"""
	name = models.CharField(max_length = 100)
	
class Student(models.Model):
	"""Student data"""
	class_name = models.ForeignKey(Class)
	student_name = models.CharField(max_length = 100)
	address = models.CharField(max_length = 100)