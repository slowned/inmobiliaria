from django.contrib import admin

from properties.models import Property

__all__ = ['PropertyAdmin']


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    class Meta:
        verbose_name = "Propiedad"
        verbose_name_plural = "Propiedades"
