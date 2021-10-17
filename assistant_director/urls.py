
from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="ad_home_page" ),
    path('register/', registrationView, name="ad_create_account"),
    path('profile/', profile, name="ad_profile"),
    path('manage-profile/', manageUsersView, name="ad_manage_accounts"),
    path('manage-reports/', manageReports, name="ad_manage_reports"),

    path('report-detail/<id>', reportDetail, name="ad_report_detail"),
    path('report-messages/<id>/<messageTo>', reportMessagesView, name="ad_report_messages"),
    path('reports-archive/', reportsArchive, name="ad_report_archive"),
    path('director-report-messages/<id>', directorReportMessagesView, name="ad_dr_report_messages"),


]
