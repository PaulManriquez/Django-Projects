from django.contrib import admin

from .models import Category,Post
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields=('Created','Updated') #<-- Set the configurations to the admin panel

class PostAdmin(admin.ModelAdmin):
    readonly_fields=('Created','Updated') #<-- Set the configurations to the admin panel

admin.site.register(Category,CategoryAdmin)
admin.site.register(Post,PostAdmin)        
