from core.decorators import role_required as role_required
from django.shortcuts import render
from django.views import View
# Create your views here.


class ReportsHome(View):
    @role_required('Wahazini', 'Mchungaji', 'Uwakili')
    def get(self, request):
        return render(request,'Reports.html')