from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin panel ka path
    path('api/', include('myapp.urls')),  # Backend API routes
]
