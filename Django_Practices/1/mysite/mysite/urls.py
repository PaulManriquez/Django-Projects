"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from views import Gretting,CurrentDate,GetMyAgeAt,Gretting_Pt2,Gretting_Pt3, Gretting_Pt4,child1_page

#List of tuples | URLS
urlpatterns = [
    path('admin/', admin.site.urls),
    path('Greeting/', Gretting),
    path('CurrentDate/',CurrentDate),
    path('GetMyAgeAt/<int:age>/<int:year>',GetMyAgeAt),
    path('Gretting_Pt2/',Gretting_Pt2),
    path('Gretting_Pt3/',Gretting_Pt3),
    path('Gretting_Pt4/',Gretting_Pt4),
    path('child1_page/',child1_page)
]
