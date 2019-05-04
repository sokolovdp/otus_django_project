from django.urls import path

from .api_views import Test

app_name = 'api'

urlpatterns = [
    path('test/', Test.as_view(), name='test'),
]
