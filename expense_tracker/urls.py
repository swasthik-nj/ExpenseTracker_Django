"""
URL configuration for expense_tracker project.
Routes all app-level URLs to the tracker app.
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tracker.urls')),  # Include all tracker app URLs
]
