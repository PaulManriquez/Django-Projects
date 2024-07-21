from django.shortcuts import render
from django.http import HttpResponse
from ordersManage.models import Items 


# Create your views here.
def search_products(request):
    return render(request,'search_products.html')

def search(request):
    Items_To_Search = request.GET.get('product_name', '')
    if not Items_To_Search:  # Check if the input is empty
        return HttpResponse("The search query is empty.")
    
    All_Products = Items.objects.filter(Name__icontains=Items_To_Search)#<--Search for the item coincidences 
    print(type(All_Products)) #<-- List of objects SQL 

    #return HttpResponse(All_Products)
    return render(request,'Searchresults.html',{'Items':All_Products,'Item':Items_To_Search})

def insertItems(request):
    if request.method == 'GET':
        return render(request, 'insertitem.html')
    elif request.method == 'POST':
        Name = request.POST.get('Product', '')
        Section = request.POST.get('Section', '')
        Price = request.POST.get('Price', '')

        if not (Name and Section and Price):
            return HttpResponse("The search query is empty.")
        
        Data = (Name, Section, Price)
        item = Items(Name=Data[0], Section=Data[1], Price=Data[2])
        item.save()
        return HttpResponse(f'Data inserted: {Data}')
    else:
        return HttpResponse("Invalid request method.")


def Contact_Us(request):

    if request.method=='POST':
        return HttpResponse("ok")

    return render(request,'ContactUs.html')