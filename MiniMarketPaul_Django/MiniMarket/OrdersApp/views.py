from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required
from StoreApp.models import Product
from django.contrib import messages
from django.core.mail import send_mail
from django.utils.html import strip_tags
from django.template.loader import render_to_string


from .models import OrderLine, Order #<--MODELS DATA BASE 
from CartApp.Cart import Cart #<-- Class of the cart 
    #  App  |File        |Class 
# Create your views here.

@login_required(login_url='Authentication/LogIn/') #<--Redirects to the url argument if you go to the url direction endpoint and you arent logged 
def process_order(request):
    order = Order.objects.create(user=request.user)#<-- Instance of the Model ORDER | returns the id in INT 
    cart = Cart(request) #<-- call an instance of the cart in the current session 
    
    #Creating and storing each order with the 
    #           OrderLine Model
    Order_Line_List = [] 
    for key,product in cart.items():
        productIdModel = Product.objects.get(id=product['Product_id']) #<-- search for the id in the models for the product that 
                                                                         #you're searching, product_id is expecting for explicity the id of the model       
        Order_Line_List.append( #List of orders model-line
            #Model instances 
            #1 Create Model instances of OrderLine and save it into a list 
            OrderLine(
                user = request.user,
                product_id =  productIdModel,
                order_id = order,
                quantity = product['Quantity']   
            )
            # order_id = order, (order)return the (int) id of the model instance 
        )
    #2 since Order_Line_list can hold multiple 'INSERT' Model instructions
    #  we use bulk_create to now, finally insert all the orders of the products in the OrderLine table  
    OrderLine.objects.bulk_create(Order_Line_List)   

    #====== Message Email of the order ======
    
    Send_Email(
        Order = str(order.id),
        Order_Line_List = Order_Line_List,
        username = request.user,
        usermail = request.user.email
    ) 
    
    cart.Clean_Cart() #<-- Clean Cart since the order was finished  
    messages.success(request,'Your order has been submitted successfully')
    return redirect('Store')

#Email sender function 
def Send_Email(**kwargs):
    subject = 'Thanks order in Minimarket Paul!'
    message = render_to_string('StoreApp/Delivery/delivery.html', {
        'Order': kwargs.get('Order'),
        'Order_Line_List': kwargs.get('Order_Line_List'),
        'UserName': kwargs.get('username')
    }) 

    Text_Message = strip_tags(message)
    from_email = 'paulmanriquezengineer@gmail.com' #<-- Email page
    to = kwargs.get('usermail') #<-- User logged email

    send_mail(subject,Text_Message,from_email,[to],html_message=message)