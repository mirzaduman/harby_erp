from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from backend.api.api import api


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api.urls)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
