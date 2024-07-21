from django.shortcuts import render,HttpResponse

from ServicesApp.models import Service
# Create your views here.


def Home(request):
    return render(request,'ProjectWebMinimarketApp/home.html')

def Services(request):
    services = Service.objects.all()
    return render(request,'ProjectWebMinimarketApp/services.html',{'Services':services})

def Store(request):
    return render(request,'ProjectWebMinimarketApp/store.html')

def Blog(request):
    return render(request,'ProjectWebMinimarketApp/blog.html')

def Contact(request):
    return render(request,'ProjectWebMinimarketApp/contact.html')