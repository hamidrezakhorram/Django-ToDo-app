from django.urls import path
from .views import  TaskViews , CreateTaskViews , DeleteTaskViews , UpdateTaskViews

app_name = 'tasks'

urlpatterns = [
   # path('' , IndexViews.as_view() , name= 'index' ),
    path('' , TaskViews.as_view() , name= 'index' ),
    path('add/' , CreateTaskViews.as_view() , name='add'), 
    path('<int:pk>/delete' , DeleteTaskViews.as_view(), name='delete'),
    path('<int:pk>/update' ,UpdateTaskViews.as_view(), name='update' ),

]