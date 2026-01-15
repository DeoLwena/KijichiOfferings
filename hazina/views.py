from django.shortcuts import render
from .models import Mtoaji
from django.http import HttpResponse
# Create your views here.

def matoleo(request):
    return render(request,'add-offering.html')

def Home(request):
    aliyetoa_queryset = Mtoaji.objects.filter(namba_ya_ushirika__range=(10,34))

    return render(request,'dashboard.html',{'name':aliyetoa_queryset})