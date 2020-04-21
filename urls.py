from django.urls import path, include
from .views import user_login, user_register, user_logout, user_profile, user_delete
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
]
