from django.shortcuts import render,redirect
from django.contrib import messages
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
         start=request.POST.get('start_time')
         end=request.POST.get('end_time')

         date=request.POST.get('date')
         user=request.user.id
         booking = Booking(user, host_name=hostname, class_name=classname, students=students,subject=subject,Datee=date,starttiming=start,endtiming=end)
         booking.save()
         print(booking.students)
        
        # if Booking.objects.filter(Datee=date).exists and Booking.objects.filter(starttiming=start).exists and Booking.objects.filter(endtiming=end).exists :
         #   messages.add_message(request,messages.INFO,"ALREADY BOOKED")
          #  return render(request,"meeting.html")    
         
         if int(booking.students) >70:
              messages.add_message(request,messages.INFO,"The class limit is 70 !!")
              return render(request,"meeting.html") 
         else: 
          
          print(booking.pk)
         
          return redirect('/book/home',{"booking":booking})
         #return render(request,'interface.html',{"booking_details":{"pk":booking.pk,"hostname":booking.host_name,"classname":booking.class_name,"students":booking.students,"timing":booking.timing}})
        
        else: 
        
          return render(request,"meeting.html")
        
def interface(request):
   interface=Booking.objects.all()
   return render(request,'interface.html',{'interface':interface})



