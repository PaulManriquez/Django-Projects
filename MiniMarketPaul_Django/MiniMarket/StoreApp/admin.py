from django.contrib import admin

from .models import CategoryProduct,Product 
# Register your models here.
class CategoryProductAdmin(admin.ModelAdmin):
    readonly_fields=('Created','Updated')

class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ('Created','Updated')

admin.site.register(CategoryProduct,CategoryProductAdmin)
admin.site.register(Product,ProductAdmin)    
