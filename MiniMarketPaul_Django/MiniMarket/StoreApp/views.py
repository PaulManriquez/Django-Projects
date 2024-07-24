from django.shortcuts import render

from .models import Product
# Create your views here.
def Store(request):
    products = Product.objects.all()
    return render(request,'StoreApp/store.html',{'Products':products})