from django.contrib import admin
from base.admin import main_admin, client_admin

from .models import Vehicle, Model as CarModel


@admin.register(CarModel, site=main_admin)
class CarModelAdmin(admin.ModelAdmin):
    pass


@admin.register(Vehicle, site=main_admin)
class VehicleAdmin(admin.ModelAdmin):
    pass


@admin.register(Vehicle, site=client_admin)
class VehicleClientAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

