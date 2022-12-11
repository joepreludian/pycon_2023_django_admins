from base.auth_backends import MultiAdminModelBackend
from base.constants import AdminSites
from django.contrib.auth import logout


class MultiAdminUserVerifierMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    @staticmethod
    def process_view(request, view_func, view_args, view_kwargs):
        if request.resolver_match.namespace in [
            AdminSites.ADMIN,
            AdminSites.CLIENT_ADMIN,
        ]:
            # User will be always here;
            can_authenticate = (
                MultiAdminModelBackend.can_user_authenticate_to_namespace(
                    request.user, request.resolver_match.namespace
                )
            )

            if not can_authenticate:
                logout(request)

    def __call__(self, request):
        response = self.get_response(request)

        return response
