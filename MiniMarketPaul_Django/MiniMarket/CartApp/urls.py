from django.urls import path 

from . import views
#=================
#app_name = 'Cart': This is a namespace for your URLs. 
#It allows you to reference these URLs unambiguously in templates and views, 
#especially useful when you have multiple apps with similar URL patterns.

app_name = 'Cart' #<--Enable to use it as url for the begining of each url in urlpatterns
urlpatterns = [
    path('Add_Product/<int:Product_id>/',views.Add_Product,name='Add'),
    path('Del_Product/<int:Product_id>/',views.Del_Product,name='Del'),
    path('Decrease_Product/<int:Product_id>/',views.Decrease_Product,name='Dec'),
    path('Clear_Cart/<int:Product_id>/',views.Clear_Cart,name='Clear'),
]

