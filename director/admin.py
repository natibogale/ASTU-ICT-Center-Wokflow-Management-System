from django.contrib import admin
from .models import (Projects,TeamProjectMessages,Reports,DirectorReportMessages)
from django.contrib.auth.admin import UserAdmin

class projects(admin.ModelAdmin):
    list_display = ('projectTitle','deadLine','created_by',
        'is_seen','is_urgent','dateAdded','assignedTeam')

    search_fields = ('projectTitle','deadLine','created_by',
        'is_seen','is_urgent','dateAdded','assignedTeam')

    readonly_fields = ['dateAdded']

    list_display_links=[
        'projectTitle',
    ]

    filter_horizontal = ()
    list_filter = ["dateAdded"]
    fieldsets = ()


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






class reports(admin.ModelAdmin):
    list_display = ('reportTitle','deadLine','created_by',
        'is_seen','dateAdded','assistantDirector')

    search_fields = ('reportTitle','deadLine','created_by',
        'is_seen','dateAdded','assistantDirector')

    readonly_fields = ['dateAdded']

    list_display_links=[
        'reportTitle',
    ]

    filter_horizontal = ()
    list_filter = ["dateAdded"]
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




admin.site.register(Projects,projects)
admin.site.register(Reports,reports)
admin.site.register(DirectorReportMessages,reportMessages)
admin.site.register(TeamProjectMessages,projectMessages)