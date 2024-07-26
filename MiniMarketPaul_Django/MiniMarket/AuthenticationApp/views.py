from django.shortcuts import render,redirect
#=====================================================
from django.views.generic import View 
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
# Create your views here.
class Register_view(View):

    def get(self,request):
        form = UserCreationForm()
        return render(request,'authenticationapp/register.html',{'form':form})
    
    def post(self,request):
        form = UserCreationForm(request.POST) #<-- Create an object form filled with the data that comes from the POST request

        if form.is_valid(): #<-- validate if there are no missing fields to fill or errors 
            user = form.save() #Save/create the user and stored in user 
            login(request,user)#login in the data base the new user 
            return redirect('Home')#<--- Here you can set a login .html to advertise to the user that now is logged and the user was created 
        else:#<-- If something wrong happends get all the error messages and redirect to the login endpoint again 
            for msg in form.error_messages:
                messages.error(request,form.error_messages[msg])
                #For each error message, it uses the messages.error function to add the error message to the Django messages framework. 
                #This allows you to display these error messages to the user on the rendered template.

            return render(request,'authenticationapp/register.html',{'form':form})   

#Log out endpoint
def Logout(request):
    logout(request)  
    return redirect('Home')      

#Log in endpoint 
def LogIn(request):

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)#<--Get the data from the form 
        if form.is_valid():
            User_Name = form.cleaned_data.get('username')#<--Get the data from the form
            User_Pass = form.cleaned_data.get('password')#<--Get the data from the form
            User = authenticate(username=User_Name,password=User_Pass) #Try to authenticate the user 
            if User is not None:
                login(request,User)#<--Log in the user
                return redirect('Home')
            else:
                messages.error(request,'User error authentication/No valid')
        else:
            messages.error(request,'Login Successfully')        

    form = AuthenticationForm()
    return render(request,'authenticationapp/login.html',{'form':form})