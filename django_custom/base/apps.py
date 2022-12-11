from django.apps import AppConfig
from .admin import main_admin


class BaseConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'base'

    def ready(self):
        from django.contrib import admin
        from django.contrib.auth.admin import GroupAdmin, UserAdmin
        from django.contrib.auth.models import Group
        from django.contrib.auth import get_user_model

        # Registering Default Permissions on Model
        user_model = get_user_model()
        main_admin.register(Group, GroupAdmin)
        main_admin.register(user_model, UserAdmin)

        admin.site = main_admin  # Overriding the default django admin site
