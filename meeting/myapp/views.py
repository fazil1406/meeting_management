from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def regis(request):
   return render(request,'regis.html')

def login(request):
   return render(request,'login.html')

def index(request):
   return render(request,'index.html')

def interface(request):
   return render(request,'interface.html')

