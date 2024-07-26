from django.urls import path 

from . import views

urlpatterns = [
    path('',views.Register_view.as_view(),name='authenticate'),
    path('Logout/',views.Logout,name='Logout'),
    path('LogIn/',views.LogIn,name='LogIn'),
]

