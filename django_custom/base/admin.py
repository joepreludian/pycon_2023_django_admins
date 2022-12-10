from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.template.response import TemplateResponse


class MainAdminSite(admin.AdminSite):
    site_header = _("Car Rental ADMIN")
    site_url = None

    def each_context(self, request):
        current_context = super().each_context(request)
        return {"admin_name": self.name, **current_context}


class ClientAdminSite(admin.AdminSite):
    site_header = _("Client Site")
    site_url = None

    def each_context(self, request):
        current_context = super().each_context(request)
        return {"admin_name": self.name, **current_context}

    # Customizations
    def index(self, request, extra_context=None):

        context = {
            **self.each_context(request),
            **(extra_context or {}),
        }

        request.current_app = self.name

        return TemplateResponse(
            request, "base/client_admin/index.html", context
        )

    # Custom Views
    def all_cars_view(self, request):
        return TemplateResponse(
            request, "base/client_admin/all_cars.html", {
                **self.each_context(request),
                'data': [1, 2, 3]
            }
        )

    def get_urls(self):
        from django.urls import path

        return [
            path('all_cars/', self.admin_view(self.all_cars_view))
        ] + super().get_urls()


# Declaring Admin Panels
main_admin = MainAdminSite()
client_admin = ClientAdminSite(name='client_admin')
