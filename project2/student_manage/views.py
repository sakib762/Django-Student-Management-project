from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Student
from .forms import StudentForm
from django.db.models import Q

def student_list(request):
    students = Student.objects.all()
    return render(request, "student_list/student_list.html" , {'student': students})

# Create your views here.
def update_student(request , id):
    if request.method == 'POST':
        student = Student.objects.get(pk = id)
        fm = StudentForm(request.POST, instance=student)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect("/")
    else:   
        student = Student.objects.get(pk = id)
        fm= StudentForm(instance=student)
    return render(request, "student_list/update_student.html", {'form':fm})

def delete_student(request , id):
    if request.method == 'POST':
        student = Student.objects.get(pk = id)
        student.delete()
        return HttpResponseRedirect("/")
    

def add_student(request):
    if request.method == 'POST':
        fm = StudentForm(request.POST)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect("/")
    else:
        fm = StudentForm()
    return render(request, "student_list/add.html", {'form':fm})
def search(request):
    if request.method == "POST":
          search1 = request.POST.get('search')
          stu = Student.objects.all()
          std = None
          if search1:
              std = Student.objects.filter(
                  Q(fname__icontains=search1)|
                  Q(lname__icontains=search1)|
                  Q(email__icontains=search1)|
                  Q(city__icontains=search1))
          return render (request, "student_list/student_list.html", {'student':std})
    
    else:
        return HttpResponse("404 - Not Found")

    