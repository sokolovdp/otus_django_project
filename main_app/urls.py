from django.urls import path

from main_app import views

app_name = 'main_app'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='user_logout'),
]
