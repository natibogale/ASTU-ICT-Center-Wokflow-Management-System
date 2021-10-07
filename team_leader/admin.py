from django.contrib import admin

from team_leader.models import (ExpertProjectMessages, ExpertReportMessages)

# Register your models here.

class projectMessages(admin.ModelAdmin):
    list_display = ('id','projectId','messageSender','messageTo',
        'message','sentDate','is_seen')

    search_fields = ('id','projectId','messageSender','messageTo',
        'message','sentDate','is_seen')

    readonly_fields = ('sentDate',)

    list_display_links=[
        'projectId',
        'id',
    ]

    filter_horizontal = ()
    list_filter = ["sentDate"]
    fieldsets = ()






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


admin.site.register(ExpertReportMessages,reportMessages)


admin.site.register(ExpertProjectMessages,projectMessages)