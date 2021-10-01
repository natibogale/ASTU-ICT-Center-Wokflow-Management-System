
from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="ad_home_page" ),
    path('register/', registrationView, name="ad_create_account"),
    path('profile/', profile, name="ad_profile"),
]
