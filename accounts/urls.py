from django.urls import path
from .views import UserLoginViews

app_name = 'accounts'

urlpatterns =[
    path('login/' , UserLoginViews.as_view() , name ='login'),
]