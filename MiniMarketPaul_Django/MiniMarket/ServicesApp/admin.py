from django.contrib import admin

from .models import Service
# Register your models here.
class ServiceAdmin(admin.ModelAdmin):
    readonly_fields = ('Created', 'Updated')

admin.site.register(Service,ServiceAdmin)
