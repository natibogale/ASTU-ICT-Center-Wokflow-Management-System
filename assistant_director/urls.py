
from django.urls import path
from .views import *

urlpatterns = [
    path('', registrationView, name="ad_create_account"),
]
