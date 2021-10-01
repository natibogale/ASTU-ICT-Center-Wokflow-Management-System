from django.contrib import admin
from .models import (User, Teams, Roles)
from django.contrib.auth.admin import UserAdmin

# Register your models here.

class listAdmin(UserAdmin):
    list_display = ('id','admin_photo','username', 'firstName','lastName',
                    'email','directorate', 'role', 'team', 'is_admin')
    search_fields = ('id','username', 'firstName','lastName',
                    'email','directorate', 'role', 'team', )
    readonly_fields = ('admin_photo','date_joined', 'last_login','lastEdit')
    
    list_display_links=[
        'username',
        'admin_photo'
    ]
    
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()




class listTeams(admin.ModelAdmin):
    list_display = ('id','teamName')
    search_fields = ('id','teamName')
    
    list_display_links=[
       'id','teamName'
    ]
    
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()



class listRoles(admin.ModelAdmin):
    list_display = ('id','roleName')
    search_fields = ('id','roleName')
    
    list_display_links=[
       'id','roleName'
    ]
    
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()




admin.site.register(User, listAdmin)
admin.site.register(Teams,listTeams)
admin.site.register(Roles,listRoles)