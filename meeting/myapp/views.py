from django.shortcuts import render,redirect
from django.http import HttpResponse
from myapp.models import register
from django.contrib.auth.models import User,auth
# Create your views here.
def regis(request):
   if request.method=='POST':
      first_name=request.POST.get['first_name'],
      last_name=request.POST.get['last_name'],
      username=request.POST['username'],
      email=request.POST.get['email'],
      password=request.POST['password'],
      comfirm_password=request.POST['confirm_password'],
      Register=User.objects.create_user(First_name= first_name,  Last_Name=last_name, Username=username,  Email=  email,Password=password)
      Register.save()
      print('User created')
      return redirect('login')
      
      
   
   else:
      return render(request,'regis.html')

def login(request):
   return render(request,'login.html' )

def index(request):
   return render(request,'index.html')

def interface(request):
   return render(request,'interface.html')

