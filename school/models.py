from django.db import models

# Create your models here.
class Class(models.Model):
	"""Class data"""
	name = models.CharField(max_length = 100)

	def __str__(self):
		return self.name
	
class Student(models.Model):
	"""Student data"""
	class_name = models.ForeignKey(Class)
	student_name = models.CharField(max_length = 100)
	address = models.CharField(max_length = 100)

	def __str__(self):
		return u'%s' % (self.student_name,)