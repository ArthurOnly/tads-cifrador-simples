from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class CypherConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.cypher"
    verbose_name = _("cypher")
