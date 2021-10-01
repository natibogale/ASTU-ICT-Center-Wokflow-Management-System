
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home, name="login_page"),
    path('assistant-director/',include('assistant_director.urls')),
    path('director/',include('director.urls')),

]
