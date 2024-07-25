from django.shortcuts import render, redirect

from .Cart import Cart #<-- Class 
from StoreApp.models import Product #<--Product object model  

# * Each endpoint is created with the  Product_id that comes from store.html  and widget.html
# * Create the object Cart and perform the respective operation 
#   if the product with the id exist in cart SESSION <----
# * Cart.py comes from CartApp that is the class that create the SESSION'cart'

# Create your views here.
#=================================== Add a new product to cart 
def Add_Product(request,Product_id):
    MyCart = Cart(request) #Create an object cart 

    ProductAdd = Product.objects.get(id=Product_id) #Get the product with the id 

    if ProductAdd:
        MyCart.Add(ProductAdd)

    return redirect('Store')    

#=================================== Delete a product from the cart 
def Del_Product(request,Product_id):
    MyCart = Cart(request) #Create an object cart 

    ProductDel = Product.objects.get(id=Product_id) #Get the product with the id 

    if ProductDel:
        MyCart.Delete_Product(ProductDel)

    return redirect('Store')


#=================================== Decrease a product from the cart 
def Decrease_Product(request,Product_id):
    MyCart = Cart(request) #Create an object cart 

    ProductDec = Product.objects.get(id=Product_id) #Get the product with the id 

    if ProductDec:
        MyCart.Decrease_Product(ProductDec)

    return redirect('Store')


#=================================== Clear Cart
def Clear_Cart(request):
    MyCart = Cart(request) #Create an object cart 

    MyCart.Clean_Cart()
    return redirect('Store')

    
