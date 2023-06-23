from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .models import Doctor,Patient,Appointment
from django.template.context_processors import csrf
# Create your views here.
def ABOUT(request):
    return render(request, 'about.html')

def HOME(request):
    return render(request,'home.html')

def CONTACT(request):
    return render(request,'contact.html')


def LOGIN(request):
    error=""
    if request.method =="POST":
        u = request.POST['uname']
        p = request.POST['pwd']
        user = authenticate(username=u,password=p)
        try:
            if user.is_staff:
                login(request,user)
                error="no"
            else:
                error="yes"
        except:
            error="yes"
    d = {'error': error}
    return render(request,'login.html',d)

def Logout_Admin(request):
    if not request.user.is_staff:
        return redirect('login')
    logout(request)
    return redirect('login')

# def Add_doctor(request):
#     return render(request,'add_doctor.html')

def View_doctor(request):
    if not request.user.is_staff:
        return redirect('login')
    # doc = Doctor.objects.all()
    # d = {'doc' : doc}
    # return render(request,'view_doctor.html',d)
    c={}
    c.update(csrf(request))
    request.session['temp']="xyz"
    c['doc']=Doctor.objects.all()
    return render(request,'view_doctor.html',c)
    

def view_patient(request):
    if not request.user.is_staff:
        return redirect('login')
    pat=Patient.objects.all()
    p={'pat':pat}
    return render(request, 'view_patient.html',p)



    
def view_appointment(request):
    app=Appointment.objects.all()
    a={'app':app}
    return render(request, 'view_appointment.html',a)

def Add_doc(request):
    error = ""
    if not request.user.is_staff:
        return redirect('login')

    if request.method == "POST":
        i =  request.POST['ID']
        n =  request.POST['Name']
        m = request.POST['mobile']
        d =  request.POST['special']
        try:
            Doctor.objects.create(ID=i,Name=n,mobile=m,special=d)
            error = 'no'
        except:
            error = 'yes'
    c = {'error': error}
    return render(request,'add_doctor.html',c)

def Add_Patient(request):
    error = ""
    if not request.user.is_staff:
        return redirect('login')

    if request.method == "POST":
        n =  request.POST['name']
        g =  request.POST['gender']
        m = request.POST['mobile']
        c =  request.POST['address']
        try:
            Patient.objects.create(name=n,gender=g,mobile=m,address=c)
            error = 'no'
        except:
            error = 'yes'
    d = {'error': error}
    return render(request,'add_patient.html',d)

def Add_appointment(request):
    error = ""
    if not request.user.is_staff:
        return redirect('login')

    if request.method == "POST":
        g =  request.POST['doctor']
        n =  request.POST['patient']
        t =  request.POST['time']
        d =  request.POST['date']
        
        try:
            Patient.objects.create(doctor=g,patient=n,time=t,date=d)
            error = 'no'
        except:
            error = 'yes'
    c = {'error': error}
    return render(request,'add_appointment.html',c)






    
