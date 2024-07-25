from django.urls import path 

from . import views

urlpatterns = [
    path('',views.Authenticate,name='authenticate'),
]

