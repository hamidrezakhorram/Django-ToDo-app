from django.urls import path
from .views import UserLoginViews , UserLogoutViews , UserCreateViews

app_name = 'accounts'

urlpatterns =[
    path('login/' , UserLoginViews.as_view() , name ='login'),
    path('logout/',UserLogoutViews.as_view() , name='logout'),
    path('signup/' ,UserCreateViews.as_view() , name='signup'),
]