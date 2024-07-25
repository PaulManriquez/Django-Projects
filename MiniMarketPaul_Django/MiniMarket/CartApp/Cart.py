#My cart Class 
class Cart:
    #Constructor 
    def __init__(self,request):
        self.request=request        #<-- Get the request
        self.session=request.session#<-- Get the current session 
        #============================== Check if the cart exist in the session, otherwise create it 
        #This ensures that self.cart always references the current cart, 
        # whether it was just created or already existed in the session. 
        # The other methods in the class then use self.cart to access and modify the cart's contents.
        cart = self.session.get('cart')
        if not cart: #<-- if the cart dont exist in the session.get it creates a cart in the session
            self.cart = self.session['cart'] ={} #<--- Creates a dictionary for each product 
            #Cart dictionary exist in both, in .cart and in session 
        else:
            self.cart = cart   #Save the content of the old cart     
        #==============================     

    def Add(self,Product):
        if(str(Product.id) not in self.cart.keys()): #if the product is not in the current cart | Add 
            self.cart[Product.id]={
                'Product_id':Product.id,
                'Name':Product.Name,
                'Price':str(Product.Price),
                'Quantity':1,
                'Image':Product.Image.url,
                'SubTotal':str(Product.Price)
            }
        else:#Product already exist | Add one more to the cart 
            for key,product in self.cart.items():#if the product is in the cart, find the id and in quantity add 1
                if key == str(Product.id):
                    product['Quantity'] += 1
                    product['SubTotal'] = product['Quantity'] * float(product['Price'])
                    break

        self.Save_Cart() #<-- Update the Cart             

    def Save_Cart(self):
        self.session['cart'] = self.cart  #<--Update the cart content in session 
        self.session.modified = True #<-- Save changes 

    def Delete_Product(self,Product):
        #Product.id = str(Product.id)
        if str(Product.id) in self.cart:
            del self.cart[str(Product.id)] #Delete the product in the cart according with the id 
            self.Save_Cart()#<-- Save changes  

    def Decrease_Product(self,Product):
        if str(Product.id) in self.cart: #If that product exist in the cart  
            for key,product in self.cart.items():#if the product is in the cart, find the id and in quantity add 1
                    if key == str(Product.id):
                        product['Quantity'] -= 1
                        product['SubTotal'] = product['Quantity'] * float(product['Price'])
                        if product['Quantity'] == 0: #<-- If the product reach to 0 | Delete it 
                            self.Delete_Product(Product)
                        break
        self.Save_Cart()#<--Update Changes 


    def Clean_Cart(self):                    
        self.session['cart']={} #<-- Set the cart to nothing 
        self.session.modified = True #<-- Save changes 

