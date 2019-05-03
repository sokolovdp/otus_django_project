from django.conf.urls import url
from main_app import views

app_name = 'main_app'

urlpatterns = [
    url(r'^register/', views.register, name='register'),
    url(r'^login/', views.user_login, name='user_login'),
    url(r'^logout/', views.user_logout, name='user_logout'),
]