from django.contrib import admin

class AbstractNotifyAdmin(admin.ModelAdmin):
    raw_id_fields = ('destiny',)
    list_display = ('destiny','actor','verb','read','public')
    list_filter = ('level','read')

    def get_queryset(self,request):#NOTE IN REQUEST VARIABLE
        qs = super(AbstractNotifyAdmin,self).get_queryset(request)
        return qs.prefetch_related('actor')