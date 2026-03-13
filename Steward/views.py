from django.shortcuts import render
from django.views import View



class StewardHome(View):
    def get(self, request):
        return render(request, 'StewardHome.html')

# Create your views here.
