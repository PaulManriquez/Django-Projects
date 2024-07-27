from django.urls import path 
from . import views

app_name = 'ToPay' #<--Enable to use it as url for the begining of each url in urlpatterns
urlpatterns = [
    path('',views.process_order,name='Pay'),
]
