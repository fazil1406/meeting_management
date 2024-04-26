from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import HttpResponse
from django.contrib import messages
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
            messages.add_message(request,messages.INFO,'Username already exists !')
            return redirect('/register')
         if User.objects.filter(email=Email).exists():
            messages.add_message(request,messages.INFO,'Email already exists !')
            return redirect('/register')
         
         else:       
            user=User.objects.create_user(first_name= Firstname,  last_name=Lastname, username=Username,  email=Email,password=Password)
            user.save()
            return redirect('/login')
         
                                       
      else:
         messages.add_message(request,messages.ERROR,'Password is incorrect !')
         return redirect('/register')
         


   else:
     return render(request,'register.html')
    

def login(request):
   
   if request.method=='POST':
       Username=request.POST['Username']
       Password=request.POST['Password']
       user=auth.authenticate(username=Username,password=Password)
       
       if user is not None:
          auth.login(request,user) 
          return redirect('/book/home')
       else:
          
          return redirect('/login')
   else:       
      return render(request,'login.html' )

def index(request):
   return render(request,'index.html')



