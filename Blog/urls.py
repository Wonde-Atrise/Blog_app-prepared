
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.contrib.auth import views as auth_views








urlpatterns = i18n_patterns(
    path('admin/', admin.site.urls),
    path('',include('simpleblog.url')),


   
)+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT )
urlpatterns += [
    path('i18n/', include('django.conf.urls.i18n')),
]
