from django.urls import path
from . import views
from django.views import *
app_name='myapp'
urlpatterns=[
     path('',views.login,name='login'),
     path('index',views.index,name='index'),
     path('register',views.register,name='register'),
     path('home',views.interface,name='interface')
]