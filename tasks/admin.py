from django.contrib import admin
from .models import Task

class TaskCustomAdmin(admin.ModelAdmin):
    model = Task
    list_display = ('title' , 'status' , 'updated_date' , 'created_date')
    list_filter =('status' , 'created_date')
    
    
    
admin.site.register(Task , TaskCustomAdmin)    

