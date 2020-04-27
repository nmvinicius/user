from django.apps import AppConfig
from django.conf import settings
from django.utils.translation import gettext_lazy as _


USER_ENABLED = 'user' in settings.INSTALLED_APPS


class UserConfig(AppConfig):
  name = 'user'
  verbose_name = _('user')
