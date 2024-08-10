from django.contrib import admin

# Register your models here.
from Notify_App.utils.admin import AbstractNotifyAdmin

from .models import Notification

admin.site.register(Notification,AbstractNotifyAdmin)