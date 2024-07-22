from django.urls import path 

from ServicesApp import views

#======= Adding where to search in media files ========= 
#To be able to see the media in the administration panel
from django.conf import settings 
from django.conf.urls.static import static
#=======================================================

urlpatterns = [
    path('',views.Services,name='Services'),
]

#======= Adding where to search in media files ========= 
#To be able to see the media in the administration panel
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
#=======================================================