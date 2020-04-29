from django.urls import path, include
from .views import user_login, user_register, user_logout, user_profile, user_delete, user_change_password, user_change_avatar
from rest_framework import routers
from .viewsets import UserViewSet


router = routers.DefaultRouter()
router.register(r'', UserViewSet)

urlpatterns = [
  path('', user_login),
  path('api/', include(router.urls)),
  path('login/', user_login, name='user_login'),
  path('register/', user_register, name='user_register'),
  path('logout/', user_logout, name='user_logout'),
  path('profile/', user_profile, name='user_profile'),
  path('delete/', user_delete, name='user_delete'),
  path('change-password/', user_change_password, name='user_change_password'),
  path('change-avatar/', user_change_avatar, name='user_change_avatar'),
]
