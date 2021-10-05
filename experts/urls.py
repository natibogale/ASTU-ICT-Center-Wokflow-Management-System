from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="exp_home_page" ),
    path('profile/', profile, name="exp_profile"),
    path('manage-projects/', manageProjects, name="exp_manage_projects"),
    path('project-messages/<id>/<messageTo>', expertMessagesView, name="exp_project_messages"),

]
