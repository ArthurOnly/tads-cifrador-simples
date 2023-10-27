from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class CipherConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.cipher"
    verbose_name = _("cipher")
