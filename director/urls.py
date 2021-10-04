
from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="dr_home_page" ),
    path('profile/', profile, name="dr_profile"),
    path('add-project/', addProjects, name="dr_add_projects"),
    path('manage-projects/', manageProjects, name="dr_manage_projects"),


]
