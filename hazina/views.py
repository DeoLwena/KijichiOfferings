from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Mtoaji
from django.http import HttpResponse
# Create your views here.
@login_required
def Addofferings(request):
    return render(request,'add-offering.html')
@login_required()
def Dashboard(request):
    return render(request,'dashboard.html')
@login_required()
def Clerks(request):
    return render(request,'Clerks.html')
@login_required()
def Reports(request):
    return render(request,'Reports.html')