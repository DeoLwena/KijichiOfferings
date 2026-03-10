from django.shortcuts import render
from django.views import View


class DashboardView(View):
    def get(self, request):
        return render(request, 'wahazini_home.html')

# Create your views here.
