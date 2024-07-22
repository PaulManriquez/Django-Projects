from django.shortcuts import render

from BlogApp.models import Post, Category
# Create your views here.
def Blog(request):
    posts = Post.objects.all()
    return render(request,'BlogApp/blog.html',{'Posts':posts})


def Category_view(request, category_id):
    category = Category.objects.get(id=category_id) #<--- Get all the categories accordin to the id related
    posts = Post.objects.filter(Categories=category) #<--- Show the post related to the category and get all the results
    return render(request, 'BlogApp/category.html', {'Category': category, 'Posts': posts})