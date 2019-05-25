from django.urls import path

from .api_views import Version

app_name = 'api'

urlpatterns = [
    path('version/', Version.as_view(), name='version'),
]
