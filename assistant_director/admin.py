from django.contrib import admin
from .models import  AssistantMessages

# Register your models here.

class reportMessages(admin.ModelAdmin):
    list_display = ('id','reportId','messageSender','messageTo',
        'message','sentDate','is_seen')

    search_fields = ('id','reportId','messageSender','messageTo',
        'message','sentDate','is_seen')

    readonly_fields = ('sentDate',)

    list_display_links=[
        'reportId',
        'id',
    ]

    filter_horizontal = ()
    list_filter = ["sentDate"]
    fieldsets = ()


admin.site.register(AssistantMessages,reportMessages)
