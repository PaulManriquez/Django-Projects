from django.urls import path 

from ProjectWebMinimarketApp import views

#======= Adding where to search in media files ========= 
#To be able to see the media in the administration panel
from django.conf import settings 
from django.conf.urls.static import static
#=======================================================

urlpatterns = [
    path('',views.Home,name='Home'),
    path('Store/',views.Store,name='Store'),
]

#======= Adding where to search in media files ========= 
#To be able to see the media in the administration panel
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
#=======================================================