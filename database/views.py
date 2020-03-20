from django.shortcuts import render
from django.http import HttpResponse
from .models import Profile,Customer,Order,ItemInOrder,Address,Item,Article,Publication
from django.contrib.auth.models import User,auth
from django.db import IntegrityError
from .forms import StudentForm

# Create your views here.
def csignup(request):
    return render(request,'csignup.html')

def psignup(request):
    return render(request,'psignup.html')

def csubmit(request):
    try:
        if (request.method=='POST'):
            fname=request.POST["fname"]
            lname=request.POST["lname"]
            email=request.POST["mail"]
            uname=request.POST["uname"]
            pwd=request.POST["pwd"]
            cpwd=request.POST["cpwd"]
            user=User.objects.create_user(first_name=fname,last_name=lname,email=email,username=uname,password=pwd)
            user_info=Profile(user_type='Consumer')
            user_info.user=user
            user_info.save()
            customer=Customer(user=user_info)
            customer.save()
        return render(request,'chome.html')
    except IntegrityError as e:
        return HttpResponse('Username exists')

def psubmit(request):
    if (request.method=='POST'):
        fname=request.POST["fname"]
        lname=request.POST["lname"]
        email=request.POST["mail"]
        uname=request.POST["uname"]
        pwd=request.POST["pwd"]
        cpwd=request.POST["cpwd"]
        user=User.objects.create_user(first_name=fname,last_name=lname,email=email,username=uname,password=pwd)
        user_info=Profile(user_type='Provider')
        user_info.user=user
        user_info.save()
    return render(request,'phome.html')

def login(request):
    if request.method=='POST':
        uname=request.POST["uname"]
        pwd=request.POST["pwd"]
        user=auth.authenticate(username=uname,password=pwd)
        if user is not None:
            auth.login(request,user)
            return render(request,'chome.html')
        else:
            return HttpResponse('Invalid Credentials')
    else:
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return render (request,"login.html")

def operate(request):
    # user1=User.objects.get(pk=2)
    # prof=Profile.objects.get(user=user1)
    # cust=Customer.objects.get(user=prof)
    # order=list(Order.objects.filter(customer=cust))
    # items=dict()
    # for i in order:
    #     if i not in items:
    #         items[i]=list(ItemInOrder.objects.filter(order=i))
    # #newaddr=cust.address_set.create(room='201',building='Sumit Bhavan',road='Jeejeebhoy Lane',area='Lalbaug',city='Mumbai',pincode='400')
    #a2.publications.add(p1, p2)
    p=Publication.objects.get(pk=3)
    xyz=p.article_set.all()
    return render(request,'test.html',{'xyz':xyz})

def index(request):
    student=StudentForm()
    return render(request,'index.html',{'form':student})

def index_submit(request):
    if request.method=='POST':
        fname=request.POST["first_name"]
        lname=request.POST["last_name"]
        status=request.POST["status"]
        return HttpResponse(fname+' '+lname+' '+status)

