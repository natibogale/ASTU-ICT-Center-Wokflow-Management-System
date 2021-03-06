
from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="dr_home_page" ),
    path('profile/', profile, name="dr_profile"),
    path('add-project/', addProjects, name="dr_add_projects"),
    path('manage-projects/', manageProjects, name="dr_manage_projects"),
    path('projects-archive/', projectsArchive, name="dr_project_archive"),
    path('project-detail/<id>', projectDetail, name="dr_project_detail"),
    path('project-messages/<id>/<messageTo>', messagesView, name="dr_project_messages"),


    path('request-project/', addReports, name="dr_request_reports"),
    path('manage-reports/', manageReports, name="dr_manage_reports"),
    path('report-messages/<id>', reportMessagesView, name="dr_report_messages"),
    path('report-detail/<id>', reportDetail, name="dr_report_detail"),
    path('reports-archive/', reportsArchive, name="dr_report_archive"),




]
