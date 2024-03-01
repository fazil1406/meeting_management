from django.shortcuts import render,redirect
from django.http import HttpResponse
from myapp.models import register
from django.contrib.auth.models import User,auth
# Create your views here.
def register(request):
   if request.method=='POST':
      Firstname=request.POST['one']
      Lastname=request.POST['last']
      Username=request.POST['Username']
      Email=request.POST['Email']
      Password=request.POST['Password']
      comfirm_password=request.POST['Confirmpassword']

      user=User.objects.create_user(first_name= Firstname,  last_name=Lastname, username=Username,  email=Email,password=Password)
      user.save()

      print('User created')

      return redirect('/')
      
      
   
   else:
      return render(request=request,template_name='register.html')

def login(request):
   return render(request,'login.html' )

def index(request):
   return render(request,'index.html')

def interface(request):
   return render(request,'interface.html')

