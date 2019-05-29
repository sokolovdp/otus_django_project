from django.urls import path

from main_app import main_views

app_name = 'main_app'

urlpatterns = [
    path('register/', main_views.register, name='register'),
    path('login/', main_views.user_login, name='user_login'),
    path('logout/', main_views.user_logout, name='user_logout'),
    path('items_list/', main_views.items_list, name='items_list'),
]
