def Total_Pay_Cart(request):
    total = 0
    if request.user.is_authenticated:
        cart = request.session.get('cart', {})
        for key, product in cart.items():
            total += float(product['Price']) * product['Quantity']
    return {'Total_Pay': total}

#======== request.session['cart'] | is a dict of dicts 
#key | Estands for each id of the product 
# product | Product specification     

#===
#cart = request.session.get('cart', {})
#This line retrieves the cart from the session. 
#The get method of the session dictionary is used to look for the key 'cart'. 
#If the key 'cart' is not found in the session, 
#it returns an empty dictionary {} instead of raising a KeyError. 
#This ensures that cart always contains a dictionary, 
#either the current cart or an empty one if no cart exists in the session.

'''
cart (dictionary)
└── '1' (key) (That holds a dictionary called 'Product')
    └── {(product)
         'Product_id': 1,
         'Name': 'Product A',
         'Price': '10.00',
         'Quantity': 2,
         'Image': 'url_to_image_a'
        } 
'''