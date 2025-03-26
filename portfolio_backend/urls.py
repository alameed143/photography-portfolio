from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('frontend.urls')),  # All API routes
    path('', include('frontend.urls')),  # Frontend routes
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 