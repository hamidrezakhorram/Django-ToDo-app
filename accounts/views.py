from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib import messages

class UserLoginViews(LoginView):
    template_name = 'accounts/index.html'
    success_url =reverse_lazy('tasks:index')
    def get_success_url(self):
        return self.success_url
   
     


