from django.urls import path
from .views import  TaskViews , CreateTaskViews

app_name = 'tasks'

urlpatterns = [
   # path('' , IndexViews.as_view() , name= 'index' ),
    path('' , TaskViews.as_view() , name= 'index' ),
    path('add/' , CreateTaskViews.as_view() , name='add'), 

]