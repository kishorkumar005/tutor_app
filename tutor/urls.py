from django.contrib import admin
from django.urls import path, include  # Import include to include app-level URLs

urlpatterns = [
    path('admin/', admin.site.urls),  # URL pattern for Django admin interface
    path('', include('tutor_app.urls')),  # Include app-level URL configurations
]
