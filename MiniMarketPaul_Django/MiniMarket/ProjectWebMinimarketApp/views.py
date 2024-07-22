from django.shortcuts import render,HttpResponse

# Create your views here.


def Home(request):
    return render(request,'ProjectWebMinimarketApp/home.html')


def Store(request):
    return render(request,'ProjectWebMinimarketApp/store.html')

def Blog(request):
    return render(request,'ProjectWebMinimarketApp/blog.html')

def Contact(request):
    return render(request,'ProjectWebMinimarketApp/contact.html')