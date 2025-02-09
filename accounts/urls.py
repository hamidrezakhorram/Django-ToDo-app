from django.urls import path
from .views import UserLoginViews , UserLogoutViews

app_name = 'accounts'

urlpatterns =[
    path('login/' , UserLoginViews.as_view() , name ='login'),
    path('logout/',UserLogoutViews.as_view() , name='logout'),
]