from django.shortcuts import render

# Create your views here.
def Authenticate(request):
    return render(request,'authenticationapp/register.html')