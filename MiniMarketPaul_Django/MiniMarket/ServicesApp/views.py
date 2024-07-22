from django.shortcuts import render

from ServicesApp.models import Service
# Create your views here.
def Services(request):
    services = Service.objects.all()
    return render(request,'Services/services.html',{'Services':services})


