from rest_framework import viewsets
from .models import Matoleo,Idara
from .serializers import IdaraSerializer,MatoleoSerializer
# from core.decorators import role_required as role_required
# from django.contrib.auth.decorators import login_required

# Create your views here.
# @role_required('Wahazini', 'Mashemasi')
# def Addofferings(request):
#     return render(request,'add-offering.html')
# @login_required()
# def Dashboard(request):
#     return render(request,'dashboard.html')




class MatoleoViewset(viewsets.ModelViewSet):
    queryset = Matoleo.objects.all()
    serializer_class = MatoleoSerializer

class IdaraViewset(viewsets.ModelViewSet):
    queryset = Idara.objects.all()
    serializer_class = IdaraSerializer