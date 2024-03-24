from django.shortcuts import render,redirect
from django.contrib.auth.models import User,UserManager,auth
from django.contrib.auth.decorators import login_required
from .models import Booking

# Create your views here.
@login_required
def meeting(request):
       if request.method=='POST':
         hostname=request.POST.get('host_name')
         classname=request.POST.get('class_name')
         students=request.POST.get('no_of_students')
         subject=request.POST.get('subject')
         timing=request.POST.get('timing')
         user=request.user.id
         booking = Booking(user, host_name=hostname, class_name=classname, students=students,subject=subject,timing=timing)
         booking.save()
         return redirect('/home')
       else:  
        return render(request,'meeting.html')
