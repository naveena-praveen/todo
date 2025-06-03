from inspect import ismethod
from .models import task
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import todoform
from django.views.generic import ListView , DeleteView
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy

class TaskListView(ListView):
    model=task
    template_name='home.html'
    context_object_name='obj1'

class TaskUpdateView(UpdateView):
    model=task
    template_name='update.html'
    context_object_name='task'
    form_class= todoform
    def get_success_url(self):
        return reverse_lazy('update',kwargs={'pk':self.object.id})
    
    
def Delete(request,id):
    obj=task.objects.get(id=id)
    obj.delete()
    return redirect('home')

def Create(request):
    if request.method=='POST':
        title=request.POST.get('title')
        description=request.POST.get('description')
        date=request.POST.get('date')
        priority=request.POST.get('priority')
        result=task(title=title,description=description,date=date,priority=priority)
        result.save()
        return redirect('home')
    return render(request,'add.html')

