from django.urls import path
from .views import IndexViews

app_name = 'tasks'

urlpatterns = [
    path('' , IndexViews.as_view() , name= 'index' ),
]