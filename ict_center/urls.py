
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from authentication import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('authentication.urls')),
    path('logout/',views.logoutView, name='logout_page'),
    # path('assistant-director/',include('assistant_director.urls')),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
