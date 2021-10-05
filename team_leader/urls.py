from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="tl_home_page" ),
    path('profile/', profile, name="tl_profile"),
    path('manage-projects/', manageProjects, name="tl_manage_projects"),
    path('assign-project/<id>', assignExpert, name="tl_assign_project"),
    path('project-messages/<id>/<messageTo>', messagesView, name="tl_project_messages"),
    path('team-project-messages/<id>/<messageTo>', teamMessagesView, name="tl_team_project_messages"),




]
