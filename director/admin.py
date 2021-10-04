from django.contrib import admin
from .models import (Projects,TeamProjectMessages)
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




admin.site.register(Projects,projects)
admin.site.register(TeamProjectMessages,projectMessages)