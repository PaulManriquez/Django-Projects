from django.shortcuts import render

from .forms import FormContact
# Create your views here.
def Contact(request):
    Form_Contacts = FormContact() #Object of FormContact 
    return render(request,'ContactApp/contact.html',{'Form_Contact':Form_Contacts})