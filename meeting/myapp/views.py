from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import HttpResponse

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
      if Password==comfirm_password:
         
         if User.objects.filter(username=Username).exists():
            messages.info(request,'Username Already Taken')
            return redirect('/register')
         if User.objects.filter(email=Email).exists():
            messages.info(request,'Email ID Already Taken') 
            return redirect('/register')
         else:       
            user=User.objects.create_user(first_name= Firstname,  last_name=Lastname, username=Username,  email=Email,password=Password)
            user.save()

            messages.success(request,'You Successfully Rgister')
      
         
            return redirect('/')
      else:
         return redirect('/register')


   else:
     return render(request,'register.html')
    

def login(request):
   return render(request,'login.html' )

def index(request):
   return render(request,'index.html')

def interface(request):
   return render(request,'interface.html')

