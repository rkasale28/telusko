from django.shortcuts import render
from django.http import HttpResponse
from .models import Destination

# Create your views here.
def home(request):
    dest1=Destination(1,'Mumbai','City',750)
    #dest1.name='Mumbai'
    return render(request,'home.html',{'dest1':dest1})

