from django.urls import path
from . import views
app_name='myapp'
urlpatterns=[
     path('',views.index),
     path('register',views.register,name='register'),
     path('login',views.login,name='login'),
     path('home',views.interface,name='interface'),
]