from django.urls import path

from .api_views import VersionView, UserProfileView

app_name = 'api'

urlpatterns = [
    path('version/', VersionView.as_view(), name='version'),
    path('users/', UserProfileView.as_view(), name='user_list'),
]
