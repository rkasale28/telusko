from django.shortcuts import render
from django.http import HttpResponse
from .models import UserInfo


# Create your views here.
def csignup(request):
    return render(request,'csignup.html')

def psignup(request):
    return render(request,'psignup.html')

def csubmit(request):
    fname=request.POST["fname"]
    lname=request.POST["lname"]
    email=request.POST["mail"]
    uname=request.POST["uname"]
    pwd=request.POST["pwd"]
    cpwd=request.POST["cpwd"]
    user_info=UserInfo(first_name=fname,last_name=lname,email_id=email,user_name=uname,pwd=pwd,user_type='Consumer')
    user_info.save()
    return render(request,'chome.html')

def psubmit(request):
    fname=request.POST["fname"]
    lname=request.POST["lname"]
    email=request.POST["mail"]
    uname=request.POST["uname"]
    pwd=request.POST["pwd"]
    cpwd=request.POST["cpwd"]
    user_info=UserInfo(first_name=fname,last_name=lname,email_id=email,user_name=uname,pwd=pwd,user_type='Provider')
    user_info.save()
    return render(request,'phome.html')
