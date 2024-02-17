from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def regis(request):
   return render(request,'regis.html',{'name':'fazil'})

