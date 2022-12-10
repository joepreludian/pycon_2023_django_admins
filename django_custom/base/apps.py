from django.apps import AppConfig
from .admin import main_admin


class BaseConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'base'

    def ready(self):
        from django.contrib import admin
        admin.site = main_admin  # Monkey Patching default admin site
