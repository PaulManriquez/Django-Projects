from django.urls import path 

from . import views

urlpatterns = [
    path('',views.Contact,name='Contact'),
]
# {% url 'Contact' %} | Name enables to access or refers 
#in a part of the project that you desire 