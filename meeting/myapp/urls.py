from django.urls import path
from . import views
app_name='myapp'
urlpatterns=[
     path('login',views.login,name='login'),
     path('',views.index,name='index'),
     path('register',views.register,name='register'),
     path('home',views.interface,name='interface'),
    
]