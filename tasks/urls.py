from django.urls import path
from .views import IndexViews , TaskViews

app_name = 'tasks'

urlpatterns = [
   # path('' , IndexViews.as_view() , name= 'index' ),
    path('' , TaskViews.as_view() , name= 'index' ),

]