from __future__ import annotations
from typing import TYPE_CHECKING

from django.contrib.auth.backends import ModelBackend

from .constants import AdminSites, ClientAdminPermission

if TYPE_CHECKING:
    from base.models import User


class MultiAdminModelBackend(ModelBackend):
    def authenticate(self, request, **kwargs):  # @todo write a docstring
        user = super().authenticate(request, **kwargs)

        is_user_allowed_given_admin = self.can_user_authenticate_to_namespace(
            user=user, admin_site=getattr(request, "current_app", None)
        )

        if is_user_allowed_given_admin:
            return user

    @staticmethod
    def can_user_authenticate_to_namespace(user: User, admin_site: str | None) -> bool:
        """
        @todo Write a better docstring
        :param user:
        :param admin_site:
        :return:
        """
        if (
                admin_site is not None
                and admin_site in [AdminSites.CLIENT_ADMIN, AdminSites.ADMIN]
                and user is None
        ):
            return False

        if admin_site == AdminSites.CLIENT_ADMIN:
            if user.is_superuser:
                return True

            return user.has_perm(f"base.{ClientAdminPermission.CLIENT_ADMIN}")

        elif admin_site == AdminSites.ADMIN:
            return user.is_superuser

        return user is not None
