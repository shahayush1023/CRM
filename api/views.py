from django.shortcuts import render,redirect
# Create your views here.
from .models import Student
from .forms import StudentForm

def list(request):
    context = {'studlist': Student.objects.all()}
    return render(request, "stulist.html", context)


def stu_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = StudentForm()
        else:
            stu = Student.objects.get(pk=id)
            form = StudentForm(instance=stu)
        return render(request, "stuform.html", {'form': form})
    else:
        if id == 0:
            form = StudentForm(request.POST)
        else:
            stu = Student.objects.get(pk=id)
            form = StudentForm(request.POST,instance=stu)
        if form.is_valid():
            form.save()
        return redirect('/api/list')


def stu_delete(request,id):
    stu = Student.objects.get(pk=id)
    stu.delete()
    return redirect('/api/list')