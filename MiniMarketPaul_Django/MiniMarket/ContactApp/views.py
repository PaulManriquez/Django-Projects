from django.shortcuts import render, redirect

from .forms import FormContact 
from django.core.mail import EmailMessage
# Create your views here.
def Contact(request):
    Form_Contacts = FormContact() #Object of FormContact 
    
    if request.method == 'POST':
        Form_Contacts = FormContact(data=request.POST) #Get the data from the post request
        if Form_Contacts.is_valid(): # <-- Check all the data was filled 
            Name = request.POST.get('Name')
            Email = request.POST.get('Email')
            Content = request.POST.get('Content')

            Email_Message =  EmailMessage('This is a massage from django',
                                          'The user: {} with Email:{} wrote this:\n{}'.format(Name,Email,Content),
                                          '',['paulmanriquezengineer@gmail.com'],reply_to=[Email])
            try:
                Email_Message.send()

                return redirect('/Contacts/?valid') #<--redirect with a parameter is like a flag 
                                                    #to tell to the 'html' that is a post request
            except:                                        
                return redirect('/Contacts/?novalid')

    return render(request,'ContactApp/contact.html',{'Form_Contact':Form_Contacts})