from django.shortcuts import render
from django.shortcuts import redirect

from school.models import Class,Student
from school.forms import ClassForm


def home(request):
	class_name = Class.objects.all()
	return render(request,'home.html', {'class_name': class_name})



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
	class_detail = Class.objects.get(pk = passed_id)
	return render(request,'classDetail.html', {'class_detail': class_detail})



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
	# if request.method == 'POST':
	
	# 	form = ClassForm(request.POST)
	# 	if form.is_valid():
	# 		instance = form.save() 
	# 		instance.save() 		      
            						                
	# else:  
	# 	form = ClassForm()

    form = "under construction"

    return render(request,'newStudent.html', {'form': form})


