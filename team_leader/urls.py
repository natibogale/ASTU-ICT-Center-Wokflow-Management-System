from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="tl_home_page" ),
    path('profile/', profile, name="tl_profile"),
    path('manage-projects/', manageProjects, name="tl_manage_projects"),
    path('assign-project/<id>', assignExpert, name="tl_assign_project"),
    path('project-messages/<id>', messagesView, name="tl_project_messages"),
    path('team-project-messages/<id>/<messageTo>', teamMessagesView, name="tl_team_project_messages"),
    path('projects-archive/', projectsArchive, name="tl_project_archive"),
    path('project-detail/<id>', projectDetail, name="tl_project_detail"),


    path('manage-reports/', manageReports, name="tl_manage_reports"),
    path('report-detail/<id>', reportDetail, name="tl_report_detail"),
    path('report-messages/<id>', reportMessagesView, name="tl_report_messages"),
    path('team-report-messages/<id>', teamReportMessagesView, name="tl_team_report_messages"),
    path('reports-archive/', reportsArchive, name="tl_report_archive"),



]
