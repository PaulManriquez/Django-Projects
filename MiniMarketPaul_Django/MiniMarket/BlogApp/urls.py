from django.urls import path 

from . import views
#==================
urlpatterns = [
    path('', views.Blog, name='BlogApp'),
    path('Category/<int:category_id>/', views.Category_view, name='Category')
]
