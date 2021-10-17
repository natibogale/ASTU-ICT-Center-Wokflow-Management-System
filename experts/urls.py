from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="exp_home_page" ),
    path('profile/', profile, name="exp_profile"),
    path('manage-projects/', manageProjects, name="exp_manage_projects"),
    path('project-messages/<id>', expertMessagesView, name="exp_project_messages"),
    path('project-detail/<id>', projectDetail, name="exp_project_detail"),
    path('projects-archive/', projectsArchive, name="exp_project_archive"),
    path('manage-reports/', manageReports, name="exp_manage_reports"),
    path('report-detail/<id>', reportDetail, name="exp_report_detail"),
    path('reports-archive/', reportsArchive, name="exp_report_archive"),
    path('team-report-messages/<id>', teamReportMessagesView, name="exp_team_report_messages"),



]
