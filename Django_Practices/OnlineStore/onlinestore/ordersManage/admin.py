from django.contrib import admin
from ordersManage.models import Customer,Items,Orders

# Register your models here.

#Here you can set how will be displayed the data according the fields of your data base 
class CustomerAdmin(admin.ModelAdmin):
    list_display=("Name","Address","Phone") #<--- This willbe the fields that appear in the Admin pannel for this data base 
    search_fields=('Name','Phone') #<--- Enable a search input to search for data in this table, in this case can be searched by Name and phone


#Add a filter colum section for a table (Admin) 
class ItemsAdmin(admin.ModelAdmin):
    list_display=("Name","Section","Price")
    list_filter=("Section",)


#Orders 
class OrdersAdmin(admin.ModelAdmin):
    list_display=('Order_Number','Name_Item','Order_Date')
    list_filter=('Order_Date',)
    date_hierarchy = "Order_Date" #<-- Enables the bar of the top 


admin.site.register(Customer,CustomerAdmin)
admin.site.register(Items,ItemsAdmin)
admin.site.register(Orders,OrdersAdmin)