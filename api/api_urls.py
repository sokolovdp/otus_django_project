from django.urls import path

from rest_framework.routers import DefaultRouter
from .api_views import ItemViewSet

from .api_views import VersionView, UserProfileView

app_name = 'api'

urlpatterns = [
    path('version/', VersionView.as_view(), name='version'),
    path('users/', UserProfileView.as_view(), name='user_list'),
]


router = DefaultRouter()
router.register(r'items', ItemViewSet, basename='item')
urlpatterns += router.urls

