from django.shortcuts import render
from django.views import View
from django.contrib.auth.models import User


# Create your views here.
class MchungajiDashboard(View):
    def get(self, request):
        return render(request,'dashboard/mchungaji/dashboard.html')

class MhaziniDashboard(View):
    def get(self, request):
        return render(request,'dashboard/mhazini/dashboard.html')

class UwakiliDashboard(View):
    def get(self, request):
        return render(request,'dashboard/uwakili/dashboard.html')

class MashemasiDashboard(View):
    def get(self, request):
        return render(request,'dashboard/mashemasi/dashboard.html')
