from django.urls import path
from .views import user_login, user_register, user_logout, user_profile, user_delete


urlpatterns = [
    path('', user_login),
    path('login/', user_login, name='user_login'),
    path('register/', user_register, name='user_register'),
    path('logout/', user_logout, name='user_logout'),
    path('profile/', user_profile, name='user_profile'),
    path('delete/', user_delete, name='user_delete'),
]
