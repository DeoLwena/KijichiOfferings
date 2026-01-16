from django.shortcuts import render
from .models import Mtoaji
from django.http import HttpResponse
# Create your views here.

def Addofferings(request):
    return render(request,'add-offering.html')

def Dashboard(request):
    return render(request,'dashboard.html')

def Clerks(request):
    return render(request,'Clerks.html')

def Reports(request):
    return render(request,'Reports.html')