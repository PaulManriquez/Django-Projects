class Cart:
    #Constructor 
    def __init__(self,request):
        self.request=request
        self.session=request.session
        cart = self.session.get('cart')
        if not cart:
            cart = self.session['cart'] ={}
        else:
            self.cart = cart        

    def Add(self,Product):
        if(str(Product.id) not in self.cart.keys()): #if the product is not in the current cart 
            self.cart[Product.id]={
                'Product_id':Product.id,
                'Name':Product.Name,
                'Price':str(Product.Price),
                'Quantity':1,
                'Image':Product.Image.url
            }
        else:
            for key,dic in self.cart.items():#if the product is in the cart, find the id and in quantity add 1
                if key == str(Product.id):
                    dic['Quantity'] += 1
                    break

        self.Save_Cart() #<-- Update the Cart             

    def Save_Cart(self):
        self.session['cart'] = self.cart 
        self.session.modified = True 

    def Delete_Product(self,Product):
        #Product.id = str(Product.id)
        if str(Product.id) in self.cart:
            del self.cart[str(Product.id)] #Delete the product in the cart according with the id 
            self.Save_Cart()#Update the cart 

    def Decrease_Product(self,Product):
        if str(Product.id) in self.cart: #If that product exist in the cart  
            for key,dic in self.cart.items():#if the product is in the cart, find the id and in quantity add 1
                    if key == str(Product.id):
                        dic['Quantity'] -= 1
                        if dic['Quantity'] == 0: #<-- If the product reach to 0 | Delete it 
                            self.Delete_Product(Product)
                        break
        self.Save_Cart()#<--Update Changes 


    def Clean_Cart(self):                    
        self.session['cart']={}
        self.session.modified = True 

