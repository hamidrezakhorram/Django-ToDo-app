from django.shortcuts import render
from django.contrib.auth.views import LoginView , LogoutView 
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm



User = get_user_model()
class UserLoginViews(LoginView):
    template_name = 'accounts/index.html'
    success_url =reverse_lazy('tasks:index')
    def get_success_url(self):
        return self.success_url
   
     
class UserLogoutViews(LogoutView):
    next_page = 'tasks:index'

class UserCreateViews(CreateView):       
    form_class = UserCreationForm
    template_name = 'accounts/index.html'
    success_url = reverse_lazy('tasks:index')
