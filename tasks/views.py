from django.shortcuts import render
from django.views.generic import TemplateView , ListView
from .models import Task

class IndexViews(TemplateView):
    template_name ='index.html'
    
    def get_context_data(self, **kwargs):
        
        return super().get_context_data(**kwargs)

class TaskViews(ListView):
    context_object_name = 'tasks'
    template_name = 'index.html'
    def get_queryset(self):
        tasks = Task.objects.all()
        return tasks