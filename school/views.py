from django.shortcuts import render
from django.shortcuts import redirect

from school.models import Class,Student
from school.forms import ClassForm,StudentForm


def home(request):
	class_name = Class.objects.all()
	student_name = Student.objects.all()
	return render(request,'home.html', {'class_name': class_name , 'student_name':student_name})



def newClass(request):
	if request.method == 'POST':
	
		form = ClassForm(request.POST)
		if form.is_valid():
			instance = form.save() 
			instance.save() 		      
            						                
	else:  
		form = ClassForm()

	return render(request,'newClass.html', {'form': form})

def detailClass(request):
	passed_id = request.GET["id"]
	# class_detail = Class.objects.get(pk = passed_id)
	class_detail = Class.objects.get (pk = passed_id)
	student_detail = Student.objects.filter (class_name = class_detail)
	return render(request,'classDetail.html', {
		'class_detail': class_detail,
		'student_detail':student_detail
	})
	# return render(request,'classDetail.html', {'class_detail': class_detail})



def editClass(request):
	passed_id =request.GET["id"]

	if request.method == 'POST':
		form = ClassForm(request.POST)

		if form.is_valid():
			classname = Class.objects.get(pk = passed_id)
			form = ClassForm(request.POST,instance =classname)
			form.save()
			return redirect('/detail_class/?id=' + passed_id )			

	else:

		classname = Class.objects.get(pk = passed_id)
		form = ClassForm(instance =classname)


	return render(request,'editClass.html', {'form': form})


def deleteClass(request):
	passed_id =request.GET["id"]

	class_name = Class.objects.get(pk = passed_id)
		
	class_name.delete()
	return redirect('/' )
			


def confirmDelete(request):
	passed_id = request.GET["id"]
	class_detail = Class.objects.get(pk = passed_id)
	
	return render(request,'deleteClass.html',{'class_detail':class_detail})

def newStudent(request):
	if request.method == 'POST':
	
		form = StudentForm(request.POST)
		if form.is_valid():
			instance = form.save() 
			instance.save() 		      
            						                
	else:  
		form = StudentForm()

	return render(request,'newStudent.html',{'form':form})


# def stud(request):
# 	a=1
# 	student = Student.objects.get ( id = a)
    
# 	return render(request,'test.html', {'student': student , 'a':a})


def detailStudent(request):
	passed_id = request.GET["id"]
	student_detail = Student.objects.get(pk = passed_id)
	return render(request,'studentDetail.html', {'student_detail': student_detail})


def editStudent(request):
	passed_id =request.GET["id"]

	if request.method == 'POST':
		form = StudentForm(request.POST)

		if form.is_valid():
			studentname = Student.objects.get(pk = passed_id)
			form = StudentForm(request.POST,instance =studentname)
			form.save()
			return redirect('/detail_student/?id=' + passed_id )			

	else:

		studentname = Student.objects.get(pk = passed_id)
		form = StudentForm(instance =studentname)


	return render(request,'editStudent.html', {'form': form})


def confirmStudentDelete(request):
	passed_id = request.GET["id"]
	student_detail = Student.objects.get(pk = passed_id)
	
	return render(request,'deleteStudent.html',{'student_detail':student_detail})

def deleteStudent(request):
	passed_id =request.GET["id"]

	student_name = Student.objects.get(pk = passed_id)
		
	student_name.delete()
	return redirect('/' )