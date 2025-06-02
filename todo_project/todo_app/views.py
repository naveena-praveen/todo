from inspect import ismethod
from .models import task
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import todoform

def home(request):
    obj1=task.objects.all()
    return render(request,'home.html',{'obj1':obj1})

def delete(request,id):
    obj=task.objects.get(id=id)
    obj.delete()
    return redirect('home')

def create(request):
    if request.method=='POST':
        title=request.POST.get('title')
        description=request.POST.get('description')
        date=request.POST.get('date')
        priority=request.POST.get('priority')
        result=task(title=title,description=description,date=date,priority=priority)
        result.save()
        return redirect('home')
    return render(request,'add.html')

def update(request,id):
    obj=task.objects.get(id=id)
    form=todoform(request.POST or None ,instance=obj)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request,'update.html',{'task':obj,'form':form})