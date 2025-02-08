from django.shortcuts import render , redirect
from django.views.generic import TemplateView , ListView , CreateView , DeleteView , UpdateView
from .models import Task
from django.urls import reverse_lazy 

class TaskViews(ListView):
    context_object_name = 'tasks'
    template_name = 'index.html'
    def get_queryset(self):
        tasks = Task.objects.all()
        return tasks
    
class CreateTaskViews(CreateView):
    model = Task
    fields = ['title']
    success_url = reverse_lazy('tasks:index')
    template_name = 'index.html'
    
    def form_valid(self, form):
        form.instance.creator =self.request.user
        return super().form_valid(form)
class DeleteTaskViews(DeleteView):
    model = Task
    success_url = reverse_lazy('tasks:index')
    
 
   

class UpdateTaskViews(UpdateView):
    model =Task
    fields =['status']
    template_name ='index.html'
    success_url = reverse_lazy('tasks:index')

    
    
    

