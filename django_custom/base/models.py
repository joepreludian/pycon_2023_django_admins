from django.db import models
from django.utils.translation import gettext as _
from .constants import ClientAdminPermission


class BaseAdminConfig(models.Model):
    class Meta:
        managed = False
        permissions = (
            (ClientAdminPermission.CLIENT_ADMIN, _('User should have access to the Client Admin')),
        )