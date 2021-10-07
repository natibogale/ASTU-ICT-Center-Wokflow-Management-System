from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="exp_home_page" ),
    path('profile/', profile, name="exp_profile"),
    path('manage-projects/', manageProjects, name="exp_manage_projects"),
    path('project-messages/<id>', expertMessagesView, name="exp_project_messages"),
    path('project-detail/<id>', projectDetail, name="exp_project_detail"),
    path('projects-archive/', projectsArchive, name="exp_project_archive"),



]
